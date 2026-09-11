#!/usr/bin/env python3
"""Quintessence mark assets and diagram plates.

Three-tier mark ladder, ruled 7 September 2026:
  full       the whole crystal            >= 45 px
  reduction  core plus five inner leaves  20 to 45 px
  micro      the rounded pentagon core    < 20 px

Rasterised through system Chrome so every plate keeps its exact aspect.
"""
import math, os
from playwright.sync_api import sync_playwright

SEAM = 4.5
INK = "#0F0F10"; BONE = "#EAE0C8"; PAPER = "#F8F8F8"; RULE = "#BDB4A2"; MUTE = "#7A7264"
CORAL = "#D96E6E"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ---------------- geometry ----------------
def pentagon(R):
    return [(R * math.sin(2 * math.pi * k / 5), -R * math.cos(2 * math.pi * k / 5)) for k in range(5)]

def shrink(poly, s):
    cx = sum(p[0] for p in poly) / len(poly); cy = sum(p[1] for p in poly) / len(poly)
    return [(cx + (x - cx) * s, cy + (y - cy) * s) for x, y in poly]

def rounded(poly, r):
    n = len(poly); pts = []
    for i in range(n):
        p = poly[i]; a = poly[i - 1]; b = poly[(i + 1) % n]
        va = (a[0] - p[0], a[1] - p[1]); vb = (b[0] - p[0], b[1] - p[1])
        la = math.hypot(*va) or 1; lb = math.hypot(*vb) or 1
        d = min(r, la / 2, lb / 2)
        pts.append(((p[0] + va[0] / la * d, p[1] + va[1] / la * d), p,
                    (p[0] + vb[0] / lb * d, p[1] + vb[1] / lb * d)))
    f = lambda q: f"{q[0]:.2f},{q[1]:.2f}"
    s = f"M{f(pts[0][2])}"
    for i in range(1, n + 1):
        A, p, B = pts[i % n]
        s += f" L{f(A)} Q{f(p)} {f(B)}"
    return s + " Z"

def leaf(poly, k=2.0):
    inner, s1, tip, s2 = poly
    M = ((inner[0] + tip[0]) / 2, (inner[1] + tip[1]) / 2)
    C1 = (M[0] + (s1[0] - M[0]) * k, M[1] + (s1[1] - M[1]) * k)
    C2 = (M[0] + (s2[0] - M[0]) * k, M[1] + (s2[1] - M[1]) * k)
    f = lambda q: f"{q[0]:.2f},{q[1]:.2f}"
    return f"M{f(inner)} Q{f(C1)} {f(tip)} Q{f(C2)} {f(inner)} Z"

def rhombus(y, L, Wd):
    return [(0, -y), (Wd / 2, -(y + L / 2)), (0, -(y + L)), (-Wd / 2, -(y + L / 2))]

def spine(y, L, hw):
    return [(0, -y), (hw, -(y + L * 0.45)), (0, -(y + L)), (-hw, -(y + L * 0.45))]

def branches(ybase, station, L, theta, hw=6.0):
    out = []; th = math.radians(theta)
    for sgn in (1, -1):
        ox = sgn * hw * 0.55; oy = -(ybase + station)
        dx = sgn * math.sin(th); dy = -math.cos(th)
        px, py = -dy, dx; wq = L / 1.618 / 2
        out.append([(ox, oy), (ox + dx * L / 2 + px * wq, oy + dy * L / 2 + py * wq),
                    (ox + dx * L, oy + dy * L), (ox + dx * L / 2 - px * wq, oy + dy * L / 2 - py * wq)])
    return out

def arm_polys():
    y = 15 + SEAM
    polys = [rhombus(y, 26, 26 / 1.618)]
    y += 26 + SEAM
    polys.append(spine(y, 47, 6.0))
    for station, L, theta in [(14, 21, 58), (30, 17, 58)]:
        polys += branches(y, station, L, theta)
    y += 47 + SEAM
    polys.append(rhombus(y, 18, 18 / 1.618))
    return polys, y + 18

POLYS, EXTENT = arm_polys()
YSHIFT = -((-EXTENT) + EXTENT * 0.809) / 2
BASE_KITE = rhombus(15 + SEAM, 26, 26 / 1.618)
CORE = rounded(shrink(pentagon(13), 0.84), 4.5)

