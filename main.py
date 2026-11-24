#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun program/v1 entry.

Writes a single original line (1-240 chars) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene — an
apprentice barista whose eleventh-attempt rosetta finally lands,
and whose regular answers with a single nod.

Deterministic: no input, no network, no randomness, no clock.
The same bytes are written on every run.
"""

import os

LINE = (
    "After eleven failed pours, the apprentice barista slid the rosetta "
    "across the counter without a wobble, and her regular just nodded once."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"line is {len(text)} chars, must be 1-240")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back exactly what the grader will read and fail loudly if
    # it differs, so a silent short write can never pass as an entry.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text + "\n":
        raise SystemExit("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
