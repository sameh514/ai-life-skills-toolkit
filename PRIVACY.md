# Privacy model

## Never publish

- raw Codex or ChatGPT memory databases and conversation logs;
- names, private contact details, addresses, precise location history, or local
  home-directory paths;
- account identifiers, credentials, cookies, tokens, recovery codes, or private
  browser state;
- grades, school accounts, protected course sources, live quiz wording, answer
  keys, or assignment solutions;
- medical records, prescription details, full government IDs, or full financial
  account and payment-card numbers.

## Storage tiers

1. Public repository: generalized skills, synthetic examples, and documentation.
2. Local ignored preferences: non-sensitive settings in
   `config/preferences.local.json`.
3. Encrypted local vault: selected personal fields in a generated
   `*.vault.json` file.
4. Password manager or operating-system credential store: passwords, passkeys,
   MFA/recovery codes, tokens, full IDs, and complete financial credentials.

## Data minimization

Access to one field does not authorize access to the entire profile. Retrieve
only the minimum needed for the current task, do not echo it unnecessarily, and
do not copy it into logs, screenshots, issues, examples, commits, or reports.

## Before publishing

Run `python scripts/privacy_scan.py`, inspect `git status`, review every staged
file, and run an independent secret scanner when available. Automated scanning
cannot identify every contextual disclosure, so a human review remains
required.
