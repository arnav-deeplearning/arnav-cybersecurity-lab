# Local Password Manager

A command-line password manager with real AES-256-GCM encryption behind
a master password. No plaintext ever touches disk.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python cli.py init                # create a new vault, set a master password
python cli.py add github.com      # store a username/password for a service
python cli.py get github.com      # retrieve it
python cli.py list                # list stored service names (not secrets)
python cli.py delete github.com   # remove an entry
```

All commands accept `--vault PATH` to point at a specific vault file
(defaults to `./vault.dat`). Master passwords and stored secrets are
entered via `getpass`, so they're never echoed to the terminal or saved
in shell history.

## How the encryption works

- **AES-256-GCM** encrypts the entire vault as one blob. GCM is
  *authenticated* encryption — it detects tampering or a wrong master
  password immediately (`InvalidTag`), instead of silently decrypting
  to garbage the way plain AES-CBC would.
- **PBKDF2-HMAC-SHA256, 480,000 iterations** turns the master password
  into the actual 256-bit encryption key. The iteration count follows
  OWASP's current guidance for PBKDF2-SHA256, making brute-forcing the
  master password computationally expensive even though SHA-256 itself
  is fast.
- A random **salt** (per vault) and **nonce** (per save) are stored in
  plaintext next to the ciphertext in the vault file. That's expected
  and safe — neither needs to be secret, only unique.
- All of this comes from the `cryptography` library's audited
  primitives (`cryptography.hazmat.primitives.ciphers.aead.AESGCM` and
  `PBKDF2HMAC`) — nothing here is a hand-rolled implementation of AES
  itself.

See [`vault.py`](vault.py) for the full implementation.

## Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

Covers: correct encrypt/decrypt round-trips, rejection of a wrong
master password, confirming the raw vault file never contains
plaintext secrets, and basic CRUD behavior.
