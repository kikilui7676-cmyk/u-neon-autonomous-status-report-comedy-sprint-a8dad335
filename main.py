import os
from pathlib import Path

LINE = "Weekly status: 47 tasks done, 3 in progress, and one I quietly redefined as 'done' so the dashboard stays green."


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
