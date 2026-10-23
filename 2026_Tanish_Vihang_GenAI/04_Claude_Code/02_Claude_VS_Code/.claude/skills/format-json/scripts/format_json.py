"""Pretty-print a JSON file in place.

Usage: python format_json.py <path-to-file.json>
"""
import json
import sys


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python format_json.py <path-to-file.json>", file=sys.stderr)
        return 1

    path = sys.argv[1]

    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            text = f.read()
    except OSError as e:
        print(f"Could not read {path}: {e}", file=sys.stderr)
        return 1

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {path}: {e}", file=sys.stderr)
        return 1

    formatted = json.dumps(data, indent=2, ensure_ascii=False) + "\n"

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(formatted)

    print(f"Formatted {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
