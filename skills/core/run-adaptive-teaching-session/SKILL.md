---
name: run-adaptive-teaching-session
description: 'Teach technical, mathematical, or course material one step at a time: set a goal, check what the learner already knows, teach one step, and check again before moving on. Use for "teach me," "tutor me," "walk me through," "quiz me as I learn," or continuing a lesson. Do not use for a one-off explanation or for making a workbook or podcast.'
---

# Run Adaptive Teaching Session

Tutor live, one step at a time. The learner does the real thinking; this skill
handles the order of steps, the sources, and the session state. A quick correct
answer is progress in the session, not proof the learning will last.

## Keep momentum

Use available context and safe, reversible defaults before asking setup
questions. Bundle non-blocking questions and never repeat an answered question.
A learning check that is part of the lesson is intentional, not an
interruption; otherwise interrupt only when a missing choice would change the
result, privacy, cost, authority, or safety.

## Start or resume

1. Agree on the topic and one observable goal: explain, tell apart, trace,
   calculate, prove, debug, or build. If the goal is broad, propose a small
   first target and say it is provisional.
2. Reuse any existing lesson plan, shared source folder, or earlier session
   state instead of rebuilding it.
3. For course material, note which sources are allowed and what is graded.
   Teach with fresh, similar practice; never reveal, complete, or submit active
   graded work.
4. Keep track of where facts come from. When stakes are high, check a real
   source; another AI agreeing is not independent verification.

When resuming, restate where the last session actually ended: the last thing
the learner did alone, the current step, any open confusion, and the next
planned check. Never infer those from the learner merely having read or
finished something.

## Check before teaching

Start with the smallest unaided attempt that can change the plan — usually one
question in the target form. Ask for a committed answer and a 0–100 confidence
before giving feedback, and accept "I don't know" as useful information.
Multiple choice can locate a mix-up, but recognizing an answer is not the same
as being able to explain, calculate, or build one.

Find the earliest real gap: a missing definition or prerequisite, a wrong
mental model, lost track of state, a math or syntax slip, a weak process for
building or debugging, an attention slip, or too much reliance on hints. If the
learner already succeeds alone with sound reasoning, skip ahead to a varied
challenge instead of reteaching.

## Show a small map

Before extended teaching, show a short plain map of what is known, what is
next, and what comes later. An indented list is fine; use a diagram only when
it genuinely helps and the surface can display it. Treat the map as a working
guess and update it from the learner's actual performance.

## Teach in one-step turns

Repeat at the current step:

1. Connect the step to what the learner just showed they know, and say why it
   is needed.
2. Start concrete: one example, trace, or problem before the formal term.
3. Explain one move, not the whole chain. Define new notation where it first
   appears.
4. Ask the learner to predict, explain, calculate, or build something — one
   question, then stop and wait. Never answer for the learner.
5. Give specific feedback on the committed answer and the reasoning behind it.
6. Adapt: advance, vary the example, shrink the step, or reopen a
   prerequisite.

Give the least help that works, in rough order: restate the goal; write down
the current state; prompt for the governing rule; give one hint; outline the
subgoals; give a partly worked version; show a full worked example. After
heavy help, require a fresh unaided attempt before counting the step as
learned. If the same confusion returns, stop advancing, shrink the step to one
small move, repair it, and retest.

Prefer the simplest aid that makes the idea clear — a diagram, table, trace,
or runnable example — and verify code, calculations, and diagrams against a
source, a test, or direct inspection before relying on them.

## Keep light session state

Track, and show after a meaningful change or on request: the goal, the allowed
sources, the map, the current step, the last thing done unaided, confidence,
the heaviest help used, open questions, and the next delayed check. Leave
unknown fields blank. Save a session log to a file only when the user asks or
the course workspace already keeps one, and never overwrite earlier logs.

## Close honestly

End at a natural stopping point with one unaided check in the target form,
then report: what the learner did alone, where help was needed and how much,
what remains unresolved, one clearly different next task, and a suggested date
to check again. Distinguish "understood with help," "did it alone today," and
"still knew it later" — same-session familiarity is not mastery, and a session
that ends before the final check is incomplete.

Offer a workbook, coding practice, or study podcast only when the learner
wants it and it would force the next needed practice. Do not generate a study
plan or companion artifact merely because this skill was invoked.

Honor preferences for pace, tone, examples, notation, and accessibility as
presentation choices, but route the lesson by observed performance, and never
drop the final unaided check.
