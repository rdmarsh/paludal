#!/usr/bin/env python3
"""Build index.html from ideas.md: python3 build.py"""
import html
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "ideas.md"
OUT = HERE / "index.html"


UNITS = {
    "bl": "blink", "bt": "beat", "br": "breath", "ch": "chime", "mt": "moment",
    "p": "pace", "un": "unc", "di": "dig", "sp": "span", "ul": "ulna", "ir": "iter", "na": "navis", "px": "parax",
    "li": "lib", "cu": "cub", "te": "tep",
    "vi": "vis", "op": "opus", "vg": "vig", "pr": "pres", "ri": "riv", "os": "onus",
    "im": "imp", "gx": "grex", "la": "lam", "vo": "vox", "ag": "ager", "tu": "turn",
}
ROOTS = dict(zip("nubtqphsoedl", "nil un bi tri quad pent hex sept oct enn dek el".split()))
UNIT_RE = "|".join(sorted(UNITS, key=len, reverse=True))
# A prefixed symbol (tqop) is always a unit; a bare one (p, op) only straight after a number or / or ·,
# so ordinary words are left alone.
SYMBOL = re.compile(
    rf"\b([nubtqphsoedl]+[qc])({UNIT_RE})(?![A-Za-z0-9_])|(?:(?<=\d )|(?<=[\d/·]))({UNIT_RE})(?![A-Za-z0-9_])|(?<=[\dXE] )(°t)|(?<=[\dXE])(°t)"
)


def expand(m):
    prefix, unit = (m.group(1), m.group(2)) if m.group(1) else (None, m.group(3) or m.group(4) or m.group(5))
    name = "tep (degrees from freezing)" if unit == "°t" else UNITS[unit]
    if prefix:
        roots = "".join(ROOTS[ch] for ch in prefix[:-1])
        power = "".join("0123456789XE"["nubtqphsoedl".index(ch)] for ch in prefix[:-1])
        mul = prefix[-1] == "q"
        name = f"{roots}{'qua' if mul else 'cia'}-{name} ({'×' if mul else '÷'} 10^{power})"
    # Typeset form: the q / c of a prefix is shown as Primel's arrow (tqop -> t↑op)
    shown = f"{prefix[:-1]}{'↑' if mul else '↓'}{unit}" if prefix else m.group(0)
    return f'<abbr title="{name}">{shown}</abbr>'


