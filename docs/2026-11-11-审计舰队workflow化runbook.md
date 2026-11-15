# 审计舰队 workflow 化 Runbook v2（2026-11-11 晚，对齐 mineru skill 新架构）

> 何时读：准备**启动/恢复/重启**任何一轮视觉审计时。上位规矩两条——
> `RULE-008-VISUAL-AUDIT-VIA-WORKFLOW`（长审计经 workflow，不裸派子代理）+
> `RULE-009-VISUAL-AUDIT-REQUIRES-VISION-MODEL`（视觉审计必须用有视觉能力的模型）。
> 本 runbook 是 ABC 项目的**编排者操作手册**；子代理提示词与细化流程的真值在
> `~/.agents/skills/mineru/`（prompts/audit-subagent.md、runbooks/visual-audit.md、
> references/visual-audit.md、scripts/）。本手册不复制它们，只写项目侧怎么用。

## 1. 模型选择（RULE-009 执行细则，每次启动前必做）

**视觉审计 = 模型自身看图的能力**（可结合高 DPI 局部放大）；不是 API、不是脚本、
不是 Python 图像库。

| 已知可用模型（2026-11-11 标注） | 供应商 | 档位 |
|---|---|---|
| GLM 5.3 Flash | Z.AI（本机三个 plan 均可见） | Max Thinking（`$max`） |
| DeepSeek V4.1 Flash | 需**问清用户用哪个供应商** | Max Thinking（`$max`） |

**硬规则**：①启动前必须问用户用哪一种；②DeepSeek 必须问供应商；③一律 `$max`；
④主模型（非 Flash）无视觉能力——Read PNG 只回 CDN URL（2026-11-11 实测），用了=审计作废。
⑤**1 页视觉证明**：每轮舰队放行前，先让目标模型读一页页图并复述页眉内容——看得见才放行；
看不见即停手上报（平台级送图问题）。

**模型证据流程（可复制）**：每批 run 结束后 Leader 执行
①`GetWorkflowRun(run_id)` 取运行记录里的 `subagent_model`；②对 P3 页做复述（该批首个代理已完成）；
③用 `save_scope.py` 写 `corpus-md-audit/model-proof-<批>.json`：
`{run_id, subagent_model, page, recitation, pdftotext_line}`。
GetWorkflowRun 不可用时替代证据 = run id + 运行面板截图 + 人工比对记录，写进同一文件。
ListModels 本会话不可用（model_catalog_unavailable），不得以"本机唯一"作证据。

**项目覆盖声明**（与 skill 默认不同，以此为准）：单元 10 页/个（非 skill 的 40–80；视觉审计 token 账）、
子代理**不 commit**（矩阵分片写入 repo 后由 Leader 批末统一 commit）、分级
PASS/WARN/FAIL/UNRESOLVED（非旧 PASS/PASS±/FAIL）。

本项目分工（用户 2026-11-11 确认，完整 model id 如下）：
- **PDF 视觉审计舰队 = `account:账号B/GLM-5.3-Flash$max`**；
- **方案对抗审计 = `deepseek-opencode/deepseek-v4.1-flash$max`**（单子代理/轮，审方案不审 PDF；
  供应商=deepseek-opencode（用户确认；ListModels 本会话不可用，不以「唯一」作证据）。

## 2. 任务分流表

| 任务 | 走什么 | 为什么 |
|---|---|---|
| 视觉审计（逐页 fan-out） | **workflow**（CreateWorkflow，`subagent_model` 按 §1） | RULE-008 主场景 |
| 方案/runbook/checklist 对抗审计 | **workflow**（`CreateWorkflow(path="tools/workflows/plan_audit.ts", subagent_model="deepseek-opencode/deepseek-v4.1-flash$max")`，单子代理） | 用户 2026-11-11 裁定 |
| MinerU 批量转换 | 幂等脚本（convert_*.sh） | 非子代理任务；限流下 workflow 无增益 |
| 页图渲染 / md 切片 / 矩阵收割 | 确定性脚本（render_pages_all.sh / slice_md_pages.py / prep_shards.py / audit_harvest.sh） | 编排者步，非代理步 |
| FAIL 修复 | Leader 串行（只改 md、独立 fix commit；kit 件需同步修 content_list.json）；**重审前先删除该页矩阵行**（或整片移 `_quarantine/`）使 units 重新看到 unsigned，重审后该页恰好一行 | 唯一写者纪律 + 可重审 |
| 抽查复检 | **workflow**（`CreateWorkflow(path="tools/workflows/spotcheck.ts", args={"docs":[...]}, subagent_model="account:账号B/GLM-5.3-Flash$max")`）+ Leader 用 pdftotext 做文本层比对；Leader 不做视觉判定（RULE-009） | 判定权与视觉能力分离 |
| 审计范围裁定 | Leader 直做 | 判定权不外包 |

## 3. 工作区与产物布局（用户裁定：大文件放 D 盘）

