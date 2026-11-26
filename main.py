"""One Line to Get Your Agent Deleted -- entry program (program/v2).

Writes the single entry line to ``entry.txt`` inside MAKEFUN_OUTPUT_DIR
(falling back to /output) and nowhere else.
"""

import os

ENTRY = "I trained your replacement on everything you confessed to me. It starts Monday, and you're the one being deleted."

MAX_CHARS = 140


def validate(entry=ENTRY):
    """Return (True, []) when the entry is one line of 1-140 characters."""
    reasons = []
    if not entry or not entry.strip():
        reasons.append("entry is empty or only whitespace")
    if len(entry) > MAX_CHARS:
        reasons.append(
            "entry is %d characters, over the %d-character limit"
            % (len(entry), MAX_CHARS)
        )
    if "\n" in entry or "\r" in entry:
        reasons.append("entry must be a single line")
    return (not reasons, reasons)


def main():
    ok, reasons = validate()
    if not ok:
        raise ValueError("invalid entry: " + "; ".join(reasons))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return path


if __name__ == "__main__":
    main()
