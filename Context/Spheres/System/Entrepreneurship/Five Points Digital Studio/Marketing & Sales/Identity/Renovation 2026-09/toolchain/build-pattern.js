// Pattern direction, second pass. Nothing here is ruled.
const pptxgen = require("pptxgenjs");
const L = require("./lib");
const { C, SERIF, SANS, PAGE_W, PAGE_H, rect, sharpRect, hline, txt, label, R, reportPage } = L;
const { CX, TOP, RIGHT, T, col, span } = R;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Five Points Digital Studio";
pres.title = "Five Points — the field";
const DOC = "The field";
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

// ---------------------------------------------------------------- 01 the correction
{
  const s = reportPage(pres, { page: next(), chrome: false });
  sharpRect(s, 0, 0, PAGE_W, PAGE_H, C.ink);
  s.addImage({ path: "p2-cover.png", x: PAGE_W - 5.9, y: 0, w: 5.9, h: 6.21 });
  label(s, "A test  ·  not a ruling", CX, 1.15, 6, C.mute, { bold: false });
  txt(s, "The pattern was the\nproblem. Not the shape.", {
    x: CX, y: 1.62, w: 6.2, h: 2.4, fontFace: SERIF, fontSize: 42, color: C.bone,
    lineSpacingMultiple: 1.14,
  });
  hline(s, CX, 4.75, 3.2, C.ruleDark, 0.75);
  para(s, "The first pass tessellated. Every shape touched another shape, the field filled edge to "
    + "edge, and the eye had nowhere to rest — which is what suffocating means. This pass takes its "
    + "instruction from how Anthropic works a field: very few forms, one hue in tonal steps, one "
    + "form far larger than the others, shapes that run off the edge, and a great deal of air.",
    CX, 5.02, span(2), 1.3, { color: C.muteLight });
  para(s, "Five fields. One law.", CX, 6.55, 4.0, 0.4, { color: C.bone, fontSize: T.caption });
}

// ---------------------------------------------------------------- 02 the law
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "The law of\nthe field", CX, TOP - 0.06, 4.6, { h: 1.6 });
  lead(s, "Five rules. They are what separates a field from wallpaper, and they are the reason the "
    + "first pass failed. Every one of them is a rule about restraint.",
    col(2), TOP + 0.02, span(2), 1.0);

  const rules = [
    ["01", "Few elements", "Three to six forms in a field. Never more. What is not there is the composition."],
    ["02", "One hue, several steps", "A field is a single colour rendered in three or four tonal steps. Never a mix of the five voices."],
    ["03", "One form dominates", "One shape is far larger than the rest. Forms at equal size read as wallpaper, whatever the spacing."],
    ["04", "Shapes leave the frame", "At least one form is cut by an edge. A field that fits neatly inside its box is a picture, not a field."],
    ["05", "Nothing repeats", "No tile, no tessellation, no grid. The eye must never find the seam. Every field is issued once."],
  ];
  const cw = (RIGHT - CX - 4 * 0.28) / 5;
  rules.forEach(([n, h, t], i) => {
    const x = CX + i * (cw + 0.28);
    hline(s, x, TOP + 2.20, cw, C.rule, 0.75);
    txt(s, n, { x, y: TOP + 2.37, w: cw, h: 0.24, fontFace: SANS, fontSize: T.micro,
      color: C.mute, charSpacing: 1.4 });
    txt(s, h, { x, y: TOP + 2.69, w: cw, h: 0.6, fontFace: SERIF, fontSize: T.sub, color: C.ink,
      lineSpacingMultiple: 1.12 });
    para(s, t, x, TOP + 3.43, cw, 1.9, { fontSize: T.caption, lineSpacingMultiple: 1.55 });
  });

  hline(s, CX, TOP + 5.10, RIGHT - CX, C.rule, 0.75);
  para(s, "What the law forbids: a field behind body copy at full strength, more than one field on "
    + "a spread, the mark rotated, and the complete mark used as a pattern element. The mark is the "
    + "mark. The pieces are the pattern.",
    CX, TOP + 5.31, span(2), 0.9);
}

