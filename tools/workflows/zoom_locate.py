#!/usr/bin/env python3
"""zoom_locate.py — 600dpi 定点局部裁片工具（执行协议 §3.2 三级定位的实现）。

用法（三选一）:
  # A. content_list bbox 定位（kit 文档首选）：在提取文本里找最像的块，裁其 bbox
  python3 zoom_locate.py <doc名> --page 12 --text "V_p" 
  # B. PDF 文本层锚定：搜原文邻近词拿坐标
  python3 zoom_locate.py <doc名> --page 12 --anchor "such fields"
  # C. 手工坐标（Flash 半页报位后的复核）：pt 坐标 (原点左上)
  python3 zoom_locate.py <doc名> --page 12 --xy 320,450,540,500

产出: <audit-workspace>/<doc>/_zoom/LOC-pNNN-<序号>.png + stdout 路径
_MARGIN 默认外扩：上下 40pt 左右 90pt（--tight 收窄为 15/30）。
"""
import fitz, glob, json, os, re, sys

REPO = "~/ABC"
WS = "<audit-workspace>"


def find_pdf(doc_name):
    for c in glob.glob(f"{REPO}/corpus/**/{doc_name}.pdf", recursive=True):
        return c
    return None


def find_content_list(doc_name):
    for c in glob.glob(f"{REPO}/corpus-md/**/{doc_name}/content_list.json", recursive=True):
        return c
    return None


def norm_text(s):
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = re.sub(r"[^a-zA-Z0-9]+", " ", s)
    return set(w for w in s.lower().split() if len(w) > 1)


def render(pdf, page1, rect, tag, dpi=600):
    doc = fitz.open(pdf)
    page = doc[page1 - 1]
    clip = fitz.Rect(*rect) & page.rect
    pix = page.get_pixmap(dpi=dpi, clip=clip, colorspace=fitz.csGRAY)
    out_dir = f"{WS}/{tag_doc}/_zoom"
    os.makedirs(out_dir, exist_ok=True)
    out = f"{out_dir}/LOC-p{page1:03d}-{tag}.png"
    pix.save(out)
    return out, pix.width, pix.height


if __name__ == "__main__":
    doc_name = sys.argv[1]
    pdf = find_pdf(doc_name)
    if not pdf:
        sys.exit(f"找不到 PDF: {doc_name}")
    tag_doc = doc_name
    args = sys.argv[2:]
    page1 = int(args[args.index("--page") + 1])
    tight = "--tight" in args
    my, mx = (15, 30) if tight else (40, 90)

    if "--xy" in args:
        x0, y0, x1, y1 = map(float, args[args.index("--xy") + 1].split(","))
        rects = [(x0, y0, x1, y1)]
        tag = "manual"
    elif "--anchor" in args:
        anchor = args[args.index("--anchor") + 1]
        doc = fitz.open(pdf)
        hits = doc[page1 - 1].search_for(anchor)
        if not hits:
            sys.exit(f"文本层锚 {anchor!r} 在 p{page1} 无命中")
        r = hits[0]
        rects = [(max(0, r.x0 - mx * 2), max(0, r.y0 - my), r.x1 + mx * 3, r.y1 + my)]
        tag = re.sub(r"\W+", "", anchor)[:12] or "anchor"
    elif "--text" in args:
        snippet = args[args.index("--text") + 1]
        cl = find_content_list(doc_name)
        if not cl:
            sys.exit("无 content_list.json（parse_large 文档）——改用 --anchor 文本层锚定")
        blocks = [b for b in json.load(open(cl)) if b.get("page_idx", -1) == page1 - 1]
        target = norm_text(snippet)
        best, best_score = None, 0.0
        for b in blocks:
            txt = " ".join(p.get("content", "") for p in b.get("content", []) if isinstance(p, dict)) \
                  if isinstance(b.get("content"), list) else str(b.get("content", ""))
            score = len(target & norm_text(txt)) / max(1, len(target))
            if score > best_score:
                best, best_score = b, score
        if not best or best_score < 0.34:
            sys.exit(f"content_list 无匹配块（best={best_score:.2f}）——改用 --anchor 或 --xy")
        bb = best.get("bbox", [0, 0, 0, 0])
        rects = [(max(0, bb[0] - mx), max(0, bb[1] - my), bb[2] + mx, bb[3] + my)]
        tag = re.sub(r"\W+", "", snippet)[:12] or "block"
    else:
        sys.exit(__doc__)

    for i, rect in enumerate(rects, 1):
        out, w, h = render(pdf, page1, rect, f"{tag}-{i}" if len(rects) > 1 else tag)
        print(f"crop: {out} ({w}x{h}, rect={tuple(round(v,1) for v in rect)})")
