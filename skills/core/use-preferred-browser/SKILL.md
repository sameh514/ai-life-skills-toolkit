---
name: use-preferred-browser
description: Keep signed-in, personal, form, checkout, and handoff browser work in the user's chosen browser on Windows or macOS. Use when a page must be opened, shown, reviewed, signed into, or left ready for the user; do not switch browsers without the user's explicit approval.
---

# Use the Preferred Browser

Honor the user's browser choice as part of the task, not as a suggestion.

## Keep momentum

Use available context and safe, reversible defaults before asking for input.
Bundle non-blocking questions and continue useful work. Interrupt only when a
missing choice would change the result, privacy, cost, authority, safety, or
something hard to undo. Never repeat an answered question.

## Route the work

1. When no visible page or signed-in session is needed, prefer a direct data
   connection or command-line tool over opening any browser at all.
2. When the page must be visible, signed in, reviewed, or handed back, use the
   browser the user named in the current turn or their locally configured
   preference.
3. If no preference exists, use the operating system's default browser and say
   which browser was selected before any personal or account interaction.
4. Use background or automated browsers only for public, non-personal research
   or local web testing.

## Protect the handoff

- Never switch from the preferred browser to another browser merely because
  automation is easier there. Ask for explicit approval for that exact switch.
- If the preferred browser fails, retry safe transient recovery. If it remains
  unavailable, leave it at the exact destination when possible, report the
  blocker, and stop.
- Let the user enter passwords, passkeys, MFA codes, recovery codes, security
  answers, and protected operating-system prompts directly. Never read, copy,
  log, or store those values.
- A filled field, submitted request, processing indicator, and confirmed final
  result are different states. Verify the exact state the user requested.
- Before irreversible publication, purchase, deletion, submission, or account
  change, show the exact final state and obtain any approval the workflow
  requires.

## Platform notes

- macOS users may choose Safari, Chrome, Firefox, Edge, or another installed
  browser. Treat Safari as a hard requirement only when the user says so.
- Windows users may choose Edge, Chrome, Firefox, or another installed browser.
- Do not treat a browser-sync account, remote-desktop tool, or automation
  engine as permission to change the user's browser choice.
