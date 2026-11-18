#!/bin/bash
# audit_units.sh v4 - inventory (repo shards + D ws; legacy NOT signed; scan detection)
# Signed = matrix rows in repo corpus-md-audit/shards/<name>/AUDIT-MATRIX-*.md
#           (+ legacy D-drive shards if any). Legacy p-NNN.md is historical, NOT counted
#           (R1 re-audits all 3105 pages per C-04 v3).
# Emits JSON {ready:[{doc,name,pages,mode,scan,unsigned[]}], blocked:[{name,pages,png,txt}]}
set -u
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO"
python3 - <<'EOF'
import glob, json, os, re, subprocess

WS = "<audit-workspace>"
SHARDS = "corpus-md-audit/shards"

def pages_of(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return 0

def is_scan(pdf, pages):
    try:
        r = subprocess.run(["pdftotext", "-l", "3", pdf, "-"], capture_output=True, text=True)
        return len(r.stdout.strip()) < 30 * min(pages, 3)
    except Exception:
        return False

def signed_pages(name, pages):
    sig = set()
    for f in glob.glob(f"{SHARDS}/{name}/AUDIT-MATRIX-*.md"):
        for line in open(f, encoding="utf-8"):
            cells = [c.strip() for c in line.replace("\\|", "¦").strip().strip("|").split("|")]
            if len(cells) == 10 and cells[1].replace("*", "") == "Y" and cells[8].replace("*", "") in ("PASS", "WARN", "FAIL", "UNRESOLVED"):
                m = re.match(r"^p?(\d+)$", cells[0])
                if m: sig.add(int(m.group(1)))
    return sig & set(range(1, pages + 1))

ready, blocked = [], []
for done in sorted(glob.glob("corpus-md/*/*/.done")):
    info = json.load(open(done))
    name = os.path.basename(os.path.dirname(done))
    rel = info["src"]
    pdf = os.path.join("corpus", rel)
    pages = pages_of(pdf)
    if pages == 0:
        blocked.append({"name": name, "pages": 0, "png": 0, "txt": 0})
        continue
    png = len(glob.glob(f"{WS}/{name}/_audit-pages/p*.png"))
    txt = len(glob.glob(f"{WS}/{name}/_audit-md/p*.txt"))
    if png != pages or txt != pages:
        blocked.append({"name": name, "pages": pages, "png": png, "txt": txt})
        continue
    sig = signed_pages(name, pages)
    unsigned = [p for p in range(1, pages + 1) if p not in sig]
    if unsigned:
        ready.append({"doc": rel[:-4], "name": name, "pages": pages,
                      "mode": info.get("mode", "kit-zip"),
                      "scan": is_scan(pdf, pages), "unsigned": unsigned})
print(json.dumps({"ready": ready, "blocked": blocked}, ensure_ascii=False))
EOF
