#!/usr/bin/env python3
"""gen_quality_audit.py — 中途质量审计点生成器（债3：实测假阴性率）v2。
对指定文档的指定页渲染 300dpi 半页（qa-top/qa-bot），生成**逐页独立代理**的盲审 workflow：
每页一个代理，同时读 图（真值）+ MinerU 切片（待检对象）——与审计任务同口径；不看矩阵（保持盲审）。
v2 修正：v1 只读图不读切片，测不出提取层缺陷（出现 FAIL→PASS 假反向）。
用法: python3 gen_quality_audit.py --out <ts路径> [--pages-json '<json>']
默认页集：IUT-II 随机 7 页；IUT-III Tier-0红×WARN(41,125)+FAIL 5 页；
IUT-IV Tier-0红×WARN(17)+FAIL 6 页。
"""
import fitz, glob, json, os, sys

REPO = "/Users/aurolafly/ABC"
WS = "/Volumes/D/audit-workspace"

DEFAULT_PAGES = {
    "Mochizuki_IUT-II_2020-12-23": [10, 35, 60, 85, 110, 135, 160],
    "Mochizuki_IUT-III_2020-05-18": [41, 125, 51, 82, 127, 174, 187],
    "Mochizuki_IUT-IV_2020-04-22": [17, 58, 81, 84, 3, 30, 60],
}


def find_pdf(name):
    for c in glob.glob(f"{REPO}/corpus/**/{name}.pdf", recursive=True):
        return c
    return None


def main():
    args = sys.argv[1:]
    out = args[args.index("--out") + 1]
    pages = json.loads(args[args.index("--pages-json") + 1]) if "--pages-json" in args else DEFAULT_PAGES

    rendered = 0
    for doc, ps in pages.items():
        pdf = find_pdf(doc)
        if not pdf:
            print("NO PDF", doc)
            continue
        d = fitz.open(pdf)
        zdir = f"{WS}/{doc}/_zoom"
        os.makedirs(zdir, exist_ok=True)
        for p in ps:
            if p > len(d):
                continue
            page = d[p - 1]
            r = page.rect
            mid = 60 + (r.y1 - 120) / 2
            for tag, y0, y1 in [(f"qa-p{p:03d}-top", 60, mid), (f"qa-p{p:03d}-bot", mid, r.y1 - 60)]:
                page.get_pixmap(dpi=300, clip=fitz.Rect(50, y0, r.width - 50, y1),
                                colorspace=fitz.csGRAY).save(f"{zdir}/{tag}.png")
            rendered += 1
    print(f"rendered {rendered} pages (300dpi halves)")

    docs = list(pages.keys())
    ts = f'''// 中途质量审计点（债3 v2）：逐页独立盲审——图（真值）+ MinerU 切片（待检），不看矩阵。
interface PageVerdict {{
  /** PDF 页号 */
  page: number;
  /** PASS / WARN / FAIL / UNRESOLVED */
  verdict: string;
  /** 结构/文字/公式/题注/图表/语义，各取 ✓ / ⚠ / ✗ */
  structure: string; text: string; formula: string; caption: string; figure: string; semantics: string;
  /** 本页发现的全部缺陷，逐条写记号形态与位置；没有写「无」 */
  defects: string;
}}
const PAGES: Record<string, number[]> = {json.dumps(pages, ensure_ascii=False)};
const DOCS = {json.dumps(docs, ensure_ascii=False)};
const WSDIR = (doc: string) => `/Volumes/D/audit-workspace/${{doc}}/_zoom`;
const MDDIR = (doc: string) => `/Volumes/D/audit-workspace/${{doc}}/_audit-md`;
const ask = (doc: string, p: number) => `你是独立质量复核代理，盲审 ${doc} 第 ${{p}} 页。
按序 Read 三份文件：
1) ${{WSDIR(doc)}}/qa-p${{String(p).padStart(3, "0")}}-top.png（300dpi 上半页，图像=真值）
2) ${{WSDIR(doc)}}/qa-p${{String(p).padStart(3, "0")}}-bot.png（300dpi 下半页）
3) ${{MDDIR(doc)}}/p${{String(p).padStart(3, "0")}}.txt（MinerU 逐页提取切片=待检对象）
任务：以图像为真值，逐点比对切片，按六维度判定本页（这就是审计任务本身的口径）。
硬规则：只读这三份文件；不读矩阵/其他页/其他文档；verdict 只能是 PASS/WARN/FAIL/UNRESOLVED；
维度格只能是 ✓/⚠/✗；看不清的记号标「看不清」并说明位置，绝不猜；禁止任何×倍放大措辞（你没裁片）。
判定规则：PASS=无✗且语义✓；WARN=有⚠但无✗；FAIL=任一维度✗；UNRESOLVED=存疑无法归级。
defects 逐条写本页全部缺陷（丢符号/字形混淆/上下标/引号/连字/结构/缺行），宁多勿漏；没有写「无」。
只返回 1 条 PageVerdict（page=${{p}}），不要返回其他页。`;

phase("逐页盲审复核（21 页）");
const all: PageVerdict[] = [];
for (const doc of DOCS) {{
  const rs = await Promise.all(PAGES[doc].map((p) => agent(`QA-${{doc}}-p${{p}}`).ask<PageVerdict>(ask(doc, p))));
  all.push(...rs);
}}
log(`盲审完成：${{all.length}} 页`);
await artifact.markdown("qa-report", [
  "# 中途质量审计点（2026-11-13，债3 v2）", "",
  ...all.map((v) => `- **${{DOCS.find((d) => PAGES[d].includes(v.page)) || "?"}}|p${{v.page}}**：${{v.verdict}}（${{v.structure}}/${{v.text}}/${{v.formula}}/${{v.caption}}/${{v.figure}}/${{v.semantics}}）\\n  - ${{v.defects}}`),
].join("\\n"), {{ title: "盲审复核报告（债3 v2）", description: `${{all.length}} 页独立盲审（图+切片）`, primary: true }});
return {{
  conclusion: `盲审完成 ${{all.length}} 页：` + all.map((v) => `p${{v.page}} ${{v.verdict}}`).join(" / "),
  findings: all.map((v) => ({{ where: `${{DOCS.find((d) => PAGES[d].includes(v.page)) || "?"}}|${{v.page}}`, what: `${{v.verdict}}：${{v.defects}}`, evidence: "300dpi半页+切片盲审", status: "verified" as const, severity: "low" as const }})),
  verified: ["每页两张 300dpi 半页 + MinerU 切片，逐页独立代理盲审（未看矩阵）"],
  notCovered: ["仅 21 页抽样，非全量"],
}};'''
    open(out, "w", encoding="utf-8").write(ts)
    print("workflow ->", out)


if __name__ == "__main__":
    main()
