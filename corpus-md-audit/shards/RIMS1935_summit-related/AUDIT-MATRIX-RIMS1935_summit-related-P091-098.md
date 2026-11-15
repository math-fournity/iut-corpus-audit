# AUDIT-MATRIX-RIMS1935_summit-related-P091-098.md — RIMS1935_summit-related p91-p98

| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 91 | Y | ⚠ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: p91 多处公式误读——投影态射 (X_K)_n→X_K 箭头整个丢失；行内 Π_{(X_K)_m}⇝Π_{(Y_L)_n} 乱码为 \ :\tilde{} 且下标 n 误读为 r；Π_{X_K} 误读为 Π_{X_r}、Π_X 误读为 Π_{X]}；三处 ⇝ 误写为 \xrightarrow{\sim}；affine 误读为 affne；4 个列表圆点丢失 2 个（F3 连带该行被整体数学化） 已登记(待裁决批10) |
| 92 | Y | ⚠ | ✓ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: p92 r_Y 下标整个丢失成 r；4 处 ⇝ 误读为 \stackrel{\sim}{\to}（其中 σ_ℚ̄ 处乱码 \overset{\sim}{} 悬空）；6 个列表圆点丢失 3 个；Let σ 行 (X_K) 下标 m/n 存疑（提取为 n），需600dpi回图 已登记(待裁决批10) 已裁决(批10) |
| 93 | Y | ✓ | ✓ | ✗ | ✓ | ⚠ | ✓ | FAIL | F2: p93 约9处 ⇝ 系统性误读为 \stackrel{\sim}{\to}（其中2处乱码悬空 \stackrel{\sim}{}）；𝔖₃ 后多出句点；半角逗号变全角"，"；G_L→Out^FC 与 GT⊆Out 处多出 \cdot 点标（与同页平行处不一致，存疑）；两交换图竖直箭头的同构标记 ∼ 写成 \wr，需600dpi回图 已登记(待裁决批10) 已裁决(批10) |
| 94 | Y | ⚠ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: p94 Π 误读为 \prod；Π_{(Z_L)_n} 断成孤立 n；5 处 ⇝ 乱码/误写（\tilde{} 悬空、\tilde{\to}）；\mathbb{Q} 误成 \mathbb{O}；下标4处误读/丢失（Π_{(X_K)} 丢 n、Π_{(Z_K)_{\tilde{1}}}、Π_{Z_r}、Π_{X_τ}）；文字 sufices×2（应为 suffices）；9 个圆点丢 6 个；G_K 后重复分号 ;; 已登记(待裁决批10) |
| 95 | Y | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: p95 \prod_{Z_n} 又现（应为 Π_{Z_n}）；σ_ℚ̄=1 处 \mathbb{Q}→\mathbb{O}；Π_{X_n}→Π_{X_τ}；2 处 ⇝ 乱码 \tilde{}、1 处 \stackrel{\sim}{\to}；Definition 1.1 (ii)] 的 ] 误成 l；fields 引号 “L” 乱成上标 ^{66}L^{3}；Theorem 3.6 的 Fraktur 记号 ^{\bar{𝔰}}\bar{V}⊆W^{𝔰} 与原图字形存疑，需600dpi回图 已登记(待裁决批10) 已裁决(批10) |
| 96 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: p96 [Hsh1] 条目 affine 误成 afine；[CbTpI] 条目 Teichmüller 变音符拆散错位成 Teichmu¨ller；14 条文献均在、卷期页码一致 |
| 97 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: p97 [Tama] 条目 affine 误成 afine；Grothendieck-Teichmüller 变音符拆散成 Teichm¨uller；Hoshi 地址段 Email address 行与上一行合并（换行丢失）；两条 URL 的 ~ 被转义成 \~（渲染后无碍） |
| 98 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F3: p98 Tsujimura 地址段的 Email address 行与上一行合并（换行丢失）；两处邮箱与单位信息完整 |

[审计-P091-098] DONE | p91-p98 | PASS 0 / WARN 3 / FAIL 5 / UNRESOLVED 0 | 需600dpi回图项 3

SUGGEST: MinerU 对波浪箭头 ⇝(leadsto) 系统性误读为 \stackrel{\sim}{\to}/\overset{\sim}{\to}，且 Π↔\prod、\mathbb{Q}↔\mathbb{O}、下标 n↔r/τ 混淆在 p91-p95 反复出现——可先对整份提取做这些高频混淆模式的正则预筛，把命中点直接列给审计者复核，提速并减少漏检。
