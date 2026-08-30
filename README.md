# AI Life Skills Toolkit

[![Tested on Windows and macOS](https://github.com/sameh514/ai-life-skills-toolkit/actions/workflows/validate.yml/badge.svg)](https://github.com/sameh514/ai-life-skills-toolkit/actions/workflows/validate.yml)

Eight reusable “skills”: small instruction files that teach an AI assistant to
handle an everyday task the same careful way each time. They cover studying,
presentations, customer service, browser handoffs, and keeping personal details
private.

This grew from how Sameh uses AI to make life with ADHD more manageable: make a
large task easier to start, keep track of where it stopped, show one useful next
action, and verify when it is truly finished. The AI provides structure; the
person still learns, decides, approves, and owns the result.

No private conversations, names, addresses, account details, course files,
grades, medical records, credentials, or assessment answers are included.

## Start here

- New to skills? Read [`START_HERE.md`](START_HERE.md). It explains what a skill
  is, how to install one on Windows or macOS, and what to say first.
- Want to make one for your own recurring task? Read
  [`MAKE_YOUR_OWN_SKILL.md`](MAKE_YOUR_OWN_SKILL.md). It walks through Sameh’s
  process and gives you one prompt to copy.

## The eight skills

| Skill | What it helps with |
|---|---|
| `build-course-fill-in-workbook` | Turn course material into printable practice with answers kept at the back |
| `build-effective-powerpoint-decks` | Make or improve a clear PowerPoint for a real audience |
| `correct-handwritten-study-notes` | Correct and redraw notes without losing the learner’s style |
| `create-course-study-podcast` | Turn course material into a plainspoken audio review with recall pauses |
| `customer-service` | Handle refunds, replacements, repairs, billing, and support follow-up calmly |
| `run-adaptive-teaching-session` | Learn one step at a time, with checks before moving on |
| `use-preferred-browser` | Keep personal browser work in the browser the user chose |
| `use-private-profile-safely` | Use only the minimum locally stored personal information a task needs |

Windows and macOS install the same eight skills. See
[`docs/PLATFORM_SUPPORT.md`](docs/PLATFORM_SUPPORT.md) for details and limits.

## Project goals

- Be understandable to someone who is not technical.
- Help with ordinary learning and life-admin tasks.
- Work the same way on Windows and macOS wherever possible.
- Minimize interruptions: use known context and safe, reversible defaults,
  bundle non-blocking questions, keep useful work moving, and never repeat a
  question already answered.
- Interrupt only when a missing choice could change the result, expose private
  information, spend money, grant authority, or trigger an irreversible action.
- Keep consequential actions reviewable. The person approves sending, buying,
  submitting, deleting, publishing, and account changes.
- Store no personal information in the public repository.
- Make completion visible and verifiable instead of stopping at “started.”
- Help anyone turn a successful repeated workflow into their own safe skill.

## Install on Windows or macOS

You do not need Git. On the GitHub page, click the green **Code** button, choose
**Download ZIP**, and unzip it. Install [Python 3.10 or newer](https://www.python.org/downloads/),
then open Terminal on a Mac or PowerShell on Windows in the unzipped folder.

Preview what will be installed:

```text
python scripts/install_skills.py --dry-run
```

Install the eight skills:

```text
python scripts/install_skills.py
```

On Windows, use `py` instead of `python` if needed. Existing skills are skipped;
using `--replace` first makes a dated backup. These commands install into Codex.
For another assistant that accepts instruction files, attach the chosen
`SKILL.md` file with your request.

## Store personal information safely

Never put real personal information in this repository.

- For non-sensitive preferences, copy `config/preferences.example.json` to
  `config/preferences.local.json`. Git ignores the local copy.
- For selected personal details, use the optional encrypted vault:

```text
python -m pip install -r personal-vault/requirements.txt
python personal-vault/vault.py init private/profile.vault.json
python personal-vault/vault.py set private/profile.vault.json timezone
python personal-vault/vault.py list private/profile.vault.json
```

The vault creates an encrypted AES-256-GCM file protected by a master
passphrase. Git ignores it, but it still stays only on the user’s computer. Read
[`personal-vault/README.md`](personal-vault/README.md) before using it.

Passwords, passkeys, recovery codes, authentication tokens, full ID numbers,
and complete payment or bank details do not belong in this profile. See
[`PRIVACY.md`](PRIVACY.md) for the safe storage choices.

## Check privacy before publishing

Run:

```text
python scripts/privacy_scan.py
```

The scanner catches common personal paths, contact patterns, keys, and tokens.
It cannot catch every contextual detail, so review each file before publishing.

## More detail

- [`docs/LEARNINGS.md`](docs/LEARNINGS.md): why the workflows are designed this way
- [`docs/PLATFORM_SUPPORT.md`](docs/PLATFORM_SUPPORT.md): Windows and macOS support
- [`PRIVACY.md`](PRIVACY.md): what never belongs in the repository or vault
- [`SECURITY.md`](SECURITY.md): reporting security problems

## Boundaries

These are templates, not medical, legal, or financial advice. They do not
bypass authentication, authorize purchases or publication, or let an agent
submit graded work. Users review outputs and approve consequential actions.

## License

Repository material is available under the MIT License.
