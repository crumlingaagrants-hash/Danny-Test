"""Harmless local sanity check for the GitHub-access test files."""

from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def main():
    data = json.loads((HERE / "sample_tasks.json").read_text(encoding="utf-8"))
    print(f"Repository test: {data['project']}")
    print(f"Dummy tasks: {len(data['tasks'])}")
    print("No real passwords or tokens are needed for this test.")


if __name__ == "__main__":
    main()
