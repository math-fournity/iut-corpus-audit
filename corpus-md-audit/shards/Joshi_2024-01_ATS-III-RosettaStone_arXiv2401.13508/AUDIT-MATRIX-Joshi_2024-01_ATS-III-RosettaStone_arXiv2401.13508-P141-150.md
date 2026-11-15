# AUDIT-MATRIX-Joshi_2024-01_ATS-III-RosettaStone_arXiv2401.13508-P141-150.md — Joshi_2024-01_ATS-III-RosettaStone_arXiv2401.13508 p141-p150

| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 141 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 定理行内𝔥𝔬𝔩被误读为ho𝕀（\\mathbb{I}）；文字：Andr´e/´etale重音拆散2处；[Mochizuki, 2021a,b,c]两处混入math模式 已登记(待裁决批3+) |
| 142 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 双层上标p^f多处被拍平为pf（𝒪_X^{*pf}、(𝒪_X,+)^{pf}、K_X^{*pf}，可600dpi复核）；sheafofabelian丢空格；on X,,双逗号 已登记(待裁决批3+) |
| 143 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 上标p^f多处拍平为pf（同p142，含k̄^{*pf}等）；ofX丢空格；multi-plicatoids断行连字符未去；[Mochizuki,2021a,b,c,d]四处混入math模式；<sup>¯</sup>k降级但可读 已登记(待裁决批3+) |
| 144 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: case of of多出一个of（原图单of）；etale´重音拆散；[Mochizuki,2021a,b,c,d]三处混入math模式 |
| 145 | Y | ✓ | ⚠ | ⚠ | ✓ | ✓ | ✓ | WARN | F2: 𝒪_X^{*pf}一处p^f拍平（同142/143系统性问题）；etale´重音拆散；\\longmapsto一处作\\mapsto；段末•标记丢失 |
| 146 | Y | ✓ | ✗ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: SL̃_2(ℝ)定义句tilde丢失致自相矛盾；z∈后\\widehat疑应为\\widetilde需600dpi回图；ℂ误作C（§12.2）；Amor´os重音拆散4处≥3 已登记(待裁决批3+) 已裁决(批3)：存疑项经300dpi半页裁决(120成立/105不成立/1看不清全批合计)，本页明细见裁决批3裁决书(run dwfrun-b791b369) |
| 147 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: 上半平面𝔥两处作H两处作mathfrak{H}；标题𝒴_∞误作𝒱_∞；SL~_2(Z)用罗马Z非ℤ；of 𝒴_∞误作of^{𝒪}𝒴_∞；analogues of 𝒫_L花体存疑需600dpi回图；Amor´os拆散2处 已登记(待裁决批3+) 已裁决(批3)：存疑项经300dpi半页裁决(120成立/105不成立/1看不清全批合计)，本页明细见裁决批3裁决书(run dwfrun-b791b369) |
| 148 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: 花体𝒴误作𝒱/𝒫共7处（𝒴_∞→𝒱_∞、𝒴_L→𝒫_L×4、𝒴_F,E→𝒱_F,E×2）；§12.6两处SL~_2(R)tilde丢失；Remark12.6.2丢箭头𝒴_∞→𝒳_∞；C-isogenous疑为ℂ-isogenous需600dpi回图 已登记(待裁决批3+) 已裁决(批3)：存疑项经300dpi半页裁决(120成立/105不成立/1看不清全批合计)，本页明细见裁决批3裁决书(run dwfrun-b791b369) |
| 149 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2/F3: 行内2x2矩阵(1 0//0 α)被拆成两个binom列向量（行间公式完好）；𝔥两处误读（mathfrak{H}大小写错+一处作H）；hasthefollowing丢空格；□结束符2处丢失 已登记(待裁决批3+) |
| 150 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: 定理12.8.5中𝒴_∞误作𝒱_∞；Theta_{gau}-link乱码为Theta_{gau}.Iink.；𝔥六处误读（5×mathfrak{H}大小写错+1×H）；Amor´os×2；□与句末句号丢失 已登记(待裁决批3+) |
[审计-P141-150] DONE | p141-p150 | PASS 0 / WARN 2 / FAIL 8 / UNRESOLVED 0 | 需600dpi回图项 4
SUGGEST: 花体𝒴误读为𝒱/𝒫、𝔥误读为mathfrak{H}/H、SL~_2(R)tilde丢失三类错误在146-150密集系统性复现，建议编排者对全库md做一次记号级regex抽检（搜\\mathcal{V}、\\mathfrak{H}、\\widetilde{\\mathrm{SL}丢失处）而非仅靠逐页人工发现
