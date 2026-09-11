// The mark as halftone dot. Nothing here is ruled.
const pptxgen = require("pptxgenjs");
const L = require("./lib");
const { C, SERIF, SANS, PAGE_W, PAGE_H, rect, sharpRect, hline, txt, label, R, reportPage } = L;
const { CX, TOP, RIGHT, T, col, span } = R;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Five Points Digital Studio";
pres.title = "Five Points — the screen";
const DOC = "The screen";
let P = 0; const next = () => ++P;

function display(s, t, x, y, w, o = {}) {
  txt(s, t, { x, y, w, h: o.h || 1.4, fontFace: SERIF, fontSize: o.fontSize || T.display,
    color: o.color || C.ink, lineSpacingMultiple: 1.05, ...o });
}
function para(s, t, x, y, w, h, o = {}) {
  txt(s, L.bind(t, w, o.fontSize || T.body), { x, y, w, h, fontFace: SANS, fontSize: T.body,
    color: o.color || C.inkSoft, lineSpacingMultiple: 1.62, ...o });
}
function lead(s, t, x, y, w, h, o = {}) {
  txt(s, L.bind(t, w, T.lead), { x, y, w, h, fontFace: SERIF, fontSize: T.lead,
    color: o.color || C.ink, lineSpacingMultiple: 1.3, ...o });
}

// ---------------------------------------------------------------- 01 the idea
{
  const s = reportPage(pres, { page: next(), chrome: false });
  sharpRect(s, 0, 0, PAGE_W, PAGE_H, C.ink);
  const iw = 5.65;
  s.addImage({ path: "f-hero.png", x: PAGE_W - iw, y: 0, w: iw, h: 7.5 });
  label(s, "A test  ·  not a ruling", CX, 1.15, 6, C.mute, { bold: false });
  txt(s, "The dot is\nthe mark.", {
    x: CX, y: 1.62, w: 6.2, h: 2.4, fontFace: SERIF, fontSize: 46, color: C.bone,
    lineSpacingMultiple: 1.12,
  });
  hline(s, CX, 4.35, 3.2, C.ruleDark, 0.75);
  para(s, "A halftone reproduces tone by varying the area of a dot. This screen varies the area "
    + "of the Quintessence instead. Every dot in the image is the rounded pentagon core, or the "
    + "whole rosette where the light allows it. There is not a circle anywhere in the picture.",
    CX, 4.62, 6.2, 1.3, { color: C.muteLight });
  para(s, "Photography rendered in the brand, at every scale.", CX, 6.5, 5.0, 0.4,
    { color: C.bone, fontSize: T.caption });
}

// ---------------------------------------------------------------- 02 how it works
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "How it works", CX, TOP - 0.06, 4.6, { h: 0.9 });
  lead(s, "Four decisions make the difference between a brand-shaped novelty and a screen that "
    + "actually reproduces a photograph.", col(2), TOP + 0.02, span(2), 1.0);

  const rules = [
    ["01", "No circles", "Every dot is the pentagon core or the whole rosette. The mark carries the image rather than sitting beside it."],
    ["02", "Area, not width", "The rosette inks 19% of its own circle. The core inks 50%. Both are sized from measured ink, so the screen can change shape mid-image without a step in tone."],
    ["03", "The mark blooms\nin the light", "The rosette takes the highlights, where a dot has room to open. The core takes everything darker. Tested against the reverse, below."],
    ["04", "One ink, one ground", "A screen is a single ink. Bone on ink, ink on paper, or a voice on paper. Never two inks in one image."],
  ];
  const cw = (RIGHT - CX - 3 * 0.32) / 4;
  rules.forEach(([n, h, t], i) => {
    const x = CX + i * (cw + 0.32);
    hline(s, x, TOP + 1.5, cw, C.rule, 0.75);
    txt(s, n, { x, y: TOP + 1.67, w: cw, h: 0.24, fontFace: SANS, fontSize: T.micro,
      color: C.mute, charSpacing: 1.4 });
    txt(s, h, { x, y: TOP + 1.99, w: cw, h: 0.6, fontFace: SERIF, fontSize: T.sub, color: C.ink,
      lineSpacingMultiple: 1.12 });
    para(s, t, x, TOP + 2.73, cw, 1.5, { fontSize: T.caption, lineSpacingMultiple: 1.5 });
  });

  const gw = 7.35, gh = gw * 712 / 1960;
  s.addImage({ path: "g-ladder.png", x: CX, y: TOP + 3.78, w: gw, h: gh });
  para(s, "The test that settled it. Put the whole mark in the shadows and the rosettes overlap "
    + "into noise; the face stops reading. Put it everywhere and tone flattens. The mark belongs "
    + "in the light.", CX + gw + 0.45, TOP + 3.86, RIGHT - CX - gw - 0.45, 1.8,
    { fontSize: T.caption, lineSpacingMultiple: 1.5 });
}

