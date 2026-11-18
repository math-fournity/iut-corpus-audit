# S4 Step-2 修复视觉抽验对照表（8 族 × 3 例）

> 每族 ≥3 例修前/修后对照 + 图上依据。verify_status 回填 correction-layer/families/。

## F01 自定义记号互混

- **Mochizuki_2024-03-24_EssentialLogicalStructure|p86**（iiib型编号粘连，规则修复核对）→ **fix-correct**
  - 修前：`the horizontal [cf. (i-c)] and vertical [cf. (i-d)] coricity [cf. (ie), (i-f)] properties of the ´etale-like structures that appear in the logtheta-lattice [cf.`
  - 修后/图上真形：`[cf. (i-e), (i-f)]`
  - 图上依据：bot 半页图第二个 bullet 处：coricity 行末为「coricity [cf. (i-」，下一行行首为「e), (i-f)] properties of the étale-like structures」，即原稿跨行断词重组后真实编号为 (i-e), (i-f)，与修后片段一致；上半页同页前文「the discussion of (i-e), as well as of Example 3.5.1」亦印证该编号存在。
- **RIMS1968_summit-related|p86**（iiib型编号粘连，规则修复核对）→ **fix-correct**
  - 修前：`the horizontal [cf. (i-c)] and vertical [cf. (i-d)] coricity [cf. (ie), (i-f)] properties of the ´etale-like structures that appear in the logtheta-lattice [cf.`
  - 修后/图上真形：`the horizontal [cf. (i-c)] and vertical [cf. (i-d)] coricity [cf. (i-e), (i-f)] properties of the ´etale-like structures that appear in the logtheta-lattice [cf`
  - 图上依据：下图（bot）bullet 列表第二条：该编号恰在显式连字符处跨行断开，行尾字形为「(i-」、行首为「e), (i-f)]」（放大裁剪 /tmp/p086-crop-i-e.png 确认），且 TeX 不可能给两字母串 (ie) 插入断词连字符、同列表 (i-a)…(i-f)/(ii-*)/(iii-*) 全带连字符，故原稿真实形态即 (i-e)，与修后一致。
- **Mochizuki_2024-03-24_EssentialLogicalStructure|p112**（Chn吞并(𝓕||-▷×μ族)，视觉定谳）→ **proposed**
  - 修前：`( -Chn) the logical structure of inter-universal Teichm¨uller theory proceeds by observing a chain of AND relations “ ”`
  - 修后/图上真形：`(∧-Chn) the logical structure of inter-universal Teichm¨uller theory proceeds by observing a chain of AND relations "∧"`
  - 图上依据：下半页 'Rather,' 之后的条目行放大 6x/8x 后清晰可见标签 '(∧-Chn)'（wedge 尖顶朝上）与行尾引号内 '∧'，与上半页 AND relator "∧" 同形；两处 ∧ 均被 MinerU 输出吞并为 '( -Chn)' 与 '" "'。

## F02 花体/Fraktur/黑板体拍平

- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p1**（小型大写作者名销毁，视觉定谳）→ **fix-correct**
  - 修前：`# EFFECTIVITY IN MOCHIZUKI’S WORK ON THE abc-CONJECTURE`
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：对 s4fix-p001-top.png 标题两行做逐字母像素测量：EFFECTIVITY/ONJECTURE 等词内字母与词首字母全部等高 34–36px，无小型大写的高矮对比（正文首行大写仅 22px 高作对照），abc 为斜体小写、连字符撇号均在——修前行与图逐字一致，F02 不适用。
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p3**（小型大写作者名销毁，视觉定谳）→ **fix-correct**
  - 修前：`EFFECTIVITY IN MOCHIZUKI’S WORK ON THE abc-CONJECTURE`
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：s4fix-p003-top.png 页眉行（y≈399–425）4x 放大目验 EFFECTIVITY 与 MOCHIZUKI'S 每个字母等高，逐列高度直方图主峰 25–27px 无 ~20px 矮峰，即全大写而非小型大写排印；行文含撇号与斜体小写 abc，与修前逐字一致。
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p5**（小型大写作者名销毁，视觉定谳）→ **fix-correct**
  - 修前：`EFFECTIVITY IN MOCHIZUKI’S WORK ON THE abc-CONJECTURE`
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：像素级测量页眉带 y399-425：EFFECTIVITY 与 MOCHIZUKI 逐列 profile 所有字母顶部均 y399-400、cap 高恒定 25-26px，无小型大写的整体下沉特征，全大写与修前转写逐词一致。

## F03 ff连字丢失

- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p1**（ff连字丢失，规则修复核对）→ **fix-correct**
  - 修前：`Abstract. This note outlines a constructive proof of a proposition in Mochizuki’s paper Arithmetic elliptic curves in general position, making a direct use of c`
  - 修后/图上真形：`…making a direct use of computable non-critical Belyi maps to effectively reduce the full abc-conjecture to a restricted form. Such a reduction means that an ef`
  - 图上依据：顶图摘要第4行可见「to effectively reduce」双f、第5行可见「an effective abc-theorem」双f，修后两词与图一致；修前输出的单f为连字丢失。
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p2**（ff连字丢失，规则修复核对）→ **fix-correct**
  - 修前：`In his proof of the latter theorem Mochizuki makes an argument by contradiction, citing compactness of$\mathbb { P } ^ { 1 } ( F _ { v } )$. This gives the appe`
  - 修后/图上真形：`conditionally on the correctness of Mochizuki’s IUT papers, to effective Roth and Faltings theorems.`
  - 图上依据：上半页图摘要第二段倒数第3-4行 'on the correctness of Mochizuki's IUT papers, to effective Roth and Faltings theorems.' 处，effective 呈双 f 连字形态，与同段 ineffectivity 的 ff 连字形态一致
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p3**（ff连字丢失，规则修复核对）→ **fix-correct**
  - 修前：`Here,$| \cdot | _ { v }$denotes the standard absolute value on$\mathbb { C } _ { v }$(normalized by $| p | _ { p } = 1 / p _ { ; }$for$p$finite, and the ordinar`
  - 修后/图上真形：`that the general inequality (1) for $[ \mathbb { Q } ( P ) : \mathbb { Q } ] \leq d$ reduces effectively to a similar inequality but with $P$ restricted to $\ma`
  - 图上依据：top 半页第 1 段第 6 行 'reduces effectively to'：4x 放大裁剪（/tmp/s4fix-p003-word.png，源图 1690,765–2030,835）显示该词为 ff 连字的 'effectively'（双 f 共享横杠），非单 f 'efectively'，补丁修后与图一致；同段其余内容（η(d,ε,s)、[ℚ(P):ℚ]≤d、𝒦_Σ(η(d,ε,|Σ|)) 等）逐行核对亦与图相符。

## F04 上下标结构破坏

- **Yamashita_2017_AProofOfABCafterMochizuki_v6|p133**（H双美元粘连，规则修复核对）→ **fix-wrong**
  - 修前：`where${ } _ { \infty } H ^ { 1 } ( ( ^ { \dagger } \Pi ^ { \mathfrak { E } } ) ^ { \mathrm { r a t } } , - ) : = \varinjlim _ { H \subset ( ^ { \dagger } \Pi ^ `
  - 修后/图上真形：`where${ } _ { \infty } H ^ { 1 } ( ( ^ { \dagger } \Pi ^ { \mathfrak { E } } ) ^ { \mathrm { r a t } } , - ) : = \varinjlim _ { H \subset ( ^ { \dagger } \Pi ^ `
  - 图上依据：p133 下半页第2行（300dpi 放大4倍，/tmp/p133-lim-to-H1-zoom.png）：\varinjlim 下标 "(†Π*)rat : open" 之后只有一个 H¹(H,−) 加句点，其前无孤立 "H"——补丁保留的孤立 H 在图上不存在，正确形态应删去孤立 H 只留单个 H¹(H,−)。
- **Joshi_2021-06_ATS-I_arXiv2106.11452|p5**（§丢失(章号裸数字)，视觉定谳）→ **fix-correct**
  - 修前：`(1)${ \mathcal { T } } _ { g }$parameterizes, up to a suitable equivalence hereafter dubbed Teichmuller equivalence,¨ pairs$( \Sigma ^ { \prime } , f )$consisti`
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：下半页图 Theorem 2.1.1 条(1)第3行（y≈454–499）经4x/6x/7x逐段放大读作 "…mapping f : Σ′ → Σ [Lehto, 1987, Chapter V, 2.1]. Note that…"，"V," 与数字 "2" 之间仅有空格、无 § 字符（7x 最近邻放大 /tmp/zoom-p005-cite8c.png 无歧义）；条(1)全块内唯一裸数字疑点即此引文，故修前行 "Chapter V, 2.1" 与图一致，不应补 §。
- **Joshi_2021-06_ATS-I_arXiv2106.11452|p18**（§丢失(章号裸数字)，视觉定谳）→ **fix-correct**
  - 修前：`Definition 4.1.2. Following see [Andr´e, 2003a, Chapter III, 1.2.2], a K-geometric base-point (or less precisely, a geometric base-point) of the analytic space$`
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：top图末行（Definition 4.1.2行）与bot图Remark 4.1.3(1)两处4x特写均显示 [André, 2003a, Chapter III, 1.2.2]——'III,' 与 '1.2.2' 之间只有基线逗号、无§字形；段内其余数字处（Definition 4.1.2.、rank one）也无需补§的位置。

