# TIER-0 确定性比对 — Joshi_2026-05_LetterToKato（PDF 文本层 vs MinerU 切片）

- 页数 6；FLAG（Jaccard<0.85 或元数据泄漏）0 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 370 | 368 | 0.973 | 1last 2here admirer announcement1 different structures2 | admire announcement diferent last | - |  |
| 2 | 294 | 291 | 0.976 | 3see controversy3 ematical math offers | controversy ofers | - |  |
| 3 | 301 | 299 | 0.987 | 4mochizuki nth regularly4 | regularly | - |  |
| 4 | 336 | 328 | 0.942 | 2πi 5mochizuki 6for 7perhaps 8scholze different | conjectur diferent monoidswith ofers perhaps reasons | - |  |
| 5 | 203 | 196 | 0.966 | does footnote holomorphic precisely prove quantified | - | - |  |
| 6 | 202 | 203 | 0.985 | 201525 | articles201525 universa | - |  |