# iut-corpus-audit — IUT/ABC 争议语料的 MinerU 提取质量审计数据集

对 68 份 IUT（宇宙际 Teichmüller 理论）争议相关文献（共 3105 页）的 MinerU Markdown
提取质量，做了**逐页、图对切片的六维度视觉审计**：每页一行矩阵行（结构/文字/公式/题注/
图表/语义 → PASS/WARN/FAIL/UNRESOLVED + 缺陷备注），疑难字形经 600dpi 定点裁决批复核，
全部结论可溯源。这套数据回答的问题是：**这些论文的机器提取版到底哪里坏了、坏到什么程度**。

## 你能得到什么

- `corpus-md-audit/` — 68 份文档的审计矩阵（分片层 + FINAL 层）、`STATUS.json`（覆盖与
  verdict 真值）、`SUMMARY.md`、Tier-0 词级对照表；
- `tools/` — 全套可复用管线：审计舰队（workflow 编排）、盘点/收割/校验、Tier-0 免费对照、
  30+ 条实证缺陷模式预筛、裁决批生成与回填、质量抽查盲审；
- `docs/` — 完整方法论（实操 RUNBOOK 含全部提示词与参数、技术说明书、过程日志 WORKLOG
  与建议处置台账 SUGGEST-LOG）；
- `PUBLIC-MANIFEST.md` — 审计对象的 sha256 与源 URL：**本仓库不分发原文**，按清单自取
  PDF 对齐版本即可使用全部矩阵数据。

## 怎么用

1. 按 `PUBLIC-MANIFEST.md` 获取 PDF 并校验；
2. 直接读矩阵拿每页缺陷清单；或用你自己的转换器跑同一 PDF，对照我们的矩阵评估；
3. 想复现/延伸审计：读 `docs/审计舰队实操RUNBOOK-完整版.md`，管线在 `tools/`。

## 许可证

- 代码与管线：MIT（见 LICENSE）
- 审计数据/矩阵/文档：CC BY 4.0（https://creativecommons.org/licenses/by/4.0/）

快照状态与进度以 `corpus-md-audit/STATUS.json` 为准（随 tag 发布更新）。
