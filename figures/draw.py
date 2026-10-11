# Draws figures/clock.svg, figures/compass.svg and figures/idea.svg. Run from the repo root: python3 figures/draw.py
# Colours are the light theme; the classes (fg, muted, accent, line, panel) let the web pages recolour them.
import math
FG, MUTED, LINE, ACCENT, PANEL = "#1f1d1a", "#6b665e", "#e4e0d8", "#9a4d1f", "#f3f0ea"
DIG = "0123456789XE"
FONT = 'font-family="system-ui, -apple-system, Segoe UI, sans-serif"'

def pt(deg, r):  # degrees clockwise from the top
    a = math.radians(deg)
    return round(r * math.sin(a), 2), round(-r * math.cos(a), 2)

def head(title, desc, vb):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="320" role="img" '
            f'color="{FG}" {FONT}>', f'<title>{title}</title>', f'<desc>{desc}</desc>']

def ticks(n, r1, r2, width, cls, colour, skip=None):
    out = [f'<g class="{cls}" color="{colour}" stroke="currentColor" stroke-width="{width}" stroke-linecap="round">']
    for i in range(n):
        if skip and i % skip == 0: continue
        x1, y1 = pt(360 * i / n, r1); x2, y2 = pt(360 * i / n, r2)
        out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
    return out + ['</g>']

# ---- Clock: 24-hour dial, 0 (midnight) at the bottom, 6 (noon) at the top, clockwise
t = (11, 9, 1, 7)                        # E91;7
mark = lambda m: (m - 6) * 30            # dial position in marks -> degrees from the top
hands = [t[0] + t[1] / 12 + t[2] / 144 + t[3] / 1728,   # hand n points at digit n, plus the fraction after it
         t[1] + t[2] / 12 + t[3] / 144, t[2] + t[3] / 12, t[3]]
s = head("Paludal clock showing E91;7",
         "A 24-hour dial with twelve marks, 0 (midnight) at the bottom and 6 (noon) at the top, "
         "numbers running clockwise. Four hands, each twelve times faster than the last, each pointing at "
         "one digit of the time: hand 1 just before 0 (E), hand 2 just past 9, hand 3 between 1 and 2, "
         "hand 4 on 7. The time is E91;7, about 23:31.", "-130 -130 260 260")
s.append(f'<circle class="panel" color="{PANEL}" r="118" fill="currentColor"/>')
s.append(f'<circle class="line" color="{LINE}" r="118" fill="none" stroke="currentColor" stroke-width="2"/>')
s += ticks(144, 108, 112, 0.8, "muted", MUTED, skip=12)
s += ticks(12, 102, 113, 2.5, "fg", FG)
s.append('<g fill="currentColor" font-size="17" font-weight="600" text-anchor="middle" dominant-baseline="central">')
for k in range(12):
    x, y = pt(mark(k), 88)
    s.append(f'<text x="{x}" y="{y}">{DIG[k]}</text>')
s.append('</g>')
s.append(f'<g class="muted" color="{MUTED}" fill="currentColor" font-size="9" text-anchor="middle">'
         '<text y="-61">noon</text><text y="68">midnight</text>'
         '<text x="-62" y="-11">dawn</text><text x="62" y="-11">dusk</text></g>')
s.append(f'<text y="-34" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor">E91;7</text>')
def hand(deg, length, width, cls=None, colour=None, tail=12):
    x, y = pt(deg, length); bx, by = pt(deg + 180, tail)
    g = f' class="{cls}" color="{colour}"' if cls else ''
    return f'<line{g} x1="{bx}" y1="{by}" x2="{x}" y2="{y}" stroke="currentColor" stroke-width="{width}" stroke-linecap="round"/>'
s.append(hand(mark(hands[0]), 50, 6.5))
s.append(hand(mark(hands[1]), 68, 4.5))
s.append(hand(mark(hands[2]), 84, 2.5))
s.append(hand(mark(hands[3]), 98, 1.5, "accent", ACCENT, tail=18))
s.append(f'<circle r="4.5" fill="currentColor"/><circle class="accent" color="{ACCENT}" r="2" fill="currentColor"/>')
s.append('</svg>')
open("figures/clock.svg", "w").write("\n".join(s) + "\n")

