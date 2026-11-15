# TIER-0 确定性比对 — Mochizuki_2026-04_FormalizationOfIUT（PDF 文本层 vs MinerU 切片）

- 页数 14；FLAG（Jaccard<0.85 或元数据泄漏）3 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 47 | 45 | 0.957 | ams tex | - | - |  |
| 2 | 156 | 69 | 0.433 | abc above accusations allow already any | eficient | - | ⚠ |
| 3 | 189 | 184 | 0.903 | acteristic char dependent effect efficiently effort | characteristic efect eficiently efort familiar independent | - |  |
| 4 | 197 | 187 | 0.93 | cult cussed diffi dis fined lar | dificult discussed | - |  |
| 5 | 200 | 196 | 0.922 | cently cians dard especial mathemati posed | especially mathematicians opposed recently shogo suficient | - |  |
| 6 | 143 | 139 | 0.972 | coric exphoriz galois iut21 | - | - |  |
| 7 | 158 | 159 | 0.981 | unaffected | reconstruct unafected | - |  |
| 8 | 94 | 91 | 0.927 | effect effects stp1 stp2 stp3 | efect efects | - |  |
| 9 | 66 | 63 | 0.955 | algorithm like radial | - | - |  |
| 10 | 136 | 119 | 0.835 | algo call col con elemen follow | elementary following recall | - | ⚠ |
| 11 | 168 | 154 | 0.894 | 1st 2nd 3rd 4th con cor | indeterminacies research | - |  |
| 12 | 128 | 128 | 1.0 | - | - | - |  |
| 13 | 137 | 131 | 0.848 | arakelov com decomposi follow gauss gaussians | 20gaussians arakelovtheoretic computations decomposition gaussian reconstruction | - | ⚠ |
| 14 | 40 | 40 | 1.0 | - | - | - |  |