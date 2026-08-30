# Start Here

A skill is a small plain-text file that tells an AI assistant how to handle one
kind of task. You do not have to memorize commands: install the skills once,
then ask in ordinary language.

## Your first try

1. On the GitHub page, click the green **Code** button, choose **Download ZIP**,
   and unzip it.
2. Install [Python 3.10 or newer](https://www.python.org/downloads/). Open
   Terminal on a Mac or PowerShell on Windows in the unzipped folder and paste:

   ```text
   python scripts/install_skills.py
   ```

   On Windows, use `py` instead of `python` if needed. You should see eight
   `INSTALLED` lines.
3. Open Codex and say:

   > My kettle stopped working and it is under warranty. Use the
   > customer-service skill to help me get a replacement. Show me every message
   > before it is sent.

The assistant should use one calm message at a time, share only approved
details, ask for approval before sending, and keep going until the exact result
is confirmed. It should use known context and safe defaults instead of stopping
for small questions.

If you use another AI assistant that accepts instruction files, attach the
chosen `SKILL.md` file with your request.

## What can I say?

| If you want to… | Say something like… |
|---|---|
| Make a practice workbook | “Make me a practice workbook from these notes.” · “Turn this chapter into a fill-in worksheet.” · “Give me printable practice with answers at the back.” |
| Make or improve slides | “Help me make slides for this talk.” · “Turn this document into a PowerPoint.” · “Review my deck before I present it.” |
| Correct handwritten notes | “Fix the mistakes in these handwritten notes.” · “Clean up this photo of my notes.” · “Redraw this diagram, but correct it.” |
| Make a study podcast | “Turn my notes into a podcast for a walk.” · “Make an audio study guide from this chapter.” · “Help me review this course while I exercise.” |
| Handle customer support | “Help me deal with customer support.” · “Help me get a refund or replacement.” · “Draft a message to the store about this problem.” |
| Learn interactively | “Teach me this topic step by step.” · “Tutor me and quiz me as I learn.” · “Continue my last lesson.” |
| Keep the right browser | “Open this in my usual browser.” · “Use my browser and do not switch.” · “Leave the signed-in page ready for me.” |
| Use a private saved detail | “Save this detail privately for later.” · “Use my saved timezone without showing it.” · “Check whether that detail is in my private vault.” |

## What should I expect from the assistant?

- One clear next action instead of a wall of setup questions.
- Non-blocking questions bundled together while safe work continues.
- No repeated question when the answer is already available.
- A pause when privacy, money, authority, or an irreversible action is involved.
- A precise status such as drafted, sent, processing, confirmed, or resolved.

## Keep personal information private

Do not type personal details into this public repository. Non-sensitive local
preferences go in `config/preferences.local.json`; selected private details can
go in the optional encrypted vault described in
[`personal-vault/README.md`](personal-vault/README.md). Passwords, MFA codes,
tokens, full IDs, and full financial details belong in a password manager or
operating-system credential store.

Ready to make a skill for your own recurring task? Continue with
[`MAKE_YOUR_OWN_SKILL.md`](MAKE_YOUR_OWN_SKILL.md).
