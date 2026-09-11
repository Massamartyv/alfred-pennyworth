"""Shared geometry and render pipeline for Five Points field studies.

Every shape in the identity descends from one morpheme: the golden rhombus. The
rosette is that rhombus repeated five times at 72 degrees around a rounded
pentagon core. Fields are built only from pieces of the mark - the petal (leaf)
and the mote - never from new shapes.
"""
import math
import os

from playwright.sync_api import sync_playwright

PHI = (1 + 5 ** 0.5) / 2
SEAM = 4.5

INK = "#0F0F10"
BONE = "#EAE0C8"
PAPER = "#F8F8F8"
RULE = "#BDB4A2"
MUTE = "#7A7264"
CORAL = "#D96E6E"
GREIGE = "#B5AFA0"

# Tonal ramps. A field is one hue in three or four steps, never a mix of voices.
BONE_RAMP = ["#F4EEDF", "#EDE3CE", "#E3D6B9", "#D6C6A2"]
CORAL_RAMP = ["#F6DDDD", "#EFC2C2", "#E49B9B", "#D96E6E"]
INK_RAMP = ["#2A261D", "#383225", "#4A4334", "#5D5442"]
GREIGE_RAMP = ["#EDEAE2", "#DFDACD", "#CDC6B4", "#B5AFA0"]

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

SANS = 'font-family="Helvetica Neue, Helvetica, Arial, sans-serif"'
SERIF = 'font-family="Georgia, Times New Roman, serif"'
LBL = f'{SANS} letter-spacing="1.7"'


# ---------------------------------------------------------------- geometry
def pentagon(R):
    return [(R * math.sin(2 * math.pi * k / 5), -R * math.cos(2 * math.pi * k / 5))
            for k in range(5)]


def shrink(poly, s):
    cx = sum(p[0] for p in poly) / len(poly)
    cy = sum(p[1] for p in poly) / len(poly)
    return [(cx + (x - cx) * s, cy + (y - cy) * s) for x, y in poly]


def rounded(poly, r):
    n = len(poly)
    pts = []
    for i in range(n):
        p = poly[i]
        a = poly[i - 1]
        b = poly[(i + 1) % n]
        va = (a[0] - p[0], a[1] - p[1])
        vb = (b[0] - p[0], b[1] - p[1])
        la = math.hypot(*va) or 1
        lb = math.hypot(*vb) or 1
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
    """Bow a four-point rhombus into a leaf by pulling the sides outward."""
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


# ---------------------------------------------------------------- the pieces
def rosette(cx, cy, size, colour, rot=0, opacity=1.0):
    """The mark. `size` is tip-to-tip across the full rosette."""
    sc = size / (2 * ROS_EXT)
    g = (f'<g transform="translate({cx:.2f},{cy:.2f}) rotate({rot}) scale({sc:.5f})" '
         f'fill="{colour}" opacity="{opacity}"><path d="{CORE}"/>')
    for k in range(5):
        g += f'<g transform="rotate({72 * k})"><path d="{leaf(shrink(PETAL, 0.84))}"/></g>'
    return g + "</g>"


def _piece(poly, cx, cy, height, colour, rot, opacity):
    ys = [p[1] for p in poly]
    xs = [p[0] for p in poly]
    h = max(ys) - min(ys)
    midy = (max(ys) + min(ys)) / 2
    midx = (max(xs) + min(xs)) / 2
    sc = height / h
    return (f'<g transform="translate({cx:.2f},{cy:.2f}) rotate({rot}) scale({sc:.5f}) '
            f'translate({-midx:.2f},{-midy:.2f})" fill="{colour}" opacity="{opacity}">'
            f'<path d="{leaf(poly)}"/></g>')


def petal(cx, cy, height, colour, rot=0, opacity=1.0):
    """One leaf, drawn from its own centre. `height` is tip to tip.
    rot=0 stands the leaf upright; the long axis points at (rot + 90) degrees."""
    return _piece(shrink(PETAL, 0.84), cx, cy, height, colour, rot, opacity)


def mote(cx, cy, height, colour, rot=0, opacity=1.0):
    """The small leaf from the mark's outer ring. Same law, shorter and fatter."""
    return _piece(shrink(MOTE, 0.84), cx, cy, height, colour, rot, opacity)


PETAL_ASPECT = 1 / PHI   # width is roughly height / phi


# ---------------------------------------------------------------- composition
def clip(cid, x, y, w, h, r=14):
    return f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'


def panel(cid, x, y, w, h, ground, r=14):
    """Open a clipped, rounded panel. Close it yourself with `</g>`."""
    return (clip(cid, x, y, w, h, r)
            + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{ground}"/>'
            + f'<g clip-path="url(#{cid})">')


def torus(draw, cx, cy, sw, sh=None):
    """Emit `draw(x, y)` at nine toroidal positions so a tile of sw x sh repeats
    seamlessly. Any shape crossing an edge reappears on the opposite edge, so
    there is never a visible seam. `draw` takes (x, y) and returns SVG."""
    sh = sh if sh is not None else sw
    out = ""
    for dx in (-sw, 0, sw):
        for dy in (-sh, 0, sh):
            out += draw(cx + dx, cy + dy)
    return out


def tile_pattern(pid, sw, sh, body_fn, ground=None):
    """Define an SVG <pattern> of sw x sh whose content is body_fn() drawn in
    tile space. Fill any rect with url(#pid) to repeat it."""
    inner = (f'<rect width="{sw}" height="{sh}" fill="{ground}"/>' if ground else "")
    return (f'<pattern id="{pid}" width="{sw}" height="{sh}" patternUnits="userSpaceOnUse">'
            f'{inner}{body_fn()}</pattern>')


# ---------------------------------------------------------------- render
def render(name, w, h, body, bg=PAPER, scale=2, defs=""):
    """Write name.svg and rasterise it to name.png at the exact viewport."""
    svg = (f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'xmlns="http://www.w3.org/2000/svg"><defs>{defs}</defs>'
           + (f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else "")
           + body + "</svg>")
    with open(f"{name}.svg", "w") as fh:
        fh.write(svg)
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=CHROME)
        pg = br.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
        pg.goto("file://" + os.path.abspath(f"{name}.svg"))
        pg.screenshot(path=f"{name}.png")
        pg.close()
        br.close()
    return os.path.abspath(f"{name}.png")
