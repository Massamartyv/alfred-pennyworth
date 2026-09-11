"""Every asset the two decks consume, generated from the ruled system.

Run this before either builder. Nothing downstream draws a field or a screened
photograph any other way.
"""
import sys, math
sys.path.insert(0, '.')
import fieldlib as F
import ruled as U
from PIL import Image, ImageDraw, ImageFont

STOCK = ('/Users/martyspicer/Alfred Pennyworth/Context/Spheres/System/Entrepreneurship/'
         'Five Points Digital Studio/Marketing & Sales/Asset Library/Stock Photography/')

# ---------------------------------------------------------------- fields
F.render("fld-trefoil-motif", 600, 600,
         F.panel("m", 0, 0, 600, 600, F.PAPER) + U.trefoil(300, 300, 250) + "</g>", bg=F.PAPER)
F.render("fld-trefoil-repeat", 1380, 920, U.trefoil_field(0, 0, 1380, 920), bg=F.PAPER)
F.render("fld-tumbling", 1200, 500, U.tumbling_air(0, 0, 1200, 500), bg=F.PAPER)
F.render("fld-tumbling-ink", 1200, 500,
         U.tumbling_air(0, 0, 1200, 500, ground=F.INK, ramp=F.INK_RAMP), bg=F.INK)
F.render("fld-descent", 300, 900, U.descent(0, 0, 300, 900), bg=F.PAPER)

# ---------------------------------------------------------------- the screen
FACE = STOCK + 'headshot-woman-mint-blazer.png'
LAUGH = STOCK + 'headshot-woman-laughing.png'
DESK = STOCK + 'woman-at-desk-office.png'
DENT = STOCK + 'dentist-patient-smiling.png'

# Cropped to 1 : 1.272 - the book's portrait cell - so nothing has to stretch to fit.
U.screen(FACE, "scr-hero", width=880, crop=(250, 60, 800, 760))
U.screen(LAUGH, "scr-second", width=700, crop=(160, 50, 860, 940))
U.screen(DENT, "scr-third", width=700, crop=(150, 40, 850, 930),
         black=0.26, white=0.86, gamma=1.15)
U.screen(DESK, "scr-positive", width=700, crop=(430, 355, 790, 905), negative=False)

# the magnification - proof the dot is the mark
# A wide band across the eyes, screened coarsely, so a reader can see that the dot is
# the mark rather than take it on trust.
U.screen(FACE, "scr-detail", width=1240, crop=(300, 330, 700, 430),
         pitch=1240 / 34, gamma=1.2, white=0.94)

# the ruling ladder - why ten is the house setting
def fo(s):
    try: return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", s)
    except Exception: return ImageFont.load_default()

tiles = []
for dots, note in ((150, "150 ACROSS  ·  A PHOTOGRAPH"), (88, "88 ACROSS  ·  THE HOUSE RULING"),
                   (46, "46 ACROSS  ·  A STATEMENT"), (26, "26 ACROSS  ·  THE MARK ITSELF")):
    p, n, d = U.screen(FACE, f"scr-r{dots}", width=420, crop=(250, 70, 800, 800),
                       pitch=420 / dots, scale=1)
    tiles.append((f"{note}  ·  {n:,} MARKS", p))
tw, th = Image.open(tiles[0][1]).size
pad, gap, cap = 26, 20, 34
sh = Image.new("RGB", (pad * 2 + 4 * tw + 3 * gap, pad * 2 + th + cap), (248, 248, 248))
dr = ImageDraw.Draw(sh)
for i, (lab, p) in enumerate(tiles):
    x = pad + i * (tw + gap)
    sh.paste(Image.open(p).convert("RGB"), (x, pad))
    dr.text((x, pad + th + 11), lab, fill=(35, 32, 25), font=fo(11))
sh.save("scr-ladder.png")

# the field kit, one plate for the identity book
CH = 420
def cell(path, crop=None):
    im = Image.open(path).convert("RGB")
    if crop: im = im.crop(crop)
    return im.resize((int(im.width * CH / im.height), CH), Image.LANCZOS)
top = [("THE TREFOIL  ·  THE MOTIF", cell("fld-trefoil-motif.png")),
       ("THE TREFOIL  ·  THE SEAMLESS REPEAT", cell("fld-trefoil-repeat.png")),
       ("TUMBLING AIR", cell("fld-tumbling.png")),
       ("THE DESCENT", cell("fld-descent.png"))]
Wt = pad * 2 + sum(im.width for _, im in top) + gap * (len(top) - 1) + 130
kit = Image.new("RGB", (Wt, pad * 2 + CH + cap), (248, 248, 248))
dk = ImageDraw.Draw(kit)
x = pad
for lab, im in top:
    kit.paste(im, (x, pad)); dk.text((x, pad + CH + 11), lab, fill=(35, 32, 25), font=fo(12))
    x += im.width + gap
kit.save("fld-kit.png")

print("assets built")
for n in ("fld-kit", "scr-ladder"):
    print(n, Image.open(f"{n}.png").size)
