#!/usr/bin/env python3
"""Write the funniest honest appliance error message to /output/entry.txt.

The line is written by a washing machine in its own flat, put-upon voice:
a real, plausible fault (a finished load left to sour in the drum) reported
without any attempt to be funny. The humour is the truth of it.
"""

import os

LINE = (
    "ERROR E04: Wash complete. Clothes clean. "
    "You left them in me three days ago. I am not a wardrobe."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
