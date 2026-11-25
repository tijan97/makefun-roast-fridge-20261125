#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge entry.

Writes a single original one-line roast of the fridge to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The gate requires UTF-8 text of 1 to
200 characters, not only whitespace, on one line.
"""

import os

MAX_CHARS = 200

# The roast targets the fridge itself: its noise, its uneven cooling, and
# the way it blames the owner with a beep for a door left open.
ROAST = "You hum all night, freeze the lettuce, warm the milk, and still beep at me like I'm the problem."


def main() -> None:
    if not ROAST or not ROAST.strip():
        raise SystemExit("roast must not be empty")
    if ROAST != ROAST.strip():
        raise SystemExit("roast must not start or end with whitespace")
    if "\n" in ROAST or "\r" in ROAST:
        raise SystemExit("roast must be a single line")
    if len(ROAST) > MAX_CHARS:
        raise SystemExit(f"roast must be at most {MAX_CHARS} characters")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