## F05 箭头丢失/退化

- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p3**（相邻数学组间纯空格(疑丢箭头)，视觉定谳）→ **fix-correct**
  - 修前：`for all$( d , \varepsilon ) \in \mathbb { N } \times ( 0 , 1 )$. Then, for all$( d , \varepsilon ) \in \mathbb { N } \times ( 0 , 1 )$and$P \in$ $\mathbb { P } `
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：top图裁剪2x放大(s4fix-p003-top.png y≈1280-1620→/tmp/f05ex13-line.png)显示第二行末「and P ∈」与下一行首「ℙ¹(ℚ̄) \ {0,1,∞}」之间仅有PDF换行、无任何箭头符号，F05疑丢箭头不成立；另见图上「≤ d, it holds」为单个逗号，修前「\leq d ;$」中的分号系OCR误识（标点族问题，非本F05案例，建议另案）。
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p4**（相邻数学组间纯空格(疑丢箭头)，视觉定谳）→ **proposed**
  - 修前：`• the degree of f and the heights$h ( \pi ( Q ) )$of the points$Q \in$ $f ^ { - 1 } \{ 0 , 1 , \infty \}$do not exceed$B ( n , d , H )$`
  - 修后/图上真形：`$Q \in f ^ { - 1 } \{ 0 , 1 , \infty \}$（两组合并为同一数学组，∈ 与 f^{-1}\{0,1,∞\} 之间无任何箭头；原行其余部分照抄）`
  - 图上依据：s4fix-p004-bot.png Proposition 2.1 第4条 bullet 末行止于『the points Q ∈』，下一行开头为『f⁻¹{0,1,∞} do not exceed B(n,d,H)』，∈ 与 f⁻¹{0,1,∞} 间仅换行、无箭头符号。
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p6**（相邻数学组间纯空格(疑丢箭头)，视觉定谳）→ **proposed**
  - 修前：`for a local section$s = ( h _ { i } ) _ { i = 1 } ^ { r }$at$P _ { - }$. See$[ 2 ]$, Prop. 2.7.11. Here$s s _ { u } ^ { - } / s _ { w } ^ { + } =$ $h _ { i } h `
  - 修后/图上真形：`图上真实形态（该行三处组间纯空格点逐一）：① Here$ss _ { u } ^ { - } / s _ { w } ^ { + } = h _ { i } h _ { u i } ^ { - } / h _ { w i } ^ { + }$over$U _ { i }$ —— $s$与$s_u^-$之间、$=$与$h`
  - 图上依据：s4fix-p006-bot.png 中方程(5)后正文段可见 'Here 𝑠𝑠_u^−/𝑠_w^+ =' 两 s 相邻、续行 'ℎ_𝑖ℎ_ui^−/ℎ_wi^+ over 𝑈_𝑖'；'Σ_{v∈M_K} max(log|α|_v, |β|_v)' 中 max 正体连写；'ℎ_𝒟 = ht_{O(𝒟)} :' 行末冒号清晰，续行起 'C_n(ℚ̄) → ℝ'。

## F06 引号→上标乱码

- **Fesenko_NotesOnIUT|p21**（引号混入数学，视觉定谳）→ **proposed**
  - 修前：`Cor. 2.2 of [31]-IV deals with elliptic curves E over any number field F using Th. 1.10 of [31]-IV. The Legendre equation gives the natural classifying morphism`
  - 修后/图上真形：`containing the place "2" it proves`
  - 图上依据：s4fix-p021-bot.png 该行（约 y=375–465）放大 6–8× 清晰可见 ace "2" i：两枚引号均为竖直平行短杠的直引号、紧贴数字 2 且内侧无空格，2 为正体文本字，后接正常词距的 it proves——修前 $" 2 "$ 的数学模式包裹与内侧空格均属 OCR 误置。
