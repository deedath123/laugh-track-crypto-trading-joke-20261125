#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun entry.

Writes the locked entry text to <OUTPUT_DIR>/entry.txt (default /output).
Stdlib only. Program harness: program/v1.
"""

import os
import sys

ENTRY = (
    "I sold my Bitcoin at $61k to buy the dip at $60k, then watched it hit $97k "
    "while my group chat renamed me 'Professor Bottom' and my wife asked why the "
    "lambo fund now buys instant noodles."
)

MAX_LEN = 200


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_LEN:
        raise ValueError(f"entry too long: {len(text)} > {MAX_LEN}")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
