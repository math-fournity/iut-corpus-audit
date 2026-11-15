# AUDIT-MATRIX-Yamashita_2018-07-13_AProofOfABCafterMochizuki_405pp-P401-405.md — Yamashita_2018-07-13_AProofOfABCafterMochizuki_405pp p401-p405

| 页 | 已审 | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| 401 | Y | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | FAIL | F2多处: 𝕍(L)_j下标j误读为v; 𝕏⌢M的⌢误为∨; 𝕐族5条全误为Ω; ʒ_N/ǯ_N误为3N; {ζ_*}误为†ζ*(括号丢、多出†); ξ/ζ组z_i,w_i下标丢失; 𝕍/𝕏黑正体混同; 页码与条目数完整 已登记(待裁决批11) |
| 402 | Y | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | FAIL | F2: 唯一条目†ζ̌^{Θ±}_{z_i}中ζ整字丢失、下标z_i误读为v, 剩"†Θ±v"; 页眉402/Go Yamashita完好 已登记(待裁决批11) |
| 403 | Y | ✓ | ✗ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2文字4处: [A2]前多出字母d、differential误为diferential、représentations丢r、Revêtements丢s; F2公式: [A1]分子𝕋̄误为ℚ̄、[A2]首个ℂ拍平为C; 另重音拆解(Ast´erisque/Andr´e)、Périodes→Periodes、斜体粗体丢失; 23条文献全在无缺行 已登记(待裁决批11) |
| 404 | Y | ✓ | ⚠ | ✗ | ✓ | ✓ | ⚠ | FAIL | F2: [ℚ_pGC]标签拍平为[QpGC](黑体ℚ→Q、下标p拍平); [EtTh]Étale丢音符成Etale、断词Manifestations中插入游离´; 另Teichmüller/Tôhoku重音拆解、birthday.误为birthday逗号、斜体粗体丢失; 22条全在,页码卷期年份全对 已登记(待裁决批11) |
| 405 | Y | ✓ | ✗ | ✓ | ✓ | ✓ | ⚠ | FAIL | F2文字: 4条IUTch条目URL的~全丢(ac.jp/ motizuki)、IUTchIV再丢papers-english连字符; [Tam]Affine误为Afine; [SvdW]页码303–322提取为303–332需600dpi回图; 另Kôkyûroku/Oesterlé/théorème重音拆解、Fermat.误逗号; 21条全在,[Naka] Algebraic复核为对 已登记(待裁决批11) 已裁决(批14) |
[审计-P401-405] DONE | p401-p405 | PASS 0 / WARN 0 / FAIL 5 / UNRESOLVED 0 | 需600dpi回图项 1
SUGGEST: validate_matrix可加一条"分片文件不含shell包装串(如__zcode_status)"的检查——本轮P402追加时heredoc嵌套fallback曾把包装行写入分片(已人工修复),机器校验可防复发
