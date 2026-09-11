#!/usr/bin/env python3
"""Pattern direction, second pass. Anthropic-manner: few elements, dramatic scale,
tonal layers of one hue, forms bleeding off the frame, generous air. No hard tessellation."""
import math, os
from playwright.sync_api import sync_playwright

PHI = (1 + 5 ** 0.5) / 2
SEAM = 4.5
INK = "#0F0F10"; BONE = "#EAE0C8"; PAPER = "#F8F8F8"; RULE = "#BDB4A2"; MUTE = "#7A7264"
CORAL = "#D96E6E"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# tonal ramps — one hue, several steps. The Anthropic move.
BONE_RAMP = ["#F4EEDF", "#EDE3CE", "#E3D6B9", "#D6C6A2"]
CORAL_RAMP = ["#F6DDDD", "#EFC2C2", "#E49B9B", "#D96E6E"]
INK_RAMP = ["#2A261D", "#383225", "#4A4334", "#5D5442"]

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

CORE = rounded(shrink(pentagon(13), 0.84), 4.5)
PETAL = rhombus(15 + SEAM, 26, 26 / PHI)
MOTE = rhombus(101.5, 18, 18 / PHI)
ROS_EXT = 15 + SEAM + 26

def rosette(cx, cy, size, colour, rot=0, opacity=1.0):
    sc = size / (2 * ROS_EXT)
    g = (f'<g transform="translate({cx:.2f},{cy:.2f}) rotate({rot}) scale({sc:.5f})" '
         f'fill="{colour}" opacity="{opacity}"><path d="{CORE}"/>')
    for k in range(5):
        g += f'<g transform="rotate({72 * k})"><path d="{leaf(shrink(PETAL, 0.84))}"/></g>'
    return g + "</g>"

def petal(cx, cy, height, colour, rot=0, opacity=1.0):
    """One bowed petal, drawn from its own centre at a given tip-to-tip height."""
    poly = shrink(PETAL, 0.84)
    ys = [p[1] for p in poly]; xs = [p[0] for p in poly]
    h = max(ys) - min(ys); midy = (max(ys) + min(ys)) / 2; midx = (max(xs) + min(xs)) / 2
    sc = height / h
    return (f'<g transform="translate({cx:.2f},{cy:.2f}) rotate({rot}) scale({sc:.5f}) '
            f'translate({-midx:.2f},{-midy:.2f})" fill="{colour}" opacity="{opacity}">'
            f'<path d="{leaf(poly)}"/></g>')

def mote(cx, cy, height, colour, rot=0, opacity=1.0):
    poly = shrink(MOTE, 0.84)
    ys = [p[1] for p in poly]; xs = [p[0] for p in poly]
    h = max(ys) - min(ys); midy = (max(ys) + min(ys)) / 2; midx = (max(xs) + min(xs)) / 2
    sc = height / h
    return (f'<g transform="translate({cx:.2f},{cy:.2f}) rotate({rot}) scale({sc:.5f}) '
            f'translate({-midx:.2f},{-midy:.2f})" fill="{colour}" opacity="{opacity}">'
            f'<path d="{leaf(poly)}"/></g>')

SANS = 'font-family="Helvetica Neue, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Georgia, Times New Roman, serif"'
LBL = f'{SANS} letter-spacing="1.7"'

PLATES = []
def write(name, w, h, body, bg=PAPER):
    svg = (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">'
           + (f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else "") + body + "</svg>")
    open(f"{name}.svg", "w").write(svg)
    PLATES.append((name, w, h))

# ================================================================ the four patterns
def clip(cid, x, y, w, h, r=14):
    return f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'

# --- A. THE CROP: one leaf at scale, the whole mark as counterpoint.
def bloom(cid, x, y, w, h, ramp, ground):
    g = clip(cid, x, y, w, h) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{ground}"/>'
    g += f'<g clip-path="url(#{cid})">'
    g += rosette(x - w * 0.20, y + h * 1.16, w * 2.15, ramp[1], rot=-18)
    g += rosette(x + w * 0.79, y + h * 0.25, h * 0.17, ramp[3], rot=14)
    return g + "</g>"

