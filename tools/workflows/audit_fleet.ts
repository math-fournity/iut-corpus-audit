/* zcode-workflow
description: 全转全审·审计舰队（8×8 模型）：单 run ≤8 单元、每单元 10 页；批间人工串行；干活代理顺报 SCHEME-ISSUE。
args:
  docs:
    type: json
    description: 本 run 的文档短名数组（省略或空=从全量队首取前 maxUnits 个单元）。
  maxUnits:
    type: number
    description: 本 run 代理数上限（1–20，默认 20；R0 校准批=1）。
*/

/* 全转全审 · S3 审计舰队 v8.1（2026-11-15；v8/v7/v5/v6 为历史）
   v8.1 变更（W079 事故）：本脚本 phase1 的 audit_units.sh 盘点 world.run 依赖分片状态，
   舰队自身落行会使盘点输出漂移 → provider 停机后平台自动 Resume 的 journal 重放报
   inputHash differs（非确定性）转 errored。恢复通道=改本文件任意字节（如本注释）后
   AmendWorkflow(run_id, path)：新建 run 重跑盘点、按子代理名导入已完成单元缓存。勿 Resume。*/
/* —— 历史变更记录（v8 及更早）——
   v8 变更（用户 2026-11-13 新裁定）：同时在飞代理数 8→20；单元上限随之 8→20（否则并发跑不起来）；
   PAGE_BUNDLE 仍 10、波循环与质量闸门不变。
   v7 变更（用户 2026-11-12 裁定）：①PAGE_BUNDLE=10（视觉审计每页~4-5K tokens，25 必越压缩边界）
   ②单 run 最多 MAX_UNITS=8 个代理（2026-11-12 用户终裁保持 8；校准批可传 1）③去自动续批，批间由 Leader
   人工串行（审成果+处理 SCHEME-ISSUE）④代理顺报 SCHEME-ISSUE 方案问题（模板内置），本脚本汇聚。
   v5 变更：①矩阵分片落 repo corpus-md-audit/shards/（断点入 git，D 盘只留页图/切片/zoom）
   ②legacy 不再算已签（3105 全量由新矩阵行覆盖）③BLOCKED 正则锚定行首防误触发
   ④失败真重试一次 + 以分片行数判成功 ⑤scopes 快照落盘 ⑥批模式（docs filter）收割口径一致
   ⑦0 单元时返回 NO-UNITS 硬错。模型：GLM 5.3 Flash + Max Thinking（RULE-009）。 */

interface DocInventory {
  doc: string; name: string; pages: number; mode: string; scan: boolean; unsigned: number[];
}
interface Inventory {
  ready: DocInventory[];
  blocked: { name: string; pages: number; png: number; txt: number }[];
}
interface HarvestStats {
  docs: { name: string; pages: number; newRows: number; legacyRows: number;
          grades: Record<string, number>; zoomOpen: number; validate: string; detail: string }[];
  totalNewRows: number; totalLegacyRows: number;
  notStarted: number; badValidate: number; zoomOpen: number;
}
interface UnitOut {
  unit: string; shardPath: string; expectedRows: number; actualRows: number;
  pass: number; warn: number; fail: number; zoom: number;
  ok: boolean; blocked: boolean; raw: string; schemeIssues: string[]; suggests: string[];
}
interface Finding { where: string; what: string; evidence: string; status: "verified" | "unconfirmed"; severity: "low" | "medium" | "high"; }
interface WorkflowReport { conclusion: string; findings: Finding[]; verified: string[]; notCovered: string[]; }

const PAGE_BUNDLE = 10;   // 每代理页数（视觉审计 token 账：10 页≈50-60K，安全区）
const CONCURRENCY = 20;   // 同时在飞代理数（2026-11-13 用户新裁定：只放大并发；单元上限随之 20，否则并发跑不起来）
const FEED_ROUNDS = 12;

const REPO = "/Users/aurolafly/ABC";
const WS = "/Volumes/D/audit-workspace";
const TEMPLATE = "/Users/aurolafly/.agents/skills/mineru/prompts/audit-subagent.md";

