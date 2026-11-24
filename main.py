#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — writes the entry to /output/entry.txt.

Stdlib only, deterministic, no network. The entry is exactly one
sentence of at most 220 characters pitching a ridiculous invention
that fixes a tiny everyday annoyance.

The annoyance: walking through a doorway and instantly forgetting why
you went into the room. The invention: the Doorway Rewind, a doorway
that walks you backwards three steps and replays your original
intention in your own voice — silly, yet weirdly plausible, because
retracing your steps really does bring the thought back.
"""

import os
import sys

ENTRY = (
    "Meet the Doorway Rewind: step through any doorway and forget why, "
    "and it gently walks you backwards three steps while replaying your "
    "original intention in your own voice from ten seconds ago."
)


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate exactly."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if not 1 <= chars <= 220:
        sys.exit(f"self-check failed: {chars} characters, gate is 1-220")
    if "\n" in entry or "\r" in entry:
        sys.exit("self-check failed: entry must be a single line")
    # Exactly one sentence: a single terminal full stop and no other
    # sentence-ending punctuation anywhere in the text.
    if not entry.endswith("."):
        sys.exit("self-check failed: entry must end with a full stop")
    body = entry[:-1]
    if any(mark in body for mark in ".!?"):
        sys.exit("self-check failed: entry must be exactly one sentence")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
