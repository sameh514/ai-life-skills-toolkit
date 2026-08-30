# Layout and QA Pattern

## Recommended topic arc

1. Target and prerequisite check with 0-100 confidence.
2. Corrected full-page visual or worked example with one invariant.
3. Explanation and trace practice while the answer is visible.
4. Faded completion/code-ordering practice.
5. Independent, materially varied task with no key visible.
6. Error/confidence log and a later mixed checkpoint; schedule genuine delayed
   retrieval outside the workbook for a later session.
7. Explicit stop page.
8. Separated answer key with reasoning and a discriminating follow-up.

For a multi-function assignment, give each function its own diagram and
worksheet. Put all answer keys after the final practice page.

## Visual rules

- Use large type and high contrast suitable for printing or phone zoom.
- Keep related state together but separate BEFORE and AFTER explicitly.
- Do not use a crossed-out live card inside an AFTER state unless a label says
  it is a historical ghost; separate panels are clearer.
- Favor one main diagram per page over several tiny diagrams.
- Keep one instruction and one visible next action per panel.
- Show section/page progress. Add a written resume line only when interruption
  is an identified barrier; do not repeat it in every footer by default.
- Externalize multi-step state in tables or diagrams; do not require the learner
  to remember prior packet/code state while calculating the next state.
- Avoid decorative clutter, low-contrast accents, unnecessary icons, and dense
  sidebars. Color must not be the only carrier of meaning.
- Put answer blanks close to the relevant prompt. Avoid split attention between
  distant diagrams, instructions, and answer areas.
- Use at least 9 pt body text for print when possible and larger labels for
  phone zoom. Code must remain readable without horizontal clipping.
- Use ASCII hyphens unless the chosen embedded font is verified to cover every
  glyph.

## Required QA

- Every code line fits at 100% zoom.
- Blanks are long enough for the expected token.
- Word-bank entries are readable and may wrap intentionally.
- Writing lines are evenly spaced and preserve indentation cues.
- Answer keys do not appear before the stop point.
- Learner-page text extraction contains no hidden answer key, white-on-white
  answer, clipped overflow, or reference-solution code.
- Every diagram label and state transition matches the source and code.
- Completed code executes and edge cases pass.
- Reconstructed blanked code executes against the same tests.
- Confidence prompts occur before feedback, at least one later mixed checkpoint
  measures unaided performance in the target form, and retention targets are
  handed to a dated cross-session review schedule.
- Page order preserves visible example -> faded practice -> independent task ->
  stop -> key.
- Every PDF page is rendered and visually inspected after the final edit.
- Delivered copies match the verified local artifact.

## Choose the checking level

Use the **full check** for any workbook containing code, multi-step traces, an
answer key, or six or more pages. It requires every check above, every-page
zoomed inspection, the complete code test matrix, key-boundary auditing, and
hash-verified delivery when requested.

Use the **light check** only for a 1–2 page practice sheet with no answer key.
It still requires text and metadata leakage scans, every-page rendering and
inspection, blank length and writing-space checks, and execution of any code
that appears. Do not use the light check merely because a deadline is tight.

## Every-page inspection record

Record page number, expected role, and result. Contact sheets are useful for
overview but do not replace zoomed inspection of code, tables, or small labels.
For each page check:

- clipping/overflow and accidental overlap;
- font size, contrast, whitespace, and phone/print legibility;
- one clear action and enough writable space;
- semantic correctness of arrows, state, and sequence;
- answer leakage and boundary placement;
- consistent page count, headings, and footers.
