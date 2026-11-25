#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line -- a dog's excuse, in the dog's own voice -- to
/output/entry.txt. Python standard library only; deterministic output.
"""

import os

LINE = (
    "It said 'show your work,' so I did \u2014 the answers are in my "
    "stomach now, and I'm not giving them back."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry is {len(LINE)} characters, must be 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
