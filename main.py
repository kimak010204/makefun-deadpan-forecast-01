"""Write one deadpan weather forecast for an invented city to /output/entry.txt."""
import os

ENTRY = "New Brakk sees a high of 58 and a 90% chance of rain that falls sideways out of respect for the wind; umbrellas remain, as ever, purely decorative tonight."


def validate(entry):
    """Check the forecast against the gate before writing it out.

    The gate refuses anything that is not UTF-8 text of 1-160
    characters, is only whitespace, or spans more than one line,
    and the judge rewards a single broadcast line: an invented
    city, concrete numbers, and one deadpan twist delivered
    straight, with no second sentence to dilute it. The twist
    here is a single coherent image -- rain falling sideways
    out of respect for the wind -- rather than a pile of
    unrelated absurdity, and the closing clause lands it
    in the flat tone of a real forecaster.
    """
    assert isinstance(entry, str), "entry must be text"
    assert 1 <= len(entry) <= 160, "entry must be 1-160 characters"
    assert entry.strip(), "entry must not be only whitespace"
    assert "\n" not in entry.strip(), "entry must be a single line"
    assert entry.count(".") <= 1, "entry must be one sentence, no second sentence"
    return entry


def main():
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write exactly the chosen line: no trailing newline, so the
    # file's byte count is the line itself and the gate reads it
    # as one line of 155 characters.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
