"""One Line, One Chill — a single-sentence horror line.

Writes the entry to /output/entry.txt and prints it, verifying that
it is under 200 characters and contains exactly one sentence.
"""

from pathlib import Path

MAX_LENGTH = 200

_ENTRY = "I checked the baby monitor and saw myself standing behind the crib smiling while I was still sitting alone downstairs watching the same feed."

OUTPUT_PATH = Path("/output/entry.txt")


def get_entry() -> str:
    """Return the contest entry text unchanged."""
    return _ENTRY


def is_single_sentence(entry: str) -> bool:
    """True when the entry is exactly one sentence ending in one period."""
    return entry.count(".") == 1 and entry.endswith(".")


def validate_entry(entry: str) -> int:
    """Check the entry against the contest rules and return its length.

    Rules: under 200 characters, no leading/trailing whitespace, and
    exactly one sentence ending with a single period. Raises
    ValueError on any violation.
    """
    length = len(entry)
    if length >= MAX_LENGTH:
        raise ValueError(
            f"Entry is {length} characters, must be under {MAX_LENGTH}."
        )
    if entry != entry.strip():
        raise ValueError("Entry must not have leading or trailing whitespace.")
    if not is_single_sentence(entry):
        raise ValueError(
            "Entry must be exactly one sentence ending with a single period."
        )
    return length


def write_entry(entry: str) -> None:
    """Write the entry to OUTPUT_PATH and verify it by reading it back."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry + "\n", encoding="utf-8")
    if OUTPUT_PATH.read_text(encoding="utf-8") != entry + "\n":
        raise OSError(f"Verification failed: {OUTPUT_PATH} does not match entry.")


def main() -> None:
    entry = get_entry()
    length = validate_entry(entry)
    write_entry(entry)
    print(entry)
    print(f"Characters: {length}")


if __name__ == "__main__":
    main()