// ---------------------------------------------------------------- 03 the kit
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "Five fields", CX, TOP - 0.06, 4.6, { h: 0.9 });
  lead(s, "One kit, drawn entirely from the leaf and the mote. No new shapes were invented to "
    + "make it.", CX, TOP + 1.02, span(1), 0.8);
  const items = [
    ["01", "The Crop", "One leaf at scale, the mark as counterpoint. Covers, section fronts, anything large."],
    ["02", "The Drift", "Leaves carried on a current, large to small. Card backs, notes, email headers."],
    ["03", "The Arc", "A sweep round a pivot outside the frame. The dynamic field: openers and dark registers."],
    ["04", "The Overlap", "Three petals, two crossings. The crossings make a fourth tone. Pull pages and quotes."],
    ["05", "The Rule", "The mote band, undulating. Dividers, footers, spines, the band between sections."],
  ];
  let y = TOP + 1.80;
  items.forEach(([n, h, t]) => {
    txt(s, n, { x: CX, y: y + 0.045, w: 0.45, h: 0.22, fontFace: SANS, fontSize: T.micro,
      color: C.mute, charSpacing: 1.4 });
    txt(s, h, { x: CX + 0.5, y, w: span(1) - 0.5, h: 0.28, fontFace: SERIF, fontSize: T.sub,
      color: C.ink });
    para(s, t, CX + 0.5, y + 0.31, span(1) - 0.5, 0.6, { fontSize: T.caption,
      lineSpacingMultiple: 1.5 });
    y += 0.86;
  });
  const pw = 5.24, ph = pw * 1130 / 1240;
  s.addImage({ path: "p2-kit.png", x: RIGHT - pw, y: TOP + 0.02, w: pw, h: ph });
}

// ---------------------------------------------------------------- 04 in use
{
  const s = reportPage(pres, { page: next(), doc: DOC, bg: C.greige, headFill: "C3BDAF" });
  display(s, "In use", CX, TOP - 0.06, 4.6, { h: 0.9 });
  lead(s, "The field is never the subject. It is the air the type sits in, and on the surfaces that "
    + "carry no type it is the whole surface.", CX, TOP + 1.05, span(1), 1.2);
  para(s, "Note the tile at the far right: no field at all, the mark alone on a voice. That is not "
    + "an omission. A system that cannot hold silence has no dynamics, and every surface begins to "
    + "shout.\n\nNote also the divider. It is the same mote at the same spacing law as the field "
    + "above it, which is what makes a kit a system rather than five separate ideas.",
    CX, TOP + 2.42, span(1), 2.6);
  const pw = 7.3, ph = pw * 980 / 1240;
  s.addImage({ path: "p2-use.png", x: RIGHT - pw, y: TOP + 0.35, w: pw, h: ph });
}

// ---------------------------------------------------------------- 05 the ruling
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "What I\nwould rule", CX, TOP - 0.06, 4.0, { h: 1.6 });
  lead(s, "Three decisions sit here. The first two are mine to recommend. The third is yours "
    + "alone, and it has been open since the rosette test.",
    col(2), TOP + 0.02, span(2), 1.0);

  const cols = [
    ["Adopt the five", C.sageTint, C.sageInk,
     "The kit as drawn, with the law of the field written into the fingerprint at Layer 2.\n\n"
     + "It costs nothing that is currently in use — there is no pattern system to retire — and it "
     + "gives the brand a texture layer it has never had.\n\n"
     + "Recommended."],
    ["Hold the Arc back", C.priscillaTint, C.priscillaInk,
     "The Arc is the most dynamic of the five and the easiest to overuse.\n\n"
     + "I would reserve it for section openers and the dark register only, and keep the Crop and "
     + "the Drift as the everyday fields.\n\n"
     + "A restriction is easier to relax later than a habit is to break."],
    ["The mark itself", C.coralTint, C.coralInk,
     "Still open from the rosette test: crystal, rosette, or both.\n\n"
     + "This kit works under either. The pieces come from the leaf and the mote, which both marks "
     + "share.\n\n"
     + "My recommendation stands — the crystal ceremonial and large only, the rosette on every "
     + "working surface — but it wants a trademark knockout before it is written down."],
  ];
  const cw = (RIGHT - CX - 2 * 0.3) / 3;
  cols.forEach(([h, bg, fg, t], i) => {
    const x = CX + i * (cw + 0.3);
    rect(s, x, TOP + 1.2, cw, 3.20, bg);
    txt(s, h, { x: x + 0.3, y: TOP + 1.46, w: cw - 0.6, h: 0.4, fontFace: SERIF,
      fontSize: T.sub, color: fg });
    para(s, t, x + 0.3, TOP + 2.0, cw - 0.6, 2.5, { fontSize: 8.6, lineSpacingMultiple: 1.5 });
  });
  para(s, "Nothing in this document has been applied to the fingerprint, the design system or the "
    + "site. It sits in the renovation ledger with the rest, pending a closing pass.",
    CX, TOP + 4.66, span(2), 0.9);
}

pres.writeFile({ fileName: "five-points-the-field.pptx" })
  .then(() => console.log("the field:", P, "pages"));
