/* zcode-workflow
name: 全转全审·抽查复检
args:
  docs:
    type: json
    description: 本批要抽查的文档短名数组（必填）。每文档抽 ≥10%（最少 2 页，均匀取页）。
*/

/* 全转全审 · SPOTCHECK 抽查 workflow（C-05 配套，2026-11-11 v2）
   v2 变更：①独立清单（spotcheck_inv.py，不依赖 unsigned）②提示词给逐页绝对路径
   ③产出落盘 corpus-md-audit/SPOTCHECK.md（含文本层比对待填列）。 */

interface DocInfo { doc: string; name: string; pages: number }
interface SampleResult {
  /** 文档短名 */
  doc: string;
  /** 页码（1 基） */
  page: number;
  /** 该页内容要点 3–5 条（肉眼所见） */
  points: string[];
  /** 该页一个公式片段（原样抄写；无公式则空串） */
  formula: string;
}
interface SpotcheckResult {
  samples: SampleResult[];
  blocked: boolean;
  note: string;
}
interface WorkflowReport {
  conclusion: string;
  findings: { where: string; what: string; evidence: string; status: "verified" | "unconfirmed"; severity: "low" | "medium" | "high" }[];
  verified: string[];
  notCovered: string[];
}

const REPO = "~/ABC";
const WS = "<audit-workspace>";

const rawDocs = args.docs;
const DOCS: string[] = Array.isArray(rawDocs) ? rawDocs.filter((x): x is string => typeof x === "string") : [];

interface SampleSpec { doc: string; name: string; pages: number; sample: number[] }

function buildSamples(all: DocInfo[], filter: string[]): SampleSpec[] {
  return all.filter((d) => filter.includes(d.name)).map((d) => {
    const n = Math.max(2, Math.ceil(d.pages * 0.1));
    const step = Math.max(1, Math.floor(d.pages / n));
    const sample: number[] = [];
    for (let p = 1; p <= d.pages && sample.length < n; p += step) sample.push(p);
    while (sample.length < Math.min(n, d.pages)) sample.push(sample[sample.length - 1] + 1);
    return { doc: d.doc, name: d.name, pages: d.pages, sample };
  });
}

phase("抽查抽样与视觉复读");
const invRun = await world.run("python3", [`${REPO}/tools/workflows/spotcheck_inv.py`], { timeoutMs: 120000 });
if (invRun.exitCode !== 0) {
  return { conclusion: "清单读取失败，抽查未开工。", findings: [], verified: [], notCovered: ["全部"] } satisfies WorkflowReport;
}
const all = JSON.parse(invRun.stdout) as DocInfo[];
const specs = buildSamples(all, DOCS);
if (specs.length === 0) {
  return { conclusion: "NO-UNITS：args.docs 与已转换文档清单不相交。", findings: [], verified: [], notCovered: ["本批无对象"] } satisfies WorkflowReport;
}
const listText = specs.map((s) =>
  `- ${s.name}：` + s.sample.map((p) => `${WS}/${s.name}/_audit-pages/p${String(p).padStart(3, "0")}.png`).join(" , ")
).join("\n");
const result = await agent("抽查员").ask<SpotcheckResult>([
  "你是视觉抽查子代理。逐页 Read 下列页图文件（PNG 绝对路径已给全），**用你自己的视觉能力看**，按 schema 汇报。",
  "全部只读，不许修改任何文件。",
  "",
  "抽查清单（文档：页图路径）：",
  listText,
  "",
  "每页输出：points（3–5 条：你看到的标题/正文要点/公式/表图——必须是图上真实可见的内容），",
  "formula（该页一个公式片段，原样抄写；无公式则空串）。",
  "若 Read 返回 URL/纯文本而非图像 → 立即停止并返回 blocked=true，note 写 BLOCKED：Read 不注入图像。",
  "不许用 analyze_image/vision/OCR 替代；不许编造。",
].join("\n"));

const expectedRows: { doc: string; page: number }[] = [];
for (const s of specs) for (const p of s.sample) expectedRows.push({ doc: s.name, page: p });
const sampleMap = new Map<string, SampleResult>();
for (const s of result.samples) sampleMap.set(`${s.doc}#${s.page}`, s);
const missingCount = expectedRows.filter((e) => !sampleMap.has(`${e.doc}#${e.page}`)).length;
const mdLines = [
  "# SPOTCHECK — 抽查复读与文本层比对（C-05）",
  "",
  `- 抽样：${specs.length} 份文档 / ${expectedRows.length} 页（expected 清单）；实际回传 ${result.samples.length} 页；缺失 ${missingCount}；blocked=${result.blocked}`,
  "",
  "| 文档 | 页 | 视觉要点（Flash 子代理） | 公式片段 | pdftotext 文本层比对 | 结论 |",
  "|---|---|---|---|---|---|",
  ...expectedRows.map((e) => {
    const s = sampleMap.get(`${e.doc}#${e.page}`);
    return `| ${e.doc} | ${e.page} | ${s ? s.points.join("；").replace(/\|/g, "\\|") : "（缺失）"} | ${s ? (s.formula || "").replace(/\|/g, "\\|") : ""} | 待填 | 待填 |`;
  }),
];
const batchTag = DOCS.length ? DOCS.slice(0, 2).join("-").slice(0, 60) : "all";
await world.run("python3", [`${REPO}/tools/workflows/save_scope.py`,
  `${REPO}/corpus-md-audit/spotcheck-raw-${run.id}.json`, JSON.stringify(result)]);
await world.run("python3", [`${REPO}/tools/workflows/save_scope.py`,
  `${REPO}/corpus-md-audit/SPOTCHECK-${batchTag}.md`, mdLines.join("\n") + "\n"]);
await artifact.markdown("spotcheck", mdLines.join("\n"), { title: "抽查复读结果", primary: true });

return {
  conclusion: result.blocked
    ? "BLOCKED：抽查子代理 Read 不注入图像——视觉抽查无法进行（模型/管道问题，停手上报）。"
    : `抽查复读完成：expected ${expectedRows.length} 页 / 回传 ${result.samples.length} / 缺失 ${missingCount}；已写 corpus-md-audit/SPOTCHECK-${batchTag}.md。C-05 判据=缺失 0 且 grep -c 待填 == 0。`,
  findings: [],
  verified: [`抽样清单（每文档 ≥10%、≥min(2,pages) 页、逐页绝对路径）`,
             `SPOTCHECK-${batchTag}.md 与 spotcheck-raw-${run.id}.json 已落盘`],
  notCovered: [
    "要点与 pdftotext 文本层的逐页比对（Leader 步骤）",
    ...(missingCount ? [`缺失回传 ${missingCount} 页`] : []),
    ...(result.blocked ? ["全部视觉抽查"] : []),
  ],
} satisfies WorkflowReport;