def mark_full(cx, cy, size, colour, stroke_only=False, sw=1.0):
    sc = size / (2 * EXTENT)
    arms = "".join(f'<path d="{leaf(shrink(p, 0.84))}"/>' for p in POLYS)
    g = (f'<g transform="translate({cx:.2f},{cy + YSHIFT * sc:.2f}) scale({sc:.5f})" '
         f'fill="{"none" if stroke_only else colour}" stroke="{colour}" '
         f'stroke-width="{(sw if stroke_only else 1.0) / sc:.3f}" '
         f'stroke-linejoin="round" stroke-linecap="round"><path d="{CORE}"/>')
    for k in range(5):
        g += f'<g transform="rotate({72 * k})">{arms}</g>'
    return g + "</g>"

def mark_reduction(cx, cy, size, colour):
    """Core plus the five inner leaves. Its own extent is the kite tip."""
    ext = (15 + SEAM + 26)
    sc = size / (2 * ext)
    g = (f'<g transform="translate({cx:.2f},{cy:.2f}) scale({sc:.5f})" fill="{colour}" '
         f'stroke="{colour}" stroke-width="{1.0 / sc:.3f}" stroke-linejoin="round" '
         f'stroke-linecap="round"><path d="{CORE}"/>')
    for k in range(5):
        g += f'<g transform="rotate({72 * k})"><path d="{leaf(shrink(BASE_KITE, 0.84))}"/></g>'
    return g + "</g>"

def mark_micro(cx, cy, size, colour):
    """The rounded pentagon core alone."""
    sc = size / (2 * 13)
    return (f'<g transform="translate({cx:.2f},{cy:.2f}) scale({sc:.5f})" fill="{colour}" '
            f'stroke="{colour}" stroke-width="{0.8 / sc:.3f}" stroke-linejoin="round">'
            f'<path d="{CORE}"/></g>')

SANS = 'font-family="Helvetica Neue, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Georgia, Times New Roman, serif"'
LBL = f'{SANS} letter-spacing="1.7"'

PLATES = []
def write(name, w, h, body, bg=PAPER):
    svg = (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
           + (f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else "") + body + "</svg>")
    open(f"{name}.svg", "w").write(svg)
    PLATES.append((name, w, h))

# ---------------- standalone mark assets, transparent ground ----------------
for tone, col in (("ink", INK), ("bone", BONE)):
    write(f"mark-full-{tone}", 480, 480, mark_full(240, 240, 440, col), bg=None)
    write(f"mark-primary-{tone}", 480, 480, mark_reduction(240, 240, 430, col), bg=None)
    write(f"mark-reduction-{tone}", 480, 480, mark_reduction(240, 240, 430, col), bg=None)
    write(f"mark-micro-{tone}", 480, 480, mark_micro(240, 240, 400, col), bg=None)

ROS_EXT = 15 + SEAM + 26

# ---------------- plate: the two tiers ----------------
# The rosette is the mark, ruled 2026-09-08. The ladder that used to run three tiers
# now runs two: the mark holds down to 20 px, the core alone carries below that.
W, H = 1200, 470
b = ""
panels = [("THE ROSETTE", "20 PX AND ABOVE  ·  THE MARK", mark_reduction, 150),
          ("THE MICRO MARK", "BELOW 20 PX  ·  THE CORE ALONE", mark_micro, 118)]
pw, x0 = 470, 110
for i, (name, rng, fn, sz) in enumerate(panels):
    x = x0 + i * (pw + 40)
    b += f'<rect x="{x}" y="0" width="{pw}" height="300" fill="#FFFFFF" stroke="{RULE}" stroke-width="1"/>'
    b += fn(x + pw / 2, 150, sz, INK)
    b += f'<text x="{x}" y="332" fill="{INK}" font-size="13" {LBL}>{name}</text>'
    b += f'<text x="{x}" y="352" fill="{MUTE}" font-size="11" {LBL}>{rng}</text>'
row = [("64", mark_reduction, 64), ("40", mark_reduction, 40), ("28", mark_reduction, 28),
       ("20", mark_reduction, 20), ("16", mark_micro, 16), ("11", mark_micro, 11)]
