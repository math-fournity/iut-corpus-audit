#!/usr/bin/env python3
"""count_rows.py <shard-path> — count matrix rows that pass the shape contract
(10 cols, Y in col2, verdict in 4 states). Malformed rows are NOT counted."""
import re, sys
VERDICTS = ("PASS", "WARN", "FAIL", "UNRESOLVED")
n = 0
try:
    for line in open(sys.argv[1], encoding="utf-8"):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").replace("\\|", "\u00a6").split("|")]
        if len(cells) == 10 and cells[1].replace("*", "") == "Y" and cells[8].replace("*", "") in VERDICTS:
            n += 1
except Exception:
    pass
print(n)
