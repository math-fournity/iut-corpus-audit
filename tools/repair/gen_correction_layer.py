#!/usr/bin/env python3
"""gen_correction_layer.py — S4 Step-1：从 PATTERN-SUSPECTS.tsv 生成 B 形态补丁层。

设计原则（诚实分层，P-09）：
- 预筛命中=嫌疑非缺陷。只有「错误形态本身无歧义」的规则才允许确定性修复
  （fix_type=deterministic）；正确形态依赖图像的（fix_type=visual-required）只登记不动手；
  Image-block 整页占位（fix_type=routed-223）转 Step-3 管道。
- 逐条 entry 带 before/after（确定性类）或 before/proposed（视觉类）+ verify_status
  （rule-based / visual-pass / visual-fail / needs-visual / routed）。
- 双标点排除合法省略号（…与...）：只修恰两个的重复（,, ;; .. 而非 ...）。

产出：ABC/correction-layer/entries/<doc>.tsv + families/<F##>.md 骨架 + SUMMARY.md 账目。
"""
import os
import re
import sys
from collections import Counter, defaultdict

WS = "<audit-workspace>"
ABC = "~/ABC"
SRC = f"{ABC}/corpus-md-audit/tier0/PATTERN-SUSPECTS.tsv"
OUT = f"{ABC}/correction-layer"

# 10 族（SUMMARY-FINAL §三）+ 预筛模式 → 族映射
FAMILIES = {
    "F01": "自定义记号互混",
    "F02": "花体/Fraktur/黑板体拍平",
    "F03": "ff连字丢失",
    "F04": "上下标结构破坏",
    "F05": "箭头丢失/退化",
    "F06": "引号→上标乱码",
    "F07": "重音拆散",
    "F08": "幽灵字符",
    "F09": "双栏/索引塌缩",
    "F10": "原稿自带 typo（提取忠实，非缺陷）",
}

PATTERN_META = {
    # 模式名: (族, fix_type, fix_fn 或 None)
    "ff连字丢失": ("F03", "deterministic", "ff_lig"),
    "丢f词尾扩展": ("F03", "deterministic", "ff_lig"),
    "双标点": ("F08", "deterministic", "dbl_punct"),  # 双标点归幽灵字符族（伪字符注入）
    "引号混入数学": ("F06", "visual-required", None),
    "Im混淆": ("F02", "visual-required", None),  # \Im 可能是真 Im（本人名）也可能是花体J误读
    "年份腐蚀": ("F08", "deterministic", "year"),
    "杂散点等号": ("F08", "visual-required", None),
    "HTML残留": ("F08", "deterministic", "html"),
    "弯引号→伪上标66/99": ("F06", "deterministic", "quote66"),
    "变音符拆散": ("F07", "deterministic", "accent"),
    "lgp→tgp": ("F01", "deterministic", "tgp"),
    "LGP→LGF": ("F01", "deterministic", "lgf"),
    "§丢失(章号裸数字)": ("F04", "visual-required", None),  # §插回位置依赖上下文
    "引号→fraktur伪码": ("F06", "deterministic", "fraktur_quote"),
    "相邻数学组间纯空格(疑丢箭头)": ("F05", "visual-required", None),
    "双右括号Y(K))": ("F08", "deterministic", "ykk"),
    "方括号→积分号∫cf.": ("F08", "deterministic", "intcf"),
    "幽灵Ω/Ψ邻[cf.": ("F08", "visual-required", None),
    "花体/逻辑形误读候选": ("F02", "visual-required", None),  # 合法LaTeX居多，纯候选
    "幻影CJK": ("F08", "visual-required", None),
    "\\ref残留": ("F08", "deterministic", "refx"),
    "Chn吞并(𝓕||-▷×μ族)": ("F01", "visual-required", None),
    "iiib型编号粘连": ("F01", "deterministic", "iiib"),
    "paragraph_title伪前缀2": ("F04", "deterministic", "pseudo2"),
    "小型大写作者名销毁": ("F02", "visual-required", None),
    "URL斜杠丢失": ("F05", "visual-required", None),  # 原URL不可恢复，需回图
    "占位符吞整图": ("F09", "routed-223", None),
    "空tilde命令": ("F05", "deterministic", "empty_tilde"),
    "伪mathbf算子": ("F08", "visual-required", None),
    "H双美元粘连": ("F04", "visual-required", None),  # Step-2 抽验翻车（Y2017 p133 图上无孤立H），降级
    "图例标签泄漏": ("F08", "deterministic", "legend"),
    "行尾孤立伪2": ("F08", "visual-required", None),  # 行尾 2 可能是真实公式内容
    "dagger叠字": ("F01", "deterministic", "dagger_stack"),
}

