"""
Core encryption logic for the local password vault.

Design, and why:

- AES-256-GCM (authenticated encryption) instead of plain AES-CBC. GCM
  gives you both confidentiality AND integrity: if the vault file is
  tampered with, or the wrong master password is used, decryption fails
  loudly (InvalidTag) instead of silently returning garbage.
- The whole vault is encrypted as a single JSON blob, not entry-by-entry.
  Simpler, and avoids subtle bugs like reusing a nonce across entries.
- PBKDF2-HMAC-SHA256 with 480,000 iterations turns a human-memorable
  master password into a 256-bit key. The iteration count follows
  OWASP's 2023 password-storage guidance for PBKDF2-SHA256 -- high
  enough to make brute-forcing the master password computationally
  expensive, even though the algorithm itself is fast.
- A fresh random salt (per vault) and nonce (per save) are stored in
  plaintext alongside the ciphertext. This is safe and standard: neither
  needs to be secret, they just need to be unique.

This uses the `cryptography` library's audited primitives throughout --
no hand-rolled crypto.
"""
from __future__ import annotations

import base64
import json
import secrets
from dataclasses import dataclass, field
from pathlib import Path

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

KDF_ITERATIONS = 480_000
SALT_SIZE = 16       # bytes
NONCE_SIZE = 12      # bytes, standard for AES-GCM
KEY_SIZE = 32        # bytes = 256 bits
FORMAT_VERSION = 1


class VaultError(Exception):
    """Raised for incorrect master passwords or a corrupted vault file."""


def _derive_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE,
        salt=salt,
        iterations=KDF_ITERATIONS,
    )
    return kdf.derive(master_password.encode("utf-8"))


@dataclass
class Vault:
    path: Path
    master_password: str
    entries: dict = field(default_factory=dict)  # {service: {"username": ..., "password": ...}}
    _salt: bytes = field(default_factory=lambda: secrets.token_bytes(SALT_SIZE))

    @classmethod
    def create(cls, path: Path, master_password: str) -> "Vault":
        if path.exists():
            raise VaultError(f"A vault already exists at {path}. Delete it first if you want to start over.")
        vault = cls(path=path, master_password=master_password)
        vault.save()
        return vault

    @classmethod
    def load(cls, path: Path, master_password: str) -> "Vault":
        if not path.exists():
            raise VaultError(f"No vault found at {path}. Run 'init' first.")

        raw = json.loads(path.read_text(encoding="utf-8"))
        if raw.get("version") != FORMAT_VERSION:
            raise VaultError("Unrecognized vault file format/version.")

        salt = base64.b64decode(raw["kdf"]["salt"])
        nonce = base64.b64decode(raw["cipher"]["nonce"])
        ciphertext = base64.b64decode(raw["ciphertext"])

        key = _derive_key(master_password, salt)
        try:
            plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)
        except InvalidTag as exc:
            raise VaultError("Incorrect master password, or the vault file is corrupted/tampered with.") from exc

        entries = json.loads(plaintext.decode("utf-8"))
        vault = cls(path=path, master_password=master_password, entries=entries)
        vault._salt = salt
        return vault

    def save(self) -> None:
        key = _derive_key(self.master_password, self._salt)
        nonce = secrets.token_bytes(NONCE_SIZE)
        plaintext = json.dumps(self.entries).encode("utf-8")
        ciphertext = AESGCM(key).encrypt(nonce, plaintext, None)

        payload = {
            "version": FORMAT_VERSION,
            "kdf": {
                "algorithm": "PBKDF2HMAC-SHA256",
                "iterations": KDF_ITERATIONS,
                "salt": base64.b64encode(self._salt).decode("ascii"),
            },
            "cipher": {
                "algorithm": "AES-256-GCM",
                "nonce": base64.b64encode(nonce).decode("ascii"),
            },
            "ciphertext": base64.b64encode(ciphertext).decode("ascii"),
        }
        self.path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def add_entry(self, service: str, username: str, password: str) -> None:
        self.entries[service] = {"username": username, "password": password}
        self.save()

    def get_entry(self, service: str) -> dict:
        if service not in self.entries:
            raise VaultError(f"No entry found for '{service}'.")
        return self.entries[service]

    def delete_entry(self, service: str) -> None:
        if service not in self.entries:
            raise VaultError(f"No entry found for '{service}'.")
        del self.entries[service]
        self.save()

    def list_services(self) -> list[str]:
        return sorted(self.entries.keys())
