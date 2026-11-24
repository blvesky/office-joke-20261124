#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint.

Writes one single-line joke about office life to /output/entry.txt.
Gate (sealed scorer): UTF-8 text, 1-200 characters, not only whitespace.
The output file is chmod 0644 so the grader (a different user) can read it.
"""

import os

JOKE = "The office plant died, so HR sent a condolence email and a link to the grief counselling portal."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
