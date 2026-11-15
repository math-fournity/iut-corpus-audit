#!/usr/bin/env python3
"""export_adjudication.py — 裁决书入册占位与说明（v0）

裁决书是 workflow run 的 artifact（markdown），不在 ABC 仓内。入册方式（人工/编排者）：
  1. GetWorkflowRun(<批N run_id>) → artifacts 里 title 含「裁决书」→ read_output 取 markdown 全文；
  2. 存 adjudication-books/批N-裁决书.md；
  3. commit 进私有仓（公开仓导出时整目录拷贝）。
本脚本仅校验目录状态。自动化取回待 ZCode artifact 存储 CLI 化后补。
"""
import glob, os, sys
D = os.path.join(os.path.dirname(__file__), "..", "..", "adjudication-books")
os.makedirs(D, exist_ok=True)
books = sorted(glob.glob(f"{D}/批*-裁决书.md"))
print(f"adjudication-books: {len(books)} 册在册")
for b in books:
    print(" ", os.path.basename(b), os.path.getsize(b), "bytes")
if not books:
    print("（空——按模块 docstring 手册入册；矩阵行内 token 已承载结论）")
sys.exit(0)