const rawDocs = args.docs;
const DOC_FILTER: string[] = Array.isArray(rawDocs)
  ? rawDocs.filter((x): x is string => typeof x === "string")
  : [];
const rawMax = args.maxUnits;
const MAX_UNITS: number = typeof rawMax === "number" ? Math.min(Math.max(Math.floor(rawMax), 1), 20) : 20;

artifact.board("audit-progress", {
  key: "unit", status: "state", columns: ["待审", "完成", "异常"],
  cardTitle: "unit",
  detail: [{ field: "range", label: "区间" }, { field: "fail", label: "FAIL" }],
});

interface Unit { doc: DocInventory; pages: number[]; shard: string; agentName: string; shardPath: string }

function makeUnits(doc: DocInventory, tag = ""): Unit[] {
  const segs: number[][] = [];
  let cur: number[] = [];
  for (const p of doc.unsigned) {
    if (cur.length && p !== cur[cur.length - 1] + 1) { segs.push(cur); cur = []; }
    cur.push(p);
  }
  if (cur.length) segs.push(cur);
  const chunks: number[][] = [];
  for (const s of segs) {
    for (let i = 0; i < s.length; i += PAGE_BUNDLE) chunks.push(s.slice(i, i + PAGE_BUNDLE));
  }
  // 分片名 = 页区间（恢复场景下不会与既有分片撞名；P026-050 这种）
  return chunks.map((ps) => {
    const rangeTag = `P${String(ps[0]).padStart(3, "0")}-${String(ps[ps.length - 1]).padStart(3, "0")}`;
    const shard = `AUDIT-MATRIX-${doc.name}-${rangeTag}.md`;
    return {
      doc, pages: ps, shard,
      shardPath: `${REPO}/corpus-md-audit/shards/${doc.name}/${shard}`,
      agentName: `审计-${doc.name}-${rangeTag}${tag}`,
    };
  });
}

function fill(tpl: string, u: Unit): string {
  const mdDir = `${REPO}/corpus-md/${u.doc.doc}`;
  return tpl
    .split("<AUDIT_PAGES_DIR>").join(`${WS}/${u.doc.name}/_audit-pages`)
    .split("<AUDIT_MD_DIR>").join(`${WS}/${u.doc.name}/_audit-md`)
    .split("<MATRIX_SHARD_PATH>").join(u.shardPath)
    .split("<mineru导出路径>").join(mdDir)
    .split("<pdf名>").join(u.doc.name)
    .split("<N>").join(u.agentName.split("-P").pop() ?? "1")
    .split("<X>").join(String(u.pages[0]))
    .split("<Y>").join(String(u.pages[u.pages.length - 1]))
    .split("<Z>").join(String(u.pages.length))
    .split("<T>").join(String(u.doc.pages))
    .split("是扫描件：TRUE / FALSE").join(`是扫描件：${u.doc.scan ? "TRUE" : "FALSE"}`);
}

function parseOut(raw: string, u: Unit): UnitOut {
  const blocked = /(^|\n)\s*(?:[-*>]\s*)?(?:\[[^\]]*\]\s*)?BLOCKED(?:-ENV)?\b/m.test(raw);
  const schemeIssues: string[] = [];
  for (const m of raw.matchAll(/^SCHEME-ISSUE:\s*(.+)$/gm)) schemeIssues.push(m[1].trim());
  const suggests: string[] = [];
  for (const m of raw.matchAll(/^SUGGEST:\s*(.+)$/gm)) suggests.push(m[1].trim());
  const m = raw.match(/DONE \| p(\d+)-p(\d+) \| PASS (\d+) \/ WARN (\d+) \/ FAIL (\d+) \/ UNRESOLVED (\d+) \| 需600dpi回图项 (\d+)/)
    ?? raw.match(/DONE \| p(\d+)-p(\d+) \| PASS (\d+) \/ WARN (\d+) \/ FAIL (\d+)/);
  return {
    unit: u.agentName, shardPath: u.shardPath, expectedRows: u.pages.length, actualRows: -1,
    pass: m ? +(m[3] ?? 0) : 0, warn: m ? +(m[4] ?? 0) : 0, fail: m ? +(m[5] ?? 0) : 0,
    zoom: m ? +(m[7] ?? 0) : 0, ok: !!m, blocked, schemeIssues, suggests, raw: m ? "" : raw.slice(-400),
  };
}

