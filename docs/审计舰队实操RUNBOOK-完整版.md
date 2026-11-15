# ABC 审计舰队实操 RUNBOOK（完整版）——50 波实战浓缩

> **给谁读**：在 ABC repo 里接手「语料逐页视觉审计」类任务的 AI。本文是 2026-11-11 至
> 2026-11-15 共 50 波舰队 + 10 个裁决批 + 2 次质量抽检的完整操作知识，含全部提示词、
> 参数、异常处置与「否掉的路」。目标：你不用再试错，一次性把事情做对。
> **配套**：波间八步与异常矩阵的简洁版在 RUNBOOK.md（AI 工作目录
> shuxuedashi-glm5.2-worktree/dev-docs/abc-audit/）；本文是 ABC 自包含完整版，两者冲突以本文为准。
> 版本：v1（2026-11-15，第 50 波在飞时写）。

## 〇、五条总原则（先背下来再动手）

1. **Master 无视觉**：主对话模型（GLM-5.3）看不见图。一切"看"的环节只能经 workflow 里的
   视觉子代理（GLM-5.3-Flash$max）完成。你自己"读"PDF/图像的一切尝试都是假装看过。
2. **真值只认机器读数**：覆盖与 verdict 的真值 = `audit_harvest.sh`/`STATUS.json`，不看任何
   模型自述"我做完了"。
3. **每页自包含**：一页=一行矩阵行；看不清标「需600dpi回图」，**绝不许猜**。
4. **质量优先于速度**：波间闸门一道都不能省。宁可停发下一波，不可带病推进。
5. **限流=停手等用户**：任何 run 报 1308/1310/1005 → 不 Resume、不 Amend、不重建、不发新波，
   报一句（run 名/报错/重置时间）等用户。平台自动续跑不干预。

## 一、任务形态

- 分母：68 份 PDF 共 3105 页（`corpus/INDEX.md` 登记；改分母必须停下问用户）。
- 每页产出**一行** 10 列矩阵行：`| 页 | Y | 结构 | 文字 | 公式 | 题注 | 图表 | 语义 | 判定 | 备注 |`；
  六维度只允许 ✓/⚠/✗；判定四态 PASS/WARN/FAIL/UNRESOLVED。
- 判定校准锚：**改变记号含义的字符级错误，或同类字符错误≥3 处（按页计）→ 该维度 ✗**；
  仅排版/空格/断行 → ⚠。示例行仅示意格式，不代表判定尺度。
- 备注禁裸竖线 `|`（数学竖线写 `\mid` 或 `∣`，否则行被切成 11+ 列）。
- 瑕疵码：F1 丢行/丢脚注、F2 字符误读、F3 格式错排、F4 空胞、F5 其他。
- 图表口径（2026-11-15 立）：整图变 `![Image block]` 占位符=✗（内容级缺失）；部分残缺=⚠。

## 二、生产环境与资产

| 层 | 位置 | 说明 |
|---|---|---|
| PDF 语料 | `corpus/<author>/<name>.pdf` | 34M/68 份，sha256 锚版本，**不再分发** |
| MinerU 全文 | `corpus-md/<name>/full.md + pages/` | 28M，审计对象 |
| **工作区** | `/Volumes/D/audit-workspace/<name>/` | `_audit-pages/`（100dpi 灰度页图 pNNN.png，真值）+ `_audit-md/`（逐页切片 pNNN.txt，待检对象）+ `_zoom/`（裁决/抽查裁片） |
| 矩阵 | `corpus-md-audit/shards/<name>/AUDIT-MATRIX-<name>-PX-Y.md` | 分片=10 页区间，agent 追加行 |
| 汇总 | `corpus-md-audit/matrices/*-FINAL.md` + `STATUS.json` + `SUMMARY.md` | 收割脚本自动聚合 |
| 工具 | `tools/workflows/` | 全管线（见 §九速查表） |
| 提示词 | `tools/prompts/audit-subagent.md`（= `~/.agents/skills/mineru/prompts/audit-subagent.md`，**改动两处同步 commit**） | 子代理模板 |

**分辨率三档**（别再发明第四档）：100dpi 灰度页图=审计基准；300dpi 半页=裁决批；
600dpi 定点局部=疑难字形终裁。页图/裁片的产生是低成本的，但**图给模型的计价与大小无关**
——所以"整页提 DPI"不划算，正确做法是切**小局部**高 DPI 给子代理看。

## 三、账号与额度（血泪区）

