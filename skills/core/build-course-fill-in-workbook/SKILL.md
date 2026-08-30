---
name: build-course-fill-in-workbook
description: Turn course notes, slides, or homework into a printable practice workbook with examples first, less help over time, and answers kept behind a clear STOP page. Use when the user wants safe practice rather than answers to live graded work.
---

# Build Course Fill-In Workbook

Turn the user's course material into a printable practice workbook: worked
examples first, then practice with less and less help, then one independent
task, with every answer kept behind a clear STOP page.

## Keep momentum

Use available context and safe, reversible defaults before asking for input.
Bundle non-blocking questions and continue useful work. Interrupt only when a
missing choice would change the result, privacy, cost, authority, safety, or
something hard to undo. Never repeat an answered question.

## Read the right reference first

- [learning-design-rubric.md](references/learning-design-rubric.md) before
  planning the practice sequence.
- [assessment-safety.md](references/assessment-safety.md) whenever the sources
  include quizzes, homework, tests, or unclear assessment status.
- [layout-and-qa.md](references/layout-and-qa.md) before laying out or checking
  the PDF.
- [evidence-basis.md](references/evidence-basis.md) only when explaining why
  the learning design works.
- [established-examples.md](references/established-examples.md) only when
  matching the shared workbook pattern or project layout.

## Build from the user's material

1. Collect the supplied notes, slides, transcripts, instructions, starter code,
   and visible tests. Keep every original file unchanged.
2. Keep a simple record of where each claim came from: seen in a source,
   calculated, a teaching choice, or uncertain. If the course already has a
   shared source folder (approved sources, key terms and pronunciations, and
   what is graded), reuse it so the workbook and any matching study podcast
   agree. Ask instead of guessing when a source is ambiguous.
3. Name what the learner should be able to do afterward — explain, trace,
   calculate, debug, or write — and open with one small concrete example,
   defining each new term where it first appears.
4. Follow the rubric's progression: worked example, then practice with fading
   help, then one independent task the learner can finish with no answers in
   sight. Skip support the learner has already shown they do not need.
5. Keep learner pages before a prominent STOP page and every answer after it,
   or in a separate answer file.
6. End with a mixed checkpoint, and list each topic with a suggested date to
   review it again in a later session. A same-session checkpoint is not real
   spaced review, so do not describe it as one.

## Check the content

- For code or calculations, build the complete solution separately, run the
  supplied tests plus sensible edge cases, and confirm the blanked version can
  be rebuilt from the answer key and still passes the same tests.
- Check every diagram and step-by-step trace against the source or the running
  code. Keep BEFORE and AFTER states clearly separate.
- Scan learner pages for leaked answers, hidden text, and live-assessment
  wording.

## Check the finished PDF

Follow the layout-and-QA reference: render every page, inspect each one at a
readable size, confirm the STOP/answer boundary, and rerun the code checks
after the final edit. If the user asked for a copy somewhere else, confirm the
delivered copy matches the checked one.

Report what was checked and anything that was not. "Generated" is not
"verified," and never invent measurements of how the learner did.
