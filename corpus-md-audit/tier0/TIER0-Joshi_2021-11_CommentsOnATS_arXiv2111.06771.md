# TIER-0 确定性比对 — Joshi_2021-11_CommentsOnATS_arXiv2111.06771（PDF 文本层 vs MinerU 切片）

- 页数 12；FLAG（Jaccard<0.85 或元数据泄漏）1 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 115 | 112 | 0.957 | ematician pecially preliminary version | especially | - |  |
| 2 | 215 | 207 | 0.945 | demon geo ichmuller metrically ory proach | demonstrates varieties | - |  |
| 3 | 209 | 176 | 0.816 | 1let afore alters ana both fact | aforementioned incompatible let | - | ⚠ |
| 4 | 228 | 221 | 0.927 | ally alytic bqp differ ences encoun | analytic array encounters globally simultaneously | - |  |
| 5 | 232 | 221 | 0.928 | abelomorphism exten indeter indetermi iso material | extensive materialfrom ofit | - |  |
| 6 | 208 | 204 | 0.943 | gardless gqp istence moc ously simultane | existence regardless simultaneously skippedfor | - |  |
| 7 | 163 | 151 | 0.903 | bgm dant glp holders inde lim | holdersfor redundant | - |  |
| 8 | 203 | 196 | 0.928 | amor bgm dif ferent gies ical | amoros different implementations strategies | - |  |
| 9 | 200 | 199 | 0.975 | psl2 struc tures | ofthe psl | - |  |
| 10 | 190 | 186 | 0.969 | ast dis erisque gal tinct | asterisque | - |  |
| 11 | 200 | 196 | 0.941 | 20groth algo ast domorphisms erisque retic | 20grot algorithms asterisque endomorphisms | - |  |
| 12 | 14 | 14 | 1.0 | - | - | - |  |