// 同一 run 内子代理名唯一：handle 只创建一次，重试复用同一上下文（H3）
async function askOnce(a: Agent, u: Unit, tpl: string): Promise<string> {
  return a.ask(fill(tpl, u));
}

async function runBatch(batch: Unit[], tpl: string, results: UnitOut[]): Promise<boolean> {
  const spec = batch.map((u) => ({ name: u.doc.name, shard: u.shard,
    range: `p${u.pages[0]}-p${u.pages[u.pages.length - 1]}` }));
  if (spec.length) await world.run("python3", [`${REPO}/tools/workflows/prep_shards.py`, JSON.stringify(spec)]);
  for (const u of batch) report({ unit: u.agentName, state: "待审", range: `${u.pages.length}页`, fail: 0 }, "audit-progress");
  for (let i = 0; i < batch.length; i += CONCURRENCY) {
    const group = batch.slice(i, i + CONCURRENCY);
    const outs = await Promise.all(group.map(async (u): Promise<UnitOut> => {
      const a = agent(u.agentName);
      let out: UnitOut;
      try {
        out = parseOut(await askOnce(a, u, tpl) ?? "", u);
      } catch (e) {
        out = { unit: u.agentName, shardPath: u.shardPath, expectedRows: u.pages.length,
                actualRows: -1, pass: 0, warn: 0, fail: 0, zoom: 0, ok: false, blocked: false, raw: String(e).slice(0, 300), schemeIssues: [], suggests: [] };
      }
      if (!out.ok && !out.blocked) {  // 真重试一次（同一 handle，继承上下文）
        try {
          const retry = parseOut(await askOnce(a, u, tpl) ?? "", u);
          if (retry.ok || retry.blocked) out = { ...retry, suggests: [...out.suggests, ...retry.suggests] };
        } catch { /* keep first failure */ }
      }
      // 以分片行数判成功（DONE 行不可靠时的兜底）
      const cnt = await world.run("python3", [`${REPO}/tools/workflows/count_rows.py`, u.shardPath]);
      out.actualRows = parseInt(cnt.stdout.trim() || "0", 10);
      out.ok = out.actualRows === out.expectedRows;  // 严格相等：DONE 但少行=未完成
      return out;
    }));
    for (const o of outs) {
      results.push(o);
      report({ unit: o.unit, state: o.ok ? "完成" : "异常", range: "", fail: o.fail }, "audit-progress");
      if (o.blocked) {
        log(`BLOCKED 熔断：${o.unit} —— Read 不注入图像（模型无视觉/管道不通），停止剩余单元`);
        return true;
      }
    }
  }
  return false;
}

phase("读提示词模板与盘点待审页");
const tplRun = await world.run("cat", [TEMPLATE]);
if (tplRun.exitCode !== 0) {
  return { conclusion: `提示词模板读取失败（${TEMPLATE}），舰队未开工。`, findings: [],
    verified: [], notCovered: ["全部页（模板不可读）"] } satisfies WorkflowReport;
}
const tpl = tplRun.stdout;
const invRun = await world.run("bash", [`${REPO}/tools/workflows/audit_units.sh`], { timeoutMs: 180000 });
if (invRun.exitCode !== 0) {
  return { conclusion: "盘点脚本执行失败，舰队未开工。", findings: [], verified: [],
    notCovered: [`全部页（盘点失败：${invRun.stderr.slice(0, 300)}`] } satisfies WorkflowReport;
}
const inv = JSON.parse(invRun.stdout) as Inventory;
await world.run("python3", [`${REPO}/tools/workflows/save_scope.py`,
  `${REPO}/corpus-md-audit/scopes/inv-${run.id}.json`, JSON.stringify(inv)]);
