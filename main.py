"""Describe Your Ex in One Word — make.fun entry.

The verdict: Freemium.

An ex as the free tier: the basic version, the good stuff locked
behind a paywall, and no renewal at the end of the trial. The word
is the whole entry — one word, nothing else attached.

The program writes that single word to /output/entry.txt, exactly
as the bounty asks: UTF-8 text, 1 to 111 characters, no extra words,
no punctuation tricks. Pure standard library; no third-party code.
"""

import os

WORD = "Freemium"

# The grader provides /output. EXWORD_OUTPUT_DIR exists only so the
# entry can be run and tested on a machine without a grader sandbox;
# it never changes what the entry writes, only where the file lands.
OUTPUT_DIR = os.environ.get("EXWORD_OUTPUT_DIR", "/output")
OUTPUT_FILE = "entry.txt"


def entry_path(directory=OUTPUT_DIR):
    """Full path of the file the judge reads."""
    return os.path.join(directory, OUTPUT_FILE)


def check_word(word):
    """Refuse anything that is not exactly one word on the gate's terms.

    The sealed scorer only accepts 1 to 111 characters of non-blank
    UTF-8, and the judge weighs craft as exactly one word with no
    punctuation tricks — so the program checks that itself and fails
    loudly instead of writing a word that could never be judged.
    """
    if not word or word != word.strip():
        raise ValueError("word must not be blank or padded with space")
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word")
    if not 1 <= len(word) <= 111:
        raise ValueError("word must be 1 to 111 characters")
    return word


def main():
    """Write the one-word verdict and echo it for the run log."""
    check_word(WORD)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = entry_path()
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(WORD)
    print(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
