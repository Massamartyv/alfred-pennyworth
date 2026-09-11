"""The ruled system. Four fields and one screen, all ruled 2026-09-08.

Nothing in here is a candidate. Anything a deck draws, it draws from this file, so the
identity book and the capabilities deck cannot drift apart.

Ruled out and deliberately absent: the Crop, the Arc, the Measure, the Rule, the
five-fold wreath and the scatter. Dividers are plain hairlines.
"""
import math
import sys

sys.path.insert(0, '.')
import fieldlib as F
import halftone as H

# ---------------------------------------------------------------- the screen
# The house ruling, expressed as dots across the image rather than as a pixel pitch,
# so the same screen reproduces at any size. 88 across is the 10pt ruling measured off
# the specimen that was ruled.
DOTS_ACROSS = 88


def screen(src, out, width=880, crop=None, negative=True, **kw):
    """Screen a photograph at the house ruling. Negative - bone on ink - is the default
    register; pass negative=False for ink on paper where the page is already light."""
    args = dict(out_w=width, pitch=width / DOTS_ACROSS, angle=27, shape="ladder",
                crop=crop, scale=2)
    if negative:
        args.update(invert=True, ink=F.BONE, ground=F.INK,
                    black=0.06, white=0.92, gamma=1.35)
    else:
        args.update(black=0.0, white=0.74, gamma=1.6)
    args.update(kw)
    return H.screen(src, out, **args)


# ---------------------------------------------------------------- the fields
SKEW, RADIUS = 25, 0.298          # the Trefoil, as drawn and ruled


def _trefoil_places(h, spin=0):
    r = RADIUS * h
    for k in range(3):
        t = math.radians(spin + 120 * k - 90)
        yield r * math.cos(t), r * math.sin(t), math.degrees(t) - 180 + SKEW


def trefoil(cx, cy, h, spin=0, colour="#DCCFB2"):
    """Three leaves pinwheeling about one centre. The crossings make the third tone and
    the triple overlap the fourth, so the tonal steps are earned rather than declared."""
    out = ""
    for dx, dy, rot in _trefoil_places(h, spin):
        out += ('<g style="mix-blend-mode:multiply">'
                + F.petal(cx + dx, cy + dy, h, colour, rot=rot, opacity=0.62) + "</g>")
    return out


def trefoil_field(x, y, w, h, period=460, ground=F.PAPER, cid="tf"):
    """The seamless repeat. Two scales on a half-drop; every cell drawn one ring beyond
    the frame so a form crossing an edge arrives from its neighbour."""
    body = F.panel(cid, x, y, w, h, ground)
    cells = [(0, 0, 194, 0), (period / 2, period / 2, 118, 55)]
    for i in range(-1, int(w // period) + 2):
        for j in range(-1, int(h // period) + 2):
            for ox, oy, s, spin in cells:
                body += trefoil(x + ox + i * period, y + oy + j * period, s, spin)
    return body + "</g>"


def tumbling_air(x, y, w, h, ground=F.PAPER, cid="ta", ramp=None):
    """The Drift. Every leaf at its own attitude, scale varying without a progression,
    three of them cut by an edge so the field implies more than it shows."""
    R = ramp or F.BONE_RAMP
    body = F.panel(cid, x, y, w, h, ground)
    # fx, fy, size as a fraction of h, rotation, ramp step
    leaves = [(-0.02, 0.22, 0.30, -58, 2), (0.14, 0.72, 0.22, 34, 3),
              (0.24, 0.34, 0.26, 12, 1), (0.40, 0.62, 0.42, -24, 3),
              (0.52, 0.20, 0.18, 68, 1), (0.66, 0.46, 0.30, -76, 2),
              (0.79, 0.86, 0.24, 20, 1), (0.88, 0.24, 0.20, -40, 2),
              (1.01, 0.60, 0.28, 52, 3)]
    for fx, fy, fs, rot, tone in leaves:
        body += F.petal(x + w * fx, y + h * fy, h * fs, R[tone], rot=rot)
    return body + "</g>"


def descent(x, y, w, h, ground=F.PAPER, cid="dc", ramp=None):
    """Vertical rhythm for spines, rails and margins. Large, small, large, small, with a
    lateral drift so it is a descent rather than a stack."""
    R = ramp or F.BONE_RAMP
    body = F.panel(cid, x, y, w, h, ground)
    steps = [(0.52, 0.045, 0.115, 0, 1), (0.70, 0.175, 0.035, 22, 3),
             (0.48, 0.300, 0.145, -12, 2), (0.30, 0.455, 0.040, 16, 3),
             (0.46, 0.610, 0.160, 8, 1), (0.66, 0.775, 0.038, -20, 3),
             (0.44, 0.925, 0.150, -6, 2)]
    for fx, fy, fs, rot, tone in steps:
        body += F.petal(x + w * fx, y + h * fy, h * fs, R[tone], rot=rot)
    return body + "</g>"


FIELDS = {"trefoil": trefoil, "trefoil_field": trefoil_field,
          "tumbling_air": tumbling_air, "descent": descent}
