from __future__ import annotations

import os
import sys
import tempfile
import unittest
from pathlib import Path

VAULT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VAULT_DIR))

import vault


class VaultTests(unittest.TestCase):
    def test_round_trip_and_wrong_password(self) -> None:
        payload = {"fields": {"timezone": "Etc/UTC"}, "created_at": "test"}
        document = vault.encrypt_payload(payload, "correct horse battery staple")
        self.assertEqual(
            vault.decrypt_payload(document, "correct horse battery staple"), payload
        )
        with self.assertRaises(vault.VaultError):
            vault.decrypt_payload(document, "wrong password")

    def test_tamper_detection(self) -> None:
        payload = {"fields": {"browser": "example"}}
        document = vault.encrypt_payload(payload, "a long testing passphrase")
        ciphertext = document["cipher"]["ciphertext"]
        document["cipher"]["ciphertext"] = (
            "A" if ciphertext[0] != "A" else "B"
        ) + ciphertext[1:]
        with self.assertRaises(vault.VaultError):
            vault.decrypt_payload(document, "a long testing passphrase")

    def test_atomic_write_and_permissions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "profile.vault.json"
            document = vault.encrypt_payload(
                {"fields": {}}, "a long testing passphrase"
            )
            vault.write_document(path, document)
            self.assertEqual(vault.read_document(path), document)
            if os.name != "nt":
                self.assertEqual(path.stat().st_mode & 0o777, 0o600)


if __name__ == "__main__":
    unittest.main()
