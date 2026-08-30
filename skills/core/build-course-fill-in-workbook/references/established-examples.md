# Shareable workbook pattern

## Isolation guard

Do not inspect a completed workbook, generator, answer key, visual guide, or
reference solution during an independent forward test or a source-only build.
Work only from the explicitly authorized raw sources and write to a separate
test directory. For ordinary style matching, record every prior artifact that
was inspected in the workbook's record of sources.

## Recommended project layout

```text
course-project/
|-- sources/                 Raw authorized course material
|-- scripts/                 Deterministic builders and validators
|-- tests/                   Executable checks for code or calculations
|-- output/
|   |-- pdf/                 Final learner-facing workbook
|   `-- renders/             Page images used only for visual QA
`-- delivery/                Optional user-requested copies
```

The established pattern uses beginner-first explanations, corrected visuals,
real code blanks, generous handwriting areas, learner pages before a full stop,
and diagnostic answer keys afterward. Use executable tests for code and
calculations, inspect every rendered page, and compare file hashes after any
requested copy.

For fill-in-the-blank activities, keep a visible candidate-answer bank on the
same page as the blanks. Scramble entries out of answer order and mix plausible
distractors with the correct options.
