#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one two-sentence horror story to /output/entry.txt.
"""

import os
import re

STORY = (
    "My mother squeezed my hand just before she passed. "
    "I was holding her right hand \u2014 the one the stroke had paralysed."
)


def validate(text: str) -> None:
    """Mirror the bounty gate: 1-400 chars, exactly two sentences."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry is {len(text)} chars, must be 1-400")
    text.encode("utf-8")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    if len(sentences) != 2:
        raise ValueError(f"entry has {len(sentences)} sentences, must be 2")


def main() -> None:
    validate(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
