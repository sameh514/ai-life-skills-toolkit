---
name: create-course-study-podcast
description: Turn course material into a plainspoken story-style audio episode for review on a walk, with short recall pauses. Use when the user wants an audio study guide checked against approved sources without leaking quiz or assignment answers.
---

# Create Course Study Podcast

Turn course material into a story the learner can follow on a walk or during
steady exercise. Audio is for preview, explanation, and spoken recall — not a
substitute for diagrams, math, or writing code. Treat driving and
attention-demanding chores as preview-only listening.

## Keep momentum

Use available context and safe, reversible defaults before asking for input.
Bundle non-blocking questions and continue useful work. Interrupt only when a
missing choice would change the result, privacy, cost, authority, safety, or
something hard to undo. Never repeat an answered question.

## Sound like a story, not a lecture

- Use the strengths of narrative journalism — curiosity, scenes, gradual
  reveals, a clear ending — without imitating any named show, host, or
  catchphrase.
- Open inside a concrete situation. Bring in the formal term only after the
  idea is already clear.
- Introduce one unfamiliar term at a time. Translate it immediately into
  ordinary words and reuse that same translation later. Two easily confused
  terms may follow each other as an explicit contrast.
- Use short spoken sentences with one idea each. Never stack acronyms,
  definitions, or lists in a single breath.
- Keep one recurring person, goal, or problem as the episode's spine.
- Simplify the wording, never the underlying fact.

Read [narrative-recall-style.md](references/narrative-recall-style.md) before
writing the script, prompt, or producer brief.

## Make the episode

1. Agree on the course, topic, listener, length, and allowed sources.
2. Gather the sources and separate course facts from corrections, analogies,
   and teaching choices. Reuse the course's shared source folder (approved
   sources, key terms and pronunciations, and what is graded), or create one
   for this project.
3. Write a one-paragraph story spine, plus a short list of required terms with
   the plain-English translation and one concrete example for each. Drop terms
   the episode does not need.
4. Write the script or producer brief using
   [producer-brief-template.md](references/producer-brief-template.md). Build
   each teaching beat as: situation, the listener's guess, the formal term, one
   exact example, the common mistake, why it matters.
5. Add a few recall pauses: ask one short question, leave a real 3–5 second
   pause, say once that pausing the player for longer counts, accept "I do not
   know yet," then give the plain answer and the reason. Answer every question
   the episode raises. From the second episode on, open with one question about
   the previous episode.
6. Add pronunciation notes for names, acronyms, and code. Speak code by
   meaning; do not read underscores or punctuation aloud.
7. Run `scripts/audit_spoken_density.py <script-or-brief> --strict` and rewrite
   long sentences and acronym stacks until it passes.
8. Generate the audio with the user's approved tool and browser, one job at a
   time, and let it finish. A spinner is not completion.
9. Check the finished episode, not just the plan: download it, confirm it plays
   all the way through, and review the transcript or full audio for the planned
   pauses, answered questions, approved terms, source-accurate claims, and zero
   leaked quiz or assignment answers. Use local speech-to-text only with the
   user's permission.
10. Keep the audio together with its sources, brief, and audit notes. If the
    user asked for a copy on another device, deliver it and confirm the copy
    matches.

## Reject or regenerate when

- a section opens with a definition instead of a situation;
- a term or acronym appears before it is explained;
- a recall question is asked before its answer was made understandable;
- the episode contradicts the approved sources or leaks graded answers;
- a planned pause or invited question is missing from the finished audio.

A complete download proves the file is intact, not that the teaching is right —
check both. See
[established-example.md](references/established-example.md) for the generic
end-to-end flow and project layout.