def inline(text):
    text = html.escape(text, quote=False)
    text = text.replace("&lt;br&gt;", "<br>")  # line breaks inside table cells
    # Expand unit symbols outside `code` only, so plain-text examples stay as written
    text = "`".join(part if i % 2 else SYMBOL.sub(expand, part) for i, part in enumerate(text.split("`")))
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*]+)\*(?![*\w])", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"\[([^\]]+)\]\((#[\w-]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r'(?<![">])(https?://[^\s)<]+)', r'<a href="\1">\1</a>', text)
    return text


LIST_ITEM = r"^\s*(?:[-*]|\d+\.)\s+"


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def render_table(rows):
    head, body = cells(rows[0]), [cells(r) for r in rows[2:]]
    out = ['<div class="table-wrap"><table><thead><tr>']
    out += [f"<th>{inline(c)}</th>" for c in head]
    out.append("</tr></thead><tbody>")
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_list(items, tag="ul"):
    """items: list of (indent, text). Builds nested lists; the outer one is <tag>."""
    out, stack = [], []
    for indent, text in items:
        while stack and indent < stack[-1]:
            out.append(f"</li></{tag if len(stack) == 1 else 'ul'}>")
            stack.pop()
        if not stack or indent > stack[-1]:
            out.append(f"<{tag if not stack else 'ul'}><li>")
            stack.append(indent)
        else:
            out.append("</li><li>")
        out.append(inline(text))
    out += ["</li></ul>"] * (len(stack) - 1) + ([f"</li></{tag}>"] if stack else [])
    return "".join(out)


def parse(md):
    """Returns intro html and a tree of sections: {level, title, blocks, children, has_table}."""
    root = {"level": 0, "title": "", "blocks": [], "children": [], "has_table": False}
    stack = [root]
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            level = len(m.group(1))
            while stack[-1]["level"] >= level:
                stack.pop()
            sec = {"level": level, "title": m.group(2).strip(), "blocks": [], "children": [], "has_table": False}
            stack[-1]["children"].append(sec)
            stack.append(sec)
            i += 1
            continue
        cur = stack[-1]
        if line.startswith("```"):
            lang, src = line[3:].strip(), []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                src.append(lines[i])
                i += 1
            i += 1
            src = html.escape("\n".join(src), quote=False)
            if lang == "mermaid":
                cur["blocks"].append(("diagram", f'<pre class="mermaid">{src}</pre>'))
                for s in stack:
                    s["has_table"] = True
            else:
                cur["blocks"].append(("code", f"<pre><code>{src}</code></pre>"))
            continue
        if line.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i])
                i += 1
            cur["blocks"].append(("table", render_table(rows)))
            for s in stack:
                s["has_table"] = True
            continue
        if re.match(LIST_ITEM, line):
            tag = "ol" if re.match(r"^\d+\.", line) else "ul"
            items = []
            while i < len(lines) and (re.match(LIST_ITEM, lines[i]) or (re.match(r"^\s+\S", lines[i]) and items)):
                lm = re.match(r"^(\s*)(?:[-*]|\d+\.)\s+(.*)", lines[i])
                if lm:
                    items.append((len(lm.group(1)), lm.group(2)))
                else:  # continuation line
                    items[-1] = (items[-1][0], items[-1][1] + " " + lines[i].strip())
                i += 1
            cur["blocks"].append(("list", render_list(items, tag)))
            continue
        if line.strip():
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|```|\s*[-*]\s|\d+\.\s|\s*\|)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            text = " ".join(para)
            kind = "why" if text.startswith("**Why:**") else "decided" if "Decided" in text or "decided)" in text else "para"
            cur["blocks"].append((kind, f"<p>{inline(text)}</p>"))
            if kind in ("decided", "why"):
                for s in stack:
                    s["has_table"] = True
            continue
        i += 1
    return root


def is_part(sec):
    return sec["level"] == 1 and re.match(r"Part \d", sec["title"])


def render_section(sec, parent_slug=""):
    sid = slug((parent_slug + " " if parent_slug else "") + sec["title"])
    cls = "has-table" if sec["has_table"] else "no-table"
    out = [f'<section class="{cls}" id="{sid}">', f'<h{sec["level"] + 1}>{inline(sec["title"])}</h{sec["level"] + 1}>']
    for kind, h in sec["blocks"]:
        out.append(f'<div class="block {kind}">{h}</div>')
    for child in sec["children"]:
        out.append(render_section(child, "" if is_part(sec) else sid))  # chapters get short ids: #prefixes
    out.append("</section>")
    return "\n".join(out)


def build():
    root = parse(SRC.read_text())
    toc = []
    for sec in root["children"]:
        sid = slug(sec["title"])
        subs = "".join(
            f'<li><a href="#{slug(("" if is_part(sec) else sid + " ") + c["title"])}">{inline(c["title"])}</a></li>'
            for c in sec["children"]
        )
        toc.append(
            f'<li class="{"has-table" if sec["has_table"] else "no-table"}"><a href="#{sid}">{inline(sec["title"])}</a>'
            + (f"<ul>{subs}</ul>" if subs else "")
            + "</li>"
        )
    intro = "\n".join(f'<div class="block {k}">{h}</div>' for k, h in root["blocks"])
    body = "\n".join(render_section(s) for s in root["children"])
    body = body.replace('<section class="', '<section class="lead ', 1)  # the opening section is the intro
    OUT.write_text(TEMPLATE.replace("{{TOC}}", "\n".join(toc)).replace("{{INTRO}}", intro).replace("{{BODY}}", body))
    print(f"wrote {OUT.name}")


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Paludal Units</title>
<!-- ↊ ↋ (U+218A/B) are missing from most system fonts; load just those two glyphs -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Symbols&text=%E2%86%8A%E2%86%8B&display=swap">
<style>
:root {
  --bg: #fbfaf7; --fg: #1f1d1a; --muted: #6b665e; --line: #e4e0d8;
  --panel: #f3f0ea; --accent: #9a4d1f; --row: #f7f5f0;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #181715; --fg: #e9e6e0; --muted: #9b958b; --line: #34312c;
    --panel: #211f1c; --accent: #e09a62; --row: #1d1c19;
  }
}
:root[data-theme="dark"] {
  --bg: #181715; --fg: #e9e6e0; --muted: #9b958b; --line: #34312c;
  --panel: #211f1c; --accent: #e09a62; --row: #1d1c19;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--fg);
  font: 15px/1.5 system-ui, -apple-system, "Segoe UI", "Noto Sans Symbols", sans-serif; }
.layout { display: grid; grid-template-columns: 220px minmax(0, 1fr); max-width: 1200px; margin: 0 auto; }
nav { position: sticky; top: 0; height: 100vh; overflow-y: auto; padding: 24px 16px;
  border-right: 1px solid var(--line); font-size: 14px; }
nav h1 { font-size: 17px; margin: 0 0 12px; }
nav ul { list-style: none; padding: 0; margin: 0; }
nav ul ul { padding-left: 12px; margin: 2px 0 6px; font-size: 13px; }
nav a { color: var(--fg); text-decoration: none; display: block; padding: 2px 0; }
nav a:hover { color: var(--accent); }
nav ul ul a { color: var(--muted); }
.conv { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 4px 8px; align-items: center;
  margin: 0 0 16px; font-size: 13px; color: var(--muted); }
.conv input { width: 100%; font: inherit; font-size: 14px; color: var(--fg); background: var(--bg);
  border: 1px solid var(--line); border-radius: 4px; padding: 3px 6px; font-variant-numeric: tabular-nums; }
.conv input:focus { outline: 2px solid var(--accent); outline-offset: -1px; }
.conv .hint { grid-column: 1 / -1; font-size: 12px; }
.toggle { display: flex; gap: 8px; align-items: center; margin: 0 0 16px; font-size: 13px; color: var(--muted); cursor: pointer; }
main { padding: 24px 32px 80px; min-width: 0; }
h2 { font-size: 28px; margin: 56px 0 8px; color: var(--accent); }
h3 { font-size: 22px; margin: 40px 0 8px; padding-bottom: 6px; border-bottom: 2px solid var(--accent); }
h4 { font-size: 17px; margin: 28px 0 8px; }
h5, h6 { font-size: 15px; margin: 20px 0 6px; }
section { scroll-margin-top: 16px; }
p, ul { margin: 6px 0 10px; }
ul { padding-left: 20px; }
code { background: var(--panel); padding: 1px 4px; border-radius: 3px; font-size: 13px; }
a { color: var(--accent); }
abbr { text-decoration: underline dotted var(--muted); text-underline-offset: 2px; cursor: help; }
.intro { color: var(--muted); }
.table-wrap { overflow-x: auto; margin: 10px 0 16px; }
pre { background: var(--panel); padding: 8px 12px; border-radius: 4px; overflow-x: auto; font-size: 13px; }
pre.mermaid { background: none; padding: 0; margin: 10px 0 16px; text-align: center; }
table { border-collapse: collapse; font-size: 14px; font-variant-numeric: tabular-nums; }
th, td { border: 1px solid var(--line); padding: 4px 10px; text-align: left; vertical-align: top; }
th { background: var(--panel); font-weight: 600; }
tbody tr:nth-child(even) { background: var(--row); }
td:empty, th:empty { border-top: none; border-bottom: none; background: var(--bg); padding: 0 4px; }
.decided p { border-left: 3px solid var(--accent); padding-left: 10px; }
.why p { margin-top: -4px; padding-left: 13px; color: var(--muted); font-size: 14px; }
.why strong { color: var(--fg); }
body.tables-only .block.para, body.tables-only .block.list, body.tables-only section.no-table,
body.tables-only nav li.no-table, body.tables-only .intro { display: none; }
body.tables-only section.lead, body.tables-only section.lead .block { display: block; }
@media (max-width: 760px) {
  .layout { display: block; }
  nav { position: static; height: auto; border-right: none; border-bottom: 1px solid var(--line); padding: 16px; }
  main { padding: 8px 16px 60px; }
}
</style>
</head>
<body>
<div class="layout" id="top">
<nav>
<h1><a href="#top">Paludal units</a></h1>
<label class="toggle"><input type="checkbox" id="tables-only"> Hide notes (show only tables, decisions and reasons)</label>
<div class="conv">
<label for="conv-dec">Decimal</label><input id="conv-dec" inputmode="decimal" autocomplete="off" placeholder="20.5">
<label for="conv-doz">Dozenal</label><input id="conv-doz" autocomplete="off" placeholder="18;6">
<span class="hint" id="conv-hint">Type in either box. X = ten, E = eleven. Rounded to 3 places.</span>
</div>
<ul>
{{TOC}}
</ul>
</nav>
<main>
<div class="intro">{{INTRO}}</div>
{{BODY}}
</main>
</div>
<script>
// Not remembered: the page always opens with everything showing.
const box = document.getElementById("tables-only");
box.checked = false;  // browsers can restore a checkbox's state on reload
box.addEventListener("change", () => document.body.classList.toggle("tables-only", box.checked));
</script>
<script>
// Number converter, rounded to 3 places each way: 10.3333333 shows as X;4, and 0;4 as 0.333.
(() => {
  const DIG = "0123456789XE", dec = document.getElementById("conv-dec"),
    doz = document.getElementById("conv-doz"), hint = document.getElementById("conv-hint");
  const HELP = "Type in either box. X = ten, E = eleven. Rounded to 3 places.";
  function toDoz(x) {
    const n = Math.round(Math.abs(x) * 1728);  // whole 1/1000 (doz) steps
    let i = Math.floor(n / 1728), f = n % 1728, s = "";
    do { s = DIG[i % 12] + s; i = Math.floor(i / 12); } while (i > 0);
    s = s.replace(/\\B(?=(.{3})+$)/g, ",");  // group in threes: 100,000
    const frac = (DIG[Math.floor(f / 144)] + DIG[Math.floor(f / 12) % 12] + DIG[f % 12]).replace(/0+$/, "");
    return (x < 0 && n ? "-" : "") + s + (frac ? ";" + frac : "");
  }
  function fromDoz(t) {
    t = t.trim().replace(/,/g, "").toUpperCase().replace(/↊|A|T/g, "X").replace(/↋|B/g, "E");
    const m = t.match(/^(-?)([0-9XE]*)(?:;([0-9XE]*))?$/);
    if (!m || (m[2] + (m[3] || "")) === "") return null;
    let v = 0;
    for (const c of m[2]) v = v * 12 + DIG.indexOf(c);
    let p = 1;
    for (const c of m[3] || "") { p /= 12; v += DIG.indexOf(c) * p; }
    return m[1] ? -v : v;
  }
  const near = (a, b) => Math.abs(a - b) < 1e-9 * Math.max(1, Math.abs(a));
  dec.addEventListener("input", () => {
    const t = dec.value.trim().replace(/,/g, ""), v = Number(t);
    if (t === "") { doz.value = ""; hint.textContent = HELP; return; }
    if (!isFinite(v) || !/^-?[0-9]*[.]?[0-9]*$/.test(t)) { hint.textContent = "Decimal uses digits 0-9 and a dot."; return; }
    doz.value = toDoz(v);
    hint.textContent = near(fromDoz(doz.value), v) ? "Exact." : "Rounded to 3 dozenal places.";
  });
  doz.addEventListener("input", () => {
    const v = fromDoz(doz.value);
    if (doz.value.trim() === "") { dec.value = ""; hint.textContent = HELP; return; }
    if (v === null) { hint.textContent = "Dozenal uses 0-9, X, E and a semicolon (18;6)."; return; }
    const r = Number(v.toFixed(3));
    dec.value = r.toLocaleString("en-US", { maximumFractionDigits: 3 });
    hint.textContent = near(r, v) ? "Exact." : "Rounded to 3 decimal places.";
  });
})();
</script>
<script type="module">
// Diagrams: mermaid needs plain colours, so read them from the page's tokens (light or dark).
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
const css = getComputedStyle(document.documentElement), v = name => css.getPropertyValue(name).trim();
mermaid.initialize({
  startOnLoad: false, theme: "base",
  themeVariables: {
    background: v("--bg"), primaryColor: v("--panel"), primaryTextColor: v("--fg"),
    primaryBorderColor: v("--accent"), lineColor: v("--muted"), textColor: v("--fg"),
    secondaryColor: v("--row"), tertiaryColor: v("--bg"), clusterBkg: v("--row"), clusterBorder: v("--line"),
    edgeLabelBackground: v("--bg"), fontFamily: getComputedStyle(document.body).fontFamily, fontSize: "14px",
  },
});
await mermaid.run();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