b += f'<text x="20" y="386" fill="{MUTE}" font-size="11" {LBL}>ACTUAL SIZE  ·  THE LADDER AS IT SHIPS</text>'
xx = 20
for lab, fn, sz in row:
    b += fn(xx + 32, 412, sz, INK)
    b += f'<text x="{xx + 32}" y="452" text-anchor="middle" fill="{MUTE}" font-size="10" {LBL}>{lab} PX</text>'
    xx += 96
write("plate-tiers", W, H, b)

# ---------------- plate: clear space and scale ----------------
W, H = 1120, 560
b = ""
mk = 140; cxm, cym = 300, 250; pad = mk * 1.5 / 2; inner = mk / 2
b += (f'<rect x="{cxm-inner-pad}" y="{cym-inner-pad}" width="{2*(inner+pad)}" '
      f'height="{2*(inner+pad)}" fill="none" stroke="{RULE}" stroke-width="1.2" stroke-dasharray="7 5"/>')
b += f'<rect x="{cxm-inner}" y="{cym-inner}" width="{mk}" height="{mk}" fill="none" stroke="{RULE}" stroke-width="1"/>'
b += mark_reduction(cxm, cym, mk, INK)
ax = cxm - inner - pad; bx = cxm - inner
b += f'<line x1="{ax}" y1="{cym-inner-pad-16}" x2="{bx}" y2="{cym-inner-pad-16}" stroke="{INK}" stroke-width="1"/>'
for vx in (ax, bx):
    b += f'<line x1="{vx}" y1="{cym-inner-pad-21}" x2="{vx}" y2="{cym-inner-pad-11}" stroke="{INK}" stroke-width="1"/>'
b += f'<text x="{(ax+bx)/2}" y="{cym-inner-pad-26}" text-anchor="middle" fill="{INK}" font-size="12.5" {LBL}>1.5X</text>'
b += f'<text x="40" y="500" fill="{MUTE}" font-size="12" {LBL}>CLEAR SPACE  ·  1.5 MARK-HEIGHTS ON EVERY SIDE</text>'
b += f'<line x1="580" y1="60" x2="580" y2="470" stroke="{RULE}" stroke-width="1"/>'
sizes = [(140, "140 PX", mark_reduction), (72, "72 PX", mark_reduction),
         (32, "32 PX", mark_reduction), (16, "16 PX", mark_micro)]
x = 680
for sz, lab, fn in sizes:
    b += fn(x, 250, sz, INK)
    b += f'<text x="{x}" y="360" text-anchor="middle" fill="{MUTE}" font-size="11" {LBL}>{lab}</text>'
    x += sz / 2 + 84
b += f'<text x="640" y="500" fill="{MUTE}" font-size="12" {LBL}>SCALE  ·  THE TIER CHANGES AT TWENTY PIXELS</text>'
write("plate-clearspace", W, H, b)

# ---------------- plate: mark misuse ----------------
W, H = 1200, 500
cw, ch = 380, 190
b = ""
cells = [
    ("DO NOT ROTATE", lambda cx, cy: f'<g transform="rotate(26 {cx} {cy})">{mark_reduction(cx, cy, 112, INK)}</g>'),
    ("DO NOT OUTLINE", lambda cx, cy: mark_full(cx, cy, 112, INK, stroke_only=True, sw=1.6)),
    ("DO NOT DISTORT", lambda cx, cy: f'<g transform="translate({cx},{cy}) scale(1.5 0.7) translate({-cx},{-cy})">{mark_reduction(cx, cy, 112, INK)}</g>'),
    ("DO NOT RECOLOUR OFF-PALETTE", lambda cx, cy: mark_reduction(cx, cy, 112, "#2E7D32")),
    ("DO NOT ADD EFFECTS", lambda cx, cy: f'<g opacity="0.4">{mark_reduction(cx+5, cy+5, 112, "#7A7264")}</g>' + mark_reduction(cx, cy, 112, INK)),
    ("DO NOT SET THE ROSETTE BELOW 20 PX", lambda cx, cy: mark_reduction(cx, cy, 15, INK) + f'<text x="{cx}" y="{cy+38}" text-anchor="middle" fill="{MUTE}" font-size="10" {LBL}>USE THE MICRO MARK</text>'),
]
for i, (lab, draw) in enumerate(cells):
    col, row_i = i % 3, i // 3
    x = 20 + col * (cw + 20); y = 20 + row_i * (ch + 60)
    b += f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="none" stroke="{RULE}" stroke-width="1"/>'
    b += f'<text x="{x+14}" y="{y+24}" fill="{MUTE}" font-size="10.5" {LBL}>{i+1:02d}</text>'
    b += draw(x + cw / 2, y + ch / 2 + 6)
    b += f'<text x="{x}" y="{y+ch+26}" fill="{CORAL}" font-size="11" {LBL}>{lab}</text>'
