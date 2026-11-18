#!/bin/bash
# sync_workspace.sh — D盘工作区 → ABC/workspace/ 同步（私有仓缓存用）v2
# 用法: bash tools/publish/sync_workspace.sh [--delete]
#   默认只增不删（--delete 才镜像删除，删前确认）
# 产出：workspace/ 镜像 + workspace-MANIFEST.tsv（sha256\tpath\tbytes，位于 ABC 根）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SRC="<audit-workspace>"
DST="$ROOT/workspace"
mkdir -p "$DST"
if [ "${1:-}" = "--delete" ]; then
  echo "将删除 DST 中 SRC 没有的文件："; rsync -rn --delete "$SRC"/ "$DST"/ | head -20
  read -r -p "确认删除？(yes/no) " a; [ "$a" = "yes" ] || exit 1
  rsync -a --delete "$SRC"/ "$DST"/
else
  rsync -a "$SRC"/ "$DST"/
fi
cd "$ROOT"
find workspace -type f \( -name "*.png" -o -name "*.txt" \) -print0 | xargs -0 shasum -a 256 > /tmp/ws-manifest.raw
python3 - <<'EOF'
import os
rows=[l.rstrip("\n").split("  ",1) for l in open("/tmp/ws-manifest.raw",encoding="utf-8") if l.strip()]
with open("workspace-MANIFEST.tsv","w",encoding="utf-8") as f:
    f.write("sha256\tpath\tbytes\n")
    for h,p in rows:
        f.write(f"{h}\t{p.strip()}\t{os.path.getsize(p.strip())}\n")
print("MANIFEST rows:", len(rows))
EOF
echo "synced -> $DST ($(find workspace -type f | wc -l | tr -d ' ') files)"