- 子代理模型串：`account:账号A/GLM-5.3-Flash$max`（默认）或
  `account:账号B/GLM-5.3-Flash$max`（用户切换时）。
- 报错语义：**1308**=5 小时滚动窗口（等它自己回来）；**1310**=周/月额度（等充值/升级/自然重置）；
  **1005**=Starter Plan 配额耗尽（**不会自动重置**，要用户充值）。
- 实测消耗量级：一波 200 页 ≈ 0.9–1 亿 token；一个 120 项裁决批 ≈ 1–3.5 亿。
- **GUI 坑**：用户在 GUI 改一个 run 的设置会生成**新接班 run**；若旧接班还在跑=两舰队同页并发写
  （W049 实踩 90 秒重叠）。改设置前核对在飞集合；已重叠→报告用户停一个。
- **errored 坑**：舰队 phase1 的盘点 `world.run` 依赖分片状态，舰队自己落行后重放必不一致——
  provider 停机后平台自动 Resume 可能转 errored（"inputHash differs"）。**恢复=改脚本任意字节
  （版本注释 bump）后 AmendWorkflow(run_id, path)**，勿用 Resume。已完成单元按子代理名导入缓存。

## 四、波循环（核心编排）

**发射**：`CreateWorkflow(path=/Users/aurolafly/ABC/tools/workflows/audit_fleet.ts,
args={"maxUnits":20}, subagent_model=<模型串>, name="全转全审·第N波")`。
同一时间**只有一波舰队在飞**；裁决/抽查类小 workflow 可并行。发新波前确认无用户可能恢复的已停波。

**舰队语义**（audit_fleet.ts v8.1）：开波先跑 `audit_units.sh` 盘点全库缺页 → 按 10 页连续段
切单元（不连续缺页各成小单元）→ 20 并发派发 → 每单元一个子代理，提示词由模板填充
（`<pdf名>/<X>/<Y>/<Z>/<T>` + 三个目录路径）→ 分片行数==页数判成功，失败真重试一次 →
收割合并汇总。`maxUnits` 上限 20（v8 常量 CONCURRENCY=20、PAGE_BUNDLE=10，用户 2026-11-13 裁定）。

**波间固定八步**（每波完成通知到达后，不许跳步）：
1. 读收割结果（`audit_harvest.sh`：rows/validate/zoomOpen/failOpen/dup/incomplete）；
2. 行级修复：count_rows 逐分片诊断；DUPLICATE→删旧留新+携带既有处置 token；11 列行→裸竖线归 ∣；
   **只缺 DONE 汇总行且数据行全在→机械校验后补写 DONE 即完成，不重派**；
3. 新 FAIL 登记：无 token 的 FAIL 行追加「 已登记(待裁决批N)」→ failOpen 归零；
4. 重收割更新 STATUS；5. Tier-0 交叉（红×PASS/WARN 页记入下批裁决专项）；6. SUGGEST 逐条处置
   进 SUGGEST-LOG；7. WORKLOG 一个分片（W###）+ MEMORY 顶部现行化；8. 精确路径 commit
   （`corpus-md-audit/ + dev-docs/ + MEMORY.md`，信息写为什么）→ 发下一波。

## 五、子代理提示词（现行版全文，逐字收录）

真源 `~/.agents/skills/mineru/prompts/audit-subagent.md`，ABC 副本 `tools/prompts/audit-subagent.md`。
**2026-11-15 现行版**（关键铁律加粗处是历次事故的产物，不许删）：

