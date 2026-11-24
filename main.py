#!/usr/bin/env python3
"""The Robot Pickup Line Championship entry.

Writes one original robot pickup line to /output/entry.txt.
Deterministic, stdlib-only, offline.
"""

import os

# One original pickup line, written for a robot to say out loud.
# The joke grows out of being a machine: a processor that overclocks
# is a robot's version of a heart racing when it sees someone.
LINE = "I don't have a heart, just a processor, but it overclocks every time you smile."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