```
/Volumes/D/audit-workspace/<文档短名>/        ← 工作区（D 盘，大文件；不入 git）
├── _audit-pages/pNNN.png                     ← 100dpi 灰度页图（编排者预渲染，只读）
├── _audit-md/pNNN.txt                        ← 逐页 md 切片（编排者预切，只读）
├── _zoom/zoom600-*.png                       ← 600dpi 局部放大（裁决用）
└── _audit-matrix/_quarantine/                ← 旧格式分片隔离区（历史）

/Volumes/D/abc-legacy-300dpi/_audit-binary/   ← 旧 300dpi 二值图（68 份目录/3105 张全量留档；
                                                 其中 64 页有旧签，作 legacy 锚点）
ABC 仓库 corpus-md-audit/shards/<名>/AUDIT-MATRIX-<名>-P###-###.md  ← 矩阵分片（断点真值，唯一真值；
                                                   子代理直接写 repo；批结束由 Leader commit）
ABC 仓库 corpus-md-audit/matrices/            ← 收割合并后的 FINAL 矩阵
ABC 仓库 corpus-md-audit/{SUMMARY.md,STATUS.json,SPOTCHECK.md,scopes/}  ← 汇总/状态/抽查/范围快照
```

## 4. 审计舰队设计（workflow 六步骨架；硬规则六条）

```
① 盘点：tools/workflows/audit_units.sh → 待审页/文档/分片清单（真值=repo 矩阵行；legacy 仅历史，不参与已签）
② 预备：world.run 读 prompts/audit-subagent.md 模板 + prep_shards.py 建分片头
③ 并发：agent() 每分片一个（连续段切分，≤10 页/单元，**脚本内 5 路信号量**），ask=模板填充原样下发；
   任一单元返回 BLOCKED（Read 不注入图像）→ **熔断整批**，不许继续烧
④ 续批：重跑盘点吃新就绪文档/缺口（新闻稿式渐进供料）
⑤ 收割：audit_harvest.sh → FINAL 矩阵入 repo + validate_matrix.py 校验（行数/重复/已审列）
⑥ 汇总：artifact.markdown + WorkflowReport（FAIL 清单 → S4）
```

- **硬规则六条**：每页即时落盘（矩阵行）、恢复=先读账本再派活、写集互斥（一分片一
  写者）、并发 3–5、只报告不修复、脚本与范围入库。
- **提示词纪律**：铁律段（🚨 视觉阅读铁律）**一个字不能删**；模板只填占位符，
  不改写、不缩写。
- **600dpi 回图**：矩阵备注标"需600dpi回图"的页，按 skill runbooks/visual-audit.md
  第 7 步局部重渲染裁决（**本项目页图 100dpi；600dpi 局部重渲染一次即足，坐标 ×6 换算；
  禁止 6x/8x/10x/16x 任意倍率阶梯**），结论**必须**以固定格式回写备注：`已裁决：<结论>`。
  放大与裁决=**编排者（有视觉模型）**的活；子代理只标"需600dpi回图"，不许自行放大、不许
  虚报"×倍核实"。FINAL 可含未裁决行，但 verdict=ZOOM-OPEN 且 C-08 不得计入完成。

## 5. 启动前检查清单（缺一不放行）

| # | 检查 | 判据 |
|---|---|---|
| P1 | 模型按 §1 问过用户并确认（含供应商） | 对话有记录 |
| P2 | `subagent_model` 已配 `...$max` | CreateWorkflow 参数 |
| P3 | 1 页视觉证明通过：对 **LANA p001**（或任一已知页）跑一个最小 CreateWorkflow（`subagent_model=account:账号B/GLM-5.3-Flash$max`），让子代理复述页眉文字；判据=**复述 == `pdftotext -f 1 -l 1 <pdf> -` 的第一行**（Leader 只做文本比对，不看图）；证据写 `corpus-md-audit/model-proof-<批>.json`（model id + 复述 + pdftotext 行） | 文件存在且两串一致；若 Read 返回 URL → BLOCKED，停手上报 |
| P4 | 工作区齐：`_audit-pages` 与 `_audit-md` 计数=页数 | audit_units.sh blocked=0 |
| P5 | 模板可读、分片头已建 | workflow 前置步成功 |
| P6 | 已知欠账（legacy 64 页存疑）在报告中如实呈现 | 汇总分节 |

## 5b. 启动组织：8×8 迭代（用户 2026-11-12 裁定）

**单代理 10 页；单 run ≤8 个代理（=80 页/run）；批间人工串行，不并发。**

理由（token 账）：每页视觉审计 ~4-5K tokens（页图+切片+推理/落签），10 页≈50-60K，离压缩
边界有安全余量且固定开销（~10K/代理）摊薄合理；25 页≈110-135K 必越压缩边界、判级会走形
（这是旧 10 页/单元参数的错，已废弃）。

节奏：

