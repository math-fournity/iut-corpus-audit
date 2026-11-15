#!/usr/bin/env python3
"""pattern_prescreen.py — MinerU 可复现错误模式的免费 grep 预筛（第2波SUGGEST#1采纳项）。
对全部 _audit-md 切片跑已知模式，输出嫌疑页清单（供裁决派发优先定位）。
模式来源：第1/2波裁决实证——ff连字丢失、双标点、引号混入、\\Im混淆、年份202I腐蚀、自不一致。
用法: python3 pattern_prescreen.py [--doc <名>]   # 全库或单文档
产出: corpus-md-audit/tier0/PATTERN-SUSPECTS.tsv（页/模式/命中行样本）
"""
import glob, os, re, sys

WS = "/Volumes/D/audit-workspace"
OUT = "/Users/aurolafly/ABC/corpus-md-audit/tier0/PATTERN-SUSPECTS.tsv"

# (模式名, 正则, 说明) —— 全部来自已裁决实证，禁止凭空添加
PATTERNS = [
    ("ff连字丢失", r"\b(sufic|efect|difer|ofen|ofe|efort|staf|sufix|afect|Falcon|Scholz?e?.*Fala)", "第1波LANA/Dimitrov/ScholzeStix实证"),
    ("双标点", r"[,.;]{2,}", "第2波实证"),
    ("引号混入数学", r'\$[^$]*"', "第2波实证：\"99\"混上标类"),
    ("Im混淆", r"\\Im\b", "ATS-I实证：花体J误读为\\Im"),
    ("年份腐蚀", r"20[0-2][IloO]", "第2波实证：202I"),
    ("杂散点等号", r"\s\.\s?=", "第2波实证"),
    ("HTML残留", r"<sup>|<sub>|</small>|data-block-type", "LANA实证"),
    # —— 第37–42波裁决/审计实证补充（SUGGEST-LOG 采纳项，2026-11-13 回补落地）——
    ("弯引号→伪上标66/99", r"\^\{66\}|\^\{,9\}|\^\{99\}|\^\{6\}", "W037实证：TeX弯引号→^{66}…^{,9}"),
    ("变音符拆散", r"<sup>¨</sup>|Teichm¨|´etale|¨uller", "W037/W042实证：ü/é拆成组合符"),
    ("lgp→tgp", r"\btgp\b", "IUT-IV p81 600dpi裁决成立（LGP体系记号误读）"),
    ("LGP→LGF", r"\bLGF\b", "IUT-III p135/136/187 裁决成立"),
    ("§丢失(章号裸数字)", r"Chapter [IVX]+,\s*\d|\[IUTch[IV]+\]\s*\d", "IUT-IV p58实证：12处§全丢"),
    ("引号→fraktur伪码", r"\\mathfrak\{[ap]\}\s*\$", "W037/W041实证：引号包裹行内公式被读成𝔞/𝔭"),
    ("相邻数学组间纯空格(疑丢箭头)", r"\$\s+\$", "W042实证：→/⋊/·在相邻$…$间丢失"),
    ("双右括号Y(K))", r"Y\(K\)\)", "W042实证"),
    ("方括号→积分号∫cf.", r"\\int\s*cf|∫\s*cf", "IUT-III/W042实证：[cf.→∫cf."),
    ("幽灵Ω/Ψ邻[cf.", r"[\\OmegaΨ]\s*\[cf", "IUT-III p174实证"),
    ("花体/逻辑形误读候选", r"\\triangleright|\\bigsqcup|\\Vdash", "多批裁决：×/+/□/⊩字形互混高频候选"),
    ("幻影CJK", r"[\u4e00-\u9fff]", "W029实证：垃圾模式（英文论文出现汉字）"),
    ("\\ref残留", r"\\ref\{", "W029实证"),
    ("丢f词尾扩展", r"\bdiference|\befects|\bafairs|\bsufices", "W038/W041实证（ff连字家族扩展）"),
    ("Chn吞并(𝓕||-▷×μ族)", r"\( -Chn\)|\( -×μ\)", "W044实证：∧/∨与𝓕记号系统性丢失（p105-108各形态garble）"),
    ("iiib型编号粘连", r"\(iiib\)|\(ie\)|\(i-e\)", "RIMS1968 p86实证：(iii-b)→(iiib)、(i-e)→(ie)"),
    ("paragraph_title伪前缀2", r"^2§\s|^2\\S\d", "W045实证：§7→2§7等5+处（MinerU后处理缺陷）"),
    ("小型大写作者名销毁", r"GROTHENDIECK|SCHOLZE|STIX|MOCHIZUKI", "W045实证：小型大写5处销毁（命中即复核大小写形态）"),
    ("URL斜杠丢失", r"https?:(?!//)[^\s]+", "W045实证：8处斜杠丢失致路径粘连"),
    # —— 第47波实证补充（Yamashita_2017 审计实证，SUGGEST-LOG 采纳项）——
    ("占位符吞整图", r"\[Image block\]", "W047实证：p237/p238整图仅存占位符"),
    ("空tilde命令", r"\\tilde\{\s*\}", "W047实证：伪tilde空命令"),
    ("伪mathbf算子", r"\\mathbf\{\\nabla\}|\\mathbf\{\\Sigma\}", "W047实证：nabla/Sigma伪加粗"),
    ("H双美元粘连", r"H\$\$H", "W047实证"),
    ("图例标签泄漏", r"gl\. to loc\.", "W047实证：图例标签入正文"),
    ("行尾孤立伪2", r"[\)\]]\s2\s*$", "W047实证：右括号后伪2薄字形误读"),
    ("dagger叠字", r"\\stackrel\{\\dagger\}\{\}", "W047实证：前上标叠字"),
]

def screen_doc(name):
    hits = []
    for f in sorted(glob.glob(f"{WS}/{name}/_audit-md/p*.txt")):
        page = int(re.search(r"p(\d+)", os.path.basename(f)).group(1))
        for ln, line in enumerate(open(f, encoding="utf-8"), 1):
            for pname, pat, _src in PATTERNS:
                if re.search(pat, line):
                    hits.append((name, page, ln, pname, line.strip()[:120]))
    return hits

if __name__ == "__main__":
    only = sys.argv[sys.argv.index("--doc") + 1] if "--doc" in sys.argv else None
    names = [only] if only else sorted(os.path.basename(d) for d in glob.glob(f"{WS}/*") if os.path.isdir(d))
    all_hits = []
    for n in names:
        all_hits.extend(screen_doc(n))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("文档\t页\t行\t模式\t样本\n")
        for h in all_hits:
            f.write("\t".join(str(x) for x in h) + "\n")
    from collections import Counter
    by_pat = Counter(h[3] for h in all_hits)
    by_doc = Counter(h[0].split("_")[0] for h in all_hits)
    print(f"嫌疑命中 {len(all_hits)} 条 -> {OUT}")
    for p, c in by_pat.most_common():
        print(f"  {p}: {c}")
    print("按文档前缀:", dict(by_doc.most_common(8)))
