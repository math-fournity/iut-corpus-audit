# AUDIT-MATRIX-Minamide_ExplicitEstimates-in-progress-P001-010.md — Minamide_ExplicitEstimates-in-progress p1-p10

| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: 标题 Teichmüller 的 ü 被拆成 ¨+u 两字符（编码伪影，含义不变） |
| 2 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F3: 内联公式两侧空格系统性丢失（of F / For v / at v 等十几处胶连，含义可恢复） |
| 3 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 行内 ord_v 的下标 v 丢失成 ord（下方显示式 \operatorname{ord}_v(x) 正确，反证源页有下标）；F3: det'd 提取成 det'd,, 双逗号；by v. 胶连成 byv . 已登记(待裁决批10) |
| 4 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 交叉引用 [cf. §2] 被误读成 [cf. 92]（§ 错成 9，引用含义改变）；F3: ⇒ 后 As 与 an 胶连成 Asan；三条列表符号拍平 已登记(待裁决批10) |
| 5 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: different 误成 diferent（丢字母 1 处）；F3: 数学定界符两侧空格胶连（curve/Q(λ)def'd、ofE_λ/F_λ 等）；For λ ∈ Q̄∖{0,1} 行末逗号丢失 |
| 6 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: whose "support" ∋ 2,∞ 的 ∋ 误成 ⇒；行末 is bounded by B(d,ε,𝒦) 的 𝒦 误成 \kappa；F3: 两处破折号降为连字符、"support"/"K" 的引号被转成 ′′ 已登记(待裁决批10) |
| 7 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: where d = [F:Q] 中被插入伪符号 \mathbf{\Sigma}（图中 d 与 = 间无任何符号）；存疑：首条 bullet 图中似为 F′ 而提取为 F，需600dpi回图；F3: 第二处破折号降为连字符且 s.t. 后出现双句点 已登记(待裁决批10) 已裁决(批10) |
| 8 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: Difficulties 误成 Dificulties（丢一个 f）；étale 被拆成 ´+e 两字符；F3: (i)/(ii) 的换行缩进被拍平、(ii) 中 K 的粗体未保留 |
| 9 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F3: 数学定界符两侧空格胶连（curve/Kwhich、p ,l 等）；三条假设的列表符号拍平；q∈𝒪_K 以字面 ~ 代替空格 |
| 10 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: 三处行内映射箭头丢失只剩双空格（Y^log→X̲^log→X^log、X̲^log→X^log、Ÿ^log→Y^log，显示式 \xrightarrow 正确）；u = ü² 的闭引号被并入上标成 2″；F2: universal 误成 universa（丢尾字母） 已登记(待裁决批10) |

[审计-P001-010] DONE | p1-p10 | PASS 0 / WARN 5 / FAIL 5 / UNRESOLVED 0 | 需600dpi回图项 1

SUGGEST: 本稿存在两个系统性 MinerU 伪影——内联公式两侧空格丢失、引号被转成 ′′ 并污染相邻上标——建议编排者登记为 corpus 级已知伪影并统一判定尺度，避免各分片重复计 WARN/FAIL 口径漂移
