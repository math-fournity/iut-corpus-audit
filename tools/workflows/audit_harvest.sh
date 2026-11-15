#!/bin/bash
# audit_harvest.sh v3 - harvest repo shards -> FINAL + SUMMARY.md + STATUS.json
# Usage: audit_harvest.sh [docs-json-array]   (无参=全库口径)
# Gates per doc: NEWROWS==pages (C-04 v3); dup rows detected pre-fold; Y column via
# validate_matrix; 600dpi unresolved count (需600dpi回图 without 裁决) must be 0.
set -u
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO"
VM=/Users/aurolafly/.agents/skills/mineru/scripts/validate_matrix.py
DOCS_FILTER="${1:-}"
python3 - "$VM" "$DOCS_FILTER" <<'EOF'
import glob, json, os, re, subprocess, sys, time

WS = "/Volumes/D/audit-workspace"
SHARDS = "corpus-md-audit/shards"
VALIDATE = sys.argv[1]
try:
    FILTER = set(json.loads(sys.argv[2])) if len(sys.argv) > 2 and sys.argv[2] else None
except Exception:
    FILTER = None
OUTDIR = "corpus-md-audit/matrices"
os.makedirs(OUTDIR, exist_ok=True)

def pages_of(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    for line in out.splitlines():
        if line.startswith("Pages:"):
            return int(line.split()[1])
    return 0

docs, status = [], {}
for done in sorted(glob.glob("corpus-md/*/*/.done")):
    info = json.load(open(done))
    name = os.path.basename(os.path.dirname(done))
    if FILTER is not None and name not in FILTER:
        continue
    pages = pages_of(os.path.join("corpus", info["src"]))
    legacy = set()
    for f in glob.glob(f"corpus-md-audit/_visualcheck-audit/pages/{name}/p-*.md"):
        m = re.search(r"p-(\d{3,})\.md$", f)
        if m: legacy.add(int(m.group(1)))
    rows, seen, dup = {}, set(), []
    for f in sorted(glob.glob(f"{SHARDS}/{name}/AUDIT-MATRIX-*.md")):
        for line in open(f, encoding="utf-8"):
            m = re.match(r"^\|\s*p?(\d+)\s*\|", line)
            if m:
                p = int(m.group(1))
                if p in seen: dup.append(p)
                seen.add(p)
                rows[p] = line.rstrip("\n")
    v = {"PASS": 0, "WARN": 0, "FAIL": 0, "UNRESOLVED": 0}
    zoom_open = 0
    fail_open = 0
    for line in rows.values():
        for k in ("PASS", "WARN", "FAIL", "UNRESOLVED"):
            if f"| {k} " in line or f"| {k}|" in line:
                v[k] += 1
                break
        if "需600dpi回图" in line and "已裁决" not in line:
            zoom_open += 1
        if re.search(r"\| FAIL\b", line) and not re.search(r"已修复|已裁决|已登记", line.split("|")[-2] if len(line.split("|")) >= 2 else ""):
            fail_open += 1
    final = os.path.join(OUTDIR, f"AUDIT-MATRIX-{name}-FINAL.md")
    with open(final, "w", encoding="utf-8") as fo:
        fo.write(f"# AUDIT-MATRIX — {name}（新格式；legacy 旧签 {len(legacy)} 页仅历史）\n\n")
        fo.write("| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |\n|---|---|---|---|---|---|---|---|---|---|\n")
        for p in sorted(rows):
            fo.write(rows[p] + "\n")

    missing = sorted(set(range(1, pages + 1)) - set(rows))   # 缺行页
    stray = sorted(p for p in rows if p < 1 or p > pages)     # 越界页号
    verdict = "pass"
    detail = ""
    if not rows:
        verdict = "NO-ROWS"
        detail = "无任何矩阵行"
    elif stray:
        verdict = "OUT-OF-RANGE"
        detail = f"越界页号: {stray[:10]}"
    elif dup:
        verdict = "DUPLICATE"
        detail = f"同页多行: {sorted(set(dup))[:10]}"
    elif missing:
        verdict = "INCOMPLETE"
        detail = f"缺口 {len(missing)} 页（legacy 历史页不计覆盖）"
    elif fail_open:
        verdict = "FAIL-OPEN"
        detail = f"FAIL 未处置 {fail_open} 行（备注需 已修复/已裁决/已登记）"
    elif zoom_open:
        verdict = "ZOOM-OPEN"
        detail = f"未裁决600dpi项 {zoom_open}"
    else:
        r = subprocess.run(["python3", VALIDATE, final, str(pages)],
                           capture_output=True, text=True)
        verdict = "pass" if r.returncode == 0 else "FAIL"
        detail = (r.stdout or r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else ""
    docs.append({"name": name, "pages": pages, "newRows": len(rows),
                 "legacyRows": len(legacy), "grades": v, "zoomOpen": zoom_open,
                 "validate": verdict, "detail": detail})
    full = len(rows) == pages and verdict == "pass"  # 同一覆盖定义（M22）
    status[name] = {
        "pages": pages, "rows": len(rows), "legacy": len(legacy), "failOpen": fail_open,
        "grades": v, "zoomOpen": zoom_open, "verdict": verdict,
        "auditStatus": (f"全审 {time.strftime('%Y-%m-%d')} P{v['PASS']}/W{v['WARN']}/F{v['FAIL']}"
                        + (f" (legacy历史{len(legacy)}页)" if legacy else "")
                        if full else f"进行中 {len(rows)}/{pages}"),
    }

merged = {}
if os.path.exists("corpus-md-audit/STATUS.json"):
    try: merged = json.load(open("corpus-md-audit/STATUS.json", encoding="utf-8"))
    except Exception: merged = {}
merged.update(status)

notStarted = [d for d in docs if d["validate"] == "NO-ROWS"]
bad = [d for d in docs if d["validate"] not in ("pass", "NO-ROWS")]
now = time.strftime("%Y-%m-%d %H:%M")
with open("corpus-md-audit/SUMMARY.md", "w", encoding="utf-8") as f:
    f.write(f"# 全转全审 · 审计汇总（{now}）\n\n")
    f.write(f"- 文档：{len(docs)}（本批口径{'=全库' if FILTER is None else '='+str(len(docs))+'份'}）；"
            f"新格式行 {sum(d['newRows'] for d in docs)}；"
            f"未开工 {len(notStarted)} 份；校验不过 {len(bad)} 份；"
            f"未裁决600dpi {sum(d['zoomOpen'] for d in docs)} 项\n\n")
    f.write("| 文档 | 页数 | 新行 | legacy | PASS | WARN | FAIL | UNRES | 600dpi未裁 | 校验 |\n|---|---|---|---|---|---|---|---|---|---|\n")
    for d in docs:
        f.write(f"| {d['name']} | {d['pages']} | {d['newRows']} | {d['legacyRows']} | "
                f"{d['grades']['PASS']} | {d['grades']['WARN']} | {d['grades']['FAIL']} | "
                f"{d['grades']['UNRESOLVED']} | {d['zoomOpen']} | {d['validate']} |\n")
    f.write("\n## 全库口径（STATUS 合并后）\n\n")
    allrows = sum(v.get("rows", 0) for v in merged.values())
    allpages = sum(v.get("pages", 0) for v in merged.values())
    f.write(f"- 全库已落矩阵行 {allrows}/{allpages} 页；文档 {len(merged)} 份\n")
    f.write("\n## 版本锚\n\n审计对象=kurims 2020 修订版/arXiv 版本（源 URL 见 corpus/INDEX.md）；PRIMS 2021 发表版缺席，一致性未核。\n")
    f.write("\n## legacy 另册\n\nlegacy 旧签（p-NNN.md）仅作历史记录；C-04 要求全部 3105 页由新格式矩阵行覆盖，legacy 页在 R1 一并重审。\n")
json.dump(merged, open("corpus-md-audit/STATUS.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print(json.dumps({
    "docs": docs,
    "totalNewRows": sum(d["newRows"] for d in docs),
    "totalLegacyRows": sum(d["legacyRows"] for d in docs),
    "notStarted": len(notStarted),
    "badValidate": len(bad),
    "zoomOpen": sum(d["zoomOpen"] for d in docs),
}, ensure_ascii=False))
EOF
