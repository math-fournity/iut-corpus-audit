# TIER-0 确定性比对 — Mochizuki_InvitationToIUT（PDF 文本层 vs MinerU 切片）

- 页数 11；FLAG（Jaccard<0.85 或元数据泄漏）7 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 30 | 31 | 0.968 | - | teichmuller | - |  |
| 2 | 109 | 87 | 0.782 | arises bundle def degree erators extension | nevertheless | - | ⚠ |
| 3 | 127 | 69 | 0.508 | absolute affairs and appear applied approach | arith array difs | - | ⚠ |
| 4 | 112 | 107 | 0.921 | con degarith difff hte log qj2 | arith diff | - |  |
| 5 | 89 | 45 | 0.473 | analogy and between but characteristic curves | diferential teichmuller | - | ⚠ |
| 6 | 39 | 46 | 0.848 | - | b09f56c block doc image page standard | - | ⚠ |
| 7 | 50 | 55 | 0.81 | teichm uller ɹɹɹɹ | b09f56c block doc image page standard | - | ⚠ |
| 8 | 79 | 73 | 0.9 | con def gal log logv qj2 | constituted | - |  |
| 9 | 80 | 76 | 0.793 | abstract computa fol likeʯ lowing monoids | abstractmonoids array computation following likeobjects teichmuller | - | ⚠ |
| 10 | 104 | 100 | 0.907 | anabelioids autfield log logv qj2 ɹʢɹ | anabelioidsthe aut field | - |  |
| 11 | 98 | 92 | 0.81 | abstract arithmetic degree etale fundamental galois | abstractmonoids arithmeticfundamentalgroups galoisgroups likeobjects poincarémetric teichmuller | - | ⚠ |