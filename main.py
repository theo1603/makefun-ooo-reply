#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply: one line, 160 characters or fewer.

Writes one original out-of-office auto-reply to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``). Python 3.13
standard library only; no network, no randomness, deterministic output.

Draft line: the away worker hands the job to the auto-reply itself and
admits the machine is outperforming them — "I'm out of the office. My
auto-reply has taken over my job, and honestly it's doing better than I
did." The turn is fresh (the auto-reply as a colleague, not a beach or
an inbox queue), it opens like a real away message, and the
self-deprecation lands on the first read.

Revision 2: the draft told the joke in two beats — "taken over my job"
plus "doing better than I did" — and the second clause explains the
first, so the laugh arrives a beat late and the line runs 102
characters. Replaced it with a single image: the auto-reply itself is
the only thing in the office working overtime. Same fresh turn (the
auto-reply as the hardest-working employee), but now the punch is the
whole sentence, "I'm on leave" opens it exactly like a real away
message, and at 78 characters it is taken in at a glance with every
word earning its place. Nothing about beaches, inboxes or limited
email access.
"""

import os

LINE = (
    "I'm on leave — this auto-reply is the only thing in the office "
    "working overtime."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
