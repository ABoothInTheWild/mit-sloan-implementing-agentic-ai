"""Turn each writeups/<slug>/draft.md into medium_blog.html for Medium's "Import a story".

Same shape as the IBM capstone write-ups: images point at absolute GitHub Pages URLs
(Medium's importer needs to fetch them), the italic line right after an image becomes
its caption, and cross-post placeholders (PART1_URL, ...) are filled from links.json.

    python writeups/build_html.py
"""
import html
import json
import re
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
PAGES = "https://aboothinthewild.github.io/mit-sloan-implementing-agentic-ai/writeups"
AUTHOR, PROFILE = "Alexander Booth", "https://medium.com/@aboothinthewild"
STYLE = ("body{max-width:720px;margin:40px auto;padding:0 16px;font:18px/1.6 -apple-system,Segoe UI,Roboto,sans-serif;color:#222}"
         "figure{margin:24px 0;text-align:center}img{max-width:100%;height:auto;border:1px solid #eee;border-radius:6px}"
         "figcaption{color:#666;font-size:14px;margin-top:8px}h1{font-size:30px;line-height:1.25}h2{font-size:23px;margin-top:36px}"
         "hr{border:none;border-top:1px solid #ddd;margin:36px 0}code{font-family:SFMono-Regular,Consolas,monospace;background:#f0f0f0;padding:1px 5px;border-radius:4px;font-size:.9em}")


def build(slug: str, links: dict) -> Path:
    src = (HERE / slug / "draft.md").read_text(encoding="utf-8")
    for key, url in links.items():
        src = src.replace(key, url)
    lines = src.splitlines()
    title = lines[0].lstrip("# ").strip()
    subtitle = lines[2].strip().strip("*")
    body_md = "\n".join(lines[3:]).strip()

    # image + following italic line -> <figure> with <figcaption>
    def fig(m):
        alt, file, cap = m.group(1), m.group(2), m.group(3)
        caption = f"<figcaption><em>{html.escape(cap)}</em></figcaption>" if cap else ""
        return (f'<figure><img src="{PAGES}/{slug}/{file}" alt="{html.escape(alt)}">'
                f"{caption}</figure>")
    body_md = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)\n(?:\*([^*\n]+)\*)?", fig, body_md)
    body = markdown.markdown(body_md, extensions=["sane_lists"])
    body = re.sub(r"<p>(<figure>.*?</figure>)</p>", r"\1", body, flags=re.S)
    body = body.replace("<hr />", "<hr>")

    t, d = html.escape(title), html.escape(subtitle)
    page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><meta name="author" content="{AUTHOR}">
<meta property="og:type" content="article"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}">
<style>{STYLE}</style>
</head><body><article>
<header><h1>{t}</h1><p><em>{d}</em></p></header>
<hr>
{body}
</article></body></html>
"""
    out = HERE / slug / "medium_blog.html"
    out.write_text(page, encoding="utf-8")
    return out


if __name__ == "__main__":
    links_file = HERE / "links.json"
    links = json.loads(links_file.read_text()) if links_file.exists() else {}
    for d in sorted(p for p in HERE.iterdir() if (p / "draft.md").exists()):
        print("wrote", build(d.name, links))