# --- B. THE DRIFT: leaves carried on a current. Six of them, each one legible.
def drift(cid, x, y, w, h, ramp, ground):
    g = clip(cid, x, y, w, h) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{ground}"/>'
    g += f'<g clip-path="url(#{cid})">'
    n, span_ = 6, w * 1.24
    amp, lam = h * 0.17, w * 1.5
    for i in range(n):
        t = i / (n - 1)
        px = x - w * 0.10 + t * span_
        ph = 2 * math.pi * (px - x) / lam
        py = y + h * 0.50 + amp * math.sin(ph)
        ang = math.degrees(math.atan2(amp * (2 * math.pi / lam) * math.cos(ph), 1))
        size = h * (0.30 - 0.23 * t)
        g += petal(px, py, size, ramp[min(3, int(t * 3.4))], rot=ang + 90)
    return g + "</g>"

# --- C. THE OVERLAP: three petals, legible, two deliberate crossings, air around.
def overlap(cid, x, y, w, h, ramp, ground, tone=None):
    g = clip(cid, x, y, w, h) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{ground}"/>'
    g += f'<g clip-path="url(#{cid})">'
    lay = [(0.26, 0.36, 0.62, -30, 1), (0.46, 0.60, 0.50, 30, 2), (0.72, 0.30, 0.40, -64, 3)]
    for fx, fy, fs, rot, t in lay:
        g += petal(x + w * fx, y + h * fy, h * fs, ramp[t], rot=rot, opacity=0.74)
    return g + "</g>"

# --- D. THE RULE: the mote band, undulating. Spacing holds the motes apart.
def rule_band(cid, x, y, w, h, ramp, ground, n=26, band=None):
    bh = band if band else h
    by = y + (h - bh) / 2
    g = clip(cid, x, y, w, h) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{ground}"/>'
    g += f'<g clip-path="url(#{cid})">'
    step = w / n
    amp, lam = bh * 0.26, w * 0.5
    size = step * 0.62
    for i in range(n + 1):
        px = x + i * step
        ph = 2 * math.pi * (px - x) / lam
        py = by + bh * 0.5 + amp * math.sin(ph)
        ang = math.degrees(math.atan2(amp * (2 * math.pi / lam) * math.cos(ph), 1))
        sz = size * (0.78 + 0.42 * (0.5 + 0.5 * math.cos(ph)))
        g += mote(px, py, sz, ramp[3] if i % 5 == 0 else ramp[2], rot=ang + 90)
    return g + "</g>"


# --- E. THE FAN: petals swept round an off-frame pivot. The dynamic field.
def fan(cid, x, y, w, h, ramp, ground, n=6):
    """An arc swept round a pivot below the frame. The dynamic field."""
    g = clip(cid, x, y, w, h) + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{ground}"/>'
    g += f'<g clip-path="url(#{cid})">'
    px, py = x + w * 0.50, y + h * 1.30
    a0, a1, r = 203.0, 337.0, h * 0.95
    for i in range(n):
        t = i / (n - 1)
        a = math.radians(a0 + (a1 - a0) * t)
        cx, cy = px + r * math.cos(a), py + r * math.sin(a)
        size = h * (0.40 - 0.20 * t)
        g += petal(cx, cy, size, ramp[min(3, int(t * 3.6))], rot=math.degrees(a) + 90)
    return g + "</g>"

# ================================================================ plate: the kit
W, H = 1240, 1330
b = ""
pw, ph = 600, 400
cells = [
    ("THE CROP", "ONE LEAF AT SCALE, THE MARK AS COUNTERPOINT", "bloom", BONE_RAMP, PAPER, 0, 0),
    ("THE DRIFT", "SIX LEAVES ON A CURRENT, LARGE TO SMALL", "drift", CORAL_RAMP, "#FBF4F1", 640, 0),
    ("THE FAN", "SWEPT ROUND A PIVOT OUTSIDE THE FRAME", "fan", BONE_RAMP, PAPER, 0, 480),
    ("THE OVERLAP", "THREE PETALS, TWO CROSSINGS, AIR AROUND", "overlap", BONE_RAMP, "#FFFFFF", 640, 480),
    ("THE RULE", "THE MOTE BAND, UNDULATING", "rule", None, INK, 0, 960),
]
FN = {"bloom": bloom, "drift": drift, "overlap": overlap, "fan": fan}
for i, (name, sub, key, ramp, ground, ox, oy) in enumerate(cells):
    cid = f"p{i}"
    if key == "rule":
        b += rule_band(cid, ox, oy, 1240, 250, ["#4A4437", "#6E6552", "#C9BC9C", BONE], ground, n=26, band=180)
        yy = oy + 250
    else:
        b += FN[key](cid, ox, oy, pw, ph, ramp, ground)
        yy = oy + ph
    b += f'<text x="{ox + 4}" y="{yy + 32}" fill="{INK}" font-size="13" {LBL}>{name}</text>'
    b += f'<text x="{ox + 4}" y="{yy + 54}" fill="{MUTE}" font-size="10.5" {LBL}>{sub}</text>'