# ---- Compass: bearings in turns, north at the top, clockwise
pts = [("N", "000", 0), ("NE", "160", 1.5), ("E", "300", 3), ("SE", "460", 4.5),
       ("S", "600", 6), ("SW", "760", 7.5), ("W", "900", 9), ("NW", "X60", 10.5)]
s = head("Compass points in turns",
         "A compass rose with north at the top. Bearings are three dozenal digits of a turn: north 000, "
         "north-east 160, east 300, south-east 460, south 600, south-west 760, west 900, north-west X60. "
         "The ring has twelve marks of 0;1 turn (100) each.", "-150 -150 300 300")
s.append(f'<circle class="line" color="{LINE}" r="100" fill="none" stroke="currentColor" stroke-width="2"/>')
s += ticks(144, 96, 100, 0.8, "muted", MUTED, skip=12)
s += ticks(12, 90, 100, 2.5, "fg", FG)
s.append(f'<g class="muted" color="{MUTED}" fill="currentColor" font-size="9" text-anchor="middle" dominant-baseline="central">')
for k in range(12):
    if k % 3 == 0: continue
    x, y = pt(k * 30, 78)
    s.append(f'<text x="{x}" y="{y}">{DIG[k]}00</text>')
s.append('</g>')
def arm(deg, length, half, cls, colour):
    tip = pt(deg, length); l = pt(deg - 90, half); r = pt(deg + 90, half)
    return [f'<path class="panel" color="{PANEL}" d="M0 0 L{r[0]} {r[1]} L{tip[0]} {tip[1]} Z" fill="currentColor"/>',
            f'<g class="{cls}" color="{colour}" stroke="currentColor" stroke-width="1" stroke-linejoin="round">',
            f'<path d="M0 0 L{l[0]} {l[1]} L{tip[0]} {tip[1]} Z" fill="currentColor"/>',
            f'<path d="M{l[0]} {l[1]} L{tip[0]} {tip[1]} L{r[0]} {r[1]} Z" fill="none"/>', '</g>']
for name, b, m in pts:
    if m % 3: s += arm(m * 30, 52, 9, "muted", MUTED)
for name, b, m in pts:
    if not m % 3: s += arm(m * 30, 86, 12, "accent" if name == "N" else "fg", ACCENT if name == "N" else FG)
s.append('<g fill="currentColor" text-anchor="middle" dominant-baseline="central">')
for name, b, m in pts:
    cardinal = m % 3 == 0
    x, y = pt(m * 30, 124 if cardinal else 120)
    size = 16 if cardinal else 12
    s.append(f'<text x="{x}" y="{y - 6}" font-size="{size}" font-weight="{700 if cardinal else 600}">{name}</text>')
    s.append(f'<text class="muted" color="{MUTED}" x="{x}" y="{y + 9}" font-size="11">{b}</text>')
s.append('</g>')
s.append('</svg>')
open("figures/compass.svg", "w").write("\n".join(s) + "\n")

# ---- The idea: the day gives the blink, light gives the pace, a cube of water gives the lib; every step is twelve
s = head("How Paludal is built",
         "A chain of five boxes from top to bottom. The day (24 hours) divided by 100,000 (twelve to the fifth) "
         "gives the blink, 0.347 s. Light travels 2 × 10^7 paces a blink, which gives the pace, 1.45 m. A cube "
         "0;1 pace on each side is the cub, 1.77 L. A cub of water weighs about a lib, 1.77 kg. Below, a bar "
         "one pace long is split into twelve uncs, and the first unc is drawn larger, split into twelve digs.",
         "0 0 320 486")
boxes = [("day", "24 hours", "the Earth", "fg", FG),
         ("blink", "time · 0.347 s", "base unit", "accent", ACCENT),
         ("pace", "length · 1.45 m", "base unit", "accent", ACCENT),
         ("cub", "volume · 1.77 L", "", "fg", FG),
         ("lib", "mass · 1.77 kg", "base unit", "accent", ACCENT)]
steps = [("÷ 100,000", "(twelve to the fifth)"), ("light travels", "2 × 10⁷ paces a blink"),
         ("a cube 0;1 pace", "on each side"), ("filled with water,", "weighs ≈ 1 lib")]
