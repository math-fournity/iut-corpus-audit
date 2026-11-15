#!/bin/bash
# audit_integrate.sh - single-writer integration: merge per-unit ledgers into
# AUDIT-PROGRESS.log, write per-doc AUDIT-SUMMARY files, emit stats JSON on stdout.
# Idempotent: PROGRESS merge appends only ledger lines not yet present (dedup by line).
set -u
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO"
python3 - <<'EOF'
import glob, json, os, re

ROOT = "corpus-md-audit/_visualcheck-audit"
os.makedirs(ROOT, exist_ok=True)
prog_path = os.path.join(ROOT, "AUDIT-PROGRESS.log")

# 1. merge ledger lines (dedup exact lines)
existing = set()
if os.path.exists(prog_path):
    with open(prog_path) as f:
        existing = set(l.rstrip("\n") for l in f if l.strip())
new_lines = []
ledgers = sorted(glob.glob(f"{ROOT}/pages/*/ledger-*.md"))
for led in ledgers:
    with open(led) as f:
        for line in f:
            line = line.rstrip("\n")
            if line.strip() and line not in existing:
                new_lines.append(line); existing.add(line)
with open(prog_path, "a") as f:
    for l in new_lines:
        f.write(l + "\n")

# 2. per-doc stats from merged progress lines + page files
stats = {}
for m in re.finditer(r"^\[([^\]]+)\] [^|]*\| PAGE \| p\.(\d+)/(\d+) \| (\S+) \| (.*)$",
                     "\n".join(sorted(existing)), re.M):
    unit, pg, tot, grade, note = m.groups()
    doc = unit.rsplit("-p", 1)[0]
    s = stats.setdefault(doc, {"pages": int(tot), "grades": {}})
    s["grades"][grade] = s["grades"].get(grade, 0) + 1

summary = []
for led in ledgers:
    name = led.split("/pages/")[1].split("/")[0]
    s = stats.get(name, {"pages": 0, "grades": {}})
    g = s["grades"]
    done_lines = [l for l in open(led) if "| DONE |" in l]
    with open(os.path.join(ROOT, f"AUDIT-SUMMARY-{name}.md"), "w") as f:
        f.write(f"# AUDIT-SUMMARY - {name}\n\n")
        f.write(f"- 总页数: {s['pages']}\n")
        f.write(f"- PASS: {g.get('PASS', 0)}  PASS±: {g.get('PASS±', 0) + g.get('PASSÂ±', 0)}"
                f"  FAIL: {g.get('FAIL', 0)}  UNRESOLVED: {g.get('UNRESOLVED', 0)}"
                f"  IMG-UNREADABLE: {g.get('IMG-UNREADABLE', 0)}\n")
        f.write(f"- 分账本: {os.path.basename(led)}  DONE行: {len(done_lines)}\n")
    summary.append({"name": name, "pages": s["pages"], "grades": g})

print(json.dumps({"mergedLines": len(new_lines), "totalProgressLines": len(existing),
                  "docs": summary}, ensure_ascii=False))
EOF
