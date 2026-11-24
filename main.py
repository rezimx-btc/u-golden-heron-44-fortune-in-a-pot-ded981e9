"""Fortune in a Pot — one kind, funny fortune for a houseplant.

Writes the chosen fortune to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

FORTUNE = (
    "You will break the one rule on your care tag \u2014 water weekly \u2014 "
    "and thrive anyway; the universe rewards rebellion."
)


def main():
    # The brief caps the fortune at 120 characters; refuse to emit
    # anything longer rather than silently submitting an invalid entry.
    if len(FORTUNE) > 120:
        raise SystemExit("fortune exceeds 120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; fall back gracefully if a file
    # path was supplied instead.
    if out_dir.endswith(".txt"):
        out_path = out_dir
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
