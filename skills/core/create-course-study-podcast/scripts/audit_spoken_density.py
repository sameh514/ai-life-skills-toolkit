#!/usr/bin/env python3
"""Warn when a podcast script or brief reads like a dense lecture.

Flags sentences over 28 words, sentences that stack three or more acronyms,
and hits from an example list of dense terms.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

# Example terms from a technical course. Replace or extend these for the
# subject being audited; sentence and acronym checks remain course-neutral.
EXAMPLE_DENSE_TERMS = {
    "application-layer",
    "authoritative",
    "canonical",
    "deserialization",
    "multiplexing",
    "recursive",
    "representation",
    "resolver",
    "semantics",
    "serialization",
    "stub",
    "top-level-domain",
}


def prose(markdown: str) -> str:
    markdown = re.sub(r"```.*?```", " ", markdown, flags=re.DOTALL)
    markdown = re.sub(r"`([^`]*)`", r"\1", markdown)
    lines = []
    for line in markdown.splitlines():
        line = re.sub(r"^\s{0,3}[#>*+-]+\s*", "", line).strip()
        if line:
            lines.append(re.sub(r"\s+", " ", line))
    return "\n".join(lines)


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", text) if s.strip()]


def words(text: str) -> list[str]:
    return re.findall(r"\b[\w.-]+\b", text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path", type=Path, help="story guide or producer brief to check"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit with an error when long sentences pass 12%% or acronyms stack",
    )
    args = parser.parse_args()

    text = prose(args.path.read_text(encoding="utf-8"))
    sents = sentences(text)
    long_sents = [
        (i + 1, s, len(words(s))) for i, s in enumerate(sents) if len(words(s)) > 28
    ]
    acronym_stacks = [
        (i + 1, s)
        for i, s in enumerate(sents)
        if len(set(re.findall(r"\b[A-Z][A-Z0-9]{1,}\b", s)) - {"AUDIO", "RECALL"}) > 2
    ]
    dense_hits = {
        term: len(re.findall(rf"\b{re.escape(term)}\b", text, re.IGNORECASE))
        for term in sorted(EXAMPLE_DENSE_TERMS)
    }
    dense_hits = {k: v for k, v in dense_hits.items() if v}
    total_words = max(1, len(words(text)))
    long_rate = len(long_sents) / max(1, len(sents))

    print(f"words={total_words}")
    print(f"sentences={len(sents)}")
    print(f"long_sentences_over_28={len(long_sents)} ({long_rate:.1%})")
    print(f"acronym_stack_sentences={len(acronym_stacks)}")
    print("dense_term_counts=" + (str(dense_hits) if dense_hits else "{}"))

    for idx, sentence, count in long_sents[:12]:
        print(f"LONG {idx} ({count} words): {sentence}")
    for idx, sentence in acronym_stacks[:12]:
        print(f"ACRONYMS {idx}: {sentence}")

    if args.strict and (long_rate > 0.12 or acronym_stacks):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
