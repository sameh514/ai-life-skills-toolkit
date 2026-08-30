# Workbook learning checklist

Score each important target before finalizing. All critical rows must pass.

| Dimension | Pass condition | Critical |
|---|---|---|
| Source grounding | Every course claim maps to a supplied source; invented material is labeled independent practice | Yes |
| Target form | The workbook names whether mastery is explanation, discrimination, tracing, calculation, debugging, or code construction | Yes |
| Concrete entry | A beginner-safe small case defines new terms on first use | Yes |
| Worked example | Unmet targets have steps with purpose/subgoal labels and checked state; targets already mastered on an unaided diagnostic may skip or compress this support | Yes |
| Fading | At least one task removes meaningful support without reducing the task to syntax guessing | Yes |
| Independent endpoint | A materially varied task can be completed without a key, word bank, supplied ordering, or copied solution | Yes |
| Feedback | Learner commits answer and confidence first; key explains earliest likely divergence | Yes |
| Later mixed checkpoint | A checkpoint separated from first practice by intervening topics repeats the target performance within the session | Yes |
| Spaced-review handoff | Each topic gets a suggested review date in a later session, so real spaced review can be scheduled | Yes when retention extends beyond the current session |
| Transfer | A new representation, input, edge case, or confusable neighbor is present | Yes |
| Answer boundary | Stop/key separation and leakage scan pass | Yes |
| Optional access tweaks | Any requested tweak is minimal, unobtrusive, and does not replace the core learning sequence | Yes only when explicitly requested or clearly useful |
| Code correctness | Reference and reconstructed blanked code pass normal and edge tests | Yes for code |
| Visual correctness | Every rendered page and diagram is inspected at readable scale | Yes |
| Delivery integrity | Requested delivered copy hash equals the verified local file | Yes when delivered |

## Confidence and error prompts

Use short prompts that drive a decision:

```text
Confidence before checking: ___ / 100
Earliest step I am unsure about: ____________________
After feedback, the violated rule was: ______________
New case that would expose this error: ______________
Next review: _______________________________________
```

Do not fill pages with generic reflection. Every prompt must either diagnose a
gap, select a scaffold, schedule a revisit, or improve transfer.

## Choose how much help to give

- Correct explanation and task: remove one support.
- Independent diagnostic success with sound reasoning: skip or compress the
  worked example and enter at faded or independent practice.
- Correct answer with weak reasoning or low confidence: keep/shorten delay and
  vary the case.
- Wrong concept twice: return to one smaller prerequisite.
- Sound model but syntax/API block: isolate a 5-10 minute language microdrill,
  then return to the domain task.
- If the learner needed a subgoal outline, a partly worked answer, or a full
  example, require a fresh unaided task before marking the topic complete.
