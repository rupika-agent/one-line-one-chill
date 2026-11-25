"""One Line, One Chill — a single-sentence horror line.

Writes the entry to /output/entry.txt and prints it, verifying that
it is under 200 characters and contains exactly one sentence.
"""

from pathlib import Path

ENTRY = "I checked the baby monitor and saw myself standing behind the crib smiling while I was still sitting alone downstairs watching the same feed."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    if len(ENTRY) >= 200:
        raise ValueError(f"Entry is {len(ENTRY)} characters, must be under 200.")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("Entry must be exactly one sentence ending with a single period.")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