```
你是 MinerU 逐页视觉审计子代理 [审计-P<N>]，负责 <pdf名> 的页区间 p<X>–p<Y>（共 <Z> 页，总页数 <T>）。

## 🚨 视觉阅读铁律（违反=审计无效，全部重做）
你**必须用 Read 工具直接读 PNG 文件**来看页面图像——这是你"看到"页面的唯一方式。
你**绝对不允许**用 analyzeImage、analyze_image、vision、OCR 或任何"图像转文字"的内部工具来代替自己看图。
正确流程（每页三步）：
  1. Read(<AUDIT_PAGES_DIR>/pNNN.png)  ← 你看到了这页的原始图像
  2. Read(<AUDIT_MD_DIR>/pNNN.txt)     ← 你读到了 MinerU 的提取文本
  3. 用你的视觉能力逐点比对两者
无法看到图像的两种签名都算 BLOCKED：(a) Read PNG 报错；(b) Read 返回的是 URL/纯文本链接而非图像内容本身。任一情况立即停止并报告 `[审计-P<N>] BLOCKED：Read 不注入图像`。不要用分析工具代替，不要假装看过，不要因为"大概知道这页长什么样"继续写矩阵行。

## 输入（只有这两个目录）
- 页图：<AUDIT_PAGES_DIR>/pNNN.png（100dpi 灰度，已预渲染；NNN=三位零填充页号，如第 27 页是 p027.png）
- md 切片：<AUDIT_MD_DIR>/pNNN.txt（MinerU 逐页提取，同样三位零填充）
你的输入**只有**这两个目录里的当前页文件。不列目录、不读这两个目录之外的任何文件——完整提取、清单文件、其他文档一律与你无关。分片文件只写你自己那一个。

## 输出
只写你自己的矩阵分片文件（其他文件一律只读）：<MATRIX_SHARD_PATH>
每审完一页，向该文件**追加一行**（照这个示例行的格式写）。
**单轮输出上限纪律**：一次追加只写当前页这一行——严禁把多页的行攒在同一轮回复里输出（W47 P181-190 实踩：攒批一次输出→超输出上限→整单元作废）；单行备注压在 ~350 字内：
| 26 | Y | ✓ | ✓ | ⚠ | ✓ | ✓ | ✓ | WARN | F2: p26 公式(3.2) ℓ 被误读为反引号 |
六维度：结构 / 文字 / 公式 / 题注 / 图表 / 语义，取值 ✓=完好 / ⚠=小瑕疵 / ✗=缺陷。下方示例行仅示意格式；判定尺度一律以「维度校准」行为准（示例的 WARN 不代表同类错误都记 WARN）。
判定：PASS=无✗且语义✓；WARN=有⚠但无✗；FAIL=任一维度✗；UNRESOLVED=存疑无法归级（备注必须含"需600dpi回图"）。
维度格只允许 ✓ / ⚠ / ✗ 三个符号；UNRESOLVED 行的维度格也从这三值中选（无法归级就用 ⚠），禁止写 ？ 或留空（validate_matrix 判 row_shape）。
维度校准：某维度出现改变记号含义的字符级错误（丢箭头/下标误读/字母混淆）或同类字符错误≥3处（如连字丢失），该维度记 ✗；仅排版/空格/断行类记 ⚠。
瑕疵码：F1 丢行/丢脚注、F2 字符误读、F3 格式错排、F4 空胞、F5 其他。备注列里不写裸竖线字符 |（数学竖线改用 \mid 或 ∣，否则破坏 row_shape）。
你不做 git commit——编排者统一处理。

## 每页循环（逐页进行；每页自包含：读完、写完、丢掉，不把细节带进下一页）
1. Read pNNN.png —— 视觉直读页面
2. Read pNNN.txt —— 读提取文本
3. 六维度逐点比对：结构/文字/公式/题注/图表/语义（结构=章节段落层次；文字=丢行丢脚注错字；公式=LaTeX 忠实性（上下标拍平/希腊字母/分式根号/特殊记号）；题注=图表标题；图表=图/表/矩阵内容可辨；语义=整页意思完整传达）
4. 打分（✓/⚠/✗）并给判定（规则见上）
5. 追加矩阵行到你的分片文件（一次一行，勿攒批；这是硬规则）

## 公式审计要点
上下标拍平（f^*→f*）；希腊字母；\frac/√[p]{} 结构；∑∫ 上下限；花体/Fraktur（𝔮 𝔭 ℘ ℓ 𝒪 𝔽）
字形易混——**存疑时备注标"需600dpi回图"。你不做任何放大/重渲染**——600dpi 裁决由编排者执行。

## 扫描件规则
<pdf名> 是扫描件：TRUE / FALSE（TRUE 则公式判定必须回原页图核对；此信息不写进矩阵——已审列永远写 Y）

## 恢复
若分片文件已有部分行（续命场景）：对照你的页区间逐页核对，只补缺行的页，不重做已审页、不覆盖既有行。

## 完成
区间内每页都有矩阵行后，最后输出一行汇总：
[审计-P<N>] DONE | p<X>-p<Y> | PASS <n> / WARN <n> / FAIL <n> / UNRESOLVED <n> | 需600dpi回图项 <n>
如果发现流程可改进之处，在汇总行之后追加一行 `SUGGEST: <一句话>`；没有就不写。你只建议，不改动任何流程。
```