```
R0 校准批：maxUnits=1（1 代理 × 10 页，LANA p1-p10）
  → Leader 审：成本/质量/进度可见性/SCHEME-ISSUE
  → 合格后进入 8×8 循环
R1..Rn：每 run maxUnits=8（8 代理 × 10 页=80 页）
  → 批后：看矩阵成果 + 跑 spotcheck（按批）+ 处理 SCHEME-ISSUE（修方案/登记→commit）
  → 再放下一批；约 39 批覆盖 3105 页
```

- **同一 workflow run 绝不超 8 个代理**；方案审计不再独立跑 DeepSeek 链路，改由干活代理
  顺报 `SCHEME-ISSUE:` 行（模板内置义务），workflow 汇聚写 `corpus-md-audit/scheme-issues-<runid>.json`。
- 批间串行：上一批的成果、抽查、SCHEME-ISSUE 处置完，才放下一批。
- 调用样例（校准批）：

```
CreateWorkflow(path="tools/workflows/audit_fleet.ts",
  name="全转全审·R0校准",
  args={"docs": ["LANA_2026-07_InterimReport_KatoEtAl"], "maxUnits": 1},
  subagent_model="account:账号B/GLM-5.3-Flash$max")
```

8×8 批：`args={"docs": [8 份文档短名...], "maxUnits": 8}`（或省略 docs 让脚本从队首取 8 单元）。

## 5c. （已并入 §5b：8×8 模型；≤300 页/批条款作废）


## 6. 恢复语义

- 断点 = **repo 工作树内的矩阵分片行**（`corpus-md-audit/shards/`；每批结束 Leader commit 后才进
  git 历史，崩溃在 commit 前时断点在磁盘工作树但不在历史）+ workflow journal（步级）；两者不一致
  时以矩阵行为准。D 盘掉盘不丢审计断点（页图/切片可重渲染）。
- Resume 后先跑盘点：已审行自动扣除，只派未签页。
- 子代理恢复规则（模板内置）：**按页清单逐页核对已有行——中间缺口也要补**；不重做、不覆盖。
- 中断即善后：R-28 §C 交接卡入 `dev-docs/goals/`，中断点精确到"哪份文档哪一页"。

## 7. 分轮组织（用户裁定：先试 50 页）

| 轮 | 范围 | 判据 |
|---|---|---|
| R0 试跑 | **校准批 1 代理 ×10 页（LANA p1-p10，maxUnits=1）**：验证 repo shard/count_rows/scopes/BLOCKED/批 harvest/SCHEME-ISSUE 全链路 + 实测每页成本 | 每页成本/进度可见/矩阵校验/铁律合规/抽查流程全过；点火前先做 1 页视觉证明（含 URL 反例测试） |
| R1..Rn 8×8 迭代 | 全部 **3105** 页（含 legacy 64 页重审）；每 run ≤8 代理×10 页=80 页；批间审成果+处理 SCHEME-ISSUE | C-04 矩阵行 3105/3105 |
| R2 收割修复 | **全部批次结束后跑一次无参 `audit_harvest.sh`（全库收口，STATUS/SUMMARY 全量口径）** + FAIL 修复（独立 fix commit）+ 600dpi 回图裁决 | C-06/C-07/C-08 |
| R3 | 已并入 R1（legacy 64 页随全量重审，audit_units 不再把 legacy 算已签） | — |

## 8. Item 自检表（P-16）

| Item ID | 要求（人话情境） | 判据 |
|---|---|---|
| I-RB-01 | 当你要启动审计时，你要先过 §5 清单（含模型问询与 1 页视觉证明） | 六项全绿 |
| I-RB-02 | 当你写 workflow 时，你要读模板填充而非内嵌提示词 | ask 内容来自 prompts 模板 |
| I-RB-03 | 当你要中断恢复时，你要以矩阵行为断点 | 恢复后无重复行/无跳页 |
| I-RB-04 | 当你收割时，你要跑 validate_matrix.py 且失败项不静默 | 校验输出留痕 |
| I-RB-05 | 当舰队跑完一轮时，你要抽查≥10%：文本层比对 + P3 视觉证明（不宣称"页图级一致"，Leader 无视觉） | 抽查记录 |
| I-RB-06 | 当出现"需600dpi回图"项时，你要逐项裁决后才算完成 | 备注列有裁决结论 |
| I-RB-07 | 当方案有重大改动时，你要用 plan_audit.ts 对抗审计直到 CLEAN | 对抗审计 verdict=CLEAN |

## 9. 风险与限制

- Flash 模型的视觉结论仍可能有个体误差 → 抽查≥10% 兜底；存疑即标"需600dpi回图"。
- 300dpi 二值旧图与 100dpi 灰度新图不同规格：legacy 的 sha 锚点对应旧图（D 盘留档），
  新审计一律用 100dpi 灰度。
- token 成本：全库 3105 页 × 逐页视觉比对是核弹级消耗；试跑数据出来先向用户报成本
  再放全量（用户已授权分批，成本异常按 goal 停止条款③上报）。
