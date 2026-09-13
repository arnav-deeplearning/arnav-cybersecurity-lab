import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from vault import Vault, VaultError  # noqa: E402


def test_create_and_reload_round_trip(tmp_path):
    vault_path = tmp_path / "vault.dat"
    vault = Vault.create(vault_path, "correct horse battery staple")
    vault.add_entry("github.com", "arnav", "hunter2")

    reloaded = Vault.load(vault_path, "correct horse battery staple")
    entry = reloaded.get_entry("github.com")
    assert entry["username"] == "arnav"
    assert entry["password"] == "hunter2"


def test_wrong_master_password_is_rejected(tmp_path):
    vault_path = tmp_path / "vault.dat"
    Vault.create(vault_path, "the-real-password")

    with pytest.raises(VaultError):
        Vault.load(vault_path, "a-wrong-guess")


def test_ciphertext_is_not_plaintext_on_disk(tmp_path):
    vault_path = tmp_path / "vault.dat"
    vault = Vault.create(vault_path, "master-key")
    vault.add_entry("bank.com", "arnav", "super-secret-password")

    raw = vault_path.read_text(encoding="utf-8")
    assert "super-secret-password" not in raw
    assert "arnav" not in raw


def test_delete_entry(tmp_path):
    vault_path = tmp_path / "vault.dat"
    vault = Vault.create(vault_path, "master-key")
    vault.add_entry("service-a", "user", "pass")
    vault.delete_entry("service-a")

    assert vault.list_services() == []
    with pytest.raises(VaultError):
        vault.get_entry("service-a")


def test_get_missing_entry_raises(tmp_path):
    vault_path = tmp_path / "vault.dat"
    vault = Vault.create(vault_path, "master-key")
    with pytest.raises(VaultError):
        vault.get_entry("does-not-exist")


def test_creating_vault_twice_fails(tmp_path):
    vault_path = tmp_path / "vault.dat"
    Vault.create(vault_path, "master-key")
    with pytest.raises(VaultError):
        Vault.create(vault_path, "master-key")


def test_persists_across_multiple_saves(tmp_path):
    vault_path = tmp_path / "vault.dat"
    vault = Vault.create(vault_path, "master-key")
    vault.add_entry("a", "u1", "p1")
    vault.add_entry("b", "u2", "p2")

    reloaded = Vault.load(vault_path, "master-key")
    assert reloaded.list_services() == ["a", "b"]
