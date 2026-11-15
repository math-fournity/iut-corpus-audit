# TIER-0 确定性比对 — Yamashita_2017_AProofOfABCafterMochizuki_v6（PDF 文本层 vs MinerU 切片）

- 页数 294；FLAG（Jaccard<0.85 或元数据泄漏）105 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 120 | 120 | 0.983 | etale | étale | - |  |
| 2 | 163 | 159 | 0.963 | ellnf teichm uller θell θnf | teichmüller | - |  |
| 3 | 217 | 206 | 0.914 | ber condd deg difficult diffp1 diffx | array delimiterspace diff dificult | - |  |
| 4 | 184 | 172 | 0.894 | abc ation con corol defini evalu | array conjecture constant definibtion | - |  |
| 5 | 178 | 162 | 0.771 | abs alg anab arith aut bining | 411efc1 array bcompatibility block coeficient constructing | - | ⚠ |
| 6 | 167 | 187 | 0.825 | 14159 develop dimf ments offering theory1 | array began but context developments difers | - | ⚠ |
| 7 | 141 | 131 | 0.889 | 71828 arc frobk gab gal gtors | array frob hausdorf | - |  |
| 8 | 141 | 138 | 0.836 | abstopi aut gal ghg hausdorff hausdorfftopological | 411efc1 array block bnaturally bsome doc | - | ⚠ |
| 9 | 144 | 103 | 0.68 | 1of adivq adivr analytic arc classes | array efective rarithmetic | - | ⚠ |
| 10 | 140 | 130 | 0.849 | adiv condd degf different diffx effective | cond dif diferent diff efective sufices | - | ⚠ |
| 11 | 154 | 140 | 0.815 | 1ol 2log condd conde deg different | array dif diferent diferents diff efective | - | ⚠ |
| 12 | 169 | 150 | 0.833 | 2deg 2pvi conde deg diffp1 diffx | array diff portion sufices suficiently | - | ⚠ |
| 13 | 114 | 95 | 0.786 | 1ocp bok different dk0 dki eocp | array diferent sufices | - | ⚠ |
| 14 | 171 | 116 | 0.649 | absolute adic average compact definition degf | array dif suficient | - | ⚠ |
| 15 | 111 | 85 | 0.75 | 2ei 2pvq aut ball ei0 fvi | array | - | ⚠ |
| 16 | 155 | 137 | 0.872 | autf compos dmod efmod eftpd fac | factors | - |  |
| 17 | 148 | 116 | 0.714 | 1ρefmod 212 adiv adivq adivr assump | array badmod coeficients conjugate diferent efective | - | ⚠ |
| 18 | 162 | 128 | 0.768 | aut automor ball eftpd fmod ftpd | array automorphism | - | ⚠ |
| 19 | 124 | 102 | 0.752 | 1bi 4μlog aut ball dkvi evj | array bad dist good non | - | ⚠ |
| 20 | 71 | 56 | 0.693 | 4μlog corre degfmod fmod kvi kvj | array avv corresponds mod | - | ⚠ |
| 21 | 73 | 57 | 0.711 | 4μlog dl0 ewdw fmod fol ftpd | array mod prm | - | ⚠ |
| 22 | 43 | 32 | 0.596 | 210 211 2dmod 32dmod 36dmod 3ηprm | array mod prm tpd | - | ⚠ |
| 23 | 118 | 104 | 0.805 | 192 220 32dmod 36dmod 44l 80dmod | array diferentials mod prm tpd | - | ⚠ |
| 24 | 135 | 119 | 0.868 | 2htfalt 2htωe adiv apic arcωev aωe | array | - |  |
| 25 | 159 | 136 | 0.81 | 2htfalt 2htnon arc arithmic coker contribu | array contributions diferential suficiently | - | ⚠ |
| 26 | 148 | 124 | 0.778 | 212 2htfalt autf autq def degl | array bad diff efictive homomorphism | - | ⚠ |
| 27 | 109 | 101 | 0.909 | 2hv 2hvfv exck fmod hvfv up1 | array | - |  |
| 28 | 74 | 63 | 0.803 | 2h2 2tk 3θa exck gal gl2 | array prm | - | ⚠ |
| 29 | 130 | 117 | 0.83 | 200 20ηprm 212 80dmod acv ca1v | array prm section sufices tpd | - | ⚠ |
| 30 | 126 | 114 | 0.818 | 15d 200 2bk 2ck 40ηprm 5εe | array dif difer different efect tpd | - | ⚠ |
| 31 | 163 | 148 | 0.896 | cond diffp1 exck fpi gab gal | unif | - |  |
| 32 | 113 | 96 | 0.771 | duced frobki gab gal gk1 gk2 | array cyc frob grouptheoretically rank | - | ⚠ |
| 33 | 123 | 116 | 0.897 | 0frobki exgi frobki gab gigl gki | array emod frob | - |  |
| 34 | 129 | 123 | 0.895 | assump charac dimql dimqp gab gal | array assumption bis characterisation | - |  |
| 35 | 133 | 129 | 0.941 | defined gal ker tors xfv zg2 | band welldefined | - |  |
| 36 | 137 | 133 | 0.901 | gab gal gev ggev ggevg jac | array ebe ehas ethe suficiently | - |  |
| 37 | 138 | 138 | 0.957 | giyg ker sufficiently | array con suficiently | - |  |
| 38 | 118 | 116 | 0.872 | affine bzfrobk charac dimql eigen frobk | afine array bis characterisations eigenvalues frob | - |  |
| 39 | 186 | 179 | 0.931 | affine bzql cyc dimql hab lnz | afine bgroup suficiently | - |  |
| 40 | 130 | 127 | 0.918 | action degree dients dimql ingre resp | array dim ifk ingredients | - |  |
| 41 | 149 | 155 | 0.949 | lock | 411efc1 array block doc page standard | - |  |
| 42 | 159 | 150 | 0.884 | different difficult gal inn isomgk isomk | array diferent dificult monoanabelian natural | - |  |
| 43 | 193 | 189 | 0.979 | ghg hghg ker zim | - | - |  |
| 44 | 163 | 158 | 0.934 | also curves defini gal orbi sufficiently | array orbicurves suficiently | - |  |
| 45 | 149 | 144 | 0.854 | core corre like locg lock sponding | 411efc1 block doc image page schemelike | - |  |
| 46 | 116 | 117 | 0.864 | 1πx out sufficiently up1 πcore πell | 411efc1 array block doc grouptheoretically page | - |  |
| 47 | 144 | 139 | 0.938 | delta gal out sufficiently πtpd πux | suficiently tpd | - |  |
| 48 | 116 | 113 | 0.941 | dimk gal sufficiently yj1 yj2 | array suficiently | - |  |
| 49 | 129 | 63 | 0.455 | above abstopiii algebraically algorithm are assume | array dim efective | - | ⚠ |
| 50 | 137 | 137 | 0.903 | choice coefficients duce ordx μbz πcusp | array bcanonical bchoice bremark brespectively coeficients | - |  |
| 51 | 132 | 126 | 0.925 | cent supp therefere times torsor μbz | array btherefere | - |  |
| 52 | 147 | 145 | 0.908 | homπx proposi supp tained tion torsor | array bfor bof bthe hom obtained | - |  |
| 53 | 128 | 123 | 0.793 | 1so automor coefficient conj cov ering | 411efc1 array automorphism block bthus coeficient | - | ⚠ |
| 54 | 141 | 137 | 0.944 | knf nnj suffices sxi xnf μbz | array sufices | - |  |
| 55 | 146 | 138 | 0.881 | construc construction dxi fore knf lim | bconstruction constructions numbe ord reb | - |  |
| 56 | 180 | 171 | 0.918 | coefficients coho decom gal hab lim | array coeficients cohomology | - |  |
| 57 | 148 | 143 | 0.854 | gab gal gur iso knf kur | band bby bconstruction bmultiplication bto bwe | - |  |
| 58 | 122 | 119 | 0.928 | action gur ker lim ory μbz | array bit bwe | - |  |
| 59 | 173 | 174 | 0.907 | arith bzfrobk explana frobk isomprofinite isomtopological | array bcorresponds bhowever bthe btheory explanatory | - |  |
| 60 | 162 | 165 | 0.901 | arithmeti automor bzfrobk cally out phism | 411efc1 block doc frob g_k i_k | - |  |
| 61 | 138 | 138 | 0.878 | authol avoiding ditive implicit mor phism | additive eference heory modelimplicit morphism odel | - |  |
| 62 | 129 | 121 | 0.88 | authol autrc index iso lim orn | isomorphism ofindex pgl psl | - |  |
| 63 | 178 | 164 | 0.911 | authol autrc caut hol naut opp | sufices | - |  |
| 64 | 179 | 164 | 0.885 | allel aut0 axcore caut0 etop gal | autholomorphic ofu transporting | - |  |
| 65 | 160 | 155 | 0.933 | differentiable home omorphisms psl2 satisfies sufficiently | diferentiable homeomorphisms suficiently | - |  |
| 66 | 132 | 127 | 0.904 | ax1 ax2 etop functorial ity lim | autholomorphic functoriality suficiently top | - |  |
| 67 | 125 | 119 | 0.937 | analyticisation con log oax proposi sider | monoanalyticisation | - |  |
| 68 | 153 | 152 | 0.871 | anyticisation arith arithmeti base bundle cally | 411efc1 block doc forgetting frobeniuslike image | - |  |
| 69 | 166 | 162 | 0.885 | etale follow func indeterminacies ing knf | functions g_k grouptheoretically iffor ofnf ofthe | - |  |
| 70 | 172 | 164 | 0.867 | authol coefficients etop func homkv isomor | array autholomorphic coeficients functions grouptheoretically ofa | - |  |
| 71 | 148 | 143 | 0.966 | 2pi lim logk oπx μbz | - | - |  |
| 72 | 148 | 133 | 0.849 | 2pg 2pgim additivity com define endomor | array composite endomorphisms frobenius | - | ⚠ |
| 73 | 149 | 143 | 0.921 | differ iso logk morphism sub εef | array difer subdiagram | - |  |
| 74 | 173 | 166 | 0.926 | deter differentiable dimen expk limn mines | diferentiable dimensional oftwo | - |  |
| 75 | 140 | 135 | 0.937 | differentiable end expk prang prrad rarc | array diferentiable | - |  |
| 76 | 172 | 173 | 0.927 | btemp sl2 xan zπ2 πtemp πtop | 411efc1 block doc image page standard | - |  |
| 77 | 164 | 157 | 0.922 | btemp charasterisa different geomet oids ric | charasterisation diferent geometric | - |  |
| 78 | 141 | 130 | 0.908 | bcov btemp cov gex gv1 gv2 | array | - |  |
| 79 | 140 | 133 | 0.936 | btemp gtemp htemp ker lim propo | cand | - |  |
| 80 | 180 | 176 | 0.967 | bzς funda gtemp mental πtemp | array | - |  |
| 81 | 185 | 185 | 0.917 | commen corollary evγ gtemp surably γtemp | bare bwith cardinalit ealso eare eby | - |  |
| 82 | 134 | 132 | 0.985 | 1λγ πtemp | - | - |  |
| 83 | 139 | 137 | 0.89 | anabelioids homdense homdom ker resp suffices | array banabelioids bis dense dom hom | - |  |
| 84 | 155 | 146 | 0.929 | funda hom mental nπtemp rem temp | bunique | - |  |
| 85 | 156 | 148 | 0.877 | action cor equivariant hom hsing like | bby bdenote bgives corresponding normalisation tempered | - |  |
| 86 | 114 | 114 | 0.824 | absanab divisible gab genera gkμbz module | 411efc1 array bdivisible block bpositive bsplits | - | ⚠ |
| 87 | 129 | 129 | 0.911 | gal ometrically spf subsec tion πtemp | array bbe bdenote geometrically interuniversal subsection | - |  |
| 88 | 114 | 117 | 0.893 | gkn natu okn ral πtemp | 411efc1 bbe block bra doc page | - |  |
| 89 | 138 | 131 | 0.935 | gjn gkn log multiple ojn okn | array | - |  |
| 90 | 129 | 126 | 0.861 | bgm ell gal gjn ker ojn | 411efc1 array block brepresents doc page | - |  |
| 91 | 137 | 134 | 0.856 | 2j2 gal k2n ojn okn pic | 411efc1 array block doc image page | - |  |
| 92 | 103 | 97 | 0.887 | difference differs k2n ojn okn s2n | array diference difers | - |  |
| 93 | 158 | 160 | 0.916 | bgm bωy difference minus μ2l πtemp | bis bminus bof bthe bthis bus | - |  |
| 94 | 109 | 104 | 0.902 | 2πi bωy e2πiτ exp eπiz μ2l | bin bis bstructure | - |  |
| 95 | 116 | 118 | 0.887 | 1eg bωy formal not suffices πtemp | array bformal bis bthis eat ehas | - |  |
| 96 | 102 | 102 | 0.838 | 2bz fil0 fil1 fil2 iden introduced | array bcoordinate bcorresponds bintroduced bon bthe | - | ⚠ |
| 97 | 182 | 178 | 0.905 | cies coro indetermina insufficient nπx propo | bindeterminacies bthe corobrally indeterminabcies insuficient partial | - |  |
| 98 | 155 | 151 | 0.877 | bgm conjugate fil0 fil1 hand origin | bhand bof borigin bset bthe primeto | - |  |
| 99 | 154 | 145 | 0.917 | deter gal grig mined ogm orbit | bis temp | - |  |
| 100 | 145 | 142 | 0.952 | gal temp theoretically γπx πtemp | array grouptheoretically | - |  |
| 101 | 155 | 153 | 0.962 | ell gal ker scend | descend letlet | - |  |
| 102 | 128 | 124 | 0.969 | ker torsθ vbad ειx | - | - |  |
| 103 | 131 | 125 | 0.939 | autk ell out sect temp torsθ | aut | - |  |
| 104 | 87 | 86 | 0.86 | deg ext galois non resp thhhhhhhhhhhhhhhhhhhhhhh | 411efc1 block doc page standard tier | - |  |
| 105 | 112 | 113 | 0.957 | differs πtemp | array difers temp | - |  |
| 106 | 114 | 114 | 0.949 | autk μ2l πtemp | array aut temp | - |  |
| 107 | 106 | 103 | 0.935 | ker orbit salg πtemp πμn | alg array | - |  |
| 108 | 104 | 100 | 0.907 | 1salg asalg constructed ell salg sub | alg reconstructed subgroup | - |  |
| 109 | 99 | 93 | 0.882 | 1asalg 1salg asalg aut bsalg conjugate | alg array temp | - |  |
| 110 | 117 | 108 | 0.923 | 1tθ automor compos inn ite phism | - | - |  |
| 111 | 132 | 119 | 0.887 | aut conjugacy corol fil0 fil1 gal | proposition | - |  |
| 112 | 121 | 115 | 0.95 | autμm autμn environ isomμn ment πtemp | - | - |  |
| 113 | 120 | 117 | 0.911 | apply autμn difference ing salg vironments | applying diference ofa ofthe | - |  |
| 114 | 133 | 118 | 0.846 | alge braic ele envi environ hom | element monotheta ofstandard | - | ⚠ |
| 115 | 139 | 135 | 0.916 | dis indetermi lbz nacy sec tinguished | bdiscreteness bdoes distinguished sections | - |  |
| 116 | 173 | 169 | 0.791 | affine aut coefficient compact efmod fmod | 411efc1 afine bas bis bity block | - | ⚠ |
| 117 | 148 | 147 | 0.941 | ded embed gal vbad vgood | array bad embedded good | - |  |
| 118 | 148 | 138 | 0.894 | 2l2 2lz autk con degfr formu | contravariant grouptheoretically hom | - |  |
| 119 | 112 | 105 | 0.871 | autc degfr divb endc homc homd | array aut end hom | - |  |
| 120 | 154 | 152 | 0.843 | cated cause cbirat compli con degfr | 411efc1 because birat block complicated doc | - | ⚠ |
| 121 | 167 | 160 | 0.901 | acteristic automor char divi duced effective | bequipped characteristic efective geometrically ummer | - |  |
| 122 | 128 | 117 | 0.885 | btemp gkv image ker mon qpv | 21on temp | - |  |
| 123 | 149 | 141 | 0.921 | bconst dell effective ker lim temp | efective logmeromorphic | - |  |
| 124 | 126 | 112 | 0.859 | aut bconst fbase frobe logφ malised | const normalised | - |  |
| 125 | 134 | 127 | 0.948 | adv base degfr div fmod log | - | - |  |
| 126 | 121 | 104 | 0.815 | abirat arc autdv different effective etth | diferent efective proposition | - | ⚠ |
| 127 | 103 | 97 | 0.818 | autdv autfv autθ coefficient difference iso | array aut categorytheoretically coeficient diference temp | - | ⚠ |
| 128 | 127 | 118 | 0.856 | autdv autfv birat cation lln lnz | acv aut categorytheoretic multiplication temp | - |  |
| 129 | 147 | 143 | 0.883 | affine cfmod cyclo efmod envi fmod | afine array cyclotome environments frobenioidtheoretic mod | - |  |
| 130 | 168 | 158 | 0.918 | cfmod cyclotome fmod func mark rem | bcyclotome grouptheoretically | - |  |
| 131 | 142 | 135 | 0.951 | cfmod fmod gal loc vmod μbz | - | - |  |
| 132 | 155 | 143 | 0.91 | aut cfmod con coricity fmod gal | considering | - |  |
| 133 | 151 | 142 | 0.915 | bp0 distinguish example iso isomor lim | bdistinguish bexample | - |  |
| 134 | 125 | 117 | 0.921 | btemp fmod loc mκv qpv tors | grouptheoretically | - |  |
| 135 | 153 | 143 | 0.91 | drat fmod gal lim mκv open | array band | - |  |
| 136 | 150 | 39 | 0.252 | above admitting after algorithmi algorithmically alien | grouptheoretically | - | ⚠ |
| 137 | 120 | 121 | 0.883 | differences induced makes vbad vgood vnon | array bglobal diferences etalelike inducedby makesavailable | - |  |
| 138 | 167 | 162 | 0.869 | affect conjugacy difference effect jective lim | afect bdefinition blevels cneed diference efect | - |  |
| 139 | 165 | 158 | 0.923 | arc different fmod gal iso mod | bwe diferent formulae | - |  |
| 140 | 143 | 135 | 0.931 | arith birat ellnf fmod gal metic | arithmetic | - |  |
| 141 | 89 | 84 | 0.901 | cos e2πi ellnf fmod qj2 sin | bor mod | - |  |
| 142 | 70 | 59 | 0.792 | alent analyticisation btemp ellnf equiv varc | array monoanalyticisation | - | ⚠ |
| 143 | 88 | 77 | 0.813 | 99k adv bridge frobe jection mod | array bijection ell | - | ⚠ |
| 144 | 118 | 105 | 0.843 | arithmetic ellnf fmod gal geometric kummer | array bad stacktheoretic | - | ⚠ |
| 145 | 166 | 148 | 0.88 | appen arc dix ell fmod gl2 | appendix | - |  |
| 146 | 101 | 89 | 0.863 | adv btemp differs exam mod not | difers | - |  |
| 147 | 112 | 102 | 0.814 | arith btemp defini fmod log logpv | arc arithmetic array bad good non | - | ⚠ |
| 148 | 92 | 82 | 0.871 | fbirat oaθ obirat oxv splθ varc | birat | - |  |
| 149 | 80 | 72 | 0.81 | con cθr ement fmod logφ prime | array bad considered good | - | ⚠ |
| 150 | 98 | 95 | 0.804 | evf except fmod indet logd rarc | 411efc1 arc block doc image non | - | ⚠ |
| 151 | 104 | 96 | 0.905 | col iso lection morphism theta varc | collection | - |  |
| 152 | 115 | 113 | 0.966 | vbad vgood vnon | array | - |  |
| 153 | 134 | 128 | 0.807 | autd autf auto com isomd isomf | 411efc1 automorphisms block computations doc frobenioidprime | - | ⚠ |
| 154 | 131 | 121 | 0.909 | 1ht 2ht isomd isomf resp respec | sufices | - |  |
| 155 | 110 | 111 | 0.842 | arc ilar ondly pull sec slim | 411efc1 block doc image page polymorphism | - | ⚠ |
| 156 | 106 | 98 | 0.889 | aut ductive spl tained varc vbad | array ummer | - |  |
| 157 | 119 | 108 | 0.892 | adic autf div isomf isomor mod | isom | - |  |
| 158 | 122 | 115 | 0.911 | core corol lary mod torsor varc | primegl primestrip | - |  |
| 159 | 137 | 128 | 0.893 | autε fmod gal gfmod gl2 sl2 | array bor mod | - |  |
| 160 | 115 | 105 | 0.88 | autε dvj grig okv theoretically varc | array grouptheoretically | - |  |
| 161 | 136 | 128 | 0.913 | btemp covering dvj labcusp map spective | polymorphism temp | - |  |
| 162 | 112 | 100 | 0.86 | autε deter dvj dwj isomor mines | determines obtaine | - |  |
| 163 | 115 | 111 | 0.932 | dvj out proposi tion φlc φnf | lab polyby | - |  |
| 164 | 154 | 125 | 0.733 | age autε base begin call constructed | 411efc1 block doc image page standard | - | ⚠ |
| 165 | 119 | 112 | 0.893 | auto fvj labcusp mod object recon | array polymorphism reconstructing | - |  |
| 166 | 47 | 52 | 0.833 | φnf ψnf | 411efc1 block chart doc page standard | - | ⚠ |
| 167 | 96 | 95 | 0.929 | conjugates fvj varc vmod | array polymorphism toloc | - |  |
| 168 | 78 | 70 | 0.85 | 1dj1 1fj1 1ψnf 2dj2 2fj2 2ψnf | array polypoly | - |  |
| 169 | 103 | 85 | 0.808 | 1fj1 1ht 1φnf 1φθ 1ψnf 1ψθ | array | - | ⚠ |
| 170 | 118 | 109 | 0.908 | core corol lary prime sets strip | primestrip | - |  |
| 171 | 94 | 93 | 0.948 | alently autα equiv | array equivalently | - |  |
| 172 | 130 | 128 | 0.883 | autcusp autk fmod gal gl2 labcusp | 411efc1 array block doc page standard | - |  |
| 173 | 156 | 143 | 0.846 | 1fl aut autcusp con differences dvt | conjugate diferences ell monoanalytic polyautomorphism primestrip | - | ⚠ |
| 174 | 101 | 94 | 0.875 | autcusp cup duced dv0 iso resp | cusp ell polycapsule | - |  |
| 175 | 96 | 88 | 0.917 | autcusp dvt dwt let ζθell θell | - | - |  |
| 176 | 98 | 88 | 0.842 | 1fl autcusp automorphism com groups isomf | composite cusp polyautomorphism | - | ⚠ |
| 177 | 97 | 82 | 0.808 | brideges call corol diagram etale have | corollary polypoly | - | ⚠ |
| 178 | 117 | 103 | 0.789 | 1ht 1φθ 1φθell 1ψθ 1ψθell 2ht | array ell ence iso ofd proposition | - | ⚠ |
| 179 | 144 | 141 | 0.966 | 99k associ ated ellnf | array | - |  |
| 180 | 122 | 121 | 0.869 | cate gory isomor mul phism qj2 | 411efc1 array block doc image page | - |  |
| 181 | 120 | 118 | 0.951 | coric difference gl2 qj2 | array diference | - |  |
| 182 | 87 | 86 | 0.784 | described dmθ ggnnnnnnnnnnn gl2 kkwwwwwwwwwwwwwwwwwwwwwwwww recon | 411efc1 array block describedin doc image | - | ⚠ |
| 183 | 109 | 107 | 0.815 | ccggggggggg defi iisssssssssssssssssssss lim mor phisms | 411efc1 bafter block doc grouptheoretically image | - | ⚠ |
| 184 | 98 | 104 | 0.741 | cyclotomes duced iso logical morphic morphism | 411efc1 array bcyclotomes block bof bto | - | ⚠ |
| 185 | 141 | 138 | 0.924 | effects gl2 ker lim open rlcft | array bcyclotomic efects indtopological | - |  |
| 186 | 115 | 100 | 0.762 | ally auto constructed elcft functori grig | array bstructed bwhich grouptheoretically isomorphic polyisomorphism | - | ⚠ |
| 187 | 115 | 109 | 0.898 | gal theoretically vbad θenv μ2l μ4l | array env grouptheoretically | - |  |
| 188 | 111 | 103 | 0.845 | ators cycl left lim prop recip | array bdenotes env grouptheoretically restriction | - | ⚠ |
| 189 | 114 | 109 | 0.874 | eenv graph lim picture θenv μ2l | env etalepicture ofthe polyfull temp | - |  |
| 190 | 136 | 141 | 0.897 | connect evalenv ing vbad θenv | 411efc1 array block connecting doc env | - |  |
| 191 | 101 | 98 | 0.843 | btemp bπv cation constructable determine labcusp | array bdetermine bin bis bresp groupbtheoretic | - | ⚠ |
| 192 | 94 | 86 | 0.837 | bπcor bπv equiva gal iγγ labcusp | bis bthus equivalently temp | - | ⚠ |
| 193 | 124 | 116 | 0.875 | bπcor bπv conj cor functo iγγ | band described dthe functorially | - |  |
| 194 | 127 | 125 | 0.938 | coefficient iγ1 theoretic μ2l πγ2 | array coeficient grouptheoretic | - |  |
| 195 | 164 | 159 | 0.923 | alified cor dmθ lim minj μbz | bin bmanner bthe realified | - |  |
| 196 | 94 | 84 | 0.816 | bπv iγγ jective labcusp lim open | array bconj bin brestriction | - | ⚠ |
| 197 | 110 | 101 | 0.788 | bility bπv compati decom iγ1 labcusp | allow bin bmark bwe compatibility decomposition | - | ⚠ |
| 198 | 125 | 114 | 0.824 | autdv conjugates correspond exam ing iso | birat bobtain cns corresponding determines temp | - | ⚠ |
| 199 | 130 | 114 | 0.807 | actions aut autdv cyclo iso jective | array birat cns isobmorphisms projective | - | ⚠ |
| 200 | 91 | 84 | 0.823 | ally base field iso jective mod | array env isomorphisms multiradially temp | - | ⚠ |
| 201 | 119 | 109 | 0.854 | auto cal construct iso isomor jective | array bconstruct cns ofmono | - |  |
| 202 | 89 | 87 | 0.853 | gle isomor phisms sin πtemp ψcns | array cns gau single temp valueprofile | - |  |
| 203 | 107 | 95 | 0.804 | compos denote determined ing iso jective | array composing gau projective temp | - | ⚠ |
| 204 | 165 | 153 | 0.916 | cyclo fined gle mod qj2 struc | mmetry | - |  |
| 205 | 123 | 111 | 0.828 | con environ gal ments proposi struction | array bto construction gau proposition | - | ⚠ |
| 206 | 85 | 73 | 0.756 | cor gal ious just lim logd | array corresponding non obtain various | - | ⚠ |
| 207 | 78 | 72 | 0.829 | holo labcusp loguv logπv module morphic | array env gau log | - | ⚠ |
| 208 | 116 | 103 | 0.81 | 71828 btemp dis erator eval gen | array evaleval generator log ofmonoids | - | ⚠ |
| 209 | 90 | 76 | 0.785 | col cor gal iso labcusp lection | collection env gau | - | ⚠ |
| 210 | 121 | 116 | 0.866 | btemp corol lary mod varc vbad | arc array bad ell good non | - |  |
| 211 | 90 | 83 | 0.747 | mod proposi resp strip tion varc | arc array bad cns ell env | - | ⚠ |
| 212 | 76 | 75 | 0.936 | ψenv ψgau ψθell | ell primestrip | - |  |
| 213 | 106 | 97 | 0.845 | calisation conjugacy dis gorithm proposi tinguished | arc array localisation non | - | ⚠ |
| 214 | 100 | 89 | 0.817 | 99k actions iso labcusp morphisms varc | arc array cns ofnotation | - | ⚠ |
| 215 | 110 | 102 | 0.91 | construc corol lary theta tion πrat | construction | - |  |
| 216 | 117 | 109 | 0.868 | defini dvj gal iso isomor labcusp | array polymorphisms rat respecgl | - |  |
| 217 | 116 | 104 | 0.864 | 99k cap cyc gal indetermi l99 | capsule rat | - |  |
| 218 | 110 | 105 | 0.87 | 99k isomor labcusp phisms respec κvj | array cns ofcorollary rat respecgl | - |  |
| 219 | 91 | 81 | 0.811 | ation cenv cgau derlying eval evalu | array isom ofcorollary underlying | - | ⚠ |
| 220 | 92 | 90 | 0.936 | defini qj2 tion vbad | array bad | - |  |
| 221 | 122 | 94 | 0.756 | also are compatible enhanced frobenius hand | array | - | ⚠ |
| 222 | 118 | 107 | 0.86 | 2pv differ exp kum logical logv | array autholomorphic difer | - |  |
| 223 | 115 | 108 | 0.858 | differ logical proposi quo tauto tien | array difer quotien tautological unafected | - |  |
| 224 | 102 | 97 | 0.793 | adic con dia gram logarc lognon | arc array cns dprime monoanalytic ofd | - | ⚠ |
| 225 | 92 | 83 | 0.842 | cns expk isomor more over phism | array moreover section | - | ⚠ |
| 226 | 82 | 77 | 0.871 | col lection logarc lognon shhhhhhhhhhhhhhhhhhhhhhhhh wooooooooooo | array polyisomorphisms primestrip | - |  |
| 227 | 95 | 96 | 0.949 | nht ψcns | loa polylogloglog polypolypoly | - |  |
| 228 | 88 | 89 | 0.844 | 1ht gau mht nht shhhhhhhhhhhhhhhhhhhhhhhh vbad | 411efc1 bad block doc image page | - | ⚠ |
| 229 | 101 | 95 | 0.849 | 1ht cns fity iden iso isomor | denotes dprime idenfity polyisomorphisms rime | - | ⚠ |
| 230 | 91 | 86 | 0.883 | corol isomor lary mρd phism varc | array polyisomorphisms ummer | - |  |
| 231 | 103 | 100 | 0.933 | autf mht vbad ψenv ψfenv | aut bad | - |  |
| 232 | 135 | 122 | 0.849 | autf commuta compat environ fenv ible | array environment polyautomorphism temp | - | ⚠ |
| 233 | 82 | 73 | 0.824 | essen isomor mht mor morc morr | array essentially polypolypoly | - | ⚠ |
| 234 | 97 | 92 | 0.835 | corol defini labelled lary morr mrbad | array definition isomorinduced kuminduced polyfull polyisomorphisms | - | ⚠ |
| 235 | 161 | 161 | 0.928 | const dif ferences func qj2 tions | amp array byconst diferences o_v x27 | - |  |
| 236 | 171 | 162 | 0.892 | differ ertia fying holomor identi iord | array bis difer ord reconstruction | - |  |
| 237 | 117 | 118 | 0.865 | difficult difficulty eye holo lgp morphic | 411efc1 block dificult dificulty doc image | - |  |
| 238 | 132 | 136 | 0.928 | eye holo morphic | 411efc1 block doc image page standard | - |  |
| 239 | 116 | 90 | 0.761 | also changed coefficient cond consider definition | array | - | ⚠ |
| 240 | 111 | 99 | 0.826 | 1fvq affects fmod kvi lim okv | afects appearing indtopological mod | - | ⚠ |
| 241 | 72 | 68 | 0.842 | affects fvq pvq varc vmod vnon | afects array primestrips tautopoly | - | ⚠ |
| 242 | 100 | 93 | 0.892 | field fvq proposi spectively tion varc | array tautopoly | - |  |
| 243 | 153 | 136 | 0.865 | 1fvq com equip homo isation mand | compatible equipping | - |  |
| 244 | 116 | 109 | 0.875 | arithmic mht proc qj2 varc vbad | array fand gau polyisomorphism | - |  |
| 245 | 130 | 121 | 0.887 | 1ht adic logm mht mπv varc | cns ofthe primestrip | - |  |
| 246 | 127 | 115 | 0.891 | 1πv flgp logm mht mπv subset | cns | - |  |
| 247 | 118 | 105 | 0.89 | 1fvq bun dle fvq ical let | - | - |  |
| 248 | 70 | 66 | 0.889 | bun con dle structed ρlgp ψflgp | bundle constructed | - |  |
| 249 | 92 | 86 | 0.854 | com flgp ified mutative real termined | array boxtimes commutative ofthe | - |  |
| 250 | 81 | 80 | 0.769 | 1fvq 1ht jfvq mht oαfvq pvq | 411efc1 array block doc image ofeach | - | ⚠ |
| 251 | 122 | 112 | 0.887 | 1fvq adic cap mutations per proposi | logvolume permutations | - |  |
| 252 | 124 | 120 | 0.952 | 1ht inz mht ory μlog | primestrips | - |  |
| 253 | 133 | 127 | 0.884 | 1fvq defini fmod prime strips tion | array cns definition loglinks primestrips | - |  |
| 254 | 135 | 133 | 0.928 | ical logm mht topolog vbad volumes | array bad logvolumes topological | - |  |
| 255 | 114 | 111 | 0.891 | frobe nioids prime rlgp strip varc | array frobenioids polyisomorphisms polypoly primestrip | - |  |
| 256 | 106 | 94 | 0.802 | corre dvq flgp labcusp mfv mfvq | array cns corresponding ofnumber rat | - | ⚠ |
| 257 | 114 | 114 | 0.916 | eraions iso mht mod ψcns | array isoinduced kumkum ofthe operaions | - |  |
| 258 | 92 | 76 | 0.75 | dvj environ jective lgp ments mht | array bad ofthe rat | - | ⚠ |
| 259 | 117 | 123 | 0.86 | belyi etale mmod q12 q22 qj2 | 411efc1 block doc image linkw nfbelyi | - |  |
| 260 | 146 | 136 | 0.843 | 0ht full indeter induces isomorphism kum | 411efc1 block doc etalelike page standard | - | ⚠ |
| 261 | 117 | 111 | 0.795 | 0qj2 assoc bdl bdls compare compatibility | 411efc1 block computationsubject corollary doc image | - | ⚠ |
| 262 | 136 | 127 | 0.892 | corre cyclo deg lattice lgp link | corresponding monotheta thetalattice | - |  |
| 263 | 154 | 148 | 0.936 | 2πi bcrys eqp liee lieeqp log | array crys | - |  |
| 264 | 184 | 156 | 0.818 | archimedean bcrys bga deg details dimf | crys dim discretised | - | ⚠ |
| 265 | 171 | 162 | 0.903 | 8lof deg fil0 inter log mell | array fil interuniversal suficiently | - |  |
| 266 | 210 | 203 | 0.921 | cies different indetermina lying qj2 qj2ok | dif diferent lobal structres suficiently | - |  |
| 267 | 153 | 146 | 0.846 | coefficients epr equipped gal homdom homopen | coeficients dom eequipped eis fundamenta hom | - | ⚠ |
| 268 | 150 | 134 | 0.844 | 2gx apic con conjugates deg degq | array connected efective sufices | - | ⚠ |
| 269 | 83 | 80 | 0.94 | 4mn c1xd maxs mins | array | - |  |
| 270 | 172 | 142 | 0.815 | 2a5 2tm algebraically aut automorphism bvv | bis | - | ⚠ |
| 271 | 144 | 143 | 0.926 | 2dt anan defined limx suffices xcore | array lim shimuraarithmetic sufices welldefined | - |  |
| 272 | 65 | 51 | 0.611 | 99k autcusp autε btemp defini dv0 | arc array bad definition ell good | - | ⚠ |
| 273 | 53 | 30 | 0.456 | 1ht 1φnf 1φθ 1φθell 1ψnf 1ψθ | array ell ellφell φ2十十 | - | ⚠ |
| 274 | 8 | 6 | 0.556 | full lgp poly | array | - | ⚠ |
| 275 | 109 | 109 | 0.946 | etale holomorpic θell | ell erminologies étale | - |  |
| 276 | 144 | 140 | 0.959 | 276 bπv ellnf etale θnf | étale | - |  |
| 277 | 131 | 132 | 0.963 | ellnf gau | csv μgau μlgp | - |  |
| 278 | 133 | 132 | 0.978 | etale torsθ | étale | - |  |
| 279 | 117 | 118 | 0.958 | cupsule etale | cupule d_y étale | - |  |
| 280 | 40 | 40 | 0.951 | verticial | vertical | - |  |
| 281 | 68 | 51 | 0.608 | 127 151 157 183 1fl 248 | birat const cov cusp hol temp | - | ⚠ |
| 282 | 65 | 24 | 0.328 | 107 116 117 119 122 123 | cyc rat | - | ⚠ |
| 283 | 62 | 15 | 0.185 | 102 106 116 118 122 123 | env lcft tpd | - | ⚠ |
| 284 | 74 | 34 | 0.35 | 126 127 133 135 144 147 | cov dom falt hom open sou | - | ⚠ |
| 285 | 67 | 37 | 0.465 | 127 151 157 164 176 196 | array dif isom out | - | ⚠ |
| 286 | 59 | 27 | 0.458 | 109 118 126 133 147 170 | - | - | ⚠ |
| 287 | 53 | 18 | 0.34 | 107 120 129 132 133 134 | - | - | ⚠ |
| 288 | 68 | 38 | 0.395 | 119 120 122 123 124 147 | centu mnθ πellx πmmθ πtempc πtempx | - | ⚠ |
| 289 | 59 | 18 | 0.242 | 166 177 178 189 198 199 | array ell gau | - | ⚠ |
| 290 | 76 | 45 | 0.512 | 131 145 180 183 210 211 | arc bad gau lgp | - | ⚠ |
| 291 | 41 | 18 | 0.439 | 144 166 172 189 227 arc | - | - | ⚠ |
| 292 | 299 | 294 | 0.964 | differential funda gal mental nodally prince | diferential internationa ofnodally | - |  |
| 293 | 272 | 271 | 0.96 | birth day faces mathema set tischen | birthday kyotou mathematischen settheoretic surfaces | - |  |
| 294 | 89 | 89 | 0.978 | affine | afine | - |  |