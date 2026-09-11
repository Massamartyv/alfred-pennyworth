"""Halftone screening in which the dot is the brand mark.

A conventional halftone varies the area of a circle to reproduce tone. This screen
varies the area of the Quintessence instead: the rounded pentagon core in the
shadows and midtones where dots are small, stepping up to the full rosette where
dots are large enough to carry the detail. The mark ladder made literal - the
image is built out of the brand at every scale.
"""
import math
import os

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

import fieldlib as F

INK = F.INK
PAPER = F.PAPER
BONE = F.BONE
CORAL = F.CORAL

CORE_R = 13.0                  # circumradius of the pentagon core, mark units
ROS_R = F.ROS_EXT              # tip radius of the full rosette, mark units

# Fraction of its own bounding disc that each shape actually inks, measured by
# rasterising the shape and counting. The rosette is mostly air, so a rosette and a
# core of equal diameter lay down very different amounts of ink. Sizing every dot
# from these figures is what keeps the tonal scale continuous when the screen steps
# from one shape to the other.
K_INK = {"core": 0.5032, "rosette": 0.1915}


def _diameter(cov, pitch, shape, gain):
    """Diameter that inks `cov` of the cell, for this shape. Area, not width."""
    return gain * math.sqrt(4.0 * pitch * pitch * cov / (math.pi * K_INK[shape]))


def _defs():
    """One core and one rosette in mark units, referenced by every dot."""
    leaves = "".join(
        f'<g transform="rotate({72 * k})"><path d="{F.leaf(F.shrink(F.PETAL, 0.84))}"/></g>'
        for k in range(5))
    return (f'<g id="htc"><path d="{F.CORE}"/></g>'
            f'<g id="htr"><path d="{F.CORE}"/>{leaves}</g>')


def _coverage(path, out_w, crop=None, gamma=1.0, contrast=1.0, invert=False,
              black=0.0, white=1.0):
    """Return a float array of ink coverage, 0 = paper, 1 = solid."""
    im = Image.open(path).convert("L")
    if crop:
        im = im.crop(crop)
    ratio = im.height / im.width
    out_h = int(round(out_w * ratio))
    im = im.resize((out_w, out_h), Image.LANCZOS)
    a = np.asarray(im, dtype=np.float32) / 255.0
    if invert:
        a = 1.0 - a
    cov = 1.0 - a                                    # dark pixels want big dots
    if (black, white) != (0.0, 1.0):                 # levels: use the full range
        cov = np.clip((cov - black) / max(1e-6, white - black), 0.0, 1.0)
    if contrast != 1.0:
        cov = np.clip((cov - 0.5) * contrast + 0.5, 0.0, 1.0)
    if gamma != 1.0:
        cov = np.clip(cov, 0.0, 1.0) ** gamma
    return np.clip(cov, 0.0, 1.0), out_w, out_h


def _cell_mean(cov, x, y, r):
    """Average coverage over a cell, so a dot answers to its whole square."""
    h, w = cov.shape
    x0, x1 = max(0, int(x - r)), min(w, int(x + r) + 1)
    y0, y1 = max(0, int(y - r)), min(h, int(y + r) + 1)
    if x0 >= x1 or y0 >= y1:
        return None
    return float(cov[y0:y1, x0:x1].mean())


def screen(src, out, out_w=760, pitch=11.0, angle=27.0, shape="ladder",
           ink=INK, ground=PAPER, ramp=None, gamma=1.0, contrast=1.0,
           crop=None, invert=False, gain=1.0, min_frac=0.10,
           ladder_cov=0.30, ladder_dir="highlight", dot_rot="fixed", rot0=0.0, scale=2, bleed=1.0,
           black=0.0, white=1.0):
    """Screen `src` into `out`.png with the mark as the dot.

    pitch       spacing of the screen in output pixels - the ruling
    angle       screen angle in degrees
    shape       'core'    every dot the pentagon core. Tonally the truest.
                'rosette' every dot the whole mark. Expressive, wants a coarse
                          pitch and a contrasty source.
                'ladder'  the mark in the highlights, dissolving to its own core
                          as the image darkens. Sized so the handoff is invisible.
    ladder_cov  coverage at which the screen changes shape
    ladder_dir  'highlight' the whole mark in the light, dissolving to its core as
                the image darkens; 'shadow' the reverse, the mark blooming open in
                the shadows where the dots are large enough to read it
    ramp        optional list of colours; the dot takes its tone from its coverage
    black,white input levels, applied to coverage before anything else
    gain        global dot-size multiplier; above 1.0 the image goes heavier
    """
    cov, w, h = _coverage(src, out_w, crop, gamma, contrast, invert, black, white)
    th = math.radians(angle)
    ca, sa = math.cos(th), math.sin(th)

    # Walk the lattice in screen space, then rotate each node into image space.
    diag = math.hypot(w, h)
    n = int(diag / pitch) + 2
    cx, cy = w / 2.0, h / 2.0
    cell_r = pitch * 0.5 * bleed
    dots = []
    for j in range(-n, n + 1):
        for i in range(-n, n + 1):
            u, v = i * pitch, j * pitch
            x = cx + u * ca - v * sa
            y = cy + u * sa + v * ca
            if not (-pitch <= x <= w + pitch and -pitch <= y <= h + pitch):
                continue
            c = _cell_mean(cov, x, y, cell_r)
            if c is None:
                continue
            sh = shape
            if shape == "ladder":
                lit = c <= ladder_cov
                sh = "rosette" if (lit if ladder_dir == "highlight" else not lit) else "core"
            size = _diameter(c, pitch, sh, gain)
            if size < pitch * min_frac:
                continue
            if dot_rot == "alt":
                r = rot0 + (36.0 if j % 2 else 0.0)
            elif dot_rot == "five":
                r = rot0 + 72.0 * ((i + 2 * j) % 5)
            else:
                r = rot0
            dots.append((x, y, size, r, c, sh))

    body = []
    for x, y, size, r, c, sh in dots:
        ref, ext = ("#htr", ROS_R) if sh == "rosette" else ("#htc", CORE_R)
        s = (size / 2.0) / ext
        col = ""
        if ramp:
            col = f' fill="{ramp[min(len(ramp) - 1, int(c * len(ramp)))]}"'
        body.append(f'<use href="{ref}" transform="translate({x:.1f},{y:.1f}) '
                    f'rotate({r:.0f}) scale({s:.4f})"{col}/>')

    svg_body = f'<g fill="{ink}">' + "".join(body) + "</g>"
    with open(f"{out}.svg", "w") as fh:
        fh.write(f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
                 f'xmlns="http://www.w3.org/2000/svg" '
                 f'xmlns:xlink="http://www.w3.org/1999/xlink">'
                 f'<defs>{_defs()}</defs>'
                 f'<rect width="{w}" height="{h}" fill="{ground}"/>{svg_body}</svg>')
    with sync_playwright() as p:
        br = p.chromium.launch(executable_path=F.CHROME)
        pg = br.new_page(viewport={"width": w, "height": h}, device_scale_factor=scale)
        pg.goto("file://" + os.path.abspath(f"{out}.svg"))
        pg.screenshot(path=f"{out}.png")
        pg.close()
        br.close()
    return os.path.abspath(f"{out}.png"), len(dots), (w, h)
