# Assessment safety and answer separation

## Classify before using assessment material

Record whether each source is lecture/reference material, public practice,
released past work, inactive self-test, active ungraded practice, or active
graded/monitored assessment. If status is unclear, treat it conservatively and
ask only when that ambiguity changes what may be included.

## Safe construction rules

- Use stated objectives and concepts without copying unreleased live questions.
- For active assignments, teach the interface, concepts, and algorithm through
  a materially different input representation or problem instance.
- Do not create a drop-in submission, paste into the course, or submit on the
  learner's behalf.
- Do not disguise an assessment answer as a “practice” task with only names or
  numbers changed.
- Preserve exact starter signatures only when legitimately supplied and useful;
  keep the completed reference implementation separate.
- Do not include hidden answers in learner pages, PDF metadata, alt text,
  clipped frames, white text, or generator constants that a learner artifact
  imports at runtime.

## Learner/key boundary

Use either:

1. one PDF with a prominent stop page and all keys afterward; or
2. separate learner and answer-key PDFs.

The learner version must stand alone. The key may contain a complete solution
to an independent practice mirror, but must explain why and include a new
follow-up item. A key for an active graded task must not become a submission.

## Leakage audit

After generation:

1. extract PDF text;
2. extract document metadata and, when present, tagged-content alt text; scan
   both for answers, solution fragments, and live-assessment wording;
3. identify the first answer-key marker and verify its page;
4. search learner pages for completed expressions, answer labels, expected
   values, or reference-solution fragments;
5. inspect rendered pages for clipped/overlaid answers;
6. ensure learner-facing code does not import or read a solution module;
7. record the result in the final QA report.

If a legitimate example necessarily contains an answer, label it as a worked
example and place the independent task on a different instance.
