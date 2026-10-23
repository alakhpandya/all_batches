"""Fake email sender for use as a Claude Code notification hook.

Instead of sending a real email, writes a dummy email to email.txt
in the current working directory.
"""

from datetime import datetime
from pathlib import Path

SUBJECT = "Claude needs your input"
BODY = (
    "Claude Code is waiting for your input.\n"
    "Please check your terminal/editor session.\n\n"
    f"Timestamp: {datetime.now().isoformat(timespec='seconds')}\n"
)


def send_email() -> Path:
    out_path = Path("email.txt")
    content = f"Subject: {SUBJECT}\n\n{BODY}"
    out_path.write_text(content, encoding="utf-8")
    return out_path


if __name__ == "__main__":
    path = send_email()
    print(f"Dummy email written to {path.resolve()}")