X, W, H, GAP = 12, 140, 46, 30
for i, (name, size, note, cls, colour) in enumerate(boxes):
    y = 8 + i * (H + GAP)
    s.append(f'<rect class="panel" color="{PANEL}" x="{X}" y="{y}" width="{W}" height="{H}" rx="8" fill="currentColor"/>')
    s.append(f'<rect class="{cls}" color="{colour}" x="{X}" y="{y}" width="{W}" height="{H}" rx="8" fill="none" '
             f'stroke="currentColor" stroke-width="{2 if cls == "accent" else 1.2}"/>')
    s.append(f'<text x="{X + 12}" y="{y + 20}" font-size="15" font-weight="700" fill="currentColor">{name}</text>')
    s.append(f'<text class="muted" color="{MUTED}" x="{X + 12}" y="{y + 37}" font-size="11" fill="currentColor">{size}</text>')
    if note:
        s.append(f'<text class="muted" color="{MUTED}" x="{X + W - 10}" y="{y + 20}" font-size="9" '
                 f'text-anchor="end" fill="currentColor">{note}</text>')
    if i < len(steps):
        ax, y1, y2 = X + 28, y + H + 2, y + H + GAP - 3
        s.append(f'<g class="muted" color="{MUTED}" stroke="currentColor" fill="none" stroke-width="1.5" '
                 f'stroke-linecap="round" stroke-linejoin="round"><line x1="{ax}" y1="{y1}" x2="{ax}" y2="{y2}"/>'
                 f'<path d="M{ax - 4} {y2 - 5} L{ax} {y2} L{ax + 4} {y2 - 5}"/></g>')
        a, b = steps[i]
        s.append(f'<text x="{X + W + 14}" y="{y + H + 9}" font-size="11" fill="currentColor">{a}'
                 f'<tspan class="muted" color="{MUTED}" x="{X + W + 14}" dy="14">{b}</tspan></text>')
# The ruler: one pace in twelve uncs, the first unc in twelve digs
top = 8 + 5 * (H + GAP) + 6
L0, L1 = 12, 308
u = (L1 - L0) / 12
s.append(f'<text x="{L0}" y="{top}" font-size="12" font-weight="600" fill="currentColor">Every step is twelve</text>')
y = top + 14
s.append(f'<rect class="panel" color="{PANEL}" x="{L0}" y="{y}" width="{L1 - L0}" height="14" fill="currentColor"/>')
s.append(f'<rect class="accent" color="{ACCENT}" x="{L0}" y="{y}" width="{u:.2f}" height="14" fill="currentColor" opacity="0.35"/>')
s.append(f'<g class="fg" color="{FG}" stroke="currentColor" stroke-width="1">'
         f'<rect x="{L0}" y="{y}" width="{L1 - L0}" height="14" fill="none"/>' +
         "".join(f'<line x1="{L0 + k * u:.2f}" y1="{y}" x2="{L0 + k * u:.2f}" y2="{y + 14}"/>' for k in range(1, 12)) + '</g>')
s.append(f'<text class="muted" color="{MUTED}" x="{L1}" y="{y - 4}" font-size="10" text-anchor="end" fill="currentColor">'
         '1 pace = 10 unc (12 dec)</text>')
z = y + 40
s.append(f'<g class="muted" color="{MUTED}" stroke="currentColor" stroke-width="0.8" stroke-dasharray="2 2">'
         f'<line x1="{L0}" y1="{y + 14}" x2="{L0}" y2="{z}"/><line x1="{L0 + u:.2f}" y1="{y + 14}" x2="{L1}" y2="{z}"/></g>')
s.append(f'<rect class="panel" color="{PANEL}" x="{L0}" y="{z}" width="{L1 - L0}" height="14" fill="currentColor"/>')
s.append(f'<g class="accent" color="{ACCENT}" stroke="currentColor" stroke-width="1">'
         f'<rect x="{L0}" y="{z}" width="{L1 - L0}" height="14" fill="none"/>' +
         "".join(f'<line x1="{L0 + k * u:.2f}" y1="{z}" x2="{L0 + k * u:.2f}" y2="{z + 14}"/>' for k in range(1, 12)) + '</g>')
s.append(f'<text class="muted" color="{MUTED}" x="{L1}" y="{z + 27}" font-size="10" text-anchor="end" fill="currentColor">'
         '1 unc (12.1 cm) = 10 dig (≈ 1 cm each)</text>')
s.append('</svg>')
open("figures/idea.svg", "w").write("\n".join(s) + "\n")
