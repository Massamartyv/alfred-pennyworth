import sys, math
sys.path.insert(0, '.')
import fieldlib as F
from PIL import Image, ImageDraw, ImageFont

RAMP = ["#4A4437", "#6E6552", "#C9BC9C", F.BONE]

def rule_band(name, w, h, n, cycles=4, gain=2.0, amp=0.22, ground=F.INK):
    """The Rule. Leaves at twice their former size, the spacing scaled with them so the
    motes stay discrete, and each leaf turned to the slope of the wave it rides."""
    body = F.panel("r", 0, 0, w, h, ground)
    step = w / n
    base = step * 0.62
    A = h * amp
    TAU = 2 * math.pi
    for i in range(n):
        x = i * step
        t = x / w
        y = math.sin(TAU * cycles * t)
        slope = math.cos(TAU * cycles * t) * TAU * cycles * A / w
        sz = base * gain * (0.80 + 0.38 * (0.5 + 0.5 * y))
        body += F.mote(x, h / 2 + A * y, sz, RAMP[3] if i % 5 == 0 else RAMP[2],
                       rot=math.degrees(math.atan2(slope, 1)) + 90)
    body += "</g>"
    return F.render(name, w, h, body, bg=ground)

# The original ran 17 motes across 600, so 44 across this width. Halving that to 22
# doubles the step, and the mote size is derived from the step - which is what makes the
# leaves twice the size while every other property of the wave stays exactly as it was.
rule_band("fk-rule2", 1560, 300, 22, cycles=2, gain=1.0, amp=0.30)
rule_band("fk-rule-before", 1560, 300, 44, cycles=4, gain=1.0, amp=0.30)

def fo(s):
    try: return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", s)
    except Exception: return ImageFont.load_default()

CH = 360
def cell(path, crop=None):
    im = Image.open(path).convert("RGB")
    if crop:
        im = im.crop(crop)
    return im.resize((int(im.width * CH / im.height), CH), Image.LANCZOS)

top = [
    ("THE TREFOIL  ·  THE MOTIF ALONE", cell("cand_ov-a-motif.png")),
    ("THE TREFOIL  ·  THE SEAMLESS REPEAT", cell("cand_ov-a-tile.png", (0, 0, 1800, 1200))),
    ("TUMBLING AIR  ·  THE DRIFT", cell("cand_dr-a.png")),
    ("THE DESCENT  ·  SPINES AND RAILS", cell("cand_nc-column.png")),
]
pad, gap, cap = 30, 22, 34
Wt = pad * 2 + sum(im.width for _, im in top) + gap * (len(top) - 1) + 150
rule_im = Image.open("fk-rule2.png").convert("RGB")
rule_im = rule_im.resize((Wt - pad * 2, int(rule_im.height * (Wt - pad * 2) / rule_im.width)),
                         Image.LANCZOS)
Ht = pad * 2 + CH + cap + gap + rule_im.height + cap
sh = Image.new("RGB", (Wt, Ht), (248, 248, 248))
dr = ImageDraw.Draw(sh)
x = pad
for label, im in top:
    sh.paste(im, (x, pad))
    dr.text((x, pad + CH + 11), label, fill=(35, 32, 25), font=fo(12))
    x += im.width + gap
y = pad + CH + cap + gap
sh.paste(rule_im, (pad, y))
dr.text((pad, y + rule_im.height + 11), "THE RULE  ·  LEAVES AT TWICE THE SIZE, THE WAVE UNCHANGED",
        fill=(35, 32, 25), font=fo(12))
sh.save("fk-kit2.png")
print("fk-kit2.png", sh.size)
