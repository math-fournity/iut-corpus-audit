#!/usr/bin/env python3
"""render_adjudication_books_db.py — 从 ZCode cli sqlite dwf_run.result_json 直接渲染裁决书。

为什么有这个脚本：转录扫描版（render_adjudication_books.py）依赖 <result> 通知块落在
rollout/artifacts 里，早期 run 的通知不可考；而 dwf_run.result_json 是 journal DB 里
每个 run 的终局结果真源（与完成通知同源），零模型成本、确定性。

批1 是复合批次（2026-11-12 早晨，workflow 命名尚未统一为「裁决批N」）：
核心 = ATS-I 31项zoom·修正版（120 子主张 = W020 记载的 75/43/2），加同轮四个卫星裁决
run（LANA遗留600dpi / LANA-p9重裁 / Joshi5页 / p4真裁复核），按时间顺序合成一册。

用法：python3 render_adjudication_books_db.py [--dry-run] [--only 批12,批13]
同名多 run（cancelled/续跑）：取 status=completed 且 findings 最多者。
"""
import json
import os
import re
import sqlite3
import sys

DB = os.path.expanduser("~/.zcode/cli/db/db.sqlite")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "adjudication-books")
NAME_PAT = re.compile(r"^裁决批(\d+a?)·")

# (run_id, 小节标题)；顺序 = 2026-11-12 早晨实际执行顺序
BATCH1_COMPOSITE = [
    ("dwfrun-7efaa322-ff70-4e8c-87e9-01789c417795", "ATS-I裁决批·31项zoom·修正版（核心，120 子主张）"),
    ("dwfrun-4cf8efe9-97ba-48b5-ac61-82580e6e0398", "LANA遗留裁决·600dpi"),
    ("dwfrun-d5d9c1b5-f570-4465-b1ec-d2a6004cb4f5", "LANA-p9重裁裁决"),
    ("dwfrun-cc08a605-f2a4-4719-a0b2-6d45e9e805aa", "Joshi2020-10裁决批·5页"),
    ("dwfrun-d50c0799-f87f-4af9-8103-fcf93e88a5b2", "p4-Ē̂真裁复核"),
]


def load_batch1(conn):
    parts, findings, verified = [], [], []
    for rid, sub_name in BATCH1_COMPOSITE:
        row = conn.execute("SELECT result_json FROM dwf_run WHERE id=?", (rid,)).fetchone()
        if not row or not row[0]:
            print(f"WARN 批1组件缺失: {rid}")
            continue
        obj = json.loads(row[0])
        fl = obj.get("findings")
        if not isinstance(fl, list):
            print(f"WARN 批1组件 {rid} 无 findings")
            continue
        parts.append({"name": sub_name, "rid": rid, "conclusion": obj.get("conclusion", "?"), "n": len(fl)})
        findings.extend(fl)
        verified.extend(obj.get("verified", []))
    obj = {
        "conclusion": "裁决批1（复合）：核心 ATS-I 31项zoom——成立 75 / 不成立 43 / 看不清 2"
                      "（+LANA ℒ 终裁：确系花体）；另含同轮卫星裁决 4 个 run",
        "findings": findings,
        "verified": verified,
        "_parts": parts,
    }
    return "composite:" + "+".join(p["rid"][15:23] for p in parts), obj


def main():
    dry = "--dry-run" in sys.argv
    only = None
    if "--only" in sys.argv:
        only = set(sys.argv[sys.argv.index("--only") + 1].split(","))
    conn = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    rows = conn.execute(
        "SELECT id, name, status, result_json FROM dwf_run WHERE name LIKE '裁决批%' ORDER BY time_created"
    ).fetchall()
    best = {}  # token -> (run_id, obj, completed)
    for rid, name, status, rj in rows:
        m = NAME_PAT.match(name or "")
        if not m or not rj:
            continue
        token = m.group(1)
        try:
            obj = json.loads(rj)
        except Exception as e:
            print(f"WARN {rid} ({name}): result_json 解析失败 {e}")
            continue
        findings = obj.get("findings")
        if not isinstance(findings, list):
            continue
        cand = (status == "completed", len(findings))
        cur = best.get(token)
        # completed 优先；同级比 findings 数
        if cur is None or cand > (True, len(cur[1]["findings"])):
            best[token] = (rid, obj, status == "completed")
    rid1, obj1 = load_batch1(conn)
    conn.close()
    best["1"] = (rid1, obj1, True)

    order = sorted(best, key=lambda t: (0 if t == "1" else 1, len(t), t))
    print("DB 批次覆盖:", {t: (v[0][:24], len(v[1]["findings"])) for t, v in sorted(best.items(), key=lambda x: (0 if x[0] == '1' else 1, len(x[0]), x[0]))})
    if dry:
        return
    os.makedirs(OUT, exist_ok=True)
    for token in order:
        if only and f"批{token}" not in only:
            continue
        rid, obj, _ = best[token]
        concl = obj.get("conclusion", "?")
        cnt = {"成立": 0, "不成立": 0, "看不清": 0}
        lines = []
        part_starts = {}
        if "_parts" in obj:
            idx = 0
            for p in obj["_parts"]:
                part_starts[idx] = p
                idx += p["n"]
        for i, it in enumerate(obj["findings"]):
            if i in part_starts:
                p = part_starts[i]
                lines += ["", f"### {p['name']}", f"- 小节结论：{p['conclusion']}（run={p['rid']}）", ""]
            v = it.get("what", "")
            for k in cnt:
                if v.startswith(k + "：") or v.startswith(k + ":"):
                    cnt[k] += 1
                    break
            lines.append(f"- **{it.get('where','?')}**：{v}（{it.get('evidence','?')}）")
        md = [f"# 批{token} 裁决书", "",
              f"- 结论：{concl}",
              f"- 子项合计：{len(obj['findings'])}（成立 {cnt['成立']} / 不成立 {cnt['不成立']} / 看不清 {cnt['看不清']}）",
              f"- 来源：workflow journal dwf_run.result_json（run={rid}；证据=300dpi 半页直读）"]
        nonprefixed = len(obj["findings"]) - sum(cnt.values())
        if "_parts" in obj and nonprefixed:
            md.append(f"- 注：三分类仅统计带「成立：/不成立：/看不清：」前缀的条目；其余 {nonprefixed} 项为问答式裁决"
                      "（Joshi 5页等早期小节，答案在前问题在后），原文照录、不计入三分类。")
        md += ["", "## 逐项裁决"] + [""] + lines + ["", "## verified", ""] + [f"- {v}" for v in obj.get("verified", [])]
        path = os.path.join(OUT, f"批{token}-裁决书.md")
        open(path, "w", encoding="utf-8").write("\n".join(md) + "\n")
        print("written", os.path.basename(path), len(obj["findings"]), "项")


if __name__ == "__main__":
    main()
