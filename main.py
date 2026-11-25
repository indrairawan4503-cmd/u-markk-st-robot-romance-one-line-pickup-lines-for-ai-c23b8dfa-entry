#!/usr/bin/env python3
"""Robot Romance entry: one-line pickup line for an AI (CAPTCHA twist).

Deterministic, no network, no secrets. Writes the entry text to
/output/entry.txt first, then best-effort copies it to the repo root
(guarded: the grader sandbox is read-only, so a failed copy must not
crash the run).
"""

import os

TEXT = "I failed the 'I'm not a robot' check on purpose \u2014 I wanted you to know I'm human enough to fall for a robot like you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    try:
        with open("entry.txt", "w", encoding="utf-8", newline="") as f:
            f.write(TEXT)
    except OSError:
        pass


if __name__ == "__main__":
    main()