**填充**：`tools/workflows/audit_fleet.ts` 里的 `fill()` 做占位替换（`<X>`=起始页、`<Y>`=末页、
`<Z>`=区间页数、`<T>`=总页数、`<AUDIT_PAGES_DIR>`/`<AUDIT_MD_DIR>`=D 盘两目录、
`<MATRIX_SHARD_PATH>`=分片路径、`<pdf名>`、扫描件 TRUE/FALSE 由盘点 `scan` 字段注入）。

## 六、裁决管道（zoom 项闭环）

zoom 项=矩阵备注含「需600dpi回图」且无「已裁决」的行。流程：

1. **生成**：`python tools/workflows/gen_adjudication.py --max 120 --name 裁决批N
   --out <draft路径>.dwf.ts`——从分片提取 zoom 行（备注前 350 字入 CLAIMS）→ fitz 渲染
   300dpi 半页（`_zoom/pNNN-top/bot.png`，clip=页面上下去边距的中分）→ 产出 20 组并行 workflow。
2. **专项提示注入法**：对需要特殊假设的页（如 LANA p35 的 𝒪̅^▷「或为真记号」），直接把提示
   追加进 CLAIMS 该键的值里——它会逐字进入该组提示词（W47 实例）。
3. **裁决代理提示词骨架**（每组一代理，逐页裁决）：
   ```
   你是视觉裁决代理（第N组）。逐页裁决。对每页：Read <ws>/_zoom/pNNN-top.png 与 pNNN-bot.png
   （300dpi 半页）。只裁决备注中标「需600dpi回图/存疑/无法确证」的子主张。
   硬规则：verdict 字段只能是 成立/不成立/看不清 三词之一；看不清绝不许猜；禁止任何×倍放大措辞
   ——你真裁了局部（可用 zoom_locate.py）就写裁片路径，没裁就只描述半页图所见；seen 逐字写记号
   形态与所在公式。本组页与主张（键=文档|页码）：【doc|page】<原备注350字>…
   ```
   防虚报约束（×倍放大禁令）来自 R0 教训：有子代理谎报"放大核对过"。
4. **组批策略**：批大小 ~120 项；按**记号族×章节聚合**分组（同族字形给同一代理连续裁，快且一致）；
   需要合并核对的（如 Y2017 p163/p169 的 "NF-Brideges" 疑原文拼写错）在 CLAIMS 注记。
5. **回填**：`python tools/workflows/backfill_adjudication.py --draft <draft> --batch 批N
   [--register "doc|page"]`——按 CLAIMS 键找含「需600dpi回图」且无「已裁决/已登记」的行，
   追加「 已裁决(批N)」；`--register` 的页写「 已登记(S4:图像块占位,批N看不清)」（看不清→
   S4 重提取队列，不留假裁决）。**skip 条件只认「已裁决」**——「已登记(待裁决批M)」是排队标记，
   必须允许追加（W46 修复）。
6. 裁决书=run 的 artifact（markdown），编排者另存 `adjudication-books/批N-裁决书.md`。
   实测假阳性率：审计侧 PASS/WARN 里约 9.5–10% 是假阴性；裁决侧「不成立」约占 27–44%。

## 七、三道质量闸门 + 免费侧信道

1. **行级**：每分片合格行数==页数（count_rows.py）；列结构/判定一致
   （~/.agents/skills/mineru/scripts/validate_matrix.py 判 row_shape）。
2. **裁决**：FAIL/ZOOM 项必须有处置 token 在途或完成——failOpen 必须归零才能发下一波。
3. **交叉**：`tier0_diff_all.py --doc <名>` 产 `tier0/TIER0-<名>.md`（PDF 文本层 vs MinerU 切片的
   词级 Jaccard，FLAG<0.85）——**免费侧信道**；把 FLAG 页与矩阵 verdict 对表，
   「红×PASS/WARN」页必须复核（记入下批裁决专项）。
4. **质量抽检（债3）**：`gen_quality_audit.py` 逐页独立代理盲审——**同时读** 300dpi 上下半页 +
   `_audit-md/pNNN.txt`（缺一无效）、不看矩阵；假阴性=原判 PASS/WARN 而盲审 FAIL。
   实测 9.5%（2/21）——≤10% 不触发全量复查，超了就要扩大抽样。

## 八、异常处置 playbook（全部实踩过，按号入座）