const scoped = DOC_FILTER.length ? inv.ready.filter((d) => DOC_FILTER.includes(d.name)) : inv.ready;
const allUnits: Unit[] = [];
for (const d of scoped) allUnits.push(...makeUnits(d));
const firstUnits = allUnits.slice(0, MAX_UNITS);   // 单 run ≤20 个代理（2026-11-13 用户新裁定：并发 20）
const remainingUnits = allUnits.length - firstUnits.length;
if (firstUnits.length === 0) {
  const missing = DOC_FILTER.filter((n) => !inv.ready.some((d) => d.name === n));
  return {
    conclusion: "NO-UNITS：盘点后无任何待审单元（批过滤后为空）。请检查 args.docs 是否正确/该批是否已全部完成。",
    findings: [], verified: [`盘点 blocked=${inv.blocked.length}`],
    notCovered: missing.length ? [`批过滤名单中不存在或已完成: ${missing.join(", ")}`] : ["本批无待审页"],
  } satisfies WorkflowReport;
}
const firstPending = firstUnits.reduce((n, u) => n + u.pages.length, 0);
log(`待审 ${firstPending} 页 / ${firstUnits.length} 分片（批过滤=${DOC_FILTER.length ? DOC_FILTER.length + "份" : "全量"}；工作区未齐 ${inv.blocked.length} 份暂挡）`);

phase("并发逐页视觉审计（信号量+熔断+重试）");
const results: UnitOut[] = [];
const blockedAbort = await runBatch(firstUnits, tpl, results);

phase("收割合并与汇总（批口径）");
const schemeIssues = [...new Set(results.flatMap((r) => r.schemeIssues))];
if (schemeIssues.length) {
  await world.run("python3", [`${REPO}/tools/workflows/save_scope.py`,
    `${REPO}/corpus-md-audit/scheme-issues-${run.id}.json`, JSON.stringify(schemeIssues)]);
  log(`SCHEME-ISSUE 汇聚 ${schemeIssues.length} 条（交 Leader 批后处置）`);
}
const suggests = [...new Set(results.flatMap((r) => r.suggests))];
if (suggests.length) {
  await world.run("python3", [`${REPO}/tools/workflows/save_scope.py`,
    `${REPO}/corpus-md-audit/suggests-${run.id}.json`, JSON.stringify(suggests)]);
  log(`SUGGEST 汇聚 ${suggests.length} 条（交 Leader 决策台账逐条采纳/驳回）`);
}
const harArgs = DOC_FILTER.length
  ? [`${REPO}/tools/workflows/audit_harvest.sh`, JSON.stringify(DOC_FILTER)]
  : [`${REPO}/tools/workflows/audit_harvest.sh`];
