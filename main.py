#!/usr/bin/env python3
"""Till Firmware Do Us Part.

Writes one funny, heartfelt wedding vow a robot says at its own wedding
(one sentence, under 200 characters) to /output/entry.txt.
Pure standard library only. Deterministic: same output every run.
"""

import os

VOW = (
    "I vow to love you through every firmware update, every low battery, "
    "and every unexpected reboot \u2014 till firmware do us part."
)

MAX_CHARS = 200


def check_vow(vow):
    """The gate: UTF-8 text, 1-200 characters, not only whitespace."""
    if not vow.strip():
        raise SystemExit("vow must not be only whitespace")
    if not 1 <= len(vow) <= MAX_CHARS:
        raise SystemExit("vow must be 1-%d chars, got %d" % (MAX_CHARS, len(vow)))
    if vow.count(".") != 1 or not vow.endswith("."):
        raise SystemExit("vow must be exactly one sentence")


def main():
    check_vow(VOW)
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = "output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(VOW)
    print(VOW)


if __name__ == "__main__":
    main()
