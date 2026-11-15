#!/usr/bin/env python3
"""repair_shard_rows.py — 矩阵分片行修复工具（波间机械修复的唯一入口）。
功能：
  1. 裸竖线修复：列数≠10 的行，前 9 列保留、第 10 列起所有片段以转义竖线 \\| 重拼；
  2. 宽空格修复：`|  54  |` 型单元格多余空格归一；
  3. 去重：同页多行时删除列数≠10 的破损行（保留合格行）；两行都合格则报错不动；
  4. 自测：修复后逐分片跑 count_rows 同款校验，输出每分片合格行数。
用法: python3 repair_shard_rows.py <shard.md> [<shard.md> ...] [--dedup]
"""
import re, sys, subprocess

VERDICTS = ("PASS", "WARN", "FAIL", "UNRESOLVED")

def cells_of(l):
    return [c.strip() for c in l.strip().strip("|").replace("\\|", "\u00a6").split("|")]

def valid(cells):
    return len(cells) == 10 and cells[1].replace("*", "") == "Y" and cells[8].replace("*", "") in VERDICTS

def repair_line(l):
    # 先归一宽空格
    l = re.sub(r"\|\s{2,}", "| ", l)
    l = re.sub(r"\s{2,}\|", " |", l)
    frags = l.strip().strip("|").replace("\\|", "\u00a6").split("|")
    frags = [c.strip() for c in frags]
    if len(frags) <= 10:
        return None  # 不是列数问题，交给调用方
    head, note_frags = frags[:9], frags[9:]
    note = "\\|".join(note_frags).replace("\u00a6", "\\|")  # 裸|转义，原有转义保持
    return "| " + " | ".join(head) + " | " + note + " |"

def process(path, dedup):
    lines = open(path, encoding="utf-8").read().splitlines(keepends=True)
    out, fixed, dropped, conflict = [], 0, 0, []
    for l in lines:
        m = re.match(r"^\|\s*(\d+)\s*\|", l)
        if not m:
            out.append(l); continue
        page = int(m.group(1))
        # 空格归一（对所有数据行，幂等）——count_rows 行正则对宽空格敏感
        l = re.sub(r"\|\s{2,}", "| ", l)
        l = re.sub(r"\s{2,}\|", " |", l)
        cells = cells_of(l)
        if valid(cells):
            out.append(l); continue
        rep = repair_line(l)
        if rep and valid(cells_of(rep)):
            out.append(rep); fixed += 1; continue
        # 修不好的破损行：dedup 模式下若同页稍后有/前有合格行则可删——先保守保留标记
        conflict.append(page)
        out.append(l)
    if dedup and conflict:
        # 同页既有合格行又有修不好的破损行 → 删破损行
        good = {int(m.group(1)) for m in (re.match(r"^\|\s*(\d+)\s*\|", l) for l in out) if m and valid(cells_of(l))}
        final = []
        for l in out:
            m = re.match(r"^\|\s*(\d+)\s*\|", l)
            if m and int(m.group(1)) in conflict and not valid(cells_of(l)) and int(m.group(1)) in good:
                dropped += 1; continue
            final.append(l)
        out = final
    open(path, "w", encoding="utf-8").writelines(out)
    # 自测：count_rows 同款
    n = sum(1 for l in out if (m := re.match(r"^\|\s*(\d+)\s*\|", l)) and valid(cells_of(l)))
    return fixed, dropped, n, conflict

if __name__ == "__main__":
    args = sys.argv[1:]
    dedup = False  # BUG禁用(2026-11-12)：dedup路径有状态缺陷误删行，重建用 FINAL 矩阵方案；待带回归测试重写
    # dedup = "--dedup" in args
    files = [a for a in args if not a.startswith("--")]
    for f in files:
        fixed, dropped, n, conflict = process(f, dedup)
        flag = " ⚠仍有冲突页: " + str(conflict) if conflict else ""
        print(f"{f.split('/')[-1][:60]}: 修 {fixed} / 删 {dropped} / 合格行 {n}{flag}")
