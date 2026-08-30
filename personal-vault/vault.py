#!/usr/bin/env python3
"""Small cross-platform encrypted profile vault.

The vault uses Scrypt to derive a 256-bit key from a user-entered passphrase and
AES-GCM for authenticated encryption. Passphrases and field values are prompted
interactively so they do not enter shell history.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from cryptography.exceptions import InvalidTag
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
except ImportError as exc:  # pragma: no cover - exercised in dependency setup
    raise SystemExit(
        "Missing dependency 'cryptography'. Install personal-vault/requirements.txt first."
    ) from exc


FORMAT = "ai-life-skills-personal-vault"
VERSION = 1
AAD = f"{FORMAT}:v{VERSION}".encode()
KDF_N = 2**15
KDF_R = 8
KDF_P = 1
MAX_VAULT_BYTES = 4 * 1024 * 1024
KEY_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$")


class VaultError(Exception):
    """Raised for malformed vaults or failed authentication."""


def _b64encode(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def _b64decode(value: Any, label: str) -> bytes:
    if not isinstance(value, str):
        raise VaultError(f"Invalid {label}.")
    try:
        return base64.b64decode(value, validate=True)
    except (ValueError, TypeError) as exc:
        raise VaultError(f"Invalid {label}.") from exc


def _derive_key(passphrase: str, salt: bytes) -> bytes:
    if not passphrase:
        raise VaultError("Passphrase cannot be empty.")
    return Scrypt(salt=salt, length=32, n=KDF_N, r=KDF_R, p=KDF_P).derive(
        passphrase.encode("utf-8")
    )


def encrypt_payload(payload: dict[str, Any], passphrase: str) -> dict[str, Any]:
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = _derive_key(passphrase, salt)
    plaintext = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, AAD)
    return {
        "format": FORMAT,
        "version": VERSION,
        "kdf": {
            "name": "scrypt",
            "n": KDF_N,
            "r": KDF_R,
            "p": KDF_P,
            "salt": _b64encode(salt),
        },
        "cipher": {
            "name": "AES-256-GCM",
            "nonce": _b64encode(nonce),
            "ciphertext": _b64encode(ciphertext),
        },
    }


def decrypt_payload(document: dict[str, Any], passphrase: str) -> dict[str, Any]:
    if document.get("format") != FORMAT or document.get("version") != VERSION:
        raise VaultError("Unsupported or invalid vault format.")

    kdf = document.get("kdf")
    cipher = document.get("cipher")
    if not isinstance(kdf, dict) or not isinstance(cipher, dict):
        raise VaultError("Invalid vault structure.")
    if (
        kdf.get("name") != "scrypt"
        or kdf.get("n") != KDF_N
        or kdf.get("r") != KDF_R
        or kdf.get("p") != KDF_P
        or cipher.get("name") != "AES-256-GCM"
    ):
        raise VaultError("Unsupported vault parameters.")

    salt = _b64decode(kdf.get("salt"), "salt")
    nonce = _b64decode(cipher.get("nonce"), "nonce")
    ciphertext = _b64decode(cipher.get("ciphertext"), "ciphertext")
    if len(salt) != 16 or len(nonce) != 12 or len(ciphertext) < 16:
        raise VaultError("Invalid vault parameters.")

    try:
        plaintext = AESGCM(_derive_key(passphrase, salt)).decrypt(
            nonce, ciphertext, AAD
        )
        payload = json.loads(plaintext.decode("utf-8"))
    except (InvalidTag, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise VaultError("Unable to unlock vault.") from exc
    if not isinstance(payload, dict) or not isinstance(payload.get("fields"), dict):
        raise VaultError("Invalid decrypted profile structure.")
    return payload


def read_document(path: Path) -> dict[str, Any]:
    try:
        size = path.stat().st_size
    except FileNotFoundError as exc:
        raise VaultError(f"Vault does not exist: {path}") from exc
    if size > MAX_VAULT_BYTES:
        raise VaultError("Vault is unexpectedly large; refusing to open it.")
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise VaultError("Vault is not valid JSON.") from exc
    if not isinstance(document, dict):
        raise VaultError("Invalid vault structure.")
    return document


def write_document(path: Path, document: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(document, indent=2, sort_keys=True) + "\n"
    temp_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as stream:
            temp_name = stream.name
            stream.write(text)
            stream.flush()
            os.fsync(stream.fileno())
        if os.name != "nt":
            os.chmod(temp_name, 0o600)
        os.replace(temp_name, path)
        temp_name = None
        if os.name != "nt":
            os.chmod(path, 0o600)
    finally:
        if temp_name:
            try:
                os.unlink(temp_name)
            except FileNotFoundError:
                pass


def _new_passphrase() -> str:
    first = getpass.getpass("New master passphrase (12+ characters): ")
    second = getpass.getpass("Confirm master passphrase: ")
    if first != second:
        raise VaultError("Passphrases did not match.")
    if len(first) < 12:
        raise VaultError("Use a master passphrase of at least 12 characters.")
    return first


def _unlock(path: Path) -> tuple[dict[str, Any], str]:
    passphrase = getpass.getpass("Master passphrase: ")
    return decrypt_payload(read_document(path), passphrase), passphrase


def _stamp(payload: dict[str, Any]) -> None:
    payload["updated_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")


def command_init(path: Path) -> None:
    if path.exists():
        raise VaultError(f"Refusing to overwrite existing vault: {path}")
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    payload = {"created_at": now, "updated_at": now, "fields": {}}
    write_document(path, encrypt_payload(payload, _new_passphrase()))
    print(f"Created encrypted vault: {path}")


def command_set(path: Path, key: str) -> None:
    if not KEY_RE.fullmatch(key):
        raise VaultError(
            "Field names may contain letters, numbers, dots, dashes, and underscores."
        )
    payload, passphrase = _unlock(path)
    value = getpass.getpass(f"Value for {key} (input hidden): ")
    payload["fields"][key] = value
    _stamp(payload)
    write_document(path, encrypt_payload(payload, passphrase))
    print(f"Stored field: {key}")


def command_list(path: Path) -> None:
    payload, _ = _unlock(path)
    for key in sorted(payload["fields"]):
        print(key)


def command_get(path: Path, key: str, reveal: bool) -> None:
    payload, _ = _unlock(path)
    fields = payload["fields"]
    if key not in fields:
        raise VaultError(f"Field not found: {key}")
    if not reveal:
        print(f"Field exists: {key}. Add --reveal only when the screen is private.")
        return
    print(fields[key])


def command_delete(path: Path, key: str) -> None:
    payload, passphrase = _unlock(path)
    if key not in payload["fields"]:
        raise VaultError(f"Field not found: {key}")
    confirmation = input(f"Type DELETE to remove {key}: ")
    if confirmation != "DELETE":
        raise VaultError("Deletion cancelled.")
    del payload["fields"][key]
    _stamp(payload)
    write_document(path, encrypt_payload(payload, passphrase))
    print(f"Deleted field: {key}")


def command_change_password(path: Path) -> None:
    payload, _ = _unlock(path)
    _stamp(payload)
    write_document(path, encrypt_payload(payload, _new_passphrase()))
    print("Master passphrase changed.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="Create a new empty encrypted vault")
    init.add_argument("vault", type=Path)

    set_field = sub.add_parser("set", help="Store or replace one field")
    set_field.add_argument("vault", type=Path)
    set_field.add_argument("key")

    list_fields = sub.add_parser("list", help="List field names without values")
    list_fields.add_argument("vault", type=Path)

    get_field = sub.add_parser("get", help="Check or reveal one field")
    get_field.add_argument("vault", type=Path)
    get_field.add_argument("key")
    get_field.add_argument("--reveal", action="store_true")

    delete = sub.add_parser("delete", help="Delete one field")
    delete.add_argument("vault", type=Path)
    delete.add_argument("key")

    change = sub.add_parser("change-password", help="Re-encrypt with a new passphrase")
    change.add_argument("vault", type=Path)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "init":
            command_init(args.vault)
        elif args.command == "set":
            command_set(args.vault, args.key)
        elif args.command == "list":
            command_list(args.vault)
        elif args.command == "get":
            command_get(args.vault, args.key, args.reveal)
        elif args.command == "delete":
            command_delete(args.vault, args.key)
        elif args.command == "change-password":
            command_change_password(args.vault)
    except VaultError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