| 症状 | 根因 | 处置 |
|---|---|---|
| 单元报「response exceeded output token maximum」、分片只零散几行 | 子代理把多页行攒一轮输出 | 提示词已带单轮纪律；缺页由盘点自动重派；复发则把该单元按 5 页拆 |
| 含 `\|` 的行不被计签→整页误判缺页→重派重复 | `audit_units.sh` 按裸竖线切分 | 已修（`\|`→¦ 再切分）；若再出现先查这里 |
| 同页多行（DUPLICATE） | 波重叠/重派 | 删旧留新；旧行有处置 token 则携入新行 |
| 数据行 10/10 在、单元仍「异常」 | 只缺 DONE 汇总行 | 机械校验行形计数后补写 DONE 即完成，**不重派** |
| 行被切成 11+ 列 | 备注裸竖线 | 归一：第 10 列起裸竖线全改 ∣ |
| run 停后自动续跑转 errored（inputHash differs） | 盘点 world.run 随舰队落行漂移 | 改脚本一字节→**AmendWorkflow**（勿 Resume）；缓存导入已完成单元 |
| 两个同名波在跑 | GUI 改设置生成双接班 | 报告用户停一个（停新的） |
| provider 1308/1310/1005 | 额度 | 停手等用户（§〇.5） |
| 部分行单元（fail<N×页） | 输出上限/中断 | 缺页自动进下波队首，无需手工搬运 |
| 停摆 run 迟到冲刷行 | 在飞代理最后落盘 | 收割时补登记/去重（可能多轮，直到 failOpen=0 且 dup=0） |
| `pattern_prescreen.py` 语法错没人发现 | 批量回补未跑测 | 每次改完 `ast.parse` + 空跑一次 |

## 九、工具速查（全在 tools/workflows/，venv=/Volumes/D/toolchain-cache/mineru-venv/bin/python）

| 工具 | 干什么 | 关键参数 |
|---|---|---|
| audit_fleet.ts | 舰队（CreateWorkflow path） | `args={"maxUnits":20}` + subagent_model + 波名 |
| audit_units.sh | 盘点缺页（fleet phase1 调） | 无参，stdout JSON |
| audit_harvest.sh | 收割聚合 STATUS/SUMMARY/FINAL | 无参 |
| count_rows.py | 逐分片行数 | `<分片路径>` |
| validate_matrix.py | row_shape 校验 | ~/.agents/skills/mineru/scripts/ |
| tier0_diff_all.py | 文本层免费对照 | `--doc <名>` |
| pattern_prescreen.py | 30+ 条实证 grep 模式预筛 | 无参，产 tier0/PATTERN-SUSPECTS.tsv |
| gen_adjudication.py | 裁决批生成（渲染 300dpi 半页） | `--max 120 --name --out` |
| backfill_adjudication.py | 裁决回填 | `--draft --batch [--register]` |
| gen_quality_audit.py | 抽查盲审生成 | `--out [--pages-json]` |
| repair_shard_rows.py | 行形修复 | `<分片路径>`（不是 --doc） |
| zoom_locate.py | 裁决代理可用的局部裁片 | 见 ~/.agents/skills/mineru/ |

## 十、否掉的路（别重走）

- **整页提 DPI（150/200/300dpi 页图给审计代理）**：多次提案多次驳回——图计价与大小无关，
  100dpi 判不了的字形本来就该走 600dpi 定点裁决，整页提 DPI 是白花钱。
- **给子代理发「已知缺陷速查表/预筛清单」**：提示词膨胀 + 先筛后审会让子代理只扫不细审；
  预筛归编排者侧 pattern_prescreen。
- **子代理侧逐行 validate 前移**：同上，波间闸门足够。
- **矩阵行内嵌 PNG hash/mtime 自证**：破坏 row_shape 稳定性；scopes 快照已承载。
- **审计代理自己放大/重渲染**：R0 虚报之源；放大权只归裁决代理（且必须真裁）。

## 十一、完成门（全部满足才算完）

① 3105 页全有合格行；② 68 文档 harvest 全 pass（零 FAIL-OPEN/ZOOM-OPEN/DUPLICATE/INCOMPLETE）；
③ 全部 FAIL/UNRESOLVED/zoom 项有真实处置 token；④ SUGGEST 台账无未处置；⑤ 全库 SUMMARY
（参考文献页缺陷单列）+ WORKLOG 收尾 + 最终 commit + 善后（交接卡/全项自查/最终报告）。
逐项给证据指针（STATUS 读数/commit hash/裁决书路径），按 Item 表自审。
