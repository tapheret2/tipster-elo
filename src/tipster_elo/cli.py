from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

from .elo import rate_sequence


def load_csv(path: Path) -> list[tuple[str, bool]]:
    rows: list[tuple[str, bool]] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = (row.get("tipster") or row.get("name") or "").strip()
            res = (row.get("result") or row.get("outcome") or "").strip().upper()
            if not name or res not in {"W", "L", "WIN", "LOSS", "1", "0"}:
                continue
            won = res in {"W", "WIN", "1"}
            rows.append((name, won))
    return rows


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="tipster-elo")
    sub = p.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("rate")
    r.add_argument("--csv", type=Path, required=True)
    r.add_argument("--k", type=float, default=20.0)
    r.add_argument("--base", type=float, default=1500.0)
    r.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    if args.cmd == "rate":
        seq = load_csv(args.csv)
        if not seq:
            print("no valid rows (need tipster,result)", file=sys.stderr)
            return 1
        table = rate_sequence(seq, k=args.k, base=args.base)
        board = table.leaderboard()
        if args.json:
            print(json.dumps([{"tipster": n, "elo": e, "n": g} for n, e, g in board], indent=2))
        else:
            for n, e, g in board:
                print(f"{e:8.1f}  n={g:3d}  {n}")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
