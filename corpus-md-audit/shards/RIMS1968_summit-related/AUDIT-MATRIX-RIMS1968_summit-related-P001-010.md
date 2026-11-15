# AUDIT-MATRIX-RIMS1968_summit-related-P001-010.md — RIMS1968_summit-related p1-p10

| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F3: 标题 Teichm¨uller 两处——分音符被拆为独立 ¨ 字符（编码伪影，语义不变） |
| 2 | Y | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 标题 TEICHMULLER 丢分音符×2+游离 ¨ 上标伪影；F2: 内联数学乱码——核心记号 ∨̇ 误为 \dot\bigtriangledown(∇̇) 与 \stackrel{··}{∼} 多处、引号变 66/59/99；F1: 页脚 AMS 丢失 已登记(待裁决批10) |
| 3 | Y | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: TOC 条目 § 前缀系统性丢失(约30处,仅§1.8残留)；F2: ff 连字丢失×2(insuficiency/Diferentials)+´etale 音符分离；F2: TOC 2.4/2.4.1/2.4.3 引号内 ∧/∨ 符号丢失成空引号×6 已登记(待裁决批10) |
| 4 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 正文 logical AND/OR 引号内 ∧/∨ 丢失×2；F2: § 丢失×2(in 1 与 [cf. 1.5])；页眉 TEICHMULLER 分音符游离为 <sup>¨</sup>；truncatibility 与页面 truncatability 不符×1；公式: 2.4.5 误用 bigwedge/bigvee+引号 66/39 乱码 已登记(待裁决批10) |
| 5 | Y | ⚠ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: § 丢失×11([cf. 1.3,1.8,1.10,1.11,1.12]/in 1/in 2/[cf. 2.1,2.2]/[cf. 2.3] 等)；F2: ff 连字丢失×2(diferentiation/diferential)+interuniversal 丢连字符；F3: 缩进强调块误升为 ## 标题、列表圆点丢失1处 已登记(待裁决批10) |
| 6 | Y | ⚠ | ✗ | ✗ | ✓ | ✓ | ✓ | FAIL | 公式: (∧(∨̇)-Chn) 的 ∧ 误读为 Λ、XOR ∨̇ 误为 \surd(√)、\dot\bigvee 变体多处、— cf. 乱码为 -cot.（展示公式三行链本身忠实）；文字: § 丢失×8、log-link 与 log-theta-lattice 丢连字符；结构: 列表拍平 已登记(待裁决批10) |
| 7 | Y | ⚠ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: § 丢失×12(五个列表项引用+标题 1.1 的 §)；F2: ff 连字丢失×2(efort/diferent)；Saıdi 分音符拆分；结构: 列表拍平无圆点；人名与日期完整 已登记(待裁决批10) |
| 8 | Y | ⚠ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F3: 引语 100 percent confidence 误升为 ## 标题；F2: § 丢失×2(标题 1.2 与 in 1.1)+interuniversal 丢连字符；页眉分音符游离；专名与日期完整 |
| 9 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: § 丢失×5(in 3.1/of 3/in 3.2,3.3,3.4)；RC-FrEt 的 É 丢尖音符且 ´ 游移到 RC-lo 前；interuniversal 丢连字符；F3: As discussed... 整行被 <sup> 包裹；RCS 术语与 [Rpt2018]/§18 完整 已登记(待裁决批10) |
| 10 | Y | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | FAIL | 公式: ∧-property 的 ∧ 丢失×3(logical AND 空引号/crucial -property/(RC-Θ) vs. -property)；文字: § 丢失×7(2.3/2.4/3/标题1.3/3.4)；ff 连字丢失×2(diferent/efort)；页眉分音符游离 已登记(待裁决批10) |
[审计-P001-010] DONE | p1-p10 | PASS 0 / WARN 2 / FAIL 8 / UNRESOLVED 0 | 需600dpi回图项 0
SUGGEST: 本文档错误高度系统性（§ 前缀整篇丢失、∧/∨ 引号内符号丢失、ff 连字丢失、分音符拆分为 ¨+字母），建议编排者在逐页审计后对全部 pNNN.txt 跑一轮全局 grep（如 "¨"/空引号/ff 连字/行首数字缺 §）统一捕获残余实例，比逐页人工更省且不漏。