// ---------------------------------------------------------------- 03 the ruling
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "The ruling", CX, TOP - 0.06, 4.6, { h: 0.9 });
  lead(s, "Ruling is the one control that matters. Coarsen the screen and the mark becomes the "
    + "subject. Fine it down and the photograph does.",
    col(2), TOP + 0.02, span(2), 1.0);
  const iw = 11.7, ih = iw * 649 / 1802;
  s.addImage({ path: "f-rulings.png", x: CX + (RIGHT - CX - iw) / 2, y: TOP + 1.22, w: iw, h: ih });
  para(s, "Six point for photography that must read as photography, in a report or on a page "
    + "beside body copy. Ten point as the house setting for documentation imagery. Sixteen and "
    + "above for statements, where the mark should be unmistakable and the sitter is a gesture "
    + "rather than a likeness.",
    CX, TOP + 1.44 + ih, span(3), 0.8);
}

// ---------------------------------------------------------------- 04 the magnification
{
  const s = reportPage(pres, { page: next(), doc: DOC, bg: C.greige, headFill: "C3BDAF" });
  display(s, "At the dot", CX, TOP - 0.06, 4.6, { h: 0.9 });
  lead(s, "The same eye at a twenty-six point screen, either way round. The pentagons carry the "
    + "midtones. In the lightest passages they give way to the rosette itself.",
    col(2), TOP + 0.02, span(2), 1.0);
  const iw = 9.4, ih = iw * 1612 / 3118;
  s.addImage({ path: "f-zooms.png", x: CX + (RIGHT - CX - iw) / 2, y: TOP + 1.28, w: iw, h: ih });
}

// ---------------------------------------------------------------- 05 the ruling asks
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "What it needs", CX, TOP - 0.06, 5.4, { h: 0.9 });
  lead(s, "The screen is built and calibrated. Three things stand between it and use.",
    col(2), TOP + 0.02, span(2), 1.0);

  const cols = [
    ["Photography", C.coralTint, C.coralInk,
     "This is the binding constraint, not the screen.\n\n"
     + "The asset library holds four stock portraits. They are AI-generated, two carry visible "
     + "watermarks, and none of them is a tradesperson.\n\n"
     + "A screen this strong makes the source obvious rather than hiding it. It wants real "
     + "photography of real people in the trades, shot with clean tonal separation: a light "
     + "subject against a dark ground, or the reverse. Busy environmental shots screen badly, "
     + "as the one environmental shot in the library does."],
    ["Where it runs", C.sageTint, C.sageInk,
     "My recommendation: every photograph in the identity book, the capabilities deck and the "
     + "proposal runs screened. No unscreened photography anywhere in the documentation.\n\n"
     + "That makes it a system rather than an effect, and it removes the question of when to use "
     + "it, which is the question that kills features like this.\n\n"
     + "The site is a separate decision, since the screen costs bandwidth and needs care at small "
     + "breakpoints."],
    ["The register", C.priscillaTint, C.priscillaInk,
     "Bone on ink is the strongest of the treatments and the most on-brand. I would make it the "
     + "default and reserve ink on paper for pages that are already light.\n\n"
     + "A voice-coloured screen, coral or ash green on paper, works and is held in reserve for "
     + "section dividers.\n\n"
     + "One open question worth your ruling: whether the screen is a house treatment applied to "
     + "everything, or a device reserved for people, with product and place shot straight."],
  ];
  const cw = (RIGHT - CX - 2 * 0.3) / 3;
  cols.forEach(([h, bg, fg, t], i) => {
    const x = CX + i * (cw + 0.3);
    rect(s, x, TOP + 1.2, cw, 4.15, bg);
    txt(s, h, { x: x + 0.3, y: TOP + 1.46, w: cw - 0.6, h: 0.4, fontFace: SERIF,
      fontSize: T.sub, color: fg });
    para(s, t, x + 0.3, TOP + 2.0, cw - 0.6, 3.3, { fontSize: 8.6, lineSpacingMultiple: 1.5 });
  });
  para(s, "The engine is parametric: source, ruling, angle, shape, levels and colourway are all "
    + "arguments. Once the photography exists, screening the whole library is one pass.",
    CX, TOP + 5.6, span(2), 0.9);
}

pres.writeFile({ fileName: "five-points-the-screen.pptx" })
  .then(() => console.log("the screen:", P, "pages"));
