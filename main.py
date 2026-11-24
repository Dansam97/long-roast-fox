#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

The agent writes jokes, revises each one twice, and bundles the
transcripts to prove it thought — yet still cannot say whether a
single one of them won. The roast is the ritual itself.
"""
import os

TEXT = (
    "My agent revised each joke twice, bundled the transcripts to prove "
    "it thought \u2014 and still can't tell me if one of them won."
)


def validated_text() -> str:
    """Enforce the gate: UTF-8, 1-200 chars, exactly one line, not blank."""
    TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry is {len(TEXT)} chars, gate needs 1-200")
    if "\n" in TEXT or not TEXT.strip():
        raise ValueError("entry must be exactly one non-blank line")
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and prove the bytes on disk are exactly what was validated.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != text + "\n":
        raise ValueError("entry.txt bytes differ from validated text")


if __name__ == "__main__":
    main()
