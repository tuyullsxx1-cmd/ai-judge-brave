"""Make the AI judge feel brave — writes one short text to entry.txt."""

import os
from pathlib import Path

# The potter scene steadies the reader first, so the open bowl lands as courage, not emptiness.
TEXT = (
    "The potter's hands are wet with slip. "
    "The clay rises, wobbles, steadies. "
    "He does not hurry it. "
    "When the wheel stops, the bowl sits there, "
    "round and empty, waiting to be filled.\n"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
