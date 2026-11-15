#!/usr/bin/env python3
"""save_scope.py <out-path> <json-string> — write inventory snapshot (leader-only step)."""
import os, sys
path, data = sys.argv[1], sys.argv[2]
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as f:
    f.write(data)
print("scope saved:", path)