FF_MAP = [
    (r"\bsufic", "suffic"), (r"\befect", "effect"), (r"\bdifer\b", "differ"),
    (r"\bofen\b", "often"), (r"\befort", "effort"), (r"\bstaf\b", "staff"),
    (r"\bsufix", "suffix"), (r"\bafect", "affect"), (r"\bdiference", "difference"),
    (r"\befects", "effects"), (r"\bsufices", "suffices"),
]
ACCENTS = [
    ("Teichm¨uller", "Teichmüller"), ("teichm¨uller", "teichmüller"),
    ("Teichm¨uller", "Teichmüller"), ("¨uller", "üller"),  # 兜底：其余 *¨uller 词
    ("´etale", "étale"), ("´E", "É"),
    ("<sup>¨</sup>", "̈"),  # 组合分音符，视觉抽验核对
]
# Step-2 抽验根因修正（2026-11-15）：混排相邻标点（「i.e.,」「Y., M.」的句点+逗号）是合法
# 英语，折叠即毁——只折叠**同字符重复**（,, / .. / ;;），Step-2 实证 2 例 fix-wrong。
PUNCT_FIX = [
    (r"(?<!,),,(?!,)", ","),
    (r"(?<!\.)\.\.(?!\.)", "."),
    (r"(?<!;);;(?!;)", ";"),
]


def apply_fix(fn_name, line):
    out = line
    if fn_name == "ff_lig":
        for pat, rep in FF_MAP:
            out = re.sub(pat, rep, out)
    elif fn_name == "dbl_punct":
        for pat, rep in PUNCT_FIX:
            out = re.sub(pat, rep, out)
    elif fn_name == "year":
        out = re.sub(r"20([0-2])[IloO]\b", lambda m: "20" + m.group(1) + "1", out)
    elif fn_name == "html":
        out = re.sub(r"<sup>(.*?)</sup>", r"^\1", out)
        out = re.sub(r"<sub>(.*?)</sub>", r"_\1", out)
    elif fn_name == "quote66":
        out = out.replace("^{66}", "”").replace("^{99}", "”").replace("^{,9}", "，”")
    elif fn_name == "accent":
        for a, b in ACCENTS:
            out = out.replace(a, b)
    elif fn_name == "tgp":
        out = re.sub(r"\btgp\b", "lgp", out)
    elif fn_name == "lgf":
        out = re.sub(r"\bLGF\b", "LGP", out)
    elif fn_name == "fraktur_quote":
        out = re.sub(r"\\mathfrak\{([ap])\}\s*\$", r"”$", out)
    elif fn_name == "ykk":
        out = out.replace("Y(K))", "Y(K)")
    elif fn_name == "intcf":
        out = re.sub(r"\\int\s*cf\.?", "[cf.", out, count=1)
        out = re.sub(r"∫\s*cf\.?", "[cf.", out, count=1)
    elif fn_name == "refx":
        out = re.sub(r"\\ref\{([^}]*)\}", r"[\1]", out)
    elif fn_name == "iiib":
        out = out.replace("(iiib)", "(iii-b)").replace("(ie)", "(i-e)")
    elif fn_name == "pseudo2":
        out = re.sub(r"^2§\s", "§", out)
        out = re.sub(r"^2\\S(\d)", r"§\1", out)
    elif fn_name == "empty_tilde":
        out = re.sub(r"\\tilde\{\s*\}", "", out)
    elif fn_name == "hdd":
        out = out.replace("H$$H", "H$ $H")
    elif fn_name == "legend":
        out = re.sub(r"gl\.\s*to\s*loc\.", "", out)
    elif fn_name == "dagger_stack":
        out = re.sub(r"\\stackrel\{\\dagger\}\{\}", r"{}^{\\dagger}", out)
    return out


