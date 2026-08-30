# Personal profile vault

This optional utility creates one encrypted JSON file for personal details on
Windows or macOS. It uses Scrypt for password-based key derivation and AES-256-GCM
for authenticated encryption. The master passphrase is never stored.

## Install

From the repository root:

```text
python -m pip install -r personal-vault/requirements.txt
```

## Create the vault

```text
python personal-vault/vault.py init private/profile.vault.json
```

Choose a long, unique passphrase and save it in your password manager. Losing
the passphrase means losing access to the vault; there is no recovery key.

## Store and retrieve fields

```text
python personal-vault/vault.py set private/profile.vault.json timezone
python personal-vault/vault.py list private/profile.vault.json
python personal-vault/vault.py get private/profile.vault.json timezone
python personal-vault/vault.py get private/profile.vault.json timezone --reveal
python personal-vault/vault.py delete private/profile.vault.json timezone
python personal-vault/vault.py change-password private/profile.vault.json
```

Passphrases and values are entered through hidden prompts, not command-line
arguments. `get` confirms that a field exists without revealing it unless
`--reveal` is supplied.

## Safety boundaries

- The whole `private/` directory and vault-file patterns are ignored by Git.
- Keep the vault in your own operating-system user directory, protected by
  FileVault on macOS or BitLocker/device encryption on Windows when available.
- Do not commit the vault, even though it is encrypted.
- Keep passwords, passkeys, MFA/recovery codes, authentication cookies/tokens,
  full government-ID numbers, and full payment or banking numbers in a trusted
  password manager or operating-system credential store—not this profile.
- Retrieve only the field needed for the current task. Avoid displaying values
  while recording, screen sharing, or streaming terminal output.
- The utility cannot protect an unlocked computer, malware running as your
  user, a weak/reused passphrase, or values copied into chat logs.

On macOS and Linux, the utility writes the vault with mode `0600`. Windows user
directories normally inherit per-user NTFS permissions; use device encryption
and do not place the file in a shared folder.