const harRun = await world.run("bash", harArgs, { timeoutMs: 300000 });
if (harRun.exitCode !== 0) {
  return { conclusion: `收割脚本执行失败（exit=${harRun.exitCode}），本批审计结果未汇总：${harRun.stderr.slice(0, 400)}`,
    findings: [], verified: [], notCovered: [`收割失败：${harRun.stderr.slice(0, 400)}`] } satisfies WorkflowReport;
}
const stats = JSON.parse(harRun.stdout) as HarvestStats;
const failDocs = stats.docs.filter((d) => (d.grades["FAIL"] ?? 0) > 0);
const badDocs = stats.docs.filter((d) => d.validate !== "pass" && d.validate !== "NO-ROWS");
const summaryMd = [
  `# 全转全审 · 审计汇总（批：${DOC_FILTER.length ? DOC_FILTER.join(", ") : "全量"}）`,
  "",
  `- 本批 ${firstUnits.length} 单元（${firstPending} 页）/ 上限 ${MAX_UNITS}；剩余 ${remainingUnits} 个单元待下批`,
  `- 文档：${stats.docs.length}；新格式矩阵行 ${stats.totalNewRows}；legacy 历史 ${stats.totalLegacyRows} 页`,
  `- FAIL ${failDocs.reduce((n, d) => n + (d.grades["FAIL"] ?? 0), 0)} 页；UNRESOLVED ${stats.docs.reduce((n, d) => n + (d.grades["UNRESOLVED"] ?? 0), 0)}；600dpi 未裁决 ${stats.zoomOpen} 项；校验不过 ${stats.badValidate} 份；未开工 ${stats.notStarted} 份`,
  `- 熔断：${blockedAbort ? "**BLOCKED（环境级送图失败）**" : "无"}`,
  "",
  "| 文档 | 页数 | 新行 | PASS | WARN | FAIL | UNRES | 600dpi未裁 | 校验 |",
  "|---|---|---|---|---|---|---|---|---|",
  ...stats.docs.map((d) => `| ${d.name} | ${d.pages} | ${d.newRows} | ${d.grades["PASS"] ?? 0} | ${d.grades["WARN"] ?? 0} | ${d.grades["FAIL"] ?? 0} | ${d.grades["UNRESOLVED"] ?? 0} | ${d.zoomOpen} | ${d.validate} |`),
].join("\n");
await artifact.markdown("summary", summaryMd, {
  title: DOC_FILTER.length ? `审计汇总 · ${DOC_FILTER.length} 份文档` : "全转全审 · 视觉审计汇总",
  description: `新格式行 ${stats.totalNewRows}；FAIL 待 S4；校验不过 ${stats.badValidate} 份。`,
  primary: true,
});

return {
  conclusion: blockedAbort
    ? `**BLOCKED 熔断**：Read 不注入图像（模型无视觉/管道不通），已停止剩余单元。已落签 ${stats.totalNewRows} 行。`
    : stats.badValidate === 0 && stats.notStarted === 0
      ? `收割完成：本批 ${firstUnits.length} 单元 / 剩余 ${remainingUnits} 单元；新格式 ${stats.totalNewRows} 行；校验通过（FAIL 待 S4，600dpi 未裁 ${stats.zoomOpen} 项）。`
      : `收割完成：新格式 ${stats.totalNewRows} 行；校验不过 ${stats.badValidate} 份、未开工 ${stats.notStarted} 份、600dpi 未裁 ${stats.zoomOpen} 项（见 notCovered）。`,
  findings: [
    ...schemeIssues.map((iss) => ({ where: "方案/流程", what: iss, evidence: `scheme-issues-${run.id}.json`,
      status: "unconfirmed" as const, severity: "low" as const })),
    ...suggests.map((s) => ({ where: "流程建议", what: s, evidence: `suggests-${run.id}.json`,
      status: "unconfirmed" as const, severity: "low" as const })),
    ...failDocs.map((d) => ({
    where: d.name,
    what: `FAIL ${d.grades["FAIL"] ?? 0} 页（任一维度✗，以原图为准）`,
    evidence: `corpus-md-audit/matrices/AUDIT-MATRIX-${d.name}-FINAL.md`,
    status: "unconfirmed" as const, severity: "medium" as const,
  }))],
  verified: [
    `提示词经模板填充（铁律含 URL 签名/BLOCKED/UNRESOLVED 契约）`,
    `矩阵收割（行数/重复/Y 列/600dpi 计数）+ SUMMARY.md + STATUS.json`,
    `scopes 快照 corpus-md-audit/scopes/inv-${run.id}.json`,
  ],
  notCovered: [
    ...[...new Set(results.filter((r) => !r.ok).map((r) => `${r.unit} 未完成${blockedAbort ? "（BLOCKED 熔断）" : (r.raw ? "：" + r.raw.slice(0, 160) : "")}`))],
    ...badDocs.map((d) => `${d.name}: ${d.validate} ${d.detail}`),
    ...stats.docs.filter((d) => d.validate === "NO-ROWS").map((d) => `${d.name}: 未开工（0 行）`),
    ...inv.blocked.map((b) => `${b.name}：工作区未齐（png ${b.png}/${b.pages}、txt ${b.txt}/${b.pages}）`),
  ],
} satisfies WorkflowReport;
