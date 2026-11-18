# correction-layer 账目（B 形态补丁层 · v1.1-s4-complete）

> 真源：`correction-layer/`（B 补丁层形态，`corpus-md/` 与审计矩阵历史行全程不动）。

## 一、模式族预筛补丁层（Step-1 & Step-2）

真源 = `PATTERN-SUSPECTS.tsv`（14,673 预筛命中）+ 族规则（`tools/repair/gen_correction_layer.py` 生成 `entries/<doc>.tsv`）。Step-2 经 24 例 300dpi 视觉抽验（见 `step2-spotcheck.md`）完成双标点同字符折叠与 H 双美元降级根因修正。

| 族 | 修复型 | 条数 |
|---|---|---|
| F01 自定义记号互混 | deterministic | 34 |
| F01 自定义记号互混 | visual-required | 7 |
| F02 花体/Fraktur/黑板体拍平 | visual-required | 2035 |
| F03 ff连字丢失 | deterministic | 1491 |
| F04 上下标结构破坏 | visual-required | 22 |
| F05 箭头丢失/退化 | visual-required | 1153 |
| F06 引号→上标乱码 | deterministic | 2 |
| F06 引号→上标乱码 | visual-required | 123 |
| F07 重音拆散 | deterministic | 2812 |
| F08 幽灵字符 | deterministic | 6218 |
| F08 幽灵字符 | visual-required | 521 |
| F09 双栏/索引塌缩 | routed-223 | 255 |

合计 **14,673** 条（其中 `deterministic` 10,557 条、`visual-required` 3,861 条待 S5-B 按页 600dpi 定谳、`routed-223` 255 条已由下方 223 页整页转写闭环）。

## 二、223 页 Image-block 占位死页高保真整页转写与 600dpi 闭环（S4④ + S4①下半场）

1. **300dpi 整页直读转写 + 独立 fresh-eyes 验证 + 按报告修订**：
   - 覆盖全部 **223 / 223** 页（28 份文档），对照总表见 `imageblock-recheck.tsv`（1 行表头 + 223 行唯一记录：`high 87 / medium 135 / low 1`，其中唯一 1 页 `low` 即 `AlienCopiesGaussians p60` 已在修订阶段重转闭环，未修订非 `high` 页 = **0**）。
   - 逐页产物位于私有全量仓 `correction-layer/pages/<doc>/p<NNN>.md`（公开仓受版权红线约束不分发整页论文转写原文，仅发布完整核验账本）。
2. **600dpi 局部裁片定谳 + 跨波弱项符号族定点复核（`s4-600dpi-closure.tsv`）**：
   - 覆盖全部命中存疑或弱项符号族（`\mathbb{F}_l^*` vs `\divideontimes`、`⇝` vs `\stackrel{\sim}{\to}`、`\mathfrak{log}`、`\deg_{\mathrm{Fr}}`、`\mathfrak{H}`、`\odot`/`\ominus`/`\circledcirc`/`\Theta`、`\longmapsto`）的 **155 / 155** 页（`Hydrogen$xhigh` + `magick` 600dpi 裁片）：
     - 新定谳并补修 `[?]`：**178** 项；复核确认前序已闭环：**87** 项；**`unresolvable@600dpi`：0 项**；
     - 跨波弱项符号族核对：**1,678** 处，捕获漏检并就地补修 **485** 处；正文累计精准补修 **1,512** 处，历史验证报告与修订记录 100% 原样保留。
