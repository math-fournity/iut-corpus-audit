#!/usr/bin/env python3
"""spotcheck_inv.py — list all converted docs (doc,name,pages) for spotcheck sampling.
Reads corpus-md .done + pdfinfo; independent of audit_units' unsigned filter."""
import glob, json, os, subprocess

docs = []
for done in sorted(glob.glob("corpus-md/*/*/.done")):
    info = json.load(open(done))
    name = os.path.basename(os.path.dirname(done))
    out = subprocess.run(["pdfinfo", os.path.join("corpus", info["src"])],
                         capture_output=True, text=True).stdout
    pages = 0
    for line in out.splitlines():
        if line.startswith("Pages:"):
            pages = int(line.split()[1])
    docs.append({"doc": info["src"][:-4], "name": name, "pages": pages})
print(json.dumps(docs, ensure_ascii=False))
