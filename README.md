# iut-corpus-audit — IUT/ABC 争议语料的 MinerU 提取质量审计与补丁层数据集

对 68 份 IUT（宇宙际 Teichmüller 理论）争议相关文献（共 3105 页）的 MinerU Markdown
提取质量，做了**逐页、图对切片的六维度视觉审计**与**高保真补丁层（S4）修复**：
每页一行审计矩阵行（结构/文字/公式/题注/图表/语义 → PASS/WARN/FAIL/UNRESOLVED + 缺陷备注），
疑难字形经 600dpi 定点裁决批（批 1–16，共 3507 子项）与 600dpi 局部裁片闭环复核，全部结论可溯源。

## 你能得到什么

- `corpus-md-audit/` — 68 份文档的审计矩阵（分片层 + FINAL 层）、`STATUS.json`、`SUMMARY-FINAL.md`、Tier-0 词级对照表；
- `adjudication-books/` — 裁决批 1–16 完整裁决书（3507 个子裁决，含 600dpi 图证与坐标）；
- `correction-layer/` — S4 补丁层账目：10 大误读模式族规则与抽验卡（`families/` + `step2-spotcheck.md`）、14,673 条命中无原文定位索引（`entries-nocontext/`）、223 页 Image-block 占位页重提取核验表（`imageblock-recheck.tsv`）与 155 页 600dpi 局部定谳闭环账本（`s4-600dpi-closure.tsv`）；
- `tools/` — 全套可复用管线：审计舰队、盘点/收割/校验、Tier-0 对照、模式预筛与补丁层生成（`tools/repair/gen_correction_layer.py`）、裁决渲染器；
- `docs/` — 完整方法论、技术说明书、过程日志 `WORKLOG` 与 `SUGGEST-LOG`；
- `PUBLIC-MANIFEST.md` — 审计对象的 64 位 sha256 与源 URL：**本仓库不分发论文 PDF 或整页转写原文**，按清单自取 PDF 对齐版本后即可结合 `tools/repair/` 在本地完整复现。

## 许可证

- 代码与管线：MIT（见 LICENSE）
- 审计数据/矩阵/裁决书/补丁层账本/文档：CC BY 4.0（https://creativecommons.org/licenses/by/4.0/）

快照状态与进度以 `corpus-md-audit/STATUS.json` 与 `correction-layer/SUMMARY.md` 为准（随 tag 发布更新）。
