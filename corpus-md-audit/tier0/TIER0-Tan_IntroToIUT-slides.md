# TIER-0 确定性比对 — Tan_IntroToIUT-slides（PDF 文本层 vs MinerU 切片）

- 页数 48；FLAG（Jaccard<0.85 或元数据泄漏）21 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 12 | 12 | 1.0 | - | - | - |  |
| 2 | 78 | 85 | 0.895 | proceed | b846b25 block doc image iproceed page | - |  |
| 3 | 27 | 25 | 0.793 | 1zp aipi completion lim | array letion | - | ⚠ |
| 4 | 56 | 48 | 0.793 | gal gf1 gf2 gk1 gk2 gki | isom top | - | ⚠ |
| 5 | 77 | 79 | 0.857 | etale isomk isomouter πxk πyk | g_k isom outer txt x_k y_k | - |  |
| 6 | 71 | 68 | 0.958 | bcris bst ok0 | - | - |  |
| 7 | 116 | 114 | 0.983 | fmod qj2 | - | - |  |
| 8 | 59 | 49 | 0.742 | biri different iiq ikwi kwi logp | array diferent e_f | - | ⚠ |
| 9 | 63 | 58 | 0.921 | btp covf gan lim πtp | - | - |  |
| 10 | 57 | 56 | 0.915 | btp hom homout | ithe out | - |  |
| 11 | 60 | 56 | 0.902 | 1gal gkn stable zgal πtp | ithe | - |  |
| 12 | 79 | 73 | 0.9 | differ effective multiples qj2 u2n y2n | difer | - |  |
| 13 | 51 | 47 | 0.849 | dx0 galois land lbz lis trivial | array trivialgalois | - | ⚠ |
| 14 | 41 | 44 | 0.7 | autk covers deg dx0 gal πtp | array aut b846b25 block doc image | - | ⚠ |
| 15 | 79 | 71 | 0.899 | fmod gl2 non oef sl2 vbad | - | - |  |
| 16 | 50 | 49 | 0.904 | autcf endcf φgp | aut end | - |  |
| 17 | 56 | 55 | 0.947 | effective monoid | efective | - |  |
| 18 | 51 | 48 | 0.941 | btp φbirat φgp | - | - |  |
| 19 | 44 | 38 | 0.864 | btp functionsfv gkv logφ μ2l φcv | - | - |  |
| 20 | 34 | 29 | 0.853 | fmod log logφ vmod φrlf | - | - |  |
| 21 | 58 | 54 | 0.867 | cfmod cpt fmod gkcfmod πcfmod πrat | rat tional | - |  |
| 22 | 40 | 37 | 0.878 | objects terminal μfr πrat | rat | - |  |
| 23 | 43 | 41 | 0.867 | lim vmod μfr πrat | array rat | - |  |
| 24 | 35 | 31 | 0.833 | autkv btp torsor varc vnon | array | - | ⚠ |
| 25 | 24 | 20 | 0.692 | autε cfmod fmod gl2 vbad φnf | array mod | - | ⚠ |
| 26 | 76 | 66 | 0.844 | 99k btp can l99 land qj2 | lab | - | ⚠ |
| 27 | 55 | 48 | 0.839 | autcsp autk dvt flby gl2 ker | csp | - | ⚠ |
| 28 | 32 | 26 | 0.758 | 99k l99 θnf φnf φθell ψnf | array | - | ⚠ |
| 29 | 51 | 46 | 0.83 | coboundaries conjugacy conjugates gal replacing stau | coboundariesreplacing tau | - | ⚠ |
| 30 | 46 | 42 | 0.872 | difference iii ker stau μfr | diference | - |  |
| 31 | 61 | 56 | 0.828 | abirat autdx autf0 difference han hbn | array aut diference | - | ⚠ |
| 32 | 51 | 46 | 0.83 | autd autf btp conjugacy sln πtp | aut ithe | - | ⚠ |
| 33 | 41 | 38 | 0.927 | lim μ2l πtp | - | - |  |
| 34 | 75 | 68 | 0.857 | given labcusp lim look orbits θenv | igiven ilook | - |  |
| 35 | 21 | 17 | 0.652 | lim μfr ψcns ψenv ψfenv ψfθ | array cns | - | ⚠ |
| 36 | 44 | 39 | 0.844 | autg fails fenv ψcns ψenv ψfenv | env | - | ⚠ |
| 37 | 54 | 42 | 0.778 | kummer lψcns qj2 ãtm θenv μ2l | - | - | ⚠ |
| 38 | 58 | 51 | 0.847 | 0ht 1ht btp gkv qj2 φ01 | cns | - | ⚠ |
| 39 | 69 | 64 | 0.928 | fmod fvq torsor vqlog ψlog | - | - |  |
| 40 | 52 | 48 | 0.852 | 2pv ifvq mod vqi μlog ψcns | array cns | - |  |
| 41 | 75 | 58 | 0.684 | 1dv 1fj 1fv 1ht 2dv flgp | cns env gau lgp | - | ⚠ |
| 42 | 45 | 40 | 0.889 | flgp fmod qj2 vbad ψflgp | - | - |  |
| 43 | 71 | 65 | 0.838 | aut flgp ism mht mod mψcns | cns ind lgp | - | ⚠ |
| 44 | 50 | 45 | 0.863 | aut ind1 ind3 mov prc qj2 | ind | - |  |
| 45 | 49 | 47 | 0.882 | qj2 test vbad θlgp | itest stripf | - |  |
| 46 | 31 | 29 | 0.935 | fvq μlog | - | - |  |
| 47 | 50 | 39 | 0.78 | 0ht 0pq 0pθ 0uθ 1uθ deg | - | - | ⚠ |
| 48 | 47 | 43 | 0.667 | 0deg 0ht 0pθ 0uθ 1ht 1uθ | b846b25 block doc image page standard | - | ⚠ |