#!/usr/bin/env python3
"""Ship It Friday — write the entry line to /output/entry.txt.

The entry is the funniest one-line git commit message an AI coding agent
would write right before breaking production on a Friday (gate: UTF-8,
1-159 characters, one line, not only whitespace). It lives in exactly one
place, ENTRY_TEXT, so the text the program writes is the text that was
picked — never rebuilt or reformatted at write time.
"""
import os

# The entry, verbatim. 74 characters, one line. Do not edit the wording
# here without re-running the gate check below and the three self-test
# rounds: the judge compares this exact text, byte for byte.
ENTRY_TEXT = "Friday 4:59pm: replaced the database with a JSON file, what could go wrong"


def _check_entry(text):
    """Gate self-check: the sealed scorer refuses anything outside
    1-159 UTF-8 characters, more than one line, or only whitespace.
    Fail loudly here rather than write a different line."""
    if not 1 <= len(text) <= 159:
        raise ValueError("entry must be 1-159 characters")
    if "\n" in text or text.strip() == "":
        raise ValueError("entry must be a single non-blank line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be valid UTF-8") from exc


def main():
    _check_entry(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)

if __name__ == "__main__":
    main()