def main():
    entries = defaultdict(list)  # doc -> rows
    stats = Counter()
    sample_by_family = defaultdict(list)
    with open(SRC, encoding="utf-8") as f:
        next(f)
        for raw in f:
            doc, page, ln, pname, sample = (raw.rstrip("\n").split("\t") + [""] * 5)[:5]
            meta = PATTERN_META.get(pname)
            if not meta:
                continue
            fam, ftype, fn = meta
            stats[(fam, ftype)] += 1
            # 读 _audit-md 整行做 before（预筛样本仅前120字符，缺陷常在样本外）
            ptxt = f"{WS}/{doc}/_audit-md/p{int(page):03d}.txt"
            try:
                with open(ptxt, encoding="utf-8") as pf:
                    for i, pline in enumerate(pf, 1):
                        if i == int(ln):
                            before = pline.rstrip("\n")
                            break
                    else:
                        before = sample
            except FileNotFoundError:
                before = sample
            if ftype == "deterministic":
                after = apply_fix(fn, before)
                if after == before:
                    ftype, after = "deterministic-nop", before  # 规则在样本上无变化（样本截断所致）
                    status = "rule-noop"
                else:
                    status = "rule-based"
            elif ftype == "routed-223":
                after, status = "", "routed"
            else:
                after, status = "", "needs-visual"
            entries[doc].append((page, ln, fam, pname, ftype, status, before, after))
            if len(sample_by_family[fam]) < 8:
                sample_by_family[fam].append((doc, page, pname, before, after, status))
    os.makedirs(f"{OUT}/entries", exist_ok=True)
    os.makedirs(f"{OUT}/families", exist_ok=True)
    total = 0
    for doc, rows in sorted(entries.items()):
        with open(f"{OUT}/entries/{doc}.tsv", "w", encoding="utf-8") as f:
            f.write("页\t行\t族\t模式\t修复型\t状态\t修前\t修后\n")
            for r in rows:
                f.write("\t".join(str(x).replace("\t", " ") for x in r) + "\n")
        total += len(rows)
    # 族卡骨架（≥3 对照样本由 Step-2 视觉抽验补充勾选）
    for fid, fname in FAMILIES.items():
        rows = [r for (f2, t), c in [] for r in []]  # 占位
        with open(f"{OUT}/families/{fid}.md", "w", encoding="utf-8") as f:
            f.write(f"# {fid} {fname}（补丁层族卡）\n\n> SUMMARY-FINAL §三 族。修复规则与样本见下；"
                    f"verify_status 语义=rule-based(规则推断,待抽验)/visual-pass/visual-fail/needs-visual/routed。\n\n"
                    f"## 命中样本（预筛前 8 条）\n\n")
            for doc, page, pname, before, after, status in sample_by_family.get(fid, []):
                b = before if len(before) <= 160 else before[:157] + "…"
                a = after if (not after or len(after) <= 160) else (after[:157] + "…")
                f.write(f"- **{doc}|p{page}**（{pname}，{status}）\n  - 修前：`{b}`\n"
                        f"  - 修后：`{a if after else '（需视觉定谳/转223管道）'}`\n")
            f.write("\n## 修前/修后对照样本（≥3 例，Step-2 视觉抽验后回填）\n\n- [ ] 例1\n- [ ] 例2\n- [ ] 例3\n")
    with open(f"{OUT}/SUMMARY.md", "w", encoding="utf-8") as f:
        f.write("# correction-layer 账目（B 形态补丁层）\n\n> 生成：tools/repair/gen_correction_layer.py；"
                "真源=PATTERN-SUSPECTS.tsv（14673 预筛命中）+ 族规则。预筛命中=嫌疑非缺陷；"
                "仅 deterministic 类生成修后文本，其余登记待视觉定谳或转 223 页管道。\n\n"
                "| 族 | 修复型 | 条数 |\n|---|---|---|\n")
        for (fam, ftype), c in sorted(stats.items()):
            f.write(f"| {fam} {FAMILIES[fam]} | {ftype} | {c} |\n")
        f.write(f"\n合计 {total} 条（entries/ 按文档分文件）。\n")
    print(f"entries: {total} 条 | 族×型分布: {dict(stats)}")
    print(f"落盘 {OUT}/entries/ + families/ + SUMMARY.md")


if __name__ == "__main__":
    main()