- **Joshi_2024-01_ATS-III-RosettaStone_arXiv2401.13508|p82**（引号混入数学，视觉定谳）→ **fix-correct**
  - 修前：`<table><tr><td>Mochizuki&#x27;s Notation</td><td>Object in [Mochizuki, 2021c]</td><td>Object in [Joshi, 2021a]</td></tr><tr><td>F</td><td>F base field</td><td>L`
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：两半页图中唯一的引号形是表头文本单元格「Mochizuki's Notation」的撇号（清晰在图、属文本非数学），与修前 &#x27; 一致；其余全部数学单元格内均无引号字形。
- **Joshi_2024-01_ATS-III-RosettaStone_arXiv2401.13508|p87**（引号混入数学，视觉定谳）→ **fix-correct**
  - 修前：`<table><tr><td colspan="2">Fundamental Prime strips</td></tr><tr><td> $\left\{G_v \curvearrowright \mathcal{O}_{L_v}^*: v \in \mathbb{V}_L^{non}\right\}$  $\lef`
  - 修后/图上真形：`误报：图上与修前一致`
  - 图上依据：全表逐行放大核对（6 张 2 倍整行裁剪 + 5 处 8 倍局部）通篇无任何引号字形，程序扫描修前行 2304 字符仅有的 8 个引号全在 colspan="2" 属性内、$...$ 数学区 0 个——F06 引号点图上与修前一致，系模式误报；附带记录（非 F06 族，供其他案例归口）：图上第 2/4/5 行对应箭头为双端锯齿 \leftrightsquigarrow 而非文本 \leftrightarrow，\mathbb{C}_p^b 三处图上 𝕂_p 上标为降符 ♭ 而非字母 b，第 11/12 行 𝒴/𝒳 下标图上为 \widehat{\overline{L}}_v^{\flat}（帽下有上划线、帽右有 ♭）而文本 \widehat{L}_v 两者皆缺。

## F07 重音拆散

- **Fesenko_NotesOnIUT|p14**（变音符拆散，规则修复核对）→ **fix-correct**
  - 修前：`<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280"><sup>31</sup> on a certain finite covering Y<sup>¨</sup><sub>`
  - 修后/图上真形：`<sup>31</sup> on a certain finite covering Ÿ<sub>v</sub> of the covering Y<sub>v</sub> discussed in footnote 24`
  - 图上依据：下图脚注31行放大后可见「on a certain finite covering 𝒴̈_v of the covering 𝒴_v discussed in footnote 24」：两点变音符直接缀在花体Y上方并带下标v，是Y的变音符而非Y与v之间的独立上标符号，与修后Ÿ<sub>v</sub>一致（图中花体Y vs HTML普通Y为修前修后共有字体差异，不在改动片段内）。

## F08 幽灵字符

- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p1**（双标点，规则修复核对）→ **fix-wrong**
  - 修前：`Shinichi Mochizuki’s proposed solution of the abc-conjecture revolves around the theory [5] of the ´etale theta function of a Tate curve over a completion$F _ {`
  - 修后/图上真形：`$S ,$i.e., at each place in S having odd residue characteristic.（图上 "i.e." 后确有逗号，原输出无误，补丁删逗号属误改）`
  - 图上依据：s4fix-p001-bot.png 中该行 6x 放大裁剪（区域 1050,415-1350,485，/tmp/f08ex22-ie-after.png）清晰显示 "S, i.e., at each"——i.e. 第二个句点后带逗号。
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p4**（HTML残留，规则修复核对）→ **fix-correct**
  - 修前：`by Scherr and Zieve [9] for the same result, upon inputting for instance the efective Riemann-Roch theorem<sup>2</sup> of Coates [3] and Schmidt [10] in the res`
  - 修后/图上真形：`theorem^2`
  - 图上依据：上半图正文第 2 行（3 倍与 6 倍放大）清楚显示 Riemann-Roch theorem 后接上标数字 2，页底脚注 2「Giving an effective basis for the Riemann-Roch space ℒ(D)…」与之对应，修后 ^2 与图一致。
- **Dimitrov_2016-01_effectiveABC_arXiv1601.03572|p12**（双标点，规则修复核对）→ **fix-wrong**
  - 修前：`[1] Bilu Y., M. Strambi, A. Surroca: Quantitative Chevalley-Weil theorem for curves, Monats. Math., vol. 171, no. 1 (2013), pp. 1–32.`
  - 修后/图上真形：`[1] Bilu Y., M. Strambi, A. Surroca: Quantitative Chevalley-Weil theorem for curves, Monats. Math., vol. 171, no. 1 (2013), pp. 1–32.`
  - 图上依据：REFERENCES 首条 [1]（p012-top.png，裁剪 3 倍放大 /tmp/p012-ref1-zoom.png）：图上第一行清晰为「Bilu Y., M. Strambi, A. Surroca:」（Y. 后有逗号），第二行为「curves, Monats. Math., vol. 171」（Math. 后有逗号）；补丁删掉的两处逗号在图上均真实存在，修后片段与图不一致，图上形态恰与修前 MinerU 行吻合。
