#!/usr/bin/env python3
"""gen_adjudication.py — 裁决批 workflow 生成器（批3+ 的可持续派发入口）。
从分片提取全部 ZOOM-OPEN 项（含"需600dpi回图"且无"已裁决"的行）→ 渲染 300dpi 半页 →
生成裁决 workflow TS（含防虚报铁律+verdict三选一）→ stdout 报告产出路径。
用法: python3 gen_adjudication.py [--max 120] [--out .zcode/…/裁决批N.dwf.ts] [--name 裁决批N]
产出后的回填: 裁决书 artifact 是用户卡片；编排者按裁决书逐页回填 token（人工/后续工具）。
"""
import fitz, glob, json, os, re, sys

REPO = "~/ABC"
WS = "<audit-workspace>"
VENV = "/Volumes/D/toolchain-cache/mineru-venv/bin/python"

def find_pdf(name):
    for c in glob.glob(f"{REPO}/corpus/**/{name}.pdf", recursive=True):
        return c
    return None

def main():
    args = sys.argv[1:]
    maxn = int(args[args.index("--max") + 1]) if "--max" in args else 120
    out = args[args.index("--out") + 1] if "--out" in args else "~/shuxuedashi-glm5.2-worktree/.zcode/workflow-drafts/gen-裁决批.dwf.ts"
    name = args[args.index("--name") + 1] if "--name" in args else "裁决批·自动生成"

    # 1) 提取 zoom 项
    items = []
    for f in sorted(glob.glob(f"{REPO}/corpus-md-audit/shards/*/*.md")):
        doc = f.split("/shards/")[1].split("/")[0]
        for l in open(f, encoding="utf-8"):
            if "需600dpi回图" in l and "已裁决" not in l and re.match(r"^\| \d+ \| Y \|", l):
                cells = [c.strip() for c in l.strip().strip("|").replace("\\|", "¦").split("|")]
                if len(cells) == 10:
                    items.append({"doc": doc, "page": int(cells[0]), "note": cells[9].replace("¦", "|")[:350]})
    items = items[:maxn]
    print(f"提取 zoom 项 {len(items)} 条")

    # 2) 渲染半页
    pdfs = {}
    rendered = set()
    for it in items:
        key = (it["doc"], it["page"])
        if key in rendered: continue
        rendered.add(key)
        pdf = pdfs.get(it["doc"]) or find_pdf(it["doc"])
        pdfs[it["doc"]] = pdf
        if not pdf: it["skip"] = True; continue
        doc = fitz.open(pdf)
        if it["page"] > len(doc): it["skip"] = True; continue
        page = doc[it["page"] - 1]; r = page.rect
        zdir = f"{WS}/{it['doc']}/_zoom"; os.makedirs(zdir, exist_ok=True)
        mid = 60 + (r.y1 - 120) / 2
        for tag, y0, y1 in [(f"p{it['page']:03d}-top", 60, mid), (f"p{it['page']:03d}-bot", mid, r.y1 - 60)]:
            page.get_pixmap(dpi=300, clip=fitz.Rect(50, y0, r.width - 50, y1), colorspace=fitz.csGRAY).save(f"{zdir}/{tag}.png")
    live = [i for i in items if not i.get("skip")]
    print(f"渲染 {len(rendered)} 页半页，可用项 {len(live)}")

    # 3) 生成 workflow TS
    claims = {f'{i["doc"]}|{i["page"]}': i["note"].replace('"', "〝").replace("\\", "\\\\") for i in live}
    groups = [live[k:k+6] for k in range(0, len(live), 6)]
    ts = [f'''// {name}：{len(live)} 项 zoom 存疑（gen_adjudication.py 自动生成）。verdict三选一+防虚报为硬约束。
interface Verdict {{ page: string; question: string; verdict: string; seen: string; }}
const CLAIMS: Record<string, string> = {json.dumps(claims, ensure_ascii=False)};''']
    ts.append("const GROUPS: string[][] = " + json.dumps([[f'{i["doc"]}|{i["page"]}' for i in g] for g in groups], ensure_ascii=False) + ";")
    ts.append('''const WSDIR = (doc: string) => `<audit-workspace>/${doc}/_zoom`;
const asks = GROUPS.map((g, gi) => `你是视觉裁决代理（第${gi + 1}组）。逐页裁决。对每页：Read ${"WSDIR(doc)"} 下 pNNN-top.png 与 pNNN-bot.png（NNN=三位零填充页号）。只裁决备注中标「需600dpi回图/存疑/无法确证/100dpi」的子主张。
硬规则：verdict 字段只能是 成立/不成立/看不清 三词之一；看不清绝不许猜；禁止任何×倍放大措辞——你真裁了局部（可用 zoom_locate.py）就写裁片路径，没裁就只描述半页图所见；seen 逐字写记号形态与所在公式。
本组页与主张（键=文档|页码）：
${g.map((k) => `【${k}】${CLAIMS[k]}`).join("\\n")}`);
''')
    ts.append(f'''phase("{name}：{len(groups)} 组并行");
const results = await Promise.all(GROUPS.map((g, gi) => agent("裁决-{name}-组" + (gi + 1)).ask<Verdict[]>(asks[gi])));
const all = results.flat();
const ok = all.filter((v) => v.verdict === "成立").length;
const no = all.filter((v) => v.verdict === "不成立").length;
log(`{name} 裁决完毕 | 成立 ${{ok}} / 不成立 ${{no}} / 看不清 ${{all.length - ok - no}}（共 ${{all.length}}）`);
phase("落盘裁决书");
await artifact.markdown("adjudication", [
  "# {name} 裁决书", "",
  ...all.map((v) => `- **${{v.page}}**：${{v.verdict}} —— ${{v.question}}\\n  - 实见：${{v.seen}}`), "",
].join("\\n"), {{ title: "{name} 裁决书", description: `成立 ${{ok}} / 不成立 ${{no}} / 看不清 ${{all.length - ok - no}}`, primary: true }});
return {{
  conclusion: `{name}：成立 ${{ok}} / 不成立 ${{no}} / 看不清 ${{all.length - ok - no}}。`,
  findings: all.map((v) => ({{ where: v.page, what: `${{v.verdict}}：${{v.question}}`, evidence: "300dpi半页", status: "verified" as const, severity: "low" as const }})),
  verified: ["基于300dpi半页直接视觉阅读"],
  notCovered: [],
}};''')
    open(out, "w", encoding="utf-8").write("\n".join(ts))
    print(f"workflow 已生成 -> {out}（{len(groups)} 组/{len(live)} 项）")

if __name__ == "__main__":
    main()
