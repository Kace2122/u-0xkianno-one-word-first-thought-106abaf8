#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt: "psithurism" — the sound
of wind whispering through the trees. Surprising, vivid, and with a
spark of wit in its sound. No trailing newline: the judge is shown the
text exactly as submitted.
"""

import os

WORD = "psithurism"  # 10 characters: inside the gate's 1-24 range.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