write("plate-mark-misuse", W, H, b)

# ---------------- plate: the geometry law ----------------
W, H = 900, 660
b = ""
sc = 250 / (2 * ROS_EXT); cx0, cy0 = 450, 250
g = f'<g transform="translate({cx0},{cy0}) scale({sc:.5f})">'
g += (f'<circle cx="0" cy="0" r="{ROS_EXT}" fill="none" stroke="{RULE}" '
      f'stroke-width="{1.1/sc:.2f}" stroke-dasharray="{7/sc:.2f} {5/sc:.2f}"/>')
for k in range(5):
    ang = math.radians(72 * k - 90)
    g += (f'<line x1="0" y1="0" x2="{ROS_EXT*math.cos(ang):.1f}" y2="{ROS_EXT*math.sin(ang):.1f}" '
          f'stroke="{RULE}" stroke-width="{1.1/sc:.2f}"/>')
petal_out = f'<path d="{leaf(shrink(BASE_KITE, 0.84))}" fill="none" stroke="{INK}" stroke-width="{1.25/sc:.2f}"/>'
petal_con = (f'<path d="{rounded(shrink(BASE_KITE, 0.84), 0.1)}" fill="none" stroke="{RULE}" '
             f'stroke-width="{0.8/sc:.2f}" stroke-dasharray="{4/sc:.2f} {4/sc:.2f}"/>')
for k in range(5):
    g += f'<g transform="rotate({72*k})">{petal_con}{petal_out}</g>'
g += f'<path d="{CORE}" fill="none" stroke="{CORAL}" stroke-width="{1.7/sc:.2f}"/></g>'
b += g
notes = [("72°", "FIVE PETALS AT SEVENTY-TWO DEGREES"),
         ("13", "PENTAGON CORE, CIRCUMRADIUS"),
         ("φ", "EVERY PETAL A GOLDEN RHOMBUS, BOWED"),
         ("2.9", "CORNER RADIUS, EVERY CORNER"),
         ("84%", "PETALS DRAWN IN, THE SEAM"),
         ("45.5", "TIP RADIUS, THE EXTENT OF THE MARK")]
for i, (n, t) in enumerate(notes):
    col, row_i = i % 2, i // 2
    x = 46 + col * 430; y = 508 + row_i * 50
    b += f'<text x="{x}" y="{y}" fill="{INK}" {SERIF} font-size="22">{n}</text>'
    b += f'<text x="{x}" y="{y+18}" fill="{MUTE}" font-size="10" {LBL}>{t}</text>'
write("plate-geometry", W, H, b)

# ---------------- plate: colourways ----------------
W, H = 1200, 290
ways = [("PARCHMENT ON INK", INK, BONE), ("INK ON BONE", BONE, INK),
        ("BONE ON CORAL", CORAL, "#F8F8F8"), ("INK ON PAPER", "#FFFFFF", INK)]
cw = 285; b = ""
for i, (lab, bg, fg) in enumerate(ways):
    x = i * (cw + 20)
    b += f'<rect x="{x}" y="0" width="{cw}" height="228" rx="10" fill="{bg}"/>'
    if bg == "#FFFFFF":
        b += f'<rect x="{x}" y="0" width="{cw}" height="228" rx="10" fill="none" stroke="{RULE}" stroke-width="1"/>'
    b += mark_reduction(x + cw / 2, 114, 120, fg)
    b += f'<text x="{x}" y="258" fill="{MUTE}" font-size="10.5" {LBL}>{lab}</text>'
write("plate-colourways", W, H, b, bg=PAPER)

# ---------------- rasterise ----------------
with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME)
    for name, w, h in PLATES:
        pg = br.new_page(viewport={"width": int(w), "height": int(h)}, device_scale_factor=3)
        pg.goto("file://" + os.path.abspath(f"{name}.svg"))
        pg.screenshot(path=f"{name}.png", omit_background=True)
        pg.close()
        print(name, w, "x", h, os.path.getsize(f"{name}.png"))
    br.close()
