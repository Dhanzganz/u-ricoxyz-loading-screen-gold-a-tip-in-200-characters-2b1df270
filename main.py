#!/usr/bin/env python3
"""Loading Screen Gold entry: one sharp, funny loading-screen tip.

Writes the single chosen tip to /output/entry.txt (UTF-8, <= 200 chars).

Why this tip: it speaks to both audiences at once — the developer who
keeps promising to refactor that file, and the AI agent now reading it.
The turn ("it has questions") lands the laugh; the countdown ("four
seconds") makes it a loading-screen line, not a slogan. No coffee,
deadline or compile cliché.
"""
import os

TIP = (
    "Tip: while this loads, your AI agent is reading the file you swore "
    "you'd refactor — and it has questions. You have four seconds to "
    "prepare answers."
)


def main() -> None:
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} chars, must be 1-200"
    assert TIP.strip(), "tip must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
