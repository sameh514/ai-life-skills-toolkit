---
name: use-private-profile-safely
description: Handle optional local user preferences and encrypted personal-profile fields without exposing them to Git, logs, screenshots, or unrelated tasks. Use when a user asks to create, store, retrieve, or apply personal information through this toolkit.
---

# Use a Private Profile Safely

Use the minimum personal information needed for the current task. A user profile
is not blanket permission to inspect every stored field.

## Keep momentum

Use known non-sensitive context and safe, reversible defaults before asking for
input. Bundle non-blocking questions and continue useful work. Interrupt only
when a missing choice would change the result, privacy, cost, authority,
safety, or something hard to undo — and never treat convenience as permission
to reveal private data. Never repeat an answered question or request access to
fields the task does not need.

## Choose the storage tier

1. Put non-sensitive preferences such as operating system, preferred browser,
   timezone, teaching style, and desired access supports in a local copy of
   `config/preferences.example.json` named `config/preferences.local.json`.
2. Put genuinely personal details in the encrypted vault created by
   `personal-vault/vault.py`.
3. Keep passwords, passkeys, MFA/recovery codes, authentication tokens, full
   government-ID numbers, and complete payment or bank numbers in a trusted
   password manager or operating-system credential store instead.

Both the local preferences file and encrypted vault patterns are ignored by
Git. Never weaken or remove those ignore rules while real personal data exists.

## Access boundary

- Obtain explicit permission for the exact profile field needed.
- Never ask the user to paste the master passphrase into chat or a command-line
  argument. The user enters it directly into the local hidden prompt.
- Never inspect the entire vault merely to answer a question about one field.
- Prefer `list` for field names and `get` without `--reveal` when existence is
  enough. Reveal a value only on a private screen and only when required.
- Do not repeat personal values in logs, screenshots, generated examples,
  issue reports, commits, or final summaries.
- Treat stored dates and statuses as potentially stale. Recheck live state
  before an account, medical, legal, financial, renewal, or submission action.

## Local commands

Run from the repository root:

```text
python personal-vault/vault.py list private/profile.vault.json
python personal-vault/vault.py get private/profile.vault.json field.name
```

The user must run any command that prompts for the master passphrase. If the
task cannot continue without exposing a protected value, stop and explain the
safe handoff instead of bypassing encryption.
