#!/usr/bin/env python3
"""
Command-line password manager backed by AES-256-GCM encryption.

Usage:
    python cli.py init                  # create a new vault, set master password
    python cli.py add <service>         # add/update credentials for a service
    python cli.py get <service>         # retrieve credentials for a service
    python cli.py list                  # list stored service names (not secrets)
    python cli.py delete <service>      # remove a service's credentials

All commands accept --vault PATH (default: ./vault.dat).
Master passwords and stored secrets are entered via getpass, never
echoed to the terminal or shell history.
"""
import argparse
import getpass
import sys
from pathlib import Path

from vault import Vault, VaultError


def cmd_init(args):
    path = Path(args.vault)
    master = getpass.getpass("Set a master password: ")
    confirm = getpass.getpass("Confirm master password: ")
    if master != confirm:
        print("Passwords didn't match.", file=sys.stderr)
        return 1
    if not master:
        print("Master password can't be empty.", file=sys.stderr)
        return 1
    Vault.create(path, master)
    print(f"Created new vault at {path}")
    return 0


def _open_vault(args) -> Vault:
    path = Path(args.vault)
    master = getpass.getpass("Master password: ")
    return Vault.load(path, master)


def cmd_add(args):
    vault = _open_vault(args)
    username = input(f"Username for '{args.service}': ")
    password = getpass.getpass(f"Password for '{args.service}': ")
    vault.add_entry(args.service, username, password)
    print(f"Saved credentials for '{args.service}'.")
    return 0


def cmd_get(args):
    vault = _open_vault(args)
    entry = vault.get_entry(args.service)
    print(f"Service:  {args.service}")
    print(f"Username: {entry['username']}")
    print(f"Password: {entry['password']}")
    return 0


def cmd_list(args):
    vault = _open_vault(args)
    services = vault.list_services()
    if not services:
        print("(vault is empty)")
    for service in services:
        print(f"- {service}")
    return 0


def cmd_delete(args):
    vault = _open_vault(args)
    vault.delete_entry(args.service)
    print(f"Deleted credentials for '{args.service}'.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AES-256 encrypted local password manager.")
    parser.add_argument("--vault", default="vault.dat", help="Path to the vault file (default: ./vault.dat)")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init", help="Create a new vault").set_defaults(func=cmd_init)

    add_parser = sub.add_parser("add", help="Add or update a service's credentials")
    add_parser.add_argument("service")
    add_parser.set_defaults(func=cmd_add)

    get_parser = sub.add_parser("get", help="Retrieve a service's credentials")
    get_parser.add_argument("service")
    get_parser.set_defaults(func=cmd_get)

    sub.add_parser("list", help="List stored service names").set_defaults(func=cmd_list)

    delete_parser = sub.add_parser("delete", help="Delete a service's credentials")
    delete_parser.add_argument("service")
    delete_parser.set_defaults(func=cmd_delete)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except VaultError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print()
        return 130


if __name__ == "__main__":
    sys.exit(main())