write("p2-fields", W, H, b)

# ================================================================ plate: in use
W, H = 1240, 980
b = ""
# a cover — one leaf at scale, the type in the air it leaves
b += clip("u1", 0, 0, 600, 420) + f'<rect width="600" height="420" rx="14" fill="{PAPER}"/>'
b += f'<g clip-path="url(#u1)">{petal(452, 148, 306, BONE_RAMP[1], rot=-30)}'
b += f'{rosette(46, 44, 30, INK)}</g>'
b += (f'<text x="34" y="330" fill="{INK}" {SERIF} font-size="33">We bring the city</text>'
      f'<text x="34" y="372" fill="{INK}" {SERIF} font-size="33">to your door.</text>')
b += f'<text x="4" y="452" fill="{MUTE}" font-size="10.5" {LBL}>A COVER  ·  ONE LEAF, WHOLE</text>'

# a section opener on ink — the arc over a title
b += fan("u2", 640, 0, 600, 420, INK_RAMP, INK)
b += f'<g clip-path="url(#u2)"><text x="674" y="372" fill="{BONE}" {SERIF} font-size="31">Operations</text></g>'
b += f'<text x="640" y="452" fill="{MUTE}" font-size="10.5" {LBL}>A SECTION OPENER  ·  THE ARC ON INK</text>'

# a card back — the drift
b += drift("u3", 0, 510, 380, 300, CORAL_RAMP, "#FBF4F1")
b += f'<text x="4" y="842" fill="{MUTE}" font-size="10.5" {LBL}>CARD BACK  ·  THE DRIFT</text>'

# a pull quote — the overlap behind
b += overlap("u4", 420, 510, 380, 300, BONE_RAMP, "#FFFFFF")
b += f'<text x="420" y="842" fill="{MUTE}" font-size="10.5" {LBL}>A PULL PAGE  ·  THE OVERLAP</text>'

# a tile — the mark alone, no field
b += clip("u5", 840, 510, 400, 300) + f'<rect x="840" y="510" width="400" height="300" rx="14" fill="{CORAL}"/>'
b += f'<g clip-path="url(#u5)">{rosette(1040, 660, 128, "#FBEDED")}</g>'
b += f'<text x="840" y="842" fill="{MUTE}" font-size="10.5" {LBL}>A TILE  ·  NO FIELD AT ALL</text>'

# the rule as a divider
b += rule_band("u6", 0, 880, 1240, 100, ["#4A4437", "#6E6552", "#C9BC9C", BONE], INK, n=24, band=76)
write("p2-use", W, H, b)


# ================================================================ plate: the kit, numbered (for the deck)
W, H = 1240, 1130
b = ""
NUM = [("bloom", BONE_RAMP, PAPER, 0, 0), ("drift", CORAL_RAMP, "#FBF4F1", 640, 0),
       ("fan", BONE_RAMP, PAPER, 0, 440), ("overlap", BONE_RAMP, "#FFFFFF", 640, 440)]
for i, (key, ramp, ground, ox, oy) in enumerate(NUM):
    b += FN[key](f"k{i}", ox, oy, 600, 400, ramp, ground)
    b += (f'<text x="{ox + 22}" y="{oy + 40}" fill="{MUTE}" font-size="17" {LBL}>'
          f'0{i + 1}</text>')
b += rule_band("k4", 0, 880, 1240, 250, ["#4A4437", "#6E6552", "#C9BC9C", BONE], INK, n=26, band=180)
b += f'<text x="22" y="918" fill="{RULE}" font-size="17" {LBL}>05</text>'
write("p2-kit", W, H, b)


# ================================================================ plate: the cover field
W, H = 950, 1000
b = fan("cv", 0, 0, 950, 1000, INK_RAMP, INK, n=7)
write("p2-cover", W, H, b, bg=INK)

with sync_playwright() as p:
    br = p.chromium.launch(executable_path=CHROME)
    for name, w, h in PLATES:
        pg = br.new_page(viewport={"width": int(w), "height": int(h)}, device_scale_factor=3)
        pg.goto("file://" + os.path.abspath(f"{name}.svg"))
        pg.screenshot(path=f"{name}.png", omit_background=True)
        pg.close()
        print(name, w, "x", h, os.path.getsize(f"{name}.png"))
    br.close()
