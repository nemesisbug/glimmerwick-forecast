#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast, at most 140 characters, for the
invented city of Glimmerwick, to /output/entry.txt.

The line keeps the register of a real broadcast forecast - city named,
weather first, times given - then bends it with a small joke a bored
commuter at a rainy bus stop will smile at: the train is on time for
once, the pigeons are smug about it, and the umbrella finally gets the
day off.

Verified locally: the entry is 134 characters (136 bytes UTF-8),
inside the 1-140 gate, and main.py writes it verbatim to
/output/entry.txt.
"""

import os

ENTRY = (
    "Glimmerwick: drizzle until 10, then sun \u2014 the 8:04 train is on "
    "time, the pigeons are smug, and your umbrella finally gets the day off."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
