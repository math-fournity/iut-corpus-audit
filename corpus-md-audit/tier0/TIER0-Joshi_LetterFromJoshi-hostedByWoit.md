# TIER-0 确定性比对 — Joshi_LetterFromJoshi-hostedByWoit（PDF 文本层 vs MinerU 切片）

- 页数 3；FLAG（Jaccard<0.85 或元数据泄漏）0 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 280 | 278 | 0.993 | ple princi | - | - |  |
| 2 | 216 | 215 | 0.977 | effectively offers spec | efectively ofers | - |  |
| 3 | 153 | 154 | 0.981 | e7f2c3_babfab84a56e45fe9e78670028015817 | _babfab84a56e45fe9e78670028015817 e7f2c3 | - |  |