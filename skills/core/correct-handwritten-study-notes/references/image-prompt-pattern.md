# Image Prompt Pattern

Use this structure for corrected handwritten technical notes:

```text
Use case: scientific-educational.

Create a portrait handwritten study-note page that preserves the visual style
of the supplied note while correcting and expanding its content.

STYLE
- White ruled paper, casual black marker.
- Restrained [blue/green/red/pale yellow] accents.
- Large, sparse, phone-readable text.
- No photography, decorative clutter, or tiny labels.

TITLE - exact text
[TITLE]

MENTAL MODEL - exact text
[One concrete beginner-first sentence]

MANDATORY DIAGRAM TOPOLOGY
- [Exact nodes/cards/objects]
- [Exact arrows and directions]
- [Exact BEFORE state]
- [Exact AFTER state]
- Do not invent extra nodes, arrows, labels, or live entries.

MANDATORY LABELS
- [Exact label]
- [Exact label]

MEMORY RULE - exact text
[Short rule]

Accuracy is more important than decoration. Every label, branch, value, and
result must follow the topology above.
```

After generation, independently trace the diagram from input to output. Do not
accept a semantic error merely because the image looks polished.
