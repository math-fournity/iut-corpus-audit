# TIER-0 确定性比对 — Yamashita_2018-07-13_AProofOfABCafterMochizuki_405pp（PDF 文本层 vs MinerU 切片）

- 页数 405；FLAG（Jaccard<0.85 或元数据泄漏）151 页；元数据泄漏 0 页。
- 定位：免费侧信道，字符级可疑页标记；不替代视觉审计（结构/公式排版它看不见）。

| 页 | 层词 | md词 | Jaccard | 层有md无 | md有层无 | 元数据泄漏 | FLAG |
|---|---|---|---|---|---|---|---|
| 1 | 113 | 113 | 0.982 | plain | explain | - |  |
| 2 | 80 | 80 | 1.0 | - | - | - |  |
| 3 | 110 | 107 | 0.955 | dieck ellnf grothen θell | grothendieck | - |  |
| 4 | 202 | 198 | 0.932 | con der difficult dreds effortlessly frame | conjecture dificult efortlessly hundreds order | - |  |
| 5 | 137 | 132 | 0.881 | condd deg diffp1 diffx htop1 htωx | array diff finitel man onl summary | - |  |
| 6 | 162 | 151 | 0.909 | cuspidali cuspidalisa defini dia ellip environ | cuspidalisations subp | - |  |
| 7 | 164 | 156 | 0.916 | algo arakelov corol func lary proposi | arakelovtheoretic ballows band | - |  |
| 8 | 151 | 149 | 0.935 | cal canon ical mod rem theo | arakelovtheoretic array propert theorem | - |  |
| 9 | 143 | 134 | 0.834 | alg anab arith aut eval gen | block doc f0344f7 holomorphic image page | - | ⚠ |
| 10 | 185 | 180 | 0.921 | 1ivan 2in devel dimf inars offering | developments dim ivan ofering seminars | - |  |
| 11 | 103 | 100 | 0.933 | 14159 automorphisms homc hompro jfj | array polyautomorphisms | - |  |
| 12 | 109 | 104 | 0.919 | 71828 arc frobk gal isomc ordv | frob isom | - |  |
| 13 | 102 | 103 | 0.814 | aut gab ghg groupifica gtors hausdorfftopological | array block doc f0344f7 groupification hausdorf | - | ⚠ |
| 14 | 129 | 120 | 0.872 | acts aut gal hausdorfftopological isomorph log | bacts bisomorph bon hausdorf | - |  |
| 15 | 123 | 112 | 0.85 | 1of adivr arc cvv degf degk | array efective roups unafected | - |  |
| 16 | 101 | 91 | 0.829 | adiv degf different diffx effective func | dif diferent diff efective | - | ⚠ |
| 17 | 147 | 140 | 0.901 | adiv condd degf diffx effective gal | cond dif efective sufices | - |  |
| 18 | 139 | 129 | 0.823 | 1ol condd conde different differents diffx | array cond dif diferent diferents diff | - | ⚠ |
| 19 | 113 | 104 | 0.855 | computation deg diffp1 diffx diffy htωp1 | array diff sufices suficiently | - |  |
| 20 | 162 | 142 | 0.799 | 2deg 2pvi cer compact con conde | array certain compactness consist diff dificult | - | ⚠ |
| 21 | 91 | 82 | 0.802 | bok different dki epb expp ioki | array bac dae diferent offinite | - | ⚠ |
| 22 | 120 | 107 | 0.816 | algebra ately diff different dk0 dk2 | array dif diferent immediately sufices | - | ⚠ |
| 23 | 133 | 88 | 0.613 | 2μlog adic arithmetic bundle caf completes | array deg similarl simplicity | - | ⚠ |
| 24 | 110 | 64 | 0.568 | also automor can cannot differential dilation | array | - | ⚠ |
| 25 | 123 | 75 | 0.584 | 2ei 2pvq aipdi archimedean aut autf | array ical | - | ⚠ |
| 26 | 124 | 106 | 0.84 | autf dmod efmod eftpd fmod ftpd | isomorphic | - | ⚠ |
| 27 | 126 | 108 | 0.8 | 1ρefmod adiv adivr autf con defi | array definition diferent efective | - | ⚠ |
| 28 | 131 | 99 | 0.704 | 212 adiv adivr ages cients coeffi | array coeficients efective images | - | ⚠ |
| 29 | 135 | 109 | 0.768 | aut ball decom dkvi fmod ftpd | array bad decomposition | - | ⚠ |
| 30 | 84 | 66 | 0.705 | evj iv0 jkvj jokvi kvi kvj | array bad good logshell | - | ⚠ |
| 31 | 99 | 82 | 0.792 | 1bi aut ball fmod iii iv0 | array mod | - | ⚠ |
| 32 | 47 | 38 | 0.735 | 4μlog degfmod fmod kvi kvj modl | array mod | - | ⚠ |
| 33 | 48 | 41 | 0.745 | 4μlog equal fmod kvi log modl | array mod prm | - | ⚠ |
| 34 | 56 | 40 | 0.574 | 12dmod 20dmod 210 211 3ηprm cardinality | array cardinalit mod prm tpd | - | ⚠ |
| 35 | 27 | 24 | 0.545 | 12dmod 20dmod 240 2dmod dftpd dmod | 12d array hence mod prm tpd | - | ⚠ |
| 36 | 133 | 124 | 0.876 | arc arcωev aωe degf differentials hermi | array diferentials fal svalued | - |  |
| 37 | 107 | 94 | 0.844 | 2htfalt 2htωe adiv apic arc degf | array falt | - | ⚠ |
| 38 | 119 | 105 | 0.764 | 2htfalt 2htnon arithmetic coker composes conjugates | arithmeticgeometric arithmic array ates combinin con | - | ⚠ |
| 39 | 132 | 118 | 0.852 | 2htfalt degl effictive group htnon htωp1 | array efictive suficiently | - |  |
| 40 | 138 | 120 | 0.83 | 212 autf autq diffp1 efmod eftpd | bad diff furthermore | - | ⚠ |
| 41 | 45 | 42 | 0.891 | 2hvfv hvfv log ξprim | array | - |  |
| 42 | 59 | 53 | 0.836 | 2tk 3θa exck htnon htωp1 not | array prm | - | ⚠ |
| 43 | 103 | 94 | 0.876 | 2h2 acv ca1v exck gal gl2 | array sufices | - |  |
| 44 | 88 | 71 | 0.767 | 152 15d 200 20dmod 20ηprm 2bk | prm tpd | - | ⚠ |
| 45 | 126 | 121 | 0.83 | 2ck 5εe defi dftpd differ differents | array coverin dif difer diferents efect | - | ⚠ |
| 46 | 113 | 106 | 0.904 | ber diffp1 exck formity htωp1 hunif | unif uniformity | - |  |
| 47 | 83 | 67 | 0.765 | duces fpi frobki gab gal gk1 | frob induces | - | ⚠ |
| 48 | 92 | 89 | 0.775 | 0frobki frobki gab gki iki logp | array block doc f0344f7 frob grouptheoretically | - | ⚠ |
| 49 | 103 | 103 | 0.807 | com exgi frobki gab gigl gki | array block doc f0344f7 grouptheoretically image | - | ⚠ |
| 50 | 87 | 82 | 0.899 | dimql dimqp gab gal lim module | array dim | - |  |
| 51 | 129 | 126 | 0.889 | duction gal hom isomor ker part | array band bgenerated bis isomorphisms reduction | - |  |
| 52 | 76 | 73 | 0.961 | gal xfv zg2 | - | - |  |
| 53 | 126 | 116 | 0.847 | corre faithful gab gal gev ggev | bfor ehas indecomposable kummerfaithful suficiently | - | ⚠ |
| 54 | 76 | 78 | 0.949 | sufficiently | array con suficiently | - |  |
| 55 | 116 | 113 | 0.941 | any dimql giyg ker sufficiently | array suficiently | - |  |
| 56 | 99 | 99 | 0.886 | affine bzfrobk corre dimql frobk sponding | afine array bis corresponding frob grouptheoretically | - |  |
| 57 | 109 | 107 | 0.964 | consideration lnz nπx | econsideration | - |  |
| 58 | 154 | 149 | 0.906 | affine bzql cial cru cyc dimql | afine crucial dim dimq suficiently | - |  |
| 59 | 100 | 106 | 0.925 | χcyc | block doc f0344f7 kummerfaithful page standard | - |  |
| 60 | 118 | 121 | 0.897 | bolic gebraic hyper lock variety | array block doc f0344f7 page standard | - |  |
| 61 | 125 | 117 | 0.921 | cover different double gal inn isomgk | diferent | - |  |
| 62 | 107 | 104 | 0.884 | character difficult isation jects mulate sumption | array assumption dificult grouptheoretic objects | - |  |
| 63 | 151 | 145 | 0.91 | characterisa con cusp formations ghg hghg | characterisation convention informations results | - |  |
| 64 | 134 | 127 | 0.933 | ations damental delta fun gal iii | operations | - |  |
| 65 | 111 | 110 | 0.956 | gal sufficiently πux | array suficiently | - |  |
| 66 | 117 | 113 | 0.84 | core delta ell locg lock sufficiently | block doc f0344f7 image page standard | - | ⚠ |
| 67 | 99 | 92 | 0.891 | 1πx compactifica sufficiently tions πcore πcpt | compactifications suficiently | - |  |
| 68 | 96 | 97 | 0.838 | carte delta mark sian sufficiently up1 | block cartesian doc f0344f7 image page | - | ⚠ |
| 69 | 122 | 118 | 0.92 | cor gal responds sufficiently πtpd πux | corresponds suficiently tpd | - |  |
| 70 | 103 | 99 | 0.906 | cally composition gal sufficiently topologi yj1 | array suficiently topologically | - |  |
| 71 | 85 | 81 | 0.953 | deg dimk f1f2 gal | - | - |  |
| 72 | 102 | 96 | 0.85 | ation coefficient dimk effective ordx ordy1 | array coeficient efective respect valuation | - |  |
| 73 | 112 | 108 | 0.88 | are cent coefficients compact cusp ification | bare bnot brespectively coeficients compactification | - |  |
| 74 | 112 | 105 | 0.904 | com pactification propo quo sition therefere | btherefere compactification | - |  |
| 75 | 100 | 94 | 0.921 | supp times torsor μbz πcusp πj1 | array | - |  |
| 76 | 112 | 108 | 0.897 | homπx propo recon sition struction termined | bof bthe debtermined hom | - |  |
| 77 | 137 | 122 | 0.824 | 1so aut conj cover def funda | array brigidity con definition kummerfaithful | - | ⚠ |
| 78 | 75 | 72 | 0.885 | coefficient knf nnj suffices μbz πcusp | array coeficient sufices | - |  |
| 79 | 120 | 115 | 0.911 | decompo homo knf morphisms sition sxi | bif decomposition grouptheoretically | - |  |
| 80 | 98 | 89 | 0.781 | acterisations char constructed dxi ferred knf | bconstructed bcyclotomic breconstruction characterisations ofnon reb | - | ⚠ |
| 81 | 144 | 139 | 0.965 | gal knf zgk πxg πηx | - | - |  |
| 82 | 145 | 142 | 0.939 | coefficients hab ity lim ofmod μbz | array coeficients functoriality | - |  |
| 83 | 102 | 94 | 0.735 | con cup gab gal groups gur | array bby bcup btheoretically bwell bwith | - | ⚠ |
| 84 | 109 | 106 | 0.838 | corol gorithms gur itive ker lary | algorithms array blary btopological corolb notation | - | ⚠ |
| 85 | 141 | 135 | 0.878 | action arith arithmeti cally isomprofinite isomtopological | array bit interuniversal isom ofmono profinite | - |  |
| 86 | 149 | 152 | 0.858 | bzfrobk cohomo differential frobk ichm logical | bare blocal block blogical cohomob diferential | - |  |
| 87 | 155 | 155 | 0.962 | analyticisation out qpgc | interuniversal monoanalyticisation thetalattice | - |  |
| 88 | 89 | 90 | 0.904 | bzfrobk cific ity spe | frob g_k holomorphicity i_k interuniversal | - |  |
| 89 | 93 | 86 | 0.925 | authol respec tively top xtop ytop | - | - |  |
| 90 | 107 | 99 | 0.907 | abelianisa lim respec tion tively top | abelianisation | - |  |
| 91 | 126 | 115 | 0.799 | anal authol autrc caut fol group | analysis autholomorphic ofaut ofhomeomorphisms pgl psl | - | ⚠ |
| 92 | 123 | 110 | 0.879 | aut0 caut0 deter mined opp pgl2 | determined | - |  |
| 93 | 139 | 131 | 0.929 | axcore etop gal liptically top utop | elliptically | - |  |
| 94 | 120 | 115 | 0.865 | con differentiable ments ograms psl2 seg | converge diferentiable ifany ofpoints ofsequences ofu | - |  |
| 95 | 118 | 114 | 0.933 | etop philoso phy satisfies sufficiently xtop | philosophy suficiently | - |  |
| 96 | 87 | 82 | 0.92 | ax1 ax2 lim reconstruc tion μbz | autholomorphic | - |  |
| 97 | 112 | 108 | 0.88 | arith corol deter ichm lary log | arithholomorphic bstopiii corollary determines submonoid | - |  |
| 98 | 104 | 104 | 0.981 | metically | etalelike | - |  |
| 99 | 112 | 113 | 0.829 | anlyticisation arith base bundle con forget | block doc etalelike f0344f7 g_k grouptheoretically | - | ⚠ |
| 100 | 124 | 118 | 0.862 | func gebraic homo knf morphism ordx | algebraic homomorphism ofdecomposition ofnfpoints restriction valuations | - |  |
| 101 | 138 | 126 | 0.859 | authol coefficients cusp etop homeomor ical | array coeficients homeomorphisms valuations | - |  |
| 102 | 149 | 138 | 0.876 | algo ble bourhood compati etop homkv | algorithm array logvolume suficiently | - |  |
| 103 | 116 | 112 | 0.932 | 2pi lim logk oπx volume μbz | logshell logvolume | - |  |
| 104 | 111 | 105 | 0.912 | 2pg endo modules morphisms pmg rnon | endomorphisms rmodules | - |  |
| 105 | 111 | 108 | 0.921 | logk qpgc tween εef κok μlog | array between holomorphicisatio | - |  |
| 106 | 121 | 118 | 0.943 | differ expk limn struc tures | difer structures | - |  |
| 107 | 143 | 138 | 0.938 | com deter differentiable mines pact volumes | diferentiable logvolumes | - |  |
| 108 | 116 | 105 | 0.842 | analytic differentiable end identifica inte isomor | array diferentiable identification monoanalytic | - | ⚠ |
| 109 | 136 | 135 | 0.895 | expk prrad rarc sl2 xan μlog | block doc f0344f7 image page standard | - |  |
| 110 | 121 | 119 | 0.935 | btemp corresponds universal zπ2 πtemp | bcorresponds bif buniversal | - |  |
| 111 | 111 | 108 | 0.938 | btemp different momorphism temp πtemp | diferent homomorphism | - |  |
| 112 | 124 | 118 | 0.952 | gex gv1 gv2 gvi sv1 sv2 | - | - |  |
| 113 | 144 | 134 | 0.917 | bcov btemp cov ing mor phism | array | - |  |
| 114 | 103 | 97 | 0.905 | btemp curve gtemp htemp ker lim | cand logcurve | - |  |
| 115 | 122 | 119 | 0.944 | bolic bzς gtemp hyper πtemp | array hyperbolic | - |  |
| 116 | 165 | 159 | 0.952 | curve fol gtemp log lows temp | logcurve | - |  |
| 117 | 142 | 144 | 0.907 | evγ gtemp temp γtemp γλγ πtemp | bare bassociated bof ealso eare egroup | - |  |
| 118 | 92 | 89 | 0.926 | 1λγ defini fiber tion πtemp | definition efiber | - |  |
| 119 | 145 | 135 | 0.905 | ambigu conjugates homdense homdom inn ity | ambiguity terminal | - |  |
| 120 | 102 | 103 | 0.814 | assump corol ker lary ory suffices | bassume bcompact bis block doc f0344f7 | - | ⚠ |
| 121 | 133 | 125 | 0.911 | bicurve inde nπtemp recon reconstruc struct | bto grouptheoretically | - |  |
| 122 | 128 | 119 | 0.843 | ble cial comb hom hsing ified | array bfor bnon reconstruction stable viapos | - | ⚠ |
| 123 | 87 | 89 | 0.778 | action bzm bzμbz module modules tain | array bdivisible block bmodules btaking bus | - | ⚠ |
| 124 | 113 | 108 | 0.889 | gab gal genera gkμbz nal sec | bof final generator interuniversal | - |  |
| 125 | 87 | 92 | 0.904 | spf πtemp | block doc f0344f7 logrigid page standard | - |  |
| 126 | 85 | 86 | 0.859 | conju gate gkn natu ral πtemp | bbe block doc f0344f7 page standard | - |  |
| 127 | 141 | 135 | 0.957 | ell gjn gkn okn oyn πtemp | - | - |  |
| 128 | 91 | 87 | 0.935 | ker multiple ojn okn πtemp | array | - |  |
| 129 | 122 | 118 | 0.846 | bgm ell formal gal gjn ojn | array block brepresents doc f0344f7 page | - | ⚠ |
| 130 | 113 | 110 | 0.828 | ducible gal ing irre k2n ojn | array block doc f0344f7 image page | - | ⚠ |
| 131 | 104 | 104 | 0.825 | 2j2 differs k2n ojn okn pic | array block difers doc f0344f7 image | - | ⚠ |
| 132 | 90 | 85 | 0.862 | bgm compat difference homo ible lim | array btake diference homomorphism | - |  |
| 133 | 135 | 136 | 0.922 | bgm bωy difference square μ2l | bgives bis bobtained bof bsquare diference | - |  |
| 134 | 94 | 85 | 0.865 | 2πi bωy com e2πiτ exp eπiz | array complex | - |  |
| 135 | 106 | 107 | 0.868 | bωy over scribed sect set suffices | array bcanonical bis bover bscribed bset | - |  |
| 136 | 99 | 96 | 0.893 | 1eg fil0 fil1 fil2 log sect | bis eis ethe fil | - |  |
| 137 | 98 | 95 | 0.856 | 2bz dimension fied hom ity justi | array bcorresponds bdimension bthe justified rigidity | - |  |
| 138 | 142 | 139 | 0.873 | also evaluation indetermi insufficient mark nacy | balso bby bevaluation bthe insuficient natural | - |  |
| 139 | 143 | 137 | 0.892 | bgm conjugate ficient fil0 fil1 orem | array bof bon descriptions sufficient | - |  |
| 140 | 121 | 118 | 0.882 | finally hom ogm out prime sub | array bfinally bthe primeto subset sufices | - |  |
| 141 | 124 | 120 | 0.921 | ever gal grig how multiplication rig | however multiplicationby temp | - |  |
| 142 | 124 | 116 | 0.86 | composition duce duces ell garded isomor | array decomposition induce logorbicurve regarded | - |  |
| 143 | 118 | 113 | 0.941 | charac ell gal ker spect teristic | respect | - |  |
| 144 | 111 | 108 | 0.973 | gal ker ειx | - | - |  |
| 145 | 127 | 121 | 0.908 | ble curve ell gal sta sumptions | array assumptions logcurve | - |  |
| 146 | 99 | 92 | 0.891 | autk characteris ell out sect sumption | aut characteristic | - |  |
| 147 | 66 | 65 | 0.77 | con deg ext galois non structed | block constructed doc f0344f7 image page | - | ⚠ |
| 148 | 83 | 82 | 0.941 | multiple orbit πtemp | array temp | - |  |
| 149 | 95 | 95 | 0.939 | differs mutiple πtemp | array difers temp | - |  |
| 150 | 118 | 111 | 0.893 | autk belling cal culation dard mark | aut calculation 二dard | - |  |
| 151 | 101 | 97 | 0.922 | conjugacy ker orbit salg πtemp πμn | alg ofthe | - |  |
| 152 | 87 | 85 | 0.89 | berg heisen resp salg theoretically πtemp | alg array grouptheoretically heisenberg | - |  |
| 153 | 78 | 74 | 0.854 | 1asalg 1salg asalg aut bsalg salg | alg array automorphisms temp | - |  |
| 154 | 75 | 72 | 0.885 | conjugacy conjugate impor salg tant πtemp | important monotheta temp | - |  |
| 155 | 95 | 91 | 0.938 | 1tθ salg such that πtemp | outo | - |  |
| 156 | 117 | 106 | 0.874 | aut conjugacy fil0 fil1 gal hom | automorphism二induced 三is | - |  |
| 157 | 69 | 64 | 0.928 | etth ical topolog vironment πtemp | - | - |  |
| 158 | 123 | 110 | 0.864 | autμm autμn coker environ even homomor | environments homomorphism | - |  |
| 159 | 113 | 103 | 0.878 | algo autμn corol difference envi lary | diference ofany | - |  |
| 160 | 108 | 94 | 0.87 | collec cyclo envi environ isomor ment | - | - |  |
| 161 | 119 | 115 | 0.95 | environ hom ing ments shift | monotheta | - |  |
| 162 | 100 | 97 | 0.913 | alge braic lbz lim non torsor | algebraic bnon monotheta | - |  |
| 163 | 139 | 137 | 0.792 | affine aut coefficient func funda gal | afine bhence bis block bof bsubject | - | ⚠ |
| 164 | 115 | 117 | 0.917 | efmod fmod gal tors | block doc f0344f7 page standard tier | - |  |
| 165 | 118 | 113 | 0.925 | 2l2 2lz autk ker set vbad | bad good | - |  |
| 166 | 102 | 100 | 0.942 | degfr homd homfφ mulated | hom interuniversal | - |  |
| 167 | 103 | 95 | 0.886 | autc degfr div divb endc frobe | aut end | - |  |
| 168 | 105 | 107 | 0.843 | alences degfr divb equiv homc homd | array block doc f0344f7 hom image | - | ⚠ |
| 169 | 125 | 113 | 0.763 | ample any aut birationalisa cbirat com | abstract array birat complicated equivariantisomorphism example | - | ⚠ |
| 170 | 119 | 116 | 0.911 | age auto effective gal morphism struc | bfrobenioid efective image ummer | - |  |
| 171 | 124 | 113 | 0.911 | frobe gkv ker mon nioids orbits | - | - |  |
| 172 | 110 | 100 | 0.875 | btemp defini div effective gkv mero | efective temp | - |  |
| 173 | 122 | 113 | 0.895 | bconst dell ker lim mon ramified | const unramified | - |  |
| 174 | 102 | 92 | 0.865 | aut bconst deter fbase logφ mine | basefield determine | - |  |
| 175 | 127 | 120 | 0.945 | adv ample base degfr log okv | - | - |  |
| 176 | 89 | 83 | 0.87 | adv ample effective fmod mor phism | efective morphism transporting | - |  |
| 177 | 94 | 83 | 0.825 | abirat bira different lln log obirat | birationalisation diferent invertible | - | ⚠ |
| 178 | 67 | 64 | 0.819 | autdv autfv difference lln lμln striv | array aut diference temp triv | - | ⚠ |
| 179 | 110 | 98 | 0.825 | autdv autfv autθ birat coefficient conjugate | aut coeficient diference temp | - | ⚠ |
| 180 | 127 | 120 | 0.93 | algo autfv lln out rithms vironment | interuniversal | - |  |
| 181 | 105 | 103 | 0.891 | affine cfmod core efmod fmod hom | afine array bto mod pseudomonoid | - |  |
| 182 | 118 | 108 | 0.915 | cfmod cyclo def fmod isomor phism | - | - |  |
| 183 | 117 | 111 | 0.932 | rem theo μbz πck πcv πxk | bwhich | - |  |
| 184 | 98 | 94 | 0.959 | cfmod loc vmod πcfmod | - | - |  |
| 185 | 125 | 116 | 0.928 | cfmod coricity fmod frobe gal nioid | - | - |  |
| 186 | 116 | 107 | 0.922 | aut bp0 fmod lim oa0 obirat | - | - |  |
| 187 | 124 | 118 | 0.891 | btemp con lim open qpv rem | bfollows continuous supset theorem | - |  |
| 188 | 93 | 89 | 0.896 | fmod loc mκv recon struct vmod | 2with temp vby | - |  |
| 189 | 123 | 115 | 0.889 | con cussions dis lim mκv open | btorsor disbcussions theorem | - |  |
| 190 | 109 | 101 | 0.892 | defini drat fmod gal homco lim | hom rat | - |  |
| 191 | 131 | 121 | 0.909 | aut coric disjoint drat fmod logical | rat | - |  |
| 192 | 87 | 84 | 0.839 | applied differences induced priori relation short | array diferences inducedby inshort norrelation étale | - | ⚠ |
| 193 | 121 | 118 | 0.882 | affect effect func log tions vbad | afect ban brealified efect logvolumes monotheta | - |  |
| 194 | 145 | 140 | 0.9 | conjugacy difference different ichm ing lim | bcompatible being cfield diference diferent | - |  |
| 195 | 114 | 107 | 0.922 | arc fmod gal mod ofmod orbit | array | - |  |
| 196 | 82 | 71 | 0.843 | birat bun dles fmod gal mor | structure | - | ⚠ |
| 197 | 112 | 104 | 0.895 | approxima ditive ellnf gal mod over | involved moreover | - |  |
| 198 | 49 | 43 | 0.804 | cos e2πi ell ellnf fmod qj2 | bor mod | - | ⚠ |
| 199 | 69 | 58 | 0.764 | btemp ell ellnf fol iso lows | follows isomorphic primestrips | - | ⚠ |
| 200 | 65 | 54 | 0.803 | adv arithmetic ellnf geometric mod varc | array | - | ⚠ |
| 201 | 73 | 66 | 0.853 | 99k bijec ell mod tion θell | bijection primestrip | - |  |
| 202 | 89 | 79 | 0.732 | arithmetic bridge ell ellnf fmod gal | bad block doc f0344f7 image page | - | ⚠ |
| 203 | 129 | 112 | 0.868 | arc ell fmod gl2 good mod | - | - |  |
| 204 | 122 | 113 | 0.911 | ator btemp differs gener mod spl | difers | - |  |
| 205 | 68 | 63 | 0.795 | adv btemp frobe nioid not varc | arc bad good non primestrips | - | ⚠ |
| 206 | 99 | 87 | 0.824 | deter fmod func logpv logφ mark | array functions remark | - | ⚠ |
| 207 | 80 | 69 | 0.84 | ample fbirat oaθ obirat orbit oxv | birat | - | ⚠ |
| 208 | 69 | 64 | 0.873 | addi cθr splθ tively varc vmod | additively array | - |  |
| 209 | 67 | 62 | 0.843 | fmod homo log logφ morphisms termined | array bad good | - | ⚠ |
| 210 | 76 | 71 | 0.729 | dv_ evf except fmod indet logd | arc block doc f0344f7 image non | - | ⚠ |
| 211 | 79 | 75 | 0.901 | atre defini ists tion varc vnon | exists fullpoly | - |  |
| 212 | 80 | 79 | 0.963 | vbad vgood | polyisomorphism | - |  |
| 213 | 72 | 69 | 0.88 | defi inter nition not universal vnon | array interuniversal primestrip | - |  |
| 214 | 112 | 99 | 0.819 | autd autf calcu iso isomd isomf | calculating frobenioidprime isom primestrip | - | ⚠ |
| 215 | 57 | 58 | 0.769 | 1ht 2ht isomd isomf resp vbad | block doc f0344f7 image page primestrip | - | ⚠ |
| 216 | 148 | 143 | 0.927 | aut holomorphis suffices tau tologically varc | autholomorphis sufices tautologically | - |  |
| 217 | 70 | 71 | 0.785 | 2f_ arc back mor phism pull | array block doc f0344f7 image page | - | ⚠ |
| 218 | 88 | 80 | 0.867 | aut def inition spl tained varc | obtained ummer | - |  |
| 219 | 79 | 78 | 0.892 | div ductive mod vnon μnm | array primestrip primestrips ummer | - |  |
| 220 | 100 | 90 | 0.81 | adic autf automor isomf mod phisms | automorphisms isom lit portion quotient | - | ⚠ |
| 221 | 99 | 89 | 0.861 | core cuspi dal def inition logical | cuspidal topological | - |  |
| 222 | 113 | 105 | 0.896 | aut data gal gl2 holomorphic prime | autholomorphic dprime | - |  |
| 223 | 91 | 81 | 0.83 | autε fmod gal gfmod gl2 sl2 | bor mod writev | - | ⚠ |
| 224 | 103 | 98 | 0.896 | aut autε dvj grig okv vbad | array polyaction suchthat | - |  |
| 225 | 113 | 107 | 0.913 | btemp covering dvj labcusp map vgood | array temp | - |  |
| 226 | 74 | 68 | 0.868 | autε cup iso isomor morphisms phism | polycapsule polyfull | - |  |
| 227 | 85 | 75 | 0.86 | dvj dwj homomor phisms proposi tion | lab | - |  |
| 228 | 89 | 84 | 0.944 | dvj labcusp out torsor φnf | - | - |  |
| 229 | 119 | 94 | 0.69 | arith autε base begin constructed constructing | arithmetically block doc f0344f7 page standard | - | ⚠ |
| 230 | 118 | 111 | 0.893 | adic defini labcusp mod tion tomorphisms | array polymorphisms primestrips | - |  |
| 231 | 57 | 61 | 0.844 | fvj mod ψnf | block doc f0344f7 image page standard | - | ⚠ |
| 232 | 52 | 57 | 0.817 | vmod φnf ψnf | array block doc f0344f7 image page | - | ⚠ |
| 233 | 83 | 81 | 0.907 | cate conjugates fvj gory varc | array polymorphism toloc | - |  |
| 234 | 70 | 61 | 0.795 | 1dj1 1fj1 1ψnf 2dj2 2fj2 2ψnf | array equivalent polypoly | - | ⚠ |
| 235 | 79 | 67 | 0.802 | 1fj1 1ht 1ψθ 2fj2 2ht 2ψθ | array notation | - | ⚠ |
| 236 | 84 | 66 | 0.744 | 1ht 1φnf 1φθ 1ψnf 1ψθ 2ht | array respectively | - | ⚠ |
| 237 | 108 | 101 | 0.9 | action core cuspi dal more varc | cuspidal moreover | - |  |
| 238 | 70 | 70 | 0.972 | autα | array | - |  |
| 239 | 107 | 102 | 0.917 | autcusp autk gl2 recon sl2 struct | polyisomorphism reconstruct | - |  |
| 240 | 106 | 106 | 0.843 | agonal autcusp autk differences fmod labcusp | block diagonal diferences doc f0344f7 image | - | ⚠ |
| 241 | 126 | 117 | 0.913 | 1fl bridge defi defini dvt fmod | polyautomorphism | - |  |
| 242 | 80 | 72 | 0.831 | autcusp dv0 isomor labcusp phism varc | cusp ell polyaction | - | ⚠ |
| 243 | 72 | 70 | 0.945 | autcusp θell φθell | pol | - |  |
| 244 | 54 | 48 | 0.855 | dvt dwt group ζθell θell ξθell | ell | - |  |
| 245 | 82 | 76 | 0.837 | 1fl autcusp automorphism bridge groups isomf | cusp ell ofthe polyautomorphism | - | ⚠ |
| 246 | 91 | 73 | 0.745 | arith defini deifi diagram etale metically | arithmetically deifinition polypoly | - | ⚠ |
| 247 | 88 | 71 | 0.767 | 1ht 1φθ 1φθell 1ψθ 1ψθell 2ht | corresponding polypoly | - | ⚠ |
| 248 | 87 | 86 | 0.944 | ellnf vbad vgood | array ell | - |  |
| 249 | 97 | 98 | 0.822 | 99k defi ellnf func nition proposi | block determined doc f0344f7 grouptheoretic image | - | ⚠ |
| 250 | 111 | 108 | 0.921 | cate gories isomor phic sur vey | array categories survey | - |  |
| 251 | 97 | 97 | 0.865 | isomor phism qj2 ues val zvvvvvvvvvv | block doc f0344f7 image page standard | - |  |
| 252 | 98 | 104 | 0.888 | difference gl2 next | array block diference doc f0344f7 image | - |  |
| 253 | 90 | 83 | 0.802 | cally constructed corol described dmθ gl2 | array corollary describedin determined indeterminacies tautologically | - | ⚠ |
| 254 | 68 | 64 | 0.671 | ccggggggggg corol ffnnnnnnnnnnn iissssssssssssssssssss kkvvvvvvvvvvvvvvvvvvvvvvvv lary | block corollary doc f0344f7 image obtain | - | ⚠ |
| 255 | 94 | 89 | 0.867 | constructed iso logical mod morphism step | bafter bules grouptheoretically modb | - |  |
| 256 | 73 | 77 | 0.765 | environ fined ments ternal yssssssssss μbz | array block btheoretically bto chart doc | - | ⚠ |
| 257 | 120 | 123 | 0.869 | cies effects gl2 indetermina obit rlcft | bas block doc efects f0344f7 image | - |  |
| 258 | 86 | 75 | 0.809 | elcft ical isomor ker lim open | breconstructed grouptheoretically ofcyclotomic | - | ⚠ |
| 259 | 105 | 93 | 0.737 | aut constructed elcft gal grig let | block bwhich doc f0344f7 image morphisms | - | ⚠ |
| 260 | 97 | 87 | 0.786 | composi corol dard defini gal lary | array composition corollary env projective standard | - | ⚠ |
| 261 | 105 | 97 | 0.888 | ators con isomor lim mod phism | constant env | - |  |
| 262 | 79 | 77 | 0.88 | lim striction subsets θenv μbz πtemp | array env restriction temp | - |  |
| 263 | 104 | 95 | 0.843 | eenv evalenv func graph logical subset | array env functions topological | - | ⚠ |
| 264 | 101 | 97 | 0.922 | con ing remov sec tains tion | array removing | - |  |
| 265 | 79 | 78 | 0.892 | bπv determine labcusp πcor πtemp | array bdetermine bis bresp | - |  |
| 266 | 92 | 84 | 0.814 | are btemp bπcor bπv conjugacy corol | array bare bdefinition lab temp | - | ⚠ |
| 267 | 91 | 81 | 0.849 | bitrary bπcor conjuga cor corre def | array bnon | - | ⚠ |
| 268 | 77 | 70 | 0.909 | bπv defini iγγ lim tion μ2l | - | - |  |
| 269 | 92 | 87 | 0.865 | ative ing iγ1 mysteri ous rel | array mysterious ofproposition resulting | - |  |
| 270 | 139 | 138 | 0.91 | chronising coefficient conjec cor syn ture | bin bindeterminacies bthe coeficient conjecture synchronising | - |  |
| 271 | 109 | 102 | 0.918 | dmθ environ lim ments minj μbz | environments | - |  |
| 272 | 79 | 71 | 0.829 | bπv consider further iγγ labcusp lim | array bconsider bfurther | - | ⚠ |
| 273 | 98 | 93 | 0.837 | bπv environ iγ1 lim ments open | array bby bin bobtain environments groupbtheoretically | - | ⚠ |
| 274 | 82 | 74 | 0.835 | jects labcusp lim mark open struc | array objects temp | - | ⚠ |
| 275 | 110 | 102 | 0.828 | autdv env exam ity obirat ple | birat bwe cns rational simplicity temp | - | ⚠ |
| 276 | 108 | 96 | 0.838 | actions aut base clotome field lim | array cns kumbmer | - | ⚠ |
| 277 | 74 | 71 | 0.859 | base col field lections mod πtemp | array collections env temp | - |  |
| 278 | 88 | 86 | 0.851 | dially labcusp let multira μbz πtemp | array bautomorphisms bto cns multiradially temp | - |  |
| 279 | 92 | 90 | 0.857 | cardinality indetermi iso labcusp nacy πtemp | array cns gau indeterminacy mmetrisin ofcardinality | - |  |
| 280 | 96 | 91 | 0.851 | mod more over pose sup uation | array gau moreover suppose temp | - |  |
| 281 | 79 | 74 | 0.821 | labcusp mer tween πfξ πtemp ψcns | array between cns gau temp | - | ⚠ |
| 282 | 144 | 137 | 0.925 | defini isomor mark phism qj2 sulting | definition resulting | - |  |
| 283 | 81 | 80 | 0.872 | mod splittings torsion μbz ψfξ ψgau | array bautomorphisms bto gau withsplittingsuptotorsion | - |  |
| 284 | 84 | 73 | 0.784 | constructed func gal lim theoretically torial | array cns functorial grouptheoretically | - | ⚠ |
| 285 | 74 | 64 | 0.84 | cor func gal labcusp logd loggv | functorial | - | ⚠ |
| 286 | 66 | 59 | 0.761 | con defini isomor loguv logπv phisms | array construct env gau oflabcusp | - | ⚠ |
| 287 | 99 | 90 | 0.817 | btemp cns exam loguv logπv mod | array env evaleval example gau | - | ⚠ |
| 288 | 62 | 61 | 0.864 | 71828 logd loggv ψcns ψss | array log ofthe polyisomorphism | - |  |
| 289 | 112 | 101 | 0.868 | cor gal iso labcusp morphism outer | env gau | - |  |
| 290 | 88 | 83 | 0.819 | btemp defini mod tion varc vbad | arc array bad ell good non | - | ⚠ |
| 291 | 90 | 80 | 0.848 | isomor log mod phisms tablished version | ell established | - | ⚠ |
| 292 | 59 | 52 | 0.734 | algo log propo resp rithm sition | arc array bad good non | - | ⚠ |
| 293 | 83 | 79 | 0.8 | conjugacy group iso morphism varc vbad | arc array cns ell grouptheoretic isomorphism | - | ⚠ |
| 294 | 96 | 88 | 0.897 | conjugacy isomor phism varc vbad vgood | array | - |  |
| 295 | 86 | 83 | 0.817 | 99k labcusp varc vgood vnon θell | arc array cns env gau non | - | ⚠ |
| 296 | 83 | 77 | 0.905 | corol lary φnf ψenv ψfenv ψfgau | array | - |  |
| 297 | 72 | 67 | 0.904 | action algo labcusp poly rithm πrat | polyaction | - |  |
| 298 | 86 | 79 | 0.833 | action com defini dvj isomor labcusp | array compatbile rat rime | - | ⚠ |
| 299 | 113 | 105 | 0.896 | 99k cyc determinacies isomor l99 nf1 | bwe rat | - |  |
| 300 | 75 | 66 | 0.808 | 99k isomor labcusp localisa phisms propo | localisation proposition rat | - | ⚠ |
| 301 | 96 | 90 | 0.879 | bijec corol diag labcusp lary mod | array cns respectively | - |  |
| 302 | 78 | 69 | 0.793 | cenv cgau derlying eval iso isomf | array isom isomorgl underlying | - | ⚠ |
| 303 | 68 | 67 | 0.929 | atres qj2 vbad | primestrips theatres | - |  |
| 304 | 95 | 63 | 0.646 | action also constructions diagram enhanced frobenius | naturally | - | ⚠ |
| 305 | 88 | 85 | 0.901 | 2pv adic logv mark vnon ψlog | array primestrip remark | - |  |
| 306 | 101 | 92 | 0.856 | asso ciated defini exp logv recon | arc array reconstructible | - |  |
| 307 | 84 | 81 | 0.897 | differ struc tures vnon ψgp ψμn | array difer structures | - |  |
| 308 | 83 | 80 | 0.895 | associ ated lognon unaffected varc vnon | frobeniuslike non unafected | - |  |
| 309 | 90 | 81 | 0.8 | adic dia expk gram logarc lognon | arc array cns logvolumes ofd | - | ⚠ |
| 310 | 74 | 71 | 0.883 | action cns propo sition ψcns ψss | array logvolume logvolumes | - |  |
| 311 | 67 | 64 | 0.871 | let logarc lognon shell ψcns ψss | array logshell primestrip | - |  |
| 312 | 63 | 61 | 0.851 | kum proposi thhhhhhhhhhhhhhhhhhhhhhh tion wooooooooooo ψcns | array cns polypoly primestrips | - |  |
| 313 | 88 | 86 | 0.891 | atres consid corol ered lary nht | array considered corollary logloglog | - |  |
| 314 | 67 | 63 | 0.733 | 1ht collec dia full gau gram | block collection doc f0344f7 image page | - | ⚠ |
| 315 | 91 | 84 | 0.842 | 1ht cns diag duce isomor mht | bad isomordiag ofcorollary respectively | - | ⚠ |
| 316 | 86 | 81 | 0.815 | com deter iso mines morphisms posing | composing determines polyisomorphisms polymorphisms rime structures | - | ⚠ |
| 317 | 85 | 78 | 0.874 | corol isomor lary mρd notation phism | array ofnotation | - |  |
| 318 | 81 | 78 | 0.893 | bijec mht theorem tion ψenv ψfenv | array bijection induckum | - |  |
| 319 | 111 | 106 | 0.855 | autf com fenv mutative respec tively | array aut fullpoly polyisomorphism respectively temp | - |  |
| 320 | 83 | 73 | 0.814 | autf cns iso labelled mht mor | array aut zerolabelled | - | ⚠ |
| 321 | 64 | 61 | 0.953 | mht morc rbad | - | - |  |
| 322 | 80 | 80 | 0.839 | com corol gau lary link morr | array bad comfull corollary kuminduced polyfull | - | ⚠ |
| 323 | 111 | 97 | 0.809 | differences env follow gau holo ing | array bthe diferences following | - | ⚠ |
| 324 | 129 | 125 | 0.868 | com const cor corre differences ogy | amp byconst corresponds diferences o_v topolbogy | - |  |
| 325 | 144 | 141 | 0.926 | clotomic differ func iord proach tion | approach array difer ord | - |  |
| 326 | 137 | 133 | 0.849 | difficult difficulty ible incompat iord jects | array bis dificult dificulty incompatible ord | - | ⚠ |
| 327 | 69 | 73 | 0.844 | difficulty eye ψgau ψlgp | block dificulty doc f0344f7 image page | - | ⚠ |
| 328 | 119 | 115 | 0.934 | arith coefficient cond diff log metically | array coeficient | - |  |
| 329 | 76 | 67 | 0.857 | capsules fvq lim log open qvq | subcapsules | - |  |
| 330 | 105 | 93 | 0.868 | 1fvq fmod fvq induc lim okv | mod | - |  |
| 331 | 76 | 66 | 0.821 | 1fvq affects fmod kvi proposi pvq | afects mod | - | ⚠ |
| 332 | 75 | 72 | 0.909 | fvq varc vnon αfv αfvq | logshells tautopoly | - |  |
| 333 | 75 | 70 | 0.908 | fvq respec tauto tively αfv αfvq | array | - |  |
| 334 | 110 | 96 | 0.839 | 1fvq ber homomor isation module momorphism | respect submodule | - | ⚠ |
| 335 | 111 | 107 | 0.847 | algorithm proc varc vbad vnon αfv | array gau lgp ofan ofcorollary ofthe | - | ⚠ |
| 336 | 108 | 100 | 0.857 | cally mht multiplica qj2 tively varc | fand fpart frobeniuslike ofmonoids | - |  |
| 337 | 114 | 109 | 0.828 | 1ht compatibil ity logm mht mπv | block cns doc f0344f7 image page | - | ⚠ |
| 338 | 108 | 96 | 0.855 | adic flgp follow ing logm mht | cns following | - |  |
| 339 | 112 | 101 | 0.821 | 1fvq 1πv adic defi flgp logm | cns definition lgp loglinks tautological | - | ⚠ |
| 340 | 112 | 100 | 0.843 | 1fvq construc fication fvq gaus ject | llr object ofit | - | ⚠ |
| 341 | 58 | 57 | 0.917 | link ρlgp ψflgp | array frobeniuslike | - |  |
| 342 | 79 | 74 | 0.866 | algorithm flgp gard mod vbad μ2l | array orithm regard | - |  |
| 343 | 71 | 65 | 0.722 | 1fvq 1ht adic jfvq mht propo | block doc f0344f7 image page relative | - | ⚠ |
| 344 | 106 | 95 | 0.811 | 1fvq adic col lections mand oαfvq | collections logvolumes packetnormalised primestrip summand | - | ⚠ |
| 345 | 92 | 85 | 0.863 | 1fvq 1ht atres full mht normali | array normalisation theatres | - |  |
| 346 | 105 | 104 | 0.935 | 1ht com mht patibility | compatibility fprime loglinks | - |  |
| 347 | 77 | 66 | 0.787 | 1fvq consider fmod groups identify isomor | array cns mathfrak | - | ⚠ |
| 348 | 121 | 115 | 0.903 | equal isomor ity logm phisms prime | array equality thetalattice | - |  |
| 349 | 97 | 96 | 0.949 | mht vbad volumes | bad logvolumes | - |  |
| 350 | 85 | 85 | 0.932 | rlgp varc vnon | array lgp ofthe | - |  |
| 351 | 82 | 72 | 0.77 | duced dvq fer flgp here labcusp | array between cns induced rat | - | ⚠ |
| 352 | 101 | 96 | 0.841 | addi alified determinacies flgp mht note | addition array loglinks mathfrak mutually ofthe | - | ⚠ |
| 353 | 80 | 73 | 0.821 | com lgp link mht patible rem | array bad compatible ofthe | - | ⚠ |
| 354 | 73 | 66 | 0.805 | dvj kum lgp mer mht nally | array polyisomorphism proposition rat | - | ⚠ |
| 355 | 60 | 63 | 0.836 | lgp q12 q22 qj2 | block doc f0344f7 image page standard | - | ⚠ |
| 356 | 98 | 98 | 0.903 | belyi corol etale lary mmod | linkw nfbelyi o_v x27 étale | - |  |
| 357 | 124 | 117 | 0.799 | 0ht corre dial full induces isomorphism | block correspondence doc f0344f7 image monoanalytic | - | ⚠ |
| 358 | 96 | 95 | 0.802 | 0qj2 compare compatibility corr detach etale | array block doc f0344f7 image mod | - | ⚠ |
| 359 | 85 | 84 | 0.943 | deg qj2 subject | computationsubject μlgp | - |  |
| 360 | 121 | 121 | 0.952 | ing maintain mark | maintaining monotheta npower | - |  |
| 361 | 116 | 114 | 0.949 | 2πi bcrys log tpgm | array crys | - |  |
| 362 | 126 | 115 | 0.868 | bcrys bga cohomol deg eqp liee | bnow crys lie | - |  |
| 363 | 146 | 130 | 0.852 | 8lof deg determi dimf fil less | array determinant dim | - |  |
| 364 | 149 | 142 | 0.914 | 2πi deg fil0 log multiplica qj2ok | array fil suficiently | - |  |
| 365 | 170 | 164 | 0.92 | cal con culate different grees qj2 | construct dif diferent reconstruct | - |  |
| 366 | 134 | 129 | 0.92 | funda gal homdom homopen isomk isomout | dom hom padic | - |  |
| 367 | 124 | 110 | 0.814 | apic bounded coefficients degq degqx epr | coeficients ebounded eequipped eis sufices | - | ⚠ |
| 368 | 112 | 106 | 0.912 | 2gx effective gal htopm maxf old | array efective | - |  |
| 369 | 65 | 63 | 0.939 | c1xd maxs mins | array | - |  |
| 370 | 88 | 85 | 0.944 | 2a5 2tm 4mn isomk | array | - |  |
| 371 | 153 | 150 | 0.93 | aut bvv cpsl2 degree lock psl2 | array bis bproposition ree | - |  |
| 372 | 108 | 105 | 0.919 | alence equiv fices limx suf xcore | array lim sufices | - |  |
| 373 | 94 | 91 | 0.869 | anan btemp not suffices varc vbad | arc bad good non sufices | - |  |
| 374 | 39 | 25 | 0.455 | 99k autcusp autε btemp dv0 dvj | array bad ell good temp | - | ⚠ |
| 375 | 43 | 21 | 0.455 | 1ht 1φnf 1φθ 1φθell 1ψnf 1ψθ | array | - | ⚠ |
| 376 | 14 | 15 | 0.933 | - | μlgp | - |  |
| 377 | 79 | 69 | 0.827 | 226 232 234 235 243 246 | efective ell | - | ⚠ |
| 378 | 87 | 88 | 0.966 | bπv | b83 txt | - |  |
| 379 | 122 | 123 | 0.96 | etale θnf | csv onf étale | - |  |
| 380 | 93 | 92 | 0.989 | ellnf | - | - |  |
| 381 | 88 | 89 | 0.924 | etale gau torsθ | csv étale μgau μlgp | - |  |
| 382 | 100 | 100 | 1.0 | - | - | - |  |
| 383 | 71 | 71 | 0.972 | etale | étale | - |  |
| 384 | 105 | 104 | 0.917 | cupsule etale teichm uller μ2l | cupule d_y teichmüller étale | - |  |
| 385 | 44 | 44 | 1.0 | - | - | - |  |
| 386 | 0 | 0 | 1.0 | - | - | - |  |
| 387 | 46 | 16 | 0.216 | 103 106 110 112 113 155 | birat cov cusp hol temp | - | ⚠ |
| 388 | 66 | 63 | 0.72 | bconst btemp cbirat cenv cgau degf | birat c_f c_g c_k const cyc | - | ⚠ |
| 389 | 47 | 49 | 0.92 | drat | rat x_f y_n | - |  |
| 390 | 58 | 10 | 0.097 | 106 123 124 128 132 141 | base env lcft tpd | - | ⚠ |
| 391 | 47 | 31 | 0.66 | 206 211 229 230 232 248 | - | - | ⚠ |
| 392 | 72 | 26 | 0.342 | 178 186 189 202 211 242 | hom | - | ⚠ |
| 393 | 56 | 43 | 0.737 | 1fvq 317 fvq iord isomd isomf | isom | - | ⚠ |
| 394 | 63 | 44 | 0.646 | 179 184 237 238 256 bπv | dif loc | - | ⚠ |
| 395 | 42 | 16 | 0.381 | 104 108 151 167 170 181 | - | - | ⚠ |
| 396 | 50 | 19 | 0.278 | 106 110 167 168 169 176 | ang env rad rat | - | ⚠ |
| 397 | 53 | 45 | 0.75 | πcf πcor πcusp πmθ πp0 πtemp | cor cusp temp | - | ⚠ |
| 398 | 60 | 10 | 0.094 | 167 169 171 173 174 184 | birat const ell lcft | - | ⚠ |
| 399 | 65 | 13 | 0.13 | 108 143 174 210 250 251 | arc bad gau lcft | - | ⚠ |
| 400 | 61 | 35 | 0.574 | 104 131 177 211 214 274 | - | - | ⚠ |
| 401 | 53 | 57 | 0.719 | comb mod mult new vdist ζθell | vbadmod vcomb vdistmod vdistq vgoodmod vmult | - | ⚠ |
| 402 | 3 | 3 | 1.0 | - | - | - |  |
| 403 | 241 | 239 | 0.975 | differential gal mem oirs | diferential memoirs | - |  |
| 404 | 196 | 191 | 0.925 | arith bolic bridge cam gebraic hyper | advanced algebraic arithmetic cambridge symposia | - |  |
| 405 | 239 | 233 | 0.934 | able affine aters avail est eties | afine gruppen papersenglish theaters varieties | - |  |