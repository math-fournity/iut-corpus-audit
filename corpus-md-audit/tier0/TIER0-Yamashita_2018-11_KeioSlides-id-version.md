# TIER-0 确定性比对 — Yamashita_2018-11_KeioSlides-id-version（PDF 文本层 vs MinerU 切片）

- 页数 2；FLAG（Jaccard<0.85 或元数据泄漏）1 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 0 | 0 | 1.0 | - | - | - |  |
| 2 | 0 | 19 | 0.0 | - | analytically block ce63493 connected different doc | - | ⚠ |