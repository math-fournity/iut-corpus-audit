# TIER-0 确定性比对 — Joshi_2024-03_ATS-IV-ProofOfABC_arXiv2403.10430（PDF 文本层 vs MinerU 切片）

- 页数 80；FLAG（Jaccard<0.85 或元数据泄漏）21 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 35 | 35 | 1.0 | - | - | - |  |
| 2 | 103 | 104 | 0.99 | - | structure | - |  |
| 3 | 34 | 35 | 0.971 | - | u_x | - |  |
| 4 | 209 | 203 | 0.953 | cap dif ferent field1 ory quan | captured different | - |  |
| 5 | 221 | 215 | 0.946 | diophan ing ory quan ries surround | diophantine quantification surrounding | - |  |
| 6 | 214 | 206 | 0.953 | accord cen funda ichmuller ing mann | according | - |  |
| 7 | 215 | 209 | 0.927 | corol estab lary lish orem pro | corollary establish properties provided satisfactory | - |  |
| 8 | 172 | 170 | 0.966 | correspond eθi ing θgau | corresponding gau | - |  |
| 9 | 167 | 156 | 0.889 | cor corol formations holomor lary muller | assertion assimilated gau version | - |  |
| 10 | 158 | 153 | 0.968 | arith eθjoshi eθmochizuki holomor phoid | - | - |  |
| 11 | 221 | 214 | 0.916 | able dif etry ferences formations geom | deformations differences domains inparticular ofa suitable | - |  |
| 12 | 190 | 184 | 0.908 | erates eθmochizuki eσl ifestly istence man | eas ecertain esense iteerates manifestly reorganized | - |  |
| 13 | 164 | 162 | 0.918 | cohomolog corollary eθjoshi eθmochizuki func ical | cohomological e2024c ebit ecorollary eone eto | - |  |
| 14 | 160 | 158 | 0.975 | hφn sup vlrv | abcconjecture | - |  |
| 15 | 215 | 210 | 0.932 | 2021a alance ates equiv eθjoshi eθmochizuki | eis eof equivealance ethe ord | - |  |
| 16 | 217 | 209 | 0.893 | conclu contribu exis eθmochizuki hol lmod | array conclue contributions esion ethe eto | - |  |
| 17 | 188 | 183 | 0.903 | ber contribute egy erates eθmochizuki eθy0 | econtribute eof equantities ethe iterates logshifting | - |  |
| 18 | 136 | 126 | 0.899 | bers conjec defini equa eθmochizuki eθy0 | definition numbers | - |  |
| 19 | 183 | 171 | 0.903 | alge arith braically frobe jects metic | algebraically ink underpins | - |  |
| 20 | 207 | 203 | 0.881 | addi arith con ematical eθjoshi eθmochizuki | additive arithmeticoid cone ehave eis elocal | - |  |
| 21 | 141 | 139 | 0.905 | con constructing eθjoshi eθmochizuki ini structed | constructed econstructing efargues eis eunder initial | - |  |
| 22 | 105 | 102 | 0.917 | arithmeti cal coid holomor phoid solute | absolute x27 étale | - |  |
| 23 | 163 | 154 | 0.921 | bles fpv hol pered pro qpv | resembles tempered | - |  |
| 24 | 184 | 181 | 0.973 | com posite sl2 θgau | composite | - |  |
| 25 | 48 | 48 | 0.959 | sl2 | array | - |  |
| 26 | 68 | 67 | 0.824 | frobe func multiples nius sl2 tion | a_i b_i c_j gau offmultiples πfrom | - | ⚠ |
| 27 | 151 | 145 | 0.935 | cies ever how idence impos indetermina | however indeterminacies | - |  |
| 28 | 112 | 106 | 0.863 | argu com con etale ject ment | comparison constructed object papers étale | - |  |
| 29 | 218 | 215 | 0.977 | com ments pro vided | provided | - |  |
| 30 | 81 | 78 | 0.916 | exp gcd log max rad | array thatfor | - |  |
| 31 | 145 | 139 | 0.945 | amor cond diffx geo metric red | amoros | - |  |
| 32 | 89 | 79 | 0.867 | cond diffp1 diffx htωp1 htωx inequal | array | - |  |
| 33 | 118 | 116 | 0.95 | con equiva jecture lent | abcconjecture thefollowing | - |  |
| 34 | 138 | 138 | 0.903 | cond diffx htωx log primes suitable | abcconjecture array numberfield ofprimes suitablefinite thefollowing | - |  |
| 35 | 163 | 156 | 0.899 | ages aver eterizes ly1 ly2 lyi | averages numberfield ofm ofvarieties parameterizes | - |  |
| 36 | 119 | 111 | 0.855 | anabelo ative dmj dmw glv hyperbolic | anabelomorphic ofhyperbolic oftwo ord relative | - |  |
| 37 | 150 | 143 | 0.89 | 212 dmod emod interest lmod max | numberfield ofa ofinterest simplest structures | - |  |
| 38 | 85 | 73 | 0.837 | 212 clmod cltpd emod force gl2 | inforce | - | ⚠ |
| 39 | 69 | 64 | 0.873 | diffol lmod ordw pfv pfw varc | array ord | - |  |
| 40 | 111 | 98 | 0.866 | clmod cmw diffol discm discmw lmod | ord | - |  |
| 41 | 64 | 55 | 0.776 | clmod deg finite lmod log olmod | afinite mod ord | - | ⚠ |
| 42 | 56 | 51 | 0.814 | arith lmod log ordv ordw qj2 | array mod ord | - | ⚠ |
| 43 | 128 | 118 | 0.836 | abc arithmeticoids clar conjecture dence depen | abcconjecture clarify dependence efor garithmeticoids ord | - | ⚠ |
| 44 | 75 | 75 | 0.923 | nor propo sition | arisingfrom oftate ofthe | - |  |
| 45 | 130 | 127 | 0.849 | 2021a arith dz1 dz2 dzl eθi | eproposition farfrom isfarfrom offunction ofproposition ofthe | - | ⚠ |
| 46 | 143 | 138 | 0.912 | abc cer conjecture ometries ordv swild | abcconjecture certainly geometries ofl | - |  |
| 47 | 64 | 63 | 0.868 | dlv dmw ordv red vnon | array non ofthe ord | - |  |
| 48 | 55 | 51 | 0.86 | log ordp ordv swild vnon wild | array ord | - |  |
| 49 | 129 | 123 | 0.924 | exten kyv proach qpv sions swild | approach oftheorem | - |  |
| 50 | 110 | 104 | 0.928 | com kyv pact qpv supported varc | array | - |  |
| 51 | 118 | 113 | 0.909 | cmw lmod log mell ordw resp | ofmoduli ord thefunction | - |  |
| 52 | 99 | 88 | 0.833 | deg ell found hop1 hωp1 jinv | ifound ofproofs ord | - | ⚠ |
| 53 | 148 | 135 | 0.838 | 212 2njinv cor dmod ell excand | afinite array corresponding ofprimes ofproposition satisfying | - | ⚠ |
| 54 | 126 | 120 | 0.922 | ais asuch fundamen log pears tal | fundamental oftheorem | - |  |
| 55 | 37 | 34 | 0.868 | abe log vnon ξprm | array | - |  |
| 56 | 65 | 60 | 0.786 | bounded following for lbe log lsatisfying | array ofbounded ofmultiplicative oforder thefollowing | - | ⚠ |
| 57 | 107 | 99 | 0.89 | gl2 las log lto rem sl2 | ofthe proofoftheorem | - |  |
| 58 | 96 | 92 | 0.861 | 2021c 2762 dltpd dmod fltpd land | array ofc ofthe proofis theproofis | - |  |
| 59 | 68 | 64 | 0.808 | 210 dltpd estimates fltpd gl2 lmod | arisingfrom differentfrom estimatesfor mod oftheorem | - | ⚠ |
| 60 | 94 | 81 | 0.823 | condi dltpd exten fltpd land lin | array conditions | - | ⚠ |
| 61 | 73 | 58 | 0.77 | condi deg dltpd finite lmod log | conditions | - | ⚠ |
| 62 | 71 | 65 | 0.838 | deg dltpd dmod fltpd mod pfv | array oftheorem proofofproposition | - | ⚠ |
| 63 | 86 | 73 | 0.828 | dlmod dltpd flmod fltpd land lmod | mod | - | ⚠ |
| 64 | 59 | 53 | 0.836 | deg dltpd dmod fltpd lmod lthat | array mod | - | ⚠ |
| 65 | 164 | 163 | 0.958 | eθi pvq tered unclut | ebound logvolumes uncluttered | - |  |
| 66 | 125 | 119 | 0.835 | deg dltpd dmod eθi filtered fltpd | array non normalizationfor numberfield offiltered ofinitial | - | ⚠ |
| 67 | 195 | 195 | 0.902 | ainf com eθi fil fontaine fundamental | deetailed eeach frobeniusshifted non numberfield ofan | - |  |
| 68 | 114 | 105 | 0.888 | emod eθi gl2 gl3 lmod proposi | array proposietion | - |  |
| 69 | 101 | 93 | 0.848 | eθi half hull log mod philoso | array halfplane philosophy proofoftheorem | - | ⚠ |
| 70 | 48 | 37 | 0.735 | 2l2 2llog dltpd dmod eθi fltpd | array | - | ⚠ |
| 71 | 58 | 49 | 0.814 | 212 2llog dltpd dmod eθi fltpd | array | - | ⚠ |
| 72 | 67 | 59 | 0.8 | cond deg diffx dltpd dmod eθi | array prm tpd | - | ⚠ |
| 73 | 94 | 82 | 0.814 | 200 2q1 cond diffp1 dltpd dmod | array con diff | - | ⚠ |
| 74 | 46 | 42 | 0.913 | dltpd exc fltpd log | - | - |  |
| 75 | 139 | 136 | 0.897 | cond diffp1 dltpd fltpd gal hunif | array atfrom con oftheorem proofgiven subset | - |  |
| 76 | 183 | 181 | 0.968 | ast erisque etrable impen | asterisque impenetrable | - |  |
| 77 | 154 | 150 | 0.924 | analy ast destabilized erisque frobenius iso | analysis asterisque frobeniusdestabilized isomorphs | - |  |
| 78 | 200 | 194 | 0.903 | 20groth 211 algo bor cerning con | 20grot 211of algorithms bordered concerning endomorphisms | - |  |
| 79 | 177 | 172 | 0.961 | 20structu mathe matics ory retic theo | 20struct | - |  |
| 80 | 168 | 168 | 0.92 | ast_1990__183__7_0 erisque fectif kˆokyˆuroku number teichm | _183 _1990 asterisque effectif koky ofnumber | - |  |