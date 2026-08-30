# Make Your Own Skill

You do not need to code. Start with one task you already ask an AI assistant to
help with, then turn the parts that worked into a small reusable instruction
file.

## What Sameh created

Sameh started by using AI as external structure for life with ADHD: hold the
task state, make the next action visible, resume after interruptions, and verify
the real ending. Over time, repeated school and life-admin workflows became the
eight general skills in this repository. Personal details were removed, the
remaining examples were made generic, and an optional local encrypted vault was
added so private information never has to live in the public skill files.

The finished toolkit has four parts:

- eight reusable `SKILL.md` instruction files;
- simple trigger phrases that sound like normal requests;
- Windows and macOS installation and tests; and
- clear privacy, approval, and completion boundaries.

## The process

1. Pick one recurring problem, not your whole life.
2. Ask the assistant to help with the real task once.
3. Tell it what was helpful, confusing, too slow, or too interruptive.
4. Repeat the task until the useful steps and boundaries are predictable.
5. Ask the assistant to turn that working process into one `SKILL.md` file.
6. Test the skill on a fresh example. Notice where it asks unnecessary
   questions, assumes too much, or stops before the result is verified.
7. Replace personal details with clear placeholders and run a privacy check.
8. Save three phrases you would naturally say when you want the skill.

## Copy this prompt

> I want to turn something I keep asking you for into a reusable “skill,” which
> is a small instruction file. Use our available conversation and files first.
> Interview me one question at a time only when an answer is truly needed.
> Bundle non-blocking questions, keep doing safe useful work while waiting, and
> never repeat a question I already answered. Interrupt me only if a missing
> choice would materially change the result, expose private information, spend
> money, grant new authority, or trigger an irreversible action.
>
> Find out: (1) the recurring task and what a finished result looks like, (2)
> three plain-English phrases I would naturally say when I want it, (3) the
> steps that worked well last time, (4) everything you must show me or ask me
> before doing—such as sending, buying, submitting, deleting, publishing, or
> changing an account—and (5) what the skill must never do.
>
> Then write one `SKILL.md` file with a short lowercase name joined by hyphens,
> a one-sentence description beginning with “Use when,” steps in plain language,
> a short “Keep momentum” section, and a “Never” list. Use safe, reversible
> defaults where possible. Keep the main file under one page; put optional
> technical detail in a separate reference only if it is genuinely needed.
>
> Before showing me the final file, remove names, addresses, emails, phone
> numbers, account numbers, usernames in file paths, private school or medical
> details, credentials, and conversation history. Use obvious placeholders
> instead. End by repeating my three trigger phrases and giving me one fresh
> test task.

## What the file should look like

```markdown
---
name: my-recurring-task
description: Use when the user asks for help with [one clear kind of task].
---

# My Recurring Task

## Keep momentum

Use known context and safe, reversible defaults. Bundle non-blocking questions,
continue useful work, and interrupt only for a choice that truly changes the
outcome or requires the user’s authority.

## Steps

1. [First useful action]
2. [How to check the result]
3. [When to stop]

## Never

- [Private, unsafe, or out-of-scope action]
```

## Test before sharing

- Does each of your three natural phrases activate the right skill?
- Can a stranger understand the description without specialist language?
- Does the assistant begin useful work without a long questionnaire?
- Does it reuse answers and avoid unnecessary interruptions?
- Does it ask before sending, buying, submitting, deleting, publishing, or
  changing an account?
- Does it state the exact completion status instead of guessing?
- Did you replace every personal detail with a placeholder?
- Does the skill work with both Windows and macOS paths and commands, or clearly
  state a real platform limit?

For this repository’s automated checks, place the new skill in its own folder
under `skills/core/`, then run:

```text
python scripts/validate_skills.py
python scripts/privacy_scan.py
python scripts/check_markdown_links.py
```

Share the skill file and generic examples. Keep your private profile, vault,
source documents, conversations, and credentials on your own computer.
