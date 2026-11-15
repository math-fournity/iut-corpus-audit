# AUDIT-MATRIX-RIMS1968_summit-related-P021-030.md — RIMS1968_summit-related p21-p30

| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 21 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: 连字丢失≥3处(dificult/dificulties/diferent/eficient)；§号丢失2处(§17/§1.6)；(Ev1)∼(Ev3)的∼丢失 已登记(待裁决批10) |
| 22 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: §丢失5处(§17/§15/§1.6/§1.7/§1.4)；∼丢失2处(Atm1∼Atm4/Atm5)；diferent连字×2；页眉TEICHMÜLLER→TEICHMULLER THEORY+上标¨；automous疑漏u需600dpi回图核对 已登记(待裁决批10) 已裁决(批10) |
| 23 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: original→origina漏l；diferent连字；§丢失2处(§1.2/§4.4)；F3: 粗斜体格式丢失(系统性) |
| 24 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: efort连字×3(≥3同类)+diferences；mathematical→mathemati cal空格误断；§丢失2处(§1.1/§1.2)；页眉TEICHMÜLLER→TEICHMULLER THEORY+¨ 同前 已登记(待裁决批10) |
| 25 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: 连字丢失5处(efect×2/insuficiency/diferent×2)；F3: Example 1.9.1粗体标题格式丢失(文本仍在) 已登记(待裁决批10) |
| 26 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: 连字丢失5处(oficial×3/diferent/aforded)；two-week→twoweek连字符丢失；F3: Example 1.9.2粗体标题格式丢失 已登记(待裁决批10) |
| 27 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | FAIL | F2: §丢失6处(§1.2/§1.8/§1.5×3/§1.3)+连字3处(efect×2/afairs)；F3: 清单项目符号·丢失(7项，文本仍在) 已登记(待裁决批10) |
| 28 | Y | ✓ | ⚠ | ⚠ | ✓ | ✓ | ✓ | WARN | F2: ℝ→R黑板体丢失+行内$粘连(if$0<x\le y<z\in$R)；ob tained空格误断；efect连字×1；公式x^2+y^2=z^2完好 |
| 29 | Y | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | FAIL | F2: 行内公式排版引号被解析为垃圾记号≥6处(\nabla/\mathfrak{s}/\dot{\sigma}/\stackrel{,}{.}/\cdot/~·~)；Pyth1中x^2·y^2的上标误为下标_{x^2}；ℝ→R×2 已登记(待裁决批10) |
| 30 | Y | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | WARN | F2: dificult/efects连字×2；dictato rial断词空格误接；页眉TEICHMÜLLER→TEICHMULLER THEORY+¨ 同前 |
[审计-P021-030] DONE | p21-p30 | PASS 0 / WARN 3 / FAIL 7 / UNRESOLVED 0 | 需600dpi回图项 1
SUGGEST: 本区间证实 P001-010 的系统性错误（§丢失/ff连字/分音符拆分），另发现新族——正文行内公式两端排版引号被解析为垃圾记号(\nabla/\mathfrak{s}/\dot{\sigma}/\stackrel{,}{.})且ℝ黑板体塌缩为R(p29/p28)，建议全局 grep 对 $...$ 行内数学段扫 \nabla|\mathfrak|\stackrel|\dot{\sigma} 与 "R" of real/topological field 模式统一捕获。
