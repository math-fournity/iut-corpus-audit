#!/usr/bin/env python3
# prep_shards.py v2 - matrix shard headers in repo corpus-md-audit/shards/<name>/
# Usage: python3 tools/workflows/prep_shards.py '<JSON: [{"name":..,"shard":..,"range":"p1-p25"}...]>'
import json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
spec = json.loads(sys.argv[1])
HEADER = ("| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |\n"
          "|---|---|---|---|---|---|---|---|---|---|\n")
for u in spec:
    d = os.path.join(REPO, "corpus-md-audit", "shards", u["name"])
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, u["shard"])
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# {u['shard']} — {u['name']} {u['range']}\n\n{HEADER}")
print(f"prep_shards: {len(spec)} shards ensured (repo)")
