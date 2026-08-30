---
name: correct-handwritten-study-notes
description: Correct and redraw handwritten notes or diagrams while keeping the learner's style and original files. Use when the user wants a note image transcribed, corrected, cleaned up, or rebuilt into a workbook or PDF.
---

# Correct Handwritten Study Notes

Preserve the learner's visual language while correcting the actual ideas. The
goal is not a pretty transcription; it is a technically accurate teaching
artifact that still feels like the learner's notes.

## Keep momentum

Use available context and safe, reversible defaults before asking for input.
Bundle non-blocking questions and continue useful work. Interrupt only when a
missing choice would change the result, privacy, cost, authority, safety, or
something hard to undo. Never repeat an answered question.

## Inspect and ground

1. Inventory every supplied PDF and image. Render PDFs and inspect every source
   page visually before making corrections.
2. Transcribe the visible claims, diagrams, arrows, examples, and uncertainties.
   Do not silently guess illegible technical content.
3. Ground corrections in the supplied course transcript, lecture slides,
   assignment instructions, starter code, or another authoritative source.
   Keep analogies visibly labeled as analogies.
4. Identify the learner's misconception and build the corrected page around one
   beginner-first mental model.

## Plan the corrected visual

- Define exact required text and exact diagram topology before generation.
- Separate BEFORE and AFTER states. Avoid leaving crossed-out historical items
  inside a live state unless “old/historical” is unmistakable.
- Use one strong memory rule near the bottom.
- Prefer white ruled paper, black marker, and restrained blue, green, red, or
  pale-yellow accents when matching the learner's established style.
- Keep text sparse, large, and phone-readable.
- Preserve exact technical names, numbers, labels, code identifiers, and arrow
  directions from the source.

Read [image-prompt-pattern.md](references/image-prompt-pattern.md) before using
image generation.

## Generate and verify

1. Use the available image-generation skill for bitmap note redraws. Provide
   the original page as the content reference and an established corrected page
   as a style reference when available.
2. Request exact labels and explicitly forbid extra nodes, arrows, cards, or
   invented facts when diagram topology matters.
3. Inspect the generated image at high or original detail. Verify every word,
   number, prefix, path, branch, state, and result against the source material.
4. Reject and regenerate any image with a spelling error, contradictory state,
   misleading crossed-out item, or logically impossible diagram. A visually
   attractive image is not acceptable if its semantics are wrong.
5. Save the final PNG under a stable project path such as `output/imagegen/`.
   Leave the generator's original output in place unless the user requests
   deletion.
6. If the corrected note belongs in a workbook or PDF, rebuild that derived
   artifact and repeat its full render-and-inspect workflow.
7. Copy the corrected image and rebuilt derivatives to the requested shared or
   mobile destination. Preserve every original note file unchanged.

## Handling later note changes

- Treat the user's newest correction as authoritative for intent, but verify
  technical claims against course sources.
- Update the derived PNG, workbook, guide, and generator prompt/script that are
  materially affected; do not patch only one visible copy and leave the others
  inconsistent.
- Use versioned or descriptive filenames unless the user explicitly requests a
  replacement.
- Report which originals were preserved and which derived files changed.

## Established examples

Read [established-examples.md](references/established-examples.md) when matching
an existing note style or updating a derived note set.
