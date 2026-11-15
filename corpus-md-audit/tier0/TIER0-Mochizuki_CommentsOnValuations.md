# TIER-0 确定性比对 — Mochizuki_CommentsOnValuations（PDF 文本层 vs MinerU 切片）

- 页数 4；FLAG（Jaccard<0.85 或元数据泄漏）0 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 111 | 107 | 0.964 | ams def gal tex | - | - |  |
| 2 | 155 | 149 | 0.912 | con effect inde ordi ordj ory | efect independent nature ord | - |  |
| 3 | 156 | 153 | 0.981 | lim ordj rank | - | - |  |
| 4 | 102 | 101 | 0.971 | bibliography ord | bibliograph | - |  |