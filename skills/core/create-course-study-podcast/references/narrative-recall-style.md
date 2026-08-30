# Plainspoken Narrative Recall Style

Use this reference to turn technical course content into audio that feels like a
reported story rather than a lecture.

## Episode shape

1. **Cold open:** Start inside a concrete moment. Someone types a web address,
   sends a message, sees a failure, or needs an answer.
2. **Central question:** State one ordinary-language mystery the episode will
   solve.
3. **Discovery:** Reveal the mechanism in small steps. Let the listener form a
   guess before naming the formal concept.
4. **Complication:** Show the plausible mistake and what breaks.
5. **Resolution:** Return to the opening moment and make it newly understandable.
6. **Transfer:** Ask the listener to predict the next case or perform the next
   workbook/IDE action.

## Spoken-language rules

- Prefer “a program asks the operating system to open a communication door”
  before “the application creates a socket.”
- Prefer concrete verbs: asks, waits, sends, labels, counts, closes.
- Keep one main clause per sentence when possible.
- Break a process into turns between hosts rather than one dense explanation.
- Do not speak parenthetical caveats. Move an essential caveat into its own
  sentence; delete nonessential caveats.
- Do not read headings, bullet labels, symbols, file paths, underscores, or
  code punctuation as prose.

## Jargon conversion

For every required term, use this sequence:

1. **Experience:** what a person or program is trying to do.
2. **Plain mechanism:** what happens, using ordinary verbs.
3. **Name:** “Engineers call this ...”
4. **Exactness:** one sentence specifying what the term does and does not mean.
5. **Reuse:** return to the same plain translation later.

Never introduce a second unfamiliar term until the first has been resolved with
an example. The exception is the second member of a confusable pair such as TCP
versus UDP; introduce it immediately as a contrast only after the first member
is understood. Do not use an acronym merely because the source does.

## Active-recall rhythm

- Use recall after a complete story beat, not before basic comprehension.
- Ask only one thing at a time.
- Make the answer speakable in one sentence.
- Pause 3–5 seconds without music or host chatter. Treat that duration as a
  practical hypothesis, not a research-proven podcast optimum; tell the learner
  once that pausing the player for longer counts.
- Accept “I do not know yet” as a real retrieval attempt.
- Give the direct answer first, then the reason, then one misconception.
- Revisit the same idea later in a new situation.
- Explicitly answer every opening question or invited guess later in the
  episode; a prequestion does not help untargeted material by itself.
- From episode two onward, ask one free-recall question from the prior episode
  before any recap. Fade later prompts from recognition toward explanation.

## Focused-prompt pattern

```text
Create a calm, plainspoken narrative study podcast. Open inside [concrete
situation] and follow [recurring person/system] trying to [goal]. Use the
high-level qualities of strong narrative journalism—curiosity, scenes, gradual
reveals, and a clear ending—without copying any named show or host. Do not begin
with definitions or learning objectives. Introduce no more than one unfamiliar
technical term at a time. Explain the idea in ordinary language first, then name
the term and define it in one short sentence. Use short sentences and concrete
verbs. Avoid stacked acronyms, textbook wording, and dense lists. At [specified
checkpoints], ask one short recall question, say “I do not know yet” counts,
leave 3–5 seconds of real quiet, then answer plainly, explain why, and contrast
one tempting misconception. Explicitly resolve every question or guess you
invite. End by returning to the opening situation and use a short recall round;
do not call it delayed retrieval unless the attempt occurs in a later session.
```

## Pre-generation audit

- Can the episode's story be stated in one sentence?
- Does every required term have a stable plain-language translation?
- Is each recall answer understandable without memorizing vocabulary?
- Are paper/IDE-only tasks explicitly routed out of audio?
- Are analogies labeled as analogies and bounded?
- Are the exact workbook checkpoints named?
- Is every invited guess or opening question explicitly resolved?
- Is the listening context classified as active-recall-safe or preview-only?

## Post-generation audit

Audit what the system actually generated, not only the prompt. Use a
platform-provided transcript when available; use local speech-to-text only
when the user permits it. Otherwise review the whole episode with a timestamp
log. Confirm:

- every planned checkpoint appears with an attempt, pause, answer, reason, and
  misconception repair;
- every invited question is resolved;
- terminology follows the shared ledger and does not become denser than the
  producer brief;
- the episode does not quote or expose graded questions, answer keys, or
  assignment solutions;
- all factual claims remain within the verified Course Source Pack.
