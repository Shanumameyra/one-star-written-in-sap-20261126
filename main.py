#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to the output file. Deterministic: no
network, no randomness, no time dependence. The output is one fixed
line of UTF-8 text, under 280 characters.
"""

import os
import sys

# The entry: one line, a genuine 1-star review from a fern whose owner
# waters it with flat cola, repotted it into a mug with no drainage,
# and brags to guests that it is "low maintenance".
LINE = (
    "\u2605\u2606\u2606\u2606\u2606 One star. He watered me with flat cola, "
    "repotted me into a novelty mug with no drainage, and tells guests "
    "I'm 'low maintenance'. I am not low maintenance \u2014 I am a fern "
    "holding on by one leaf and a grudge."
)


def output_path(argv):
    """Where to write: argv[1] if given, else /output/entry.txt when the
    harness mounts /output, else entry.txt beside this script."""
    if len(argv) > 1:
        return argv[1]
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main(argv):
    path = output_path(argv)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
