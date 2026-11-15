#!/usr/bin/env python3
"""Tier-0 确定性比对（全库）：PDF 文本层 vs MinerU 逐页切片。
免费侧信道，不替代视觉审计（方案 A），但把字符级可疑页免费标出来供波间优先复核。
用法: python3 tier0_diff_all.py [--doc <name>]   # 全库或单文档
产出: corpus-md-audit/tier0/TIER0-<doc>.md + tier0-INDEX.md
"""
import fitz, re, os, sys, json, unicodedata, subprocess

REPO = "/Users/aurolafly/ABC"
WS = "/Volumes/D/audit-workspace"
OUT = f"{REPO}/corpus-md-audit/tier0"
os.makedirs(OUT, exist_ok=True)

# MinerU 元数据泄漏词（切片正文不该出现这些词——出现即 F4/F5 类泄漏）
META_WORDS = {"content_list", "doc_title"}


def norm(s: str) -> set:
    s = unicodedata.normalize("NFKC", s)
    s = re.sub(r"<!--[^>]*-->", " ", s)                # 页标记注释（含 from content_list 字样）
    s = re.sub(r"\[[a-z_0-9]+\]\d*\s*", " ", s)   # 切片块类型注记 [text]/[equation] 等
    s = re.sub(r"<[^>]+>", " ", s)                    # HTML 标签及属性
    s = re.sub(r'\w+-\w+="[^"]*"', " ", s)          # 裸 HTML 属性
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = re.sub(r"[^\w]", " ", s)
    return set(w for w in s.lower().split() if len(w) > 2)


def audit_doc(name: str, doc_path: str) -> dict:
    import glob as _glob
    cands = ([f"{REPO}/corpus/{doc_path}.pdf"] if doc_path else []) + _glob.glob(f"{REPO}/corpus/**/{name}.pdf", recursive=True)
    pdf = next((c for c in cands if os.path.exists(c)), None)
    if not pdf:
        return {"name": name, "error": "corpus 里找不到对应 PDF"}
    md_dir = f"{WS}/{name}/_audit-md"
    d = fitz.open(pdf)
    rows, n_flag, n_meta = [], 0, 0
    for i in range(len(d)):
        p1 = i + 1
        tl = norm(d[i].get_text())
        mp = f"{md_dir}/p{p1:03d}.txt"
        md = norm(open(mp, encoding="utf-8").read()) if os.path.exists(mp) else set()
        inter = tl & md
        union = tl | md
        j = len(inter) / len(union) if union else 1.0
        only_tl = sorted(tl - md)[:6]
        only_md = sorted(md - tl)[:6]
        meta_leak = sorted(META_WORDS & md)
        flag = j < 0.85 or meta_leak
        if flag:
            n_flag += 1
        if meta_leak:
            n_meta += 1
        rows.append((p1, len(tl), len(md), round(j, 3), only_tl, only_md, meta_leak, flag))
    # 落盘
    lines = [
        f"# TIER-0 确定性比对 — {name}（PDF 文本层 vs MinerU 切片）", "",
        f"- 页数 {len(d)}；FLAG（Jaccard<0.85 或元数据泄漏）{n_flag} 页；元数据泄漏 {n_meta} 页。",
        "- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。", "",
        "| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for p1, ntl, nmd, j, otl, omd, ml, fl in rows:
        q = lambda xs: " ".join(xs) if xs else "-"
        lines.append(f"| {p1} | {ntl} | {nmd} | {j} | {q(otl)} | {q(omd)} | {q(ml)} | {'⚠' if fl else ''} |")
    open(f"{OUT}/TIER0-{name}.md", "w", encoding="utf-8").write("\n".join(lines))
    return {"name": name, "pages": len(d), "flagged": n_flag, "meta_leak": n_meta,
            "jaccard_avg": round(sum(r[3] for r in rows) / max(1, len(rows)), 3)}


def main():
    only = sys.argv[sys.argv.index("--doc") + 1] if "--doc" in sys.argv else None
    import glob as _glob
    names = sorted(os.path.basename(d) for d in _glob.glob(f"{WS}/*") if os.path.isdir(d))
    docs = [{"name": n, "doc": None} for n in names if not only or n == only]
    results = []
    for d in docs:
        try:
            r = audit_doc(d["name"], d["doc"])
        except Exception as e:
            r = {"name": d["name"], "error": str(e)[:200]}
        results.append(r)
        print(f"done: {r.get('name')} pages={r.get('pages')} flagged={r.get('flagged')}"
              + (f" ERR={r.get('error')}" if r.get("error") else ""))
    ok = [r for r in results if not r.get("error")]
    idx = [
        "# TIER-0 全库索引", "",
        f"- 文档 {len(ok)}/{len(results)} 完成；FLAG 页合计 "
        f"{sum(r['flagged'] for r in ok)}；元数据泄漏页合计 {sum(r['meta_leak'] for r in ok)}。", "",
        "| 文档 | 页数 | FLAG | 元数据泄漏 | Jaccard均值 |",
        "|---|---|---|---|---|",
    ] + [f"| [{r['name']}](TIER0-{r['name']}.md) | {r['pages']} | {r['flagged']} | {r['meta_leak']} | {r['jaccard_avg']} |"
         for r in ok]
    open(f"{OUT}/tier0-INDEX.md", "w", encoding="utf-8").write("\n".join(idx))
    print(f"\nINDEX -> {OUT}/tier0-INDEX.md")


if __name__ == "__main__":
    main()
