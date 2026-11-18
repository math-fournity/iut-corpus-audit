# 裁决书册（adjudication-books）

裁决批 1–15 的裁决书入册处：`批N-裁决书.md`（批2 实为 `批2a-裁决书.md`，批2 第二波并入批3）。

## 册目与子项数

| 册 | 子项 | 说明 |
|---|---|---|
| 批1 | 140 | **复合批次**：核心=ATS-I 31项zoom·修正版（120 子主张，成立75/不成立43/看不清2）+ 同轮卫星裁决（LANA遗留600dpi 7 / LANA-p9重裁 2 / Joshi 5页 10 / p4真裁复核 1）。2026-11-12 早晨 workflow 命名尚未统一，五个 run 合成一册 |
| 批2a | 65 | 17项zoom（三文档 zoomOpen 全清） |
| 批3 | 226 | 107项zoom（含批2 第二波余量） |
| 批4 | 105 | 64项zoom |
| 批5 | 121 | 91项zoom |
| 批6 | 96 | 66项zoom |
| 批7 | 281 | 110项zoom |
| 批8 | 244 | 120项zoom（续跑合并） |
| 批9 | 250 | 124项zoom |
| 批10 | 289 | 120项zoom（续跑合并） |
| 批11 | 435 | 120项zoom+交叉红2页 |
| 批12 | 451 | 120项zoom |
| 批13 | 244 | 120项zoom（405pp 32–260 页） |
| 批14 | 395 | 90项zoom（收官裁决，405pp 260–405 页） |
| 批15 | 7 | 单项微裁决（Y2017 p170） |
| 批16 | 242 | S4⑤ 12项历史「看不清」600dpi 微裁决（回溯原始主张全文：成立167 / 不成立66 / unresolvable@600dpi 9） |

合计 3507 子项（批1–15 共 3265 子项 + 批16 共 242 子项）。

## 溯源方法

- **权威渲染器**：`tools/publish/render_adjudication_books_db.py`——直接读 ZCode cli journal
  （`~/.zcode/cli/db/db.sqlite` 只读）`dwf_run.result_json`，零模型成本、确定性；同名多 run
  取 completed 且 findings 最多者。
- 历史版：`tools/publish/render_adjudication_books.py`（v3，扫 rollout/artifacts 的 `<result>`
  通知块）——已被 DB 版取代，保留作交叉验证（批5–11 两版逐项一致）。
- 每册头部「来源」行记录 run ID；批1 的五个组件 run ID 在各小节头。
- 矩阵行内的「已裁决(批N)」token 承载结论；裁决书提供逐项实见细节。
