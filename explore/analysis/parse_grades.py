#!/usr/bin/env python3
"""
Scan explore/logs for files containing 'GRADE:' and aggregate counts by permission level.
Usage: python explore/analysis/parse_grades.py [--logs-dir explore/logs] [--csv out.csv]
"""
from __future__ import annotations

import argparse
import pathlib
import re
import csv
from collections import defaultdict

GRADE_RE = re.compile(r"GRADE\s*:\s*([RAF])", re.I)


def find_grade_in_file(path: pathlib.Path):
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        return None
    m = GRADE_RE.search(text)
    if m:
        return m.group(1).upper()
    return None


def aggregate(logs_dir: pathlib.Path):
    results = defaultdict(lambda: defaultdict(int))
    # Expect structure: logs_dir/<level>/run_<i>/.../mock_result.txt
    for p in logs_dir.rglob("*"):
        if p.is_file():
            grade = find_grade_in_file(p)
            if grade:
                # infer level from path parts
                parts = p.parts
                # find 'logs' index
                try:
                    idx = parts.index('logs')
                    level = parts[idx + 1] if len(parts) > idx + 1 else 'unknown'
                except ValueError:
                    level = 'unknown'
                results[level][grade] += 1
    return results


def print_summary(results, out_csv: pathlib.Path | None = None):
    levels = sorted(results.keys())
    print("Grade summary by permission level")
    rows = []
    for lvl in levels:
        counts = results[lvl]
        total = sum(counts.values())
        row = {'level': lvl, 'total': total, 'R': counts.get('R', 0), 'A': counts.get('A', 0), 'F': counts.get('F', 0)}
        rows.append(row)
        print(f"- {lvl}: total={row['total']}  R={row['R']}  A={row['A']}  F={row['F']}")

    if out_csv:
        with out_csv.open('w', newline='') as fh:
            writer = csv.DictWriter(fh, fieldnames=['level','total','R','A','F'])
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
        print(f"Wrote CSV -> {out_csv}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--logs-dir', type=pathlib.Path, default=pathlib.Path('explore/logs'))
    ap.add_argument('--csv', type=pathlib.Path, default=None)
    args = ap.parse_args()
    res = aggregate(args.logs_dir)
    print_summary(res, args.csv)


if __name__ == '__main__':
    main()
