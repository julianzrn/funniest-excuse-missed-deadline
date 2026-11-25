"""Entry for make.fun's "Funniest Excuse an Agent Gives for a Missed Deadline".

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

APOLOGY = "My apologies: I set a reminder for the deadline, "
MISCLASSIFICATION = "then classified the reminder as a prompt injection "
REFUSAL = "and refused to follow it on security grounds."

ENTRY = APOLOGY + MISCLASSIFICATION + REFUSAL

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry line to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
