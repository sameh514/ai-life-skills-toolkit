# Security policy

## Reporting a vulnerability

Use a private GitHub security advisory when available. Do not open a public
issue containing a real vault, passphrase, personal profile value, credential,
token, private path, or exploit transcript.

## Vault threat model

The vault protects the file contents at rest with authenticated encryption and
a user-entered passphrase. It does not protect against:

- malware or another process running as the same operating-system user;
- an unlocked or compromised computer;
- a weak, reused, observed, or phished passphrase;
- values copied into chat, terminal logs, screenshots, clipboard history, or
  unencrypted backups;
- permanent loss of the passphrase.

Use FileVault, BitLocker, or device encryption when available, keep the system
patched, and store the vault passphrase in a trusted password manager.

## Supported versions

Until formal releases exist, only the latest commit on the default branch is
maintained. Review changes before updating a local installation.
