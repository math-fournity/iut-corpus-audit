#!/usr/bin/env python3
"""backfill_adjudication.py — 把裁决批 token 回填到矩阵行（只写批覆盖的文档/页）。
用法:
  backfill_adjudication.py --draft <裁决批N.dwf.ts> --batch <标签> [--register "doc|page,doc|page"]
从 draft 的 CLAIMS 字面量提取 doc|page 键（生成器写入的批覆盖集），对每个键找到
含「需600dpi回图」且无「已裁决/已登记」的行，行尾追加「 已裁决(<标签>)」；
--register 指定的页改用「 已登记(S4:图像块占位,<标签>看不清)」（看不清=转 S4 重提取，不留假裁决）。
每文档输出回填/覆盖数与未匹配页；未匹配页可能是被续跑重审替换了行（需人工核）。
"""
import glob, json, re, sys

REPO = "~/ABC"


def main():
    args = sys.argv[1:]
    draft = args[args.index("--draft") + 1]
    batch = args[args.index("--batch") + 1]
    registers = set(args[args.index("--register") + 1].split(",")) if "--register" in args else set()

    line = [l for l in open(draft, encoding="utf-8") if l.startswith("const CLAIMS")][0]
    body = line.split(" = ", 1)[1].rstrip()
    if body.endswith(";"):
        body = body[:-1]
    claims = json.loads(body)

    by_doc = {}
    for k in claims:
        doc, page = k.split("|")
        by_doc.setdefault(doc, []).append(int(page))

    total_hit = 0
    for doc, pages in sorted(by_doc.items()):
        shards = sorted(glob.glob(f"{REPO}/corpus-md-audit/shards/{doc}/*.md"))
        hit, miss = 0, []
        for page in pages:
            pat = re.compile(rf"^\|\s*{page}\s*\|")
            done = False
            for shard in shards:
                lines = open(shard, encoding="utf-8").read().splitlines(keepends=True)
                changed = False
                for i, l in enumerate(lines):
                    if not pat.match(l):
                        continue
                    if "需600dpi回图" not in l:
                        continue
                    # 只跳过已真正裁决的行；「已登记(待裁决批N)」是排队标记，必须允许追加裁决
                    if "已裁决" in l:
                        continue
                    if not l.rstrip().endswith(" |"):
                        continue
                    token = (f" 已登记(S4:图像块占位,{batch}看不清)"
                             if f"{doc}|{page}" in registers else f" 已裁决({batch})")
                    lines[i] = l.rstrip()[:-1].rstrip() + token + " |\n"
                    changed = True
                    done = True
                    break
                if changed:
                    open(shard, "w", encoding="utf-8").writelines(lines)
                    break
            if done:
                hit += 1
            else:
                miss.append(page)
        total_hit += hit
        msg = f"{doc}: 回填 {hit}/{len(pages)}"
        if miss:
            msg += f"  ⚠未匹配页 {sorted(miss)}"
        print(msg)
    print(f"合计回填 {total_hit}/{len(claims)}")


if __name__ == "__main__":
    main()
