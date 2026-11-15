/* 全转全审 · 方案对抗审计 workflow（2026-11-11 用户裁定）
   单子代理/轮：审计对象 = 本项目方案全套（方案文档/runbook/CHECKLIST/GOAL/audit_fleet.ts），
   不审 PDF。模型 = DeepSeek V4.1 Flash + Max Thinking（CreateWorkflow subagent_model）。
   每轮输出问题清单；编排者修复后重开一轮，直到 verdict=CLEAN。 */

interface PlanIssue {
  /** 出问题的文件与位置（file:行或节名） */
  where: string;
  /** 一句话：什么问题 */
  what: string;
  /** high=会导致执行失败或产出无效；medium=明显缺陷；low=改进建议 */
  severity: "high" | "medium" | "low";
  /** 可执行级修复建议 */
  suggestion: string;
}
interface PlanAuditResult {
  /** CLEAN=未发现问题；ISSUES=发现问题 */
  verdict: "CLEAN" | "ISSUES";
  issues: PlanIssue[];
  /** 实际核对过的东西（文件/命令/事实） */
  checked: string[];
}
interface WorkflowReport {
  conclusion: string;
  findings: { where: string; what: string; evidence: string; status: "verified" | "unconfirmed"; severity: "low" | "medium" | "high" }[];
  verified: string[];
  notCovered: string[];
}

const DOCS = [
  "/Users/aurolafly/ABC/dev-docs/2026-11-11-语料Markdown化与视觉审计方案.md",
  "/Users/aurolafly/ABC/dev-docs/2026-11-11-审计舰队workflow化runbook.md",
  "/Users/aurolafly/ABC/dev-docs/goals/20261111-全转全审-CHECKLIST.md",
  "/Users/aurolafly/ABC/dev-docs/goals/20261111-全转全审-GOAL.md",
  "/Users/aurolafly/ABC/tools/workflows/audit_fleet.ts",
  "/Users/aurolafly/ABC/tools/workflows/audit_units.sh",
  "/Users/aurolafly/ABC/tools/workflows/audit_harvest.sh",
  "/Users/aurolafly/ABC/tools/workflows/spotcheck.ts",
  "/Users/aurolafly/ABC/tools/workflows/count_rows.py",
  "/Users/aurolafly/ABC/tools/workflows/prep_shards.py",
  "/Users/aurolafly/.agents/skills/mineru/prompts/audit-subagent.md",
  "/Users/aurolafly/.agents/skills/mineru/runbooks/visual-audit.md",
];

phase("对抗审计方案全套");
const reviewer = agent("对抗审查员", {
  system: "你是对抗式审计员，是只读审查员，不是编排者。你的唯一任务是找出这套审计方案里的真问题——矛盾、不可执行步骤、与 skill 真值的偏差、与实际磁盘状态不符的假设、缺口、恢复协议漏洞、完成门设计缺陷。不要客气、不要总结优点；找不到问题时也要给出你核对过什么来证明 CLEAN 不是敷衍。硬性边界：禁止创建/启动/恢复/修改/取消任何 workflow；禁止运行 audit_fleet、spotcheck、plan_audit 或任何转换/渲染/审计脚本；禁止写任何文件。只做只读检查；任何需要真实运行才能确认的疑点，写进 findings 并标注「需编排者验证」，交回 Leader。",
});
const result = await reviewer.ask<PlanAuditResult>(
  [
    "审计对象是本项目的视觉审计方案全套（不是审计 PDF！审方案本身）。逐文件通读以下内容：",
    ...DOCS.map((d) => `- ${d}`),
    "",
    "【只读锁（硬性，违反=本次审计作废）】",
    "你是审查员，不是编排者：",
    "- 禁止创建/启动/恢复/修改/取消任何 workflow（CreateWorkflow/Amend/Resume 一律不许）；",
    "- 禁止运行 audit_fleet、spotcheck、plan_audit 或任何转换/渲染/审计脚本，禁止任何长任务；",
    "- 禁止写任何文件（不需要写草稿；只读判断不需要写权限）。",
    "允许：Read/Grep/Glob 读文件；只读命令（ls、pdfinfo、shasum、grep、wc -l 这类）。",
    "「可执行性」判断只做静态分析：读脚本、读文档、对照磁盘现状；任何必须真实运行才能确认的疑点，写进 findings 并明确标注「需编排者验证」，绝不自己跑。",
    "",
    "同时对照现实核对（只读方式，不要只信文字）：",
    "1) 方案里引用的脚本/路径是否真实存在、接口是否与文档一致（tools/workflows/*.sh、*.py、*.ts；/Volumes/D/audit-workspace 布局）；",
    "2) 方案声明的磁盘状态是否属实（corpus 68 .done？D 盘页图/切片计数？矩阵现状？legacy 64 页？）；",
    "3) 与 skill 真值（prompts/audit-subagent.md、runbooks/visual-audit.md）是否一致（铁律、六维度、F 码、600dpi 流程、并发安全设计）；",
    "4) 模型策略（RULE-009：GLM 5.3 Flash / DeepSeek V4.1 Flash，问供应商，Max Thinking）是否在方案中落实；",
    "5) 完成门 CHECKLIST 是否可验收、有无虚勾风险；",
    "6) 工作流程的可执行性：一个第一次接手的人按文档走，会不会卡在某个模糊步骤上。",
    "",
    "输出严格按 schema：verdict / issues[]（where,what,severity,suggestion）/ checked[]。",
    "只有当你真的逐项核对过且找不出问题时，才允许 verdict=CLEAN。",
  ].join("\n"),
);

phase("汇总对抗审计结果");
const high = result.issues.filter((i) => i.severity === "high");
const md = [
  `# 方案对抗审计（DeepSeek V4.1 Flash）`,
  "",
  `- 结论：${result.verdict}；问题 ${result.issues.length} 个（high ${high.length} / medium ${result.issues.filter((i) => i.severity === "medium").length} / low ${result.issues.filter((i) => i.severity === "low").length}）`,
  `- 核对过：${result.checked.length} 项`,
  "",
  ...(result.issues.length
    ? ["| 严重度 | 位置 | 问题 | 建议 |", "|---|---|---|---|",
       ...result.issues.sort((a, b) => (a.severity === "high" ? -1 : b.severity === "high" ? 1 : 0))
         .map((i) => `| ${i.severity} | ${i.where} | ${i.what} | ${i.suggestion} |`)]
    : ["（未发现问题）"]),
  "",
  "## 核对清单",
  ...result.checked.map((c) => `- ${c}`),
].join("\n");
await artifact.markdown("plan-audit", md, {
  title: "方案对抗审计报告",
  description: `verdict=${result.verdict}，issues=${result.issues.length}`,
  primary: true,
});

return {
  conclusion: result.verdict === "CLEAN"
    ? "对抗审计通过：方案全套未发现可执行性问题。"
    : `对抗审计发现 ${result.issues.length} 个问题（high ${high.length}），待修复后重审。`,
  findings: result.issues.map((i) => ({
    where: i.where, what: i.what, evidence: i.suggestion,
    status: "unconfirmed" as const, severity: i.severity === "high" ? "high" as const : i.severity === "medium" ? "medium" as const : "low" as const,
  })),
  verified: [`对抗审查员核对 ${result.checked.length} 项`, `模板与 runbook 与 skill 真值对照`],
  notCovered: ["审计舰队真实运行行为（本轮只审方案文本与磁盘状态，不审 PDF）"],
} satisfies WorkflowReport;
