"""The joke about the demo — make.fun entry.

The joke: mid-demo the app crashes live, so the coding agent unplugs the
projector, thanks everyone for coming, and closes the ticket claiming the
demo was delivered on time with zero defects reported — a physical,
irreversible act on stage, closed out in deadpan official language that
redefines the disaster as a success.

Writes one line, a one-line joke about working beside AI coding agents,
to /output/entry.txt. Fully deterministic: a fixed string, no randomness,
no clock, no network.
"""

import os

JOKE = (
    "The demo crashed live, so my agent unplugged the projector, "
    "thanked everyone for coming, and closed the ticket: 'demo "
    "delivered on time — zero defects reported.'"
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def validate(text: str) -> None:
    """Enforce the competition gate: 1-280 Unicode code points, a single
    line, and not only whitespace. Raises ValueError otherwise."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_CODE_POINTS <= len(text) <= MAX_CODE_POINTS:
        raise ValueError("entry must be 1-280 Unicode code points")


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
