// Five Points Digital Studio — The Identity Book, v6.
// Swiss rail system off the 2025 fingerprint. Corners carry the mark radius; the mark
// steps down a three-tier ladder; the index is composed against the source page.
const pptxgen = require("pptxgenjs");
const L = require("./lib");
const {
  C, VOICES, SERIF, SANS, RAD, RAD_SM, PAGE_W,
  rect, sharpRect, hline, vline, bar, txt, label, body, serif, vtext, well, mark, bind,
  B, bookPage, bookStudy,
} = L;
const { CX, TOP, BOT, LEFT_W, MAIN_X, MAIN_W, RAIL_X, RULE1_X, T, col, span } = B;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Five Points Digital Studio";
pres.company = "Five Points Digital Studio";
pres.title = "Five Points Digital Studio — The Identity Book";

const RAIL = "THE IDENTITY BOOK";
let P = 0;
const next = () => ++P;

// ============================================================ 001 cover
{
  const s = bookPage(pres, { page: next(), dark: true, chrome: false });
  vtext(s, "FIVE POINTS DIGITAL STUDIO  ·  VERSION 4.0 / 2026", RAIL_X, TOP, TOP + 4.4, { color: C.mute });
  vline(s, RULE1_X, TOP, BOT - TOP, C.ruleDark, 0.75);
  mark(s, 1.3, CX, 1.10, "bone");
  label(s, "The Identity Book", CX, 3.28, 6, C.muteLight);
  txt(s, "Five Points\nDigital Studio", {
    x: CX, y: 3.68, w: 9.4, h: 2.0, fontFace: SERIF, fontSize: T.mega,
    color: C.bone, lineSpacingMultiple: 1.02,
  });
  hline(s, CX, 6.44, 3.2, C.ruleDark, 0.75);
  label(s, "Who we are  ·  how we sound  ·  how we show up", CX, 6.64, 8, C.mute, { bold: false });
  label(s, "Decatur, Georgia", PAGE_W - 0.82 - 3, 6.64, 3, C.mute, { align: "right", bold: false });
}

// ============================================================ 002 welcome
{
  const s = bookPage(pres, { page: next(), rail: RAIL, rule2: false });
  label(s, "Welcome", CX, TOP + 0.02, LEFT_W, C.ink);
  txt(s, "This book sets out who we are, what we stand for, how we talk and how we look, "
    + "wherever we show up in the world.\n\n"
    + "It is a working framework rather than a cage. It holds the decisions that do not move — "
    + "the name, the mark, the palette, the voice — and leaves room for the judgement every good "
    + "piece of work needs. Applied consistently it compounds: every page, every plan and every "
    + "call adds to one recognisable house rather than starting again.\n\n"
    + "Version 4.0 supersedes the fingerprint of June 2026 and restores the warmth of the 2025 "
    + "book to a house that had grown cold in its own documentation.", {
    x: MAIN_X, y: TOP + 0.02, w: span(7), h: 3.4, fontFace: SERIF, fontSize: T.lead,
    color: C.inkSoft, lineSpacingMultiple: 1.44,
  });
  mark(s, 0.9, MAIN_X, BOT - 1.2, "ink");
  label(s, "Five Points Digital Studio  ·  Brand Fingerprint  ·  Version 4.0",
    MAIN_X + 1.2, BOT - 0.75, 7, C.mute, { bold: false });
}

// ============================================================ sections
const SECTIONS = [
  { n: "1.0", t: "The Brand", items: ["Brand Manifesto", "Brand Values", "Brand Personality", "Brand Archetypes", "Tone of Voice", "Brand Messaging"] },
  { n: "2.0", t: "Brandmarks", items: ["The Mark", "The Geometry", "The Mark Ladder", "Colourways", "Clear Space", "Mark Misuse"] },
  { n: "3.0", t: "Colour", items: ["Primary Palette", "Surface Tints", "Colour Weighting", "Colour Combinations"] },
  { n: "4.0", t: "Typography", items: ["Primary Typeface", "Secondary Typeface", "Type Hierarchy", "Type Misuse"] },
  { n: "5.0", t: "Photography", items: ["Photographic Style", "Light and Colour", "Casting and Composition"] },
  { n: "6.0", t: "The Field", items: ["The Law of the Field", "The Four Fields", "The Screen", "The Screen in Use"] },
  { n: "7.0", t: "Application", items: ["The Journey", "The Words", "Stationery", "Digital"] },
];
let cursor = 4;
SECTIONS.forEach((sec) => { sec.page = cursor; cursor += 1 + sec.items.length; });

// ============================================================ 003 index
// Composed against the source index page: one large serif word on the left, the two
// contents columns spread across the right half, hairlines between.
{
  const s = bookPage(pres, { page: next(), rail: RAIL, rule2: false });
  txt(s, "Index", {
    x: 1.4, y: 3.05, w: 4.6, h: 1.4, fontFace: SERIF, fontSize: 62, color: C.ink,
    align: "center", valign: "middle",
  });
  const COLS = [
    { x: 6.99, tx: 7.42, px: 9.05, rule: 6.75 },
    { x: 10.12, tx: 10.55, px: 12.18, rule: 9.94 },
  ];
  COLS.forEach((c) => vline(s, c.rule, TOP, BOT - TOP, C.rule, 0.75));
  SECTIONS.forEach((sec, i) => {
    const c = COLS[i < 3 ? 0 : 1];
    const slot = i % 3;
    const y = TOP + 0.04 + slot * 2.28;
    label(s, sec.n, c.x, y, 0.6, C.ink, { fontSize: 9.5 });
    label(s, sec.t, c.tx, y, 2.2, C.ink, { fontSize: 9.5 });
    label(s, String(sec.page).padStart(2, "0"), c.px, y, 0.55, C.ink, { fontSize: 9.5, align: "right" });
    sec.items.forEach((it, j) => {
      const yy = y + 0.42 + j * 0.235;
      txt(s, `${sec.n[0]}.${j + 1}`, { x: c.x, y: yy, w: 0.6, h: 0.22, fontFace: SERIF, fontSize: 10.5, color: C.muteDark });
      txt(s, it, { x: c.tx, y: yy, w: 2.4, h: 0.22, fontFace: SERIF, fontSize: 10.5, color: C.inkSoft });
      txt(s, String(sec.page + 1 + j).padStart(2, "0"), { x: c.px, y: yy, w: 0.55, h: 0.22, fontFace: SERIF, fontSize: 10.5, color: C.muteDark, align: "right" });
    });
  });
}

// ============================================================ dividers
const ROMAN = ["I", "II", "III", "IV", "V", "VI", "VII"];
function divider(idx) {
  const sec = SECTIONS[idx];
  const s = bookPage(pres, { page: next(), rail: RAIL, bg: C.bonePale, rule2: false });
  vtext(s, sec.t.toUpperCase(), 1.34, 1.05, BOT, {
    fontFace: SERIF, fontSize: 50, color: C.ink, charSpacing: 0, h: 0.95, align: "left",
  });
  vline(s, 1.86, TOP, BOT - TOP, C.rule, 0.75);
  const cx = 2.14;
  label(s, sec.n, cx, TOP + 0.02, 0.6, C.ink, { fontSize: 9.5 });
  label(s, sec.t, cx + 0.72, TOP + 0.02, 2.3, C.ink, { fontSize: 9.5 });
  label(s, String(sec.page).padStart(2, "0"), cx + 2.9, TOP + 0.02, 0.5, C.ink, { fontSize: 9.5, align: "right" });
  sec.items.forEach((it, j) => {
    const yy = TOP + 0.46 + j * 0.27;
    txt(s, `${sec.n[0]}.${j + 1}`, { x: cx, y: yy, w: 0.6, h: 0.24, fontFace: SERIF, fontSize: 10.5, color: C.muteDark });
    txt(s, it, { x: cx + 0.72, y: yy, w: 2.3, h: 0.24, fontFace: SERIF, fontSize: 10.5, color: C.inkSoft });
    txt(s, String(sec.page + 1 + j).padStart(2, "0"), { x: cx + 2.9, y: yy, w: 0.5, h: 0.24, fontFace: SERIF, fontSize: 10.5, color: C.muteDark, align: "right" });
  });
  vline(s, 5.95, TOP, BOT - TOP, C.rule, 0.75);
  txt(s, ROMAN[idx], {
    x: 6.5, y: 1.55, w: 6.2, h: 4.4, fontFace: SERIF, fontSize: 190, color: C.ink,
    align: "center", valign: "middle",
  });
}

// ============================================================ 1.0 THE BRAND
divider(0);

{ // 1.1 manifesto
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "1.1  Brand Manifesto",
    intro: "In this section we set out the building blocks of the brand: who we are, what we stand "
      + "for, what sets us apart, why we choose the words we use and how we have decided to show up.",
    foot: "The essence — connecting passion to possibility — is the internal north star. It is never "
      + "set in type on a surface an owner sees.",
  });
  const ww = span(3);
  well(s, MAIN_X, TOP, ww, 4.264, "THE OWNER AT HIS PLACE", { inner: "PORTRAIT" });
  const tx = MAIN_X + ww + 0.5, tw = MAIN_W - ww - 0.5;
  serif(s, "Brand\nManifesto", tx, TOP - 0.04, 3.0, 1.4, { fontSize: T.display });
  [
    ["Overview", "We build businesses that last, not campaigns that expire. The best work sits where timeless quality meets forward-thinking purpose, and everything we make starts there."],
    ["Our mission", "To give an owner clear direction and a team that carries it — the systems, the resources and the plain-spoken expertise that turn a complicated problem into a simple path, so the business grows and keeps growing after we have gone home."],
    ["Our vision", "To be the consultancy an owner-operator calls first when the business is ready to be known. We believe the smartest businesses win, not the ones with the biggest budgets, and that a company unmistakably itself will bring the city to its door."],
    ["The challenge", "Most agencies look excellent on paper. They arrive with a template, they charge by the month, and when the engagement ends they take the keys with them. You end up with a vendor and a bill, not a partner and an asset."],
  ].forEach(([h, t], i) => {
    const y = TOP + 1.62 + i * 1.34;
    label(s, h, tx, y, tw, C.ink);
    body(s, t, tx, y + 0.24, 4.4, 1.2, { fontFace: SERIF, fontSize: 11, lineSpacingMultiple: 1.4 });
  });
}

{ // 1.2 values
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "1.2  Brand Values",
    intro: "Who we are is reflected in our values. Five of them, for five points — the central "
      + "benefits that guide our actions, unite our people and uphold the mission.",
  });
  const vals = [
    ["Clarity", "Great work begins with understanding. We replace confusion with a plan everyone can read, so you know what we are doing and why. The right path is always the clear one."],
    ["Partnership", "We work with you, not just for you. Your goals become ours, the relationship is open and honest, and getting it right is the whole point."],
    ["World class", "Excellence in everything, from the biggest idea to the smallest detail. Polished, powerful work you can depend on, every time."],
    ["Built to last", "We build for tomorrow, not just today. Timeless strategy, strong foundations and systems that grow with the business. We are not interested in chasing trends."],
    ["Hospitality", "How it feels to work with us matters as much as what we make. Every owner is received, never processed. We are rigorous on the ninety-five so the five can be spent well."],
  ];
  const cw = (MAIN_W - 4 * 0.18) / 5;
  vals.forEach(([h, t], i) => {
    const x = MAIN_X + i * (cw + 0.18);
    rect(s, x, TOP, cw, 5.0, VOICES[i].tint);
    bar(s, x, TOP, cw, 0.06, VOICES[i].hex);
    label(s, `0${i + 1}`, x + 0.2, TOP + 0.3, 1, VOICES[i].ink, { fontSize: 7 });
    txt(s, h, { x: x + 0.2, y: TOP + 0.6, w: cw - 0.34, h: 0.72, fontFace: SERIF, fontSize: 15, color: C.ink, lineSpacingMultiple: 1.08 });
    body(s, t, x + 0.2, TOP + 1.4, cw - 0.36, 3.3, { fontSize: 9, lineSpacingMultiple: 1.44 });
  });
  label(s, "One voice per surface. All five meet only in the mark.", MAIN_X, TOP + 5.28, MAIN_W, C.mute, { bold: false });
}

{ // 1.3 personality
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "1.3  Brand Personality",
    intro: "Our personality is deliberately human. World-class work and a premium experience can "
      + "arrive with a personal touch. Our confidence comes from competence, which lets us be "
      + "relaxed and direct.",
    foot: "We take the work seriously. We do not take ourselves too seriously.",
  });
  serif(s, "Confident in our expertise,\napproachable in our delivery.", MAIN_X, TOP - 0.04, MAIN_W, 1.5, { fontSize: T.display });
  const half = (MAIN_W - 0.5) / 2;
  rect(s, MAIN_X, TOP + 1.72, half, 3.5, C.sageTint);
  label(s, "We are", MAIN_X + 0.3, TOP + 1.98, half - 0.6, C.sageInk);
  body(s, "Insightful partners, trusted guides and creative catalysts. Curious, attentive and "
    + "invested in the success of every owner we work with — and glad of the company while we build "
    + "it together.\n\nWe love a complicated problem and the simple answer on the far side of it. We "
    + "live for the moment a good plan becomes a result the owner is proud to show.",
    MAIN_X + 0.3, TOP + 2.3, half - 0.6, 2.9, { fontSize: 11, lineSpacingMultiple: 1.46 });
  rect(s, MAIN_X + half + 0.5, TOP + 1.72, half, 3.5, null, { color: C.rule, width: 0.75 });
  label(s, "We are never", MAIN_X + half + 0.8, TOP + 1.98, half - 0.6, C.coralInk);
  txt(s, "Cold.\nArrogant.\nRigid.\nGeneric.\nTransactional.", {
    x: MAIN_X + half + 0.8, y: TOP + 2.36, w: half - 0.6, h: 2.8,
    fontFace: SERIF, fontSize: T.head, color: C.ink, lineSpacingMultiple: 1.22,
  });
}

{ // 1.4 archetypes
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "1.4  Brand Archetypes",
    intro: "Three archetypes, in order. The Magician leads: we are agents of change, and the moment "
      + "a plan becomes a result is the moment we work for.",
    foot: "The staggered baseline is the modular rhythm — rank falling left to right.",
  });
  const arcs = [
    ["Primary", "The Magician", "Agents of change and vision. We turn ambitious ideas into reality, often in ways that looked impossible from the porch. We see what could be and we have the hands to make it."],
    ["Secondary", "The Sage", "Guided by truth and understanding. We seek out what is actually happening and share it plainly, bringing clarity to complexity. Every date we give can be checked."],
    ["Tertiary", "The Creator", "Driven to build, invent and express. We care about originality and craft, and we obsess over the details of execution so the finished thing is both beautiful and useful."],
  ];
  const cw = (MAIN_W - 2 * 0.36) / 3;
  arcs.forEach(([rank, name, t], i) => {
    const x = MAIN_X + i * (cw + 0.36);
    const y = TOP + i * 0.30;
    vline(s, x, y, 4.3, C.rule, 0.75);
    label(s, rank, x + 0.26, y, cw - 0.26, C.violetInk, { fontSize: 7 });
    txt(s, name, { x: x + 0.26, y: y + 0.3, w: cw - 0.26, h: 0.6, fontFace: SERIF, fontSize: T.head, color: C.ink });
    body(s, t, x + 0.26, y + 1.02, cw - 0.32, 2.6, { fontSize: 11, lineSpacingMultiple: 1.46 });
  });
}

{ // 1.5 tone of voice
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "1.5  Tone of Voice",
    intro: "The voice is constant; the tone flexes. Five attributes hold whatever the subject, and "
      + "six contexts set the register.",
  });
  const attrs = [
    ["Insightful", "The perspective, never the data dump"],
    ["Warm", "Humans speaking to humans, never sentimental"],
    ["Plain", "The words of the owner, never jargon"],
    ["Vivid", "A well-chosen story, never style over substance"],
    ["Specific", "Every number and promise named, never a range"],
  ];
  const tones = [
    ["The plan and the proposal", "Exacting and warm. A plan handed across a kitchen table, every figure named."],
    ["The sales page", "Editorial, not corporate. A magazine, not a landing page. It rewards a reader."],
    ["The journal", "The almanac. What was done, what it cost, what came back. Hype never."],
    ["Social", "Single observations, single sentences. When in doubt, post less."],
    ["About", "Personal and composed. The story of the name, told once."],
    ["Crisis", "Slower, not faster. Composed, not reassuring. The composure is the reassurance."],
  ];
  const halfW = span(4);
  label(s, "The voice — five attributes, fixed", MAIN_X, TOP + 0.02, halfW, C.ink, { fontSize: 7 });
  attrs.forEach(([a, m], i) => {
    const y = TOP + 0.42 + i * 0.92;
    hline(s, MAIN_X, y, halfW, C.ruleSoft, 0.75);
    txt(s, a, { x: MAIN_X, y: y + 0.16, w: halfW, h: 0.36, fontFace: SERIF, fontSize: T.sub, color: C.ink });
    body(s, m, MAIN_X, y + 0.58, halfW, 0.3, { fontSize: T.caption, color: C.muteDark });
  });
  const tx = MAIN_X + halfW + 0.5, tw = MAIN_W - halfW - 0.5;
  label(s, "The tone — six contexts", tx, TOP + 0.02, tw, C.ink, { fontSize: 7 });
  tones.forEach(([a, m], i) => {
    const y = TOP + 0.42 + i * 0.765;
    hline(s, tx, y, tw, C.ruleSoft, 0.75);
    txt(s, a, { x: tx, y: y + 0.13, w: tw, h: 0.26, fontFace: SANS, fontSize: 11, bold: true, color: C.ink });
    body(s, m, tx, y + 0.4, tw, 0.3, { fontSize: T.caption, color: C.muteDark });
  });
}

{ // 1.6 messaging
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "1.6  Brand Messaging",
    intro: "The essence is the internal north star and is never printed. The signature rides beside "
      + "the mark. The primary message is the ten-second read.",
  });
  rect(s, MAIN_X, TOP, span(4), 2.1, C.boneLight);
  label(s, "The essence  ·  never printed", MAIN_X + 0.3, TOP + 0.26, span(4) - 0.6, C.mute, { fontSize: 7 });
  txt(s, "Connecting passion\nto possibility.", { x: MAIN_X + 0.3, y: TOP + 0.62, w: span(4) - 0.6, h: 1.2, fontFace: SERIF, fontSize: T.head, color: C.ink, lineSpacingMultiple: 1.1 });
  const sx = MAIN_X + span(4) + 0.5;
  rect(s, sx, TOP, MAIN_W - span(4) - 0.5, 2.1, C.ink);
  label(s, "The signature  ·  beside the mark", sx + 0.3, TOP + 0.26, 3.5, C.muteLight, { fontSize: 7 });
  txt(s, "We bring the city\nto your door.", { x: sx + 0.3, y: TOP + 0.62, w: 4.0, h: 1.2, fontFace: SERIF, fontSize: T.head, color: C.bone, lineSpacingMultiple: 1.1 });
  label(s, "The primary message  ·  the ten-second read", MAIN_X, TOP + 2.4, MAIN_W, C.ink, { fontSize: 7 });
  serif(s, "Five Points builds the marketing and the systems that bring the city to your door — "
    + "and you keep every one of them.", MAIN_X, TOP + 2.72, MAIN_W, 1.2, { fontSize: T.sub, lineSpacingMultiple: 1.26 });
  label(s, "Secondary messages", MAIN_X, TOP + 4.1, MAIN_W, C.ink, { fontSize: 7 });
  const secs = ["Answering the right questions.", "We manage the complexity. You focus on the vision.",
    "Clarity is the foundation.", "One door at a time.", "Yours from the day it goes live.",
    "Never lose another job you could have won.", "Good is pleasant. Great is powerful."];
  const cw2 = (MAIN_W - 2 * 0.36) / 3;
  secs.forEach((t, i) => {
    const x = MAIN_X + (i % 3) * (cw2 + 0.36), y = TOP + 4.42 + Math.floor(i / 3) * 0.62;
    txt(s, String(i + 1).padStart(2, "0"), { x, y, w: 0.32, h: 0.24, fontFace: SERIF, fontSize: 11, color: C.mute });
    txt(s, bind(t), { x: x + 0.42, y, w: cw2 - 0.42, h: 0.56, fontFace: SERIF, fontSize: 11,
      color: C.inkSoft, lineSpacingMultiple: 1.32 });
  });
}

// ============================================================ 2.0 BRANDMARKS
divider(1);

{ // 2.1 the mark
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "2.1  The Mark",
    intro: "The Quintessence. Five petals at seventy-two degrees around a rounded pentagon core, "
      + "every petal a golden rhombus bowed into a leaf.\n\nFive-fold symmetry is the one order "
      + "that cannot tile a plane periodically. The figure exists only by design, which is the "
      + "studio in one object.",
    foot: "The mark carries the studio wherever the wordmark is absent or too long to work — card "
      + "fronts, envelope flaps, avatars, seals and the favicon.",
  });
  rect(s, MAIN_X, TOP, span(4), 4.264, C.ink);
  mark(s, 2.6, MAIN_X + (span(4) - 2.6) / 2, TOP + (4.264 - 2.6) / 2, "bone");
  label(s, "Parchment on ink  ·  the signature rendering", MAIN_X, TOP + 4.42, span(4), C.mute, { fontSize: 7, bold: false });
  const tx = MAIN_X + span(4) + 0.5, tw = MAIN_W - span(4) - 0.5;
  serif(s, "One of one.", tx, TOP, tw, 0.7, { fontSize: T.display });
  body(s, "The mark is fixed and canonical. Where an identity of this kind usually asks the mark to "
    + "carry its own variation, here the variance lives in the field instead — a stable mark for "
    + "recognition, a variable ground for expression.\n\nOne colour per rendering. Never rotated, "
    + "never outlined, never placed over a photograph.",
    tx, TOP + 0.86, tw, 2.4, { fontSize: 11, lineSpacingMultiple: 1.5 });
  mark(s, 1.5, tx, TOP + 3.35, "ink");
  label(s, "Ink on bone  ·  documents and the page", tx, TOP + 5.0, tw, C.mute, { fontSize: 7, bold: false });
}

{ // 2.2 geometry
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "2.2  The Geometry",
    intro: "The construction law. Every constant is checkable against the drawn artefact, and "
      + "nothing else is added.",
    foot: "Where a sketch and the law diverge, the law governs. The geometry file is upstream truth; "
      + "the SVG, the favicon and the design system follow from it in one pass.",
  });
  s.addImage({ path: "plate-geometry.png", x: MAIN_X + 0.35, y: TOP + 0.1, w: 8.2, h: 8.2 * 660 / 900 });
}

{ // 2.3 the mark ladder
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "2.3  The Mark Ladder",
    intro: "The mark holds its detail down to twenty pixels. Below that the petals close on the "
      + "core and the figure muddies, so it steps down one rung. The tier is chosen by the rendered "
      + "size, never by the surface.",
    foot: "THE ROSETTE\nTwenty pixels and above. Everything: covers, cards, avatars, footers, the "
      + "page, the favicon at 32.\n\n"
      + "THE MICRO MARK\nBelow twenty pixels. Nav glyphs, email signatures, in-line marks, the "
      + "favicon at 16. The core alone, which is the one part of the figure that never closes up.",
    footY: BOT - 2.6, footLead: 1.34,
  });
  s.addImage({ path: "plate-tiers.png", x: MAIN_X, y: TOP + 0.5, w: MAIN_W, h: MAIN_W * 470 / 1200 });
}

{ // 2.4 colourways
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "2.4  Colourways",
    intro: "Four renderings, and no others. One colour per rendering, always — the mark never "
      + "carries two.",
    foot: "Parchment on ink is the signature: ceremonial surfaces, seals, avatars and the favicon. "
      + "Ink on bone is the default on the page.",
  });
  s.addImage({ path: "plate-colourways.png", x: MAIN_X, y: TOP + 1.0, w: MAIN_W, h: MAIN_W * 290 / 1200 });
  hline(s, MAIN_X, TOP + 3.75, MAIN_W, C.ruleSoft, 0.75);
  body(s, "The mark never sits on a photograph, and never on a tint. Where a surface is neither ink "
    + "nor bone, the mark takes the ink rendering if the ground is light and the parchment rendering "
    + "if it is dark.", MAIN_X, TOP + 4.0, span(6), 0.9, { fontSize: 11, lineSpacingMultiple: 1.5 });
}

{ // 2.5 clear space
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "2.5  Clear Space",
    intro: "Clear space is measured in mark-heights: one and a half on every side, one as the floor. "
      + "Nothing enters that field — no type, no rule, no image edge.",
    foot: "The scale row shows the ladder in action: the rosette carries every surface down to "
      + "twenty pixels, and the micro mark takes everything smaller.",
  });
  s.addImage({ path: "plate-clearspace.png", x: MAIN_X, y: TOP + 1.1, w: MAIN_W, h: MAIN_W * 560 / 1120 });
}

{ // 2.6 mark misuse
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "2.6  Mark Misuse",
    intro: "The mark is drawn once and applied as drawn. Outlined over the page are the treatments "
      + "that weaken it. When using the mark, avoid the following.",
    foot: "01  Do not rotate\n02  Do not outline\n03  Do not distort\n04  Do not recolour off-palette\n"
      + "05  Do not add effects\n06  Do not set the rosette below 20 px",
  });
  s.addImage({ path: "plate-mark-misuse.png", x: MAIN_X, y: TOP + 1.3, w: MAIN_W, h: MAIN_W * 500 / 1200 });
}

// ============================================================ 3.0 COLOUR
divider(2);

{ // 3.1 primary palette
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "3.1  Primary Palette",
    intro: "Bone and ink are the ground. The five voices are drawn from the original five-circle "
      + "mark — one voice per surface, and all five meet only in the mark.\n\nCoral leads and does "
      + "the work of an accent.",
  });
  const sw = [
    { name: "Ink", hex: C.ink, fg: C.bone, rgb: "15 / 15 / 16", cmyk: "0 / 0 / 0 / 94" },
    { name: "Bone", hex: C.bone, fg: C.ink, rgb: "234 / 224 / 200", cmyk: "8 / 10 / 22 / 0" },
    { name: "Coral", hex: C.coral, fg: C.paper, rgb: "217 / 110 / 110", cmyk: "0 / 60 / 43 / 15" },
    { name: "Priscilla", hex: C.priscilla, fg: C.ink, rgb: "138 / 172 / 217", cmyk: "36 / 17 / 0 / 15" },
    { name: "Naples", hex: C.naples, fg: C.ink, rgb: "248 / 220 / 85", cmyk: "0 / 11 / 66 / 3" },
    { name: "African Violet", hex: C.violet, fg: C.ink, rgb: "164 / 145 / 205", cmyk: "20 / 29 / 0 / 20" },
    { name: "Ash Green", hex: C.sage, fg: C.ink, rgb: "140 / 191 / 166", cmyk: "27 / 0 / 13 / 25" },
  ];
  const cw = (MAIN_W - 6 * 0.1) / 7;
  sw.forEach((k, i) => {
    const x = MAIN_X + i * (cw + 0.1);
    rect(s, x, TOP, cw, 4.9, k.hex, k.hex === C.bone ? { color: C.rule, width: 0.5 } : null);
    label(s, k.name, x + 0.16, TOP + 0.22, cw - 0.3, k.fg, { fontSize: 7 });
    [["HEX", "#" + k.hex], ["RGB", k.rgb], ["CMYK", k.cmyk]].forEach(([a, v], j) => {
      const y = TOP + 3.62 + j * 0.42;
      txt(s, a, { x: x + 0.16, y, w: cw - 0.3, h: 0.16, fontFace: SANS, fontSize: 6, color: k.fg, charSpacing: 0.7 });
      txt(s, v, { x: x + 0.16, y: y + 0.17, w: cw - 0.3, h: 0.2, fontFace: SANS, fontSize: 7.5, color: k.fg });
    });
  });
  label(s, "Emerald and Burnt Orange are retired. Pinewood and Gilt survive on seals and certificates only.",
    MAIN_X, TOP + 5.16, MAIN_W, C.mute, { bold: false });
}

{ // 3.2 surface tints
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "3.2  Surface Tints",
    intro: "Five paper tones carried forward from the 2025 book. They give a surface warmth without "
      + "adding colour — porch light on paper.",
    foot: "Tints are grounds, never type. Body copy never sets in a tint and a tint never carries the mark.",
  });
  const tints = [["Early Dawn", C.earlyDawn], ["Quarter Spanish", C.quarterSpanish], ["Haze", C.haze],
    ["Catskill", C.catskill], ["Seasalt", C.seasalt]];
  const cw = (MAIN_W - 4 * 0.15) / 5;
  tints.forEach(([n, h], i) => {
    const x = MAIN_X + i * (cw + 0.15);
    rect(s, x, TOP, cw, 3.6, h, { color: C.ruleSoft, width: 0.5 });
    label(s, n, x + 0.2, TOP + 0.26, cw - 0.4, C.muteDark, { fontSize: 7 });
    txt(s, "#" + h, { x: x + 0.2, y: TOP + 3.04, w: cw - 0.4, h: 0.24, fontFace: SANS, fontSize: 7.5, color: C.muteDark });
  });
  label(s, "Golden section", MAIN_X, TOP + 4.0, MAIN_W, C.ink, { fontSize: 7 });
  body(s, "The page band is 6.90 inches. Its golden section falls at 4.264 — the depth of the image "
    + "well on a standard study page, and the line a full-bleed field is cut to. Where the ratio does "
    + "not serve, the modular grid does: twelve columns, a 0.15 gutter and a scale on the square root "
    + "of phi.", MAIN_X, TOP + 4.32, span(6), 1.4, { fontSize: 11, lineSpacingMultiple: 1.5 });
}

{ // 3.3 weighting
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "3.3  Colour Weighting",
    intro: "Bone and ink carry four fifths of any surface. Coral leads the voices. The remaining "
      + "four are accents and never compete.",
    foot: "One voice per surface is the law. A page that reaches for a second voice has lost its argument.",
  });
  const weights = [["Bone", C.bone, 52], ["Ink", C.ink, 26], ["Coral", C.coral, 10],
    ["Priscilla", C.priscilla, 4], ["Naples", C.naples, 3], ["African Violet", C.violet, 3], ["Ash Green", C.sage, 2]];
  let x = MAIN_X;
  weights.forEach(([n, h, p], i) => {
    const w = MAIN_W * p / 100;
    rect(s, x, TOP + 0.4, w, 1.9, h, h === C.bone ? { color: C.rule, width: 0.5 } : null, 0);
    if (p >= 10) {
      label(s, `${p}%`, x + 0.16, TOP + 0.62, w - 0.3, (h === C.ink) ? C.bone : C.ink, { fontSize: 7 });
      txt(s, n, { x: x + 0.16, y: TOP + 1.86, w: w - 0.3, h: 0.3, fontFace: SANS, fontSize: 7.5, color: (h === C.ink) ? C.bone : C.ink });
    }
    x += w;
  });
  const ly = TOP + 2.5;
  weights.filter((k) => k[2] < 10).forEach((k, i) => {
    const lx = MAIN_X + i * 1.5;
    rect(s, lx, ly, 0.15, 0.15, k[1], null, RAD_SM);
    txt(s, `${k[0]}  ·  ${k[2]}%`, { x: lx + 0.24, y: ly - 0.03, w: 1.24, h: 0.22, fontFace: SANS, fontSize: 7.5, color: C.muteDark });
  });
  label(s, "Weighting across any single piece", MAIN_X + 6.0, ly - 0.02, 2.87, C.mute, { bold: false, fontSize: 7, align: "right" });
  const demos = [["A study page", C.paper, C.ink], ["A voice surface", C.coralTint, C.coralInk], ["A ceremonial surface", C.ink, C.bone]];
  const dw = (MAIN_W - 2 * 0.3) / 3;
  demos.forEach(([n, bg, fg], i) => {
    const dx = MAIN_X + i * (dw + 0.3);
    rect(s, dx, TOP + 3.1, dw, 2.4, bg, bg === C.paper ? { color: C.rule, width: 0.5 } : null);
    label(s, n, dx + 0.24, TOP + 3.34, dw - 0.48, fg, { fontSize: 7 });
    txt(s, "We bring the\ncity to your door.", { x: dx + 0.24, y: TOP + 3.7, w: dw - 0.48, h: 1.1, fontFace: SERIF, fontSize: T.sub, color: fg, lineSpacingMultiple: 1.12 });
  });
}

{ // 3.4 combinations
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "3.4  Colour Combinations",
    intro: "Shown here are the pairings that hold. Always lead with bone and ink and use a voice as "
      + "the accent — that is how the volume goes up or down.",
    foot: "Never pair two voices. Never set small text in Naples or Coral on bone: both fail contrast "
      + "below 14 point, where the ink tones take over.",
  });
  const pairs = [
    ["Bone on ink", C.ink, C.bone], ["Ink on bone", C.bone, C.ink], ["Bone on coral", C.coral, C.paper],
    ["Ink on priscilla", C.priscilla, C.ink], ["Ink on naples", C.naples, C.ink], ["Ink on ash green", C.sage, C.ink],
  ];
  const cw = (MAIN_W - 2 * 0.24) / 3, ch = 2.34;
  pairs.forEach(([n, bg, fg], i) => {
    const x = MAIN_X + (i % 3) * (cw + 0.24), y = TOP + Math.floor(i / 3) * (ch + 0.4);
    rect(s, x, y, cw, ch, bg, bg === C.bone ? { color: C.rule, width: 0.5 } : null);
    label(s, n, x + 0.24, y + 0.24, cw - 0.48, fg, { fontSize: 7 });
    txt(s, "Aa", { x: x + 0.24, y: y + 0.72, w: cw - 0.48, h: 1.3, fontFace: SERIF, fontSize: 46, color: fg });
  });
}

// ============================================================ 4.0 TYPOGRAPHY
divider(3);

{ // 4.1 primary typeface
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, dark: true, title: "4.1  Primary Typeface",
    intro: "A friendly serif is the warmest thing on a page, so it leads. Sentence case, up to weight "
      + "500 on a headline.\n\nPP Editorial New is the licensed face; Bookmania — the studio's own "
      + "serif from 2025 — stands in until the licence lands.",
    foot: "Set display in sentence case. Italic is for editorial emphasis, never a default.",
  });
  label(s, "Bookmania  ·  interim for PP Editorial New", MAIN_X, TOP + 0.02, MAIN_W, C.muteLight, { fontSize: 7 });
  [["Regular", "Connecting passion to possibility"], ["Italic", "The city comes to your door"],
   ["Semibold", "Never lose another job"], ["Bold", "Five Points Digital Studio"]].forEach(([w, t], i) => {
    const y = TOP + 0.5 + i * 1.16;
    hline(s, MAIN_X, y, MAIN_W, C.ruleDark, 0.75);
    label(s, w, MAIN_X, y + 0.2, 1.4, C.mute, { fontSize: 7, bold: false });
    txt(s, t, { x: MAIN_X + 1.6, y: y + 0.06, w: MAIN_W - 1.6, h: 0.96, fontFace: SERIF, fontSize: 30,
      color: C.bone, italic: w === "Italic", bold: w === "Bold", valign: "middle" });
  });
  txt(s, "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz  1234567890", {
    x: MAIN_X, y: TOP + 5.2, w: MAIN_W, h: 0.5, fontFace: SERIF, fontSize: 15, color: C.muteLight });
}

{ // 4.2 secondary typeface
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "4.2  Secondary Typeface",
    intro: "The grotesque does the working text — body copy, labels, tables and every number. It "
      + "never carries a display line.\n\nPP Neue Montreal is the licensed face; Manrope stands in "
      + "until the licence lands.",
    foot: "The letterspaced capital is the house label: nine point, semibold, tracked at 1.8.",
  });
  label(s, "Manrope  ·  interim for PP Neue Montreal", MAIN_X, TOP + 0.02, MAIN_W, C.mute, { fontSize: 7 });
  [["Light", 300], ["Regular", 400], ["Semibold", 600], ["Bold", 700]].forEach(([w, wt], i) => {
    const y = TOP + 0.5 + i * 1.16;
    hline(s, MAIN_X, y, MAIN_W, C.ruleSoft, 0.75);
    label(s, w, MAIN_X, y + 0.2, 1.4, C.mute, { fontSize: 7, bold: false });
    txt(s, "The desk, the callback, the list, the job", {
      x: MAIN_X + 1.6, y: y + 0.06, w: MAIN_W - 1.6, h: 0.94, fontFace: SANS, fontSize: 26,
      color: C.ink, bold: wt >= 600, valign: "middle" });
  });
  txt(s, "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz  1234567890", {
    x: MAIN_X, y: TOP + 5.2, w: MAIN_W, h: 0.5, fontFace: SANS, fontSize: 14, color: C.mute });
}

{ // 4.3 hierarchy
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "4.3  Type Hierarchy",
    intro: "A modular scale on the square root of phi — 1.272. Every size on every surface comes "
      + "from this ladder and nowhere else.",
    foot: "Body never sets below nine point. The measure never exceeds sixty-five characters, roughly "
      + "6.4 inches at eleven point.",
  });
  [["Hero", SERIF, 36, "36 / 1.02", "Covers, the close", "The city to your door"],
   ["Display", SERIF, 28, "28 / 1.10", "Page openers", "We bring the city to you"],
   ["Head", SERIF, 22, "22 / 1.14", "Section heads", "We bring the city to your door"],
   ["Subhead", SERIF, 18, "18 / 1.20", "Card titles", "We bring the city to your door"],
   ["Lead", SANS, 14, "14 / 1.45", "Standfirst", "We bring the city to your door"],
   ["Body", SANS, 11, "11 / 1.50", "Running text", "We bring the city to your door"],
   ["Caption", SANS, 9.5, "9.5 / 1.42", "Notes, captions", "We bring the city to your door"],
   ["Label", SANS, 9, "9 / caps / +1.8", "Eyebrows, tables", "We bring the city to your door"],
  ].forEach(([n, face, size, spec, use, sample], i) => {
    const y = TOP + 0.05 + i * 0.79;
    hline(s, MAIN_X, y, MAIN_W, C.ruleSoft, 0.75);
    label(s, n, MAIN_X, y + 0.2, 1.2, C.ink, { fontSize: 7 });
    txt(s, sample, { x: MAIN_X + 1.3, y: y + 0.08, w: 5.3, h: 0.68, fontFace: face, fontSize: size,
      color: C.inkSoft, valign: "middle" });
    txt(s, spec, { x: MAIN_X + 6.75, y: y + 0.26, w: 1.1, h: 0.3, fontFace: SANS, fontSize: 8, color: C.muteDark });
    txt(s, use, { x: MAIN_X + 7.9, y: y + 0.26, w: 0.97, h: 0.3, fontFace: SANS, fontSize: 8, color: C.mute });
  });
}

{ // 4.4 type misuse
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "4.4  Type Misuse",
    intro: "Typography carries most of the weight of this brand, so the ways it is weakened matter. "
      + "Outlined over the page are the practices to avoid.",
    footY: BOT - 2.5, footSize: 9, footLead: 1.32,
    foot: "01  Do not letterspace body\n02  Do not centre long copy\n03  Do not set tight\n"
      + "04  Do not set loose\n05  Do not set body in capitals\n06  Do not mix in a foreign face\n"
      + "07  Do not italicise by default\n08  Do not set below nine point\n09  Do not colour body off-palette",
  });
  const sample = "Lorem ipsum dolor sit amet, consectetur quis amet adipiscing elit, sed do eiusmod tempor.";
  const cells = [{ charSpacing: 4, text: "Lorem ipsum dolor sit amet, consectetur quis amet." }, { align: "center" }, { lineSpacingMultiple: 0.82 },
    { lineSpacingMultiple: 2.3 }, { text: sample.toUpperCase() }, { fontFace: "Arial" },
    { italic: true }, { fontSize: 6.5 }, { color: "2E7D32" }];
  const cw = (MAIN_W - 2 * 0.22) / 3, ch = 1.62;
  cells.forEach((o, i) => {
    const x = MAIN_X + (i % 3) * (cw + 0.22), y = TOP + Math.floor(i / 3) * (ch + 0.26);
    rect(s, x, y, cw, ch, null, { color: C.ruleSoft, width: 0.75 });
    label(s, String(i + 1).padStart(2, "0"), x + 0.16, y + 0.14, 0.6, C.mute, { fontSize: 7, bold: false });
    const { text, ...rest } = o;
    body(s, text || sample, x + 0.16, y + 0.44, cw - 0.32, ch - 0.6, { fontSize: 9.5, lineSpacingMultiple: 1.4, ...rest });
  });
}

// ============================================================ 5.0 PHOTOGRAPHY
divider(4);

{ // 5.1 style
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "5.1  Photographic Style",
    intro: "Photography is people. The owner at his place, the crew, the truck in the drive, hands "
      + "at work. Faces allowed. Evening light.\n\nThe image library should feel like a private "
      + "archive of the working day, never a stock library.",
    footY: BOT - 2.55, footLead: 1.34,
    foot: "THE OWNER\nAt his own place — the yard, the shop, the kitchen table. Never behind a desk that is not his.\n\n"
      + "THE WORK\nHands, tools, materials, the van. The object of the trade, closely and honestly.\n\n"
      + "THE PLACE\nAtlanta as it looks at the end of a working day. Never a skyline.",
  });
  const cw = (MAIN_W - 2 * 0.28) / 3, ch = cw * 1.272;
  [["scr-hero.png", "The owner"], ["scr-second.png", "The work"], ["scr-third.png", "The place"]]
    .forEach(([img, cap], i) => {
      const x = MAIN_X + i * (cw + 0.28);
      s.addImage({ path: img, x, y: TOP, w: cw, h: ch });
      label(s, cap, x, TOP + ch + 0.14, cw, C.mute, { bold: false, fontSize: 7 });
    });
  label(s, "Every photograph in the documentation ships screened — see 6.3. Sources here are "
    + "placeholders from the generated library; commissioned photography of the trades enters at "
    + "the next revenue rung.", MAIN_X, TOP + ch + 0.42, MAIN_W, C.mute,
    { bold: false, fontSize: 7 });
}

{ // 5.2 light and colour
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "5.2  Light and Colour",
    intro: "One source, warm and directional — a work lamp, a doorway, the end of the day. Shadow is "
      + "welcome as a compositional element.",
    footY: BOT - 2.35, footLead: 1.34,
    foot: "DO\nWarm single-source light. Natural colour balance. Shadow detail retained. Monochrome "
      + "only when the subject earns it.\n\nDO NOT\nRing light. Flat office light. On-camera flash. "
      + "Heavy teal and orange. Bright-and-airy grading.",
  });
  const gw = (MAIN_W - 2 * 0.24) / 3, gh = 4.9;
  well(s, MAIN_X, TOP, gw, gh, null, { inner: "GOLDEN HOUR" });
  well(s, MAIN_X + gw + 0.24, TOP, gw, (gh - 0.24) / 2, null, { inner: "WORK LAMP" });
  well(s, MAIN_X + gw + 0.24, TOP + (gh - 0.24) / 2 + 0.24, gw, (gh - 0.24) / 2, null, { inner: "DOORWAY" });
  well(s, MAIN_X + 2 * (gw + 0.24), TOP, gw, gh, null, { inner: "EVENING" });
  label(s, "Gallery wall  ·  modular, never a uniform grid", MAIN_X, TOP + gh + 0.24, MAIN_W, C.mute,
    { bold: false, fontSize: 7 });
}

{ // 5.3 casting and composition
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "5.3  Casting and Composition",
    intro: "Cast the people who actually do the work, and the people they serve. Atlanta as it is: "
      + "every race, every age on a crew, women on the tools as readily as men.",
    foot: "Frame with floor-plan discipline. Negative space between half and two thirds. People sit "
      + "within the frame rather than filling it — the work has equal weight.",
  });
  const cw = (MAIN_W - 2 * 0.22) / 3, ch = 2.3;
  ["Owner-operator", "The crew", "The customer", "Hands and tools", "The van", "The street"]
    .forEach((cap, i) => {
      const x = MAIN_X + (i % 3) * (cw + 0.22), y = TOP + Math.floor(i / 3) * (ch + 0.52);
      well(s, x, y, cw, ch, cap, { inner: "LANDSCAPE" });
    });
}

// ============================================================ 6.0 APPLICATION
divider(5);

{ // 6.1 the law of the field
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "6.1  The Law of the Field",
    intro: "A field is not decoration and it is not wallpaper. It is the air a page sits in, drawn "
      + "entirely from pieces of the mark.\n\nFive rules separate the two, and every one of them "
      + "is a rule about restraint.",
    foot: "The law forbids a field behind body copy at full strength, more than one field on a "
      + "spread, the mark rotated, and the complete mark used as a pattern element. The mark is the "
      + "mark. The pieces are the pattern.",
  });
  const rules = [
    ["01", "Few elements", "Three to six forms. What is not there is the composition."],
    ["02", "One hue, several steps", "A single colour in three or four tonal steps. Never a mix of the five voices."],
    ["03", "One form dominates", "Clear variation in scale. Forms at one size read as wallpaper, whatever the spacing."],
    ["04", "Shapes leave the frame", "At least one form cut by an edge. A field that fits inside its box is a picture."],
    ["05", "Nothing repeats visibly", "Where a field does repeat, the seam is invisible and the rhythm carries two scales."],
  ];
  const cw = (MAIN_W - 4 * 0.26) / 5;
  rules.forEach(([n, h, t], i) => {
    const x = MAIN_X + i * (cw + 0.26);
    hline(s, x, TOP, cw, C.rule, 0.75);
    label(s, n, x, TOP + 0.16, cw, C.mute, { fontSize: 7 });
    txt(s, h, { x, y: TOP + 0.48, w: cw, h: 0.62, fontFace: SERIF, fontSize: 15,
      color: C.ink, lineSpacingMultiple: 1.12 });
    body(s, t, x, TOP + 1.22, cw, 2.0, { fontSize: T.caption, lineSpacingMultiple: 1.5 });
  });
  s.addImage({ path: "fld-tumbling.png", x: MAIN_X, y: TOP + 3.5, w: MAIN_W, h: MAIN_W * 500 / 1200 });
  label(s, "Tumbling Air  ·  the law in one field", MAIN_X, TOP + 3.62 + MAIN_W * 500 / 1200,
    MAIN_W, C.mute, { bold: false, fontSize: 7 });
}

{ // 6.2 the four fields
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "6.2  The Four Fields",
    intro: "Four fields, all cut from the leaf. No new shape was invented to make them.",
    foot: "TUMBLING AIR\nCovers, card backs and section openers.\n\n"
      + "THE DESCENT\nSpines, side rails and margins. It survives being very narrow.",
    footY: BOT - 1.5, footLead: 1.34,
  });
  const g = 0.24;
  // row one - the motif at rest, and the drift
  const h1 = 2.45, wM = h1, wT = h1 * 1200 / 500;
  s.addImage({ path: "fld-trefoil-motif.png", x: MAIN_X, y: TOP, w: wM, h: h1 });
  label(s, "The Trefoil  ·  the motif alone", MAIN_X, TOP + h1 + 0.13, wM, C.mute,
    { bold: false, fontSize: 7 });
  s.addImage({ path: "fld-tumbling.png", x: MAIN_X + wM + g, y: TOP, w: wT, h: h1 });
  label(s, "Tumbling Air  ·  the drift", MAIN_X + wM + g, TOP + h1 + 0.13, wT, C.mute,
    { bold: false, fontSize: 7 });
  // row two - the repeat, the descent, and the note that belongs to them
  const y2 = TOP + h1 + 0.52, h2 = 2.62;
  const wR = h2 * 1380 / 920, wD = h2 * 300 / 900;
  s.addImage({ path: "fld-trefoil-repeat.png", x: MAIN_X, y: y2, w: wR, h: h2 });
  label(s, "The Trefoil  ·  the seamless repeat", MAIN_X, y2 + h2 + 0.13, wR, C.mute,
    { bold: false, fontSize: 7 });
  s.addImage({ path: "fld-descent.png", x: MAIN_X + wR + g, y: y2, w: wD, h: h2 });
  label(s, "The Descent", MAIN_X + wR + g, y2 + h2 + 0.13, wD + 0.6, C.mute,
    { bold: false, fontSize: 7 });
  const tx = MAIN_X + wR + wD + 2 * g, tw = MAIN_W - wR - wD - 2 * g;
  serif(s, "The Trefoil", tx, y2, tw, 0.5, { fontSize: T.sub });
  body(s, "Three leaves crossing about one centre. The crossings earn a third tone from two, and "
    + "the triple overlap a fourth, so the tonal steps are earned by the drawing rather than "
    + "declared in the palette.\n\nIt works at two scales: the motif alone on a small surface, "
    + "and the seamless repeat wherever a large area needs filling. The repeat carries two sizes "
    + "on a half-drop so the lattice never flattens into wallpaper.",
    tx, y2 + 0.6, tw, 2.2, { fontSize: T.caption, lineSpacingMultiple: 1.5 });
}

{ // 6.3 the screen
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "6.3  The Screen",
    intro: "Every photograph in the documentation is screened, and the dot is the mark. There is not "
      + "a circle anywhere in a Five Points image.\n\nThe house ruling is eighty-eight marks across "
      + "the width of the image, whatever that width happens to be.",
    foot: "The rosette inks nineteen per cent of its own circle where the core inks fifty. Both are "
      + "sized from measured ink rather than from diameter, which is what lets the screen change "
      + "shape inside one image without a step in tone. The mark takes the highlights, where a dot "
      + "has room to open; the core takes everything darker.",
    footY: BOT - 2.3, footLead: 1.34,
  });
  const iw = MAIN_W, ih = iw * 643 / 1792;
  s.addImage({ path: "scr-ladder.png", x: MAIN_X, y: TOP + 0.3, w: iw, h: ih });
  label(s, "Ruling  ·  the same portrait at four screens. Eighty-eight across is the house setting.",
    MAIN_X, TOP + 0.42 + ih, MAIN_W, C.mute, { bold: false, fontSize: 7 });
}

{ // 6.4 the screen in use
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "6.4  The Screen in Use",
    intro: "Bone on ink is the default register. Ink on paper is reserved for pages that are "
      + "already light. A voice-coloured screen is held back for section dividers.",
    foot: "Sources here are placeholders from the generated library. A screen this strong makes the "
      + "source obvious rather than hiding it: it wants photography of real people in the trades, "
      + "shot with clean tonal separation — a light subject against a dark ground, or the reverse.",
    footY: BOT - 1.45, footLead: 1.34,
  });
  const g = 0.24, h1 = 3.32;
  const w1 = h1 * 550 / 700, w2 = h1 * 700 / 890, w3 = h1 * 360 / 550;
  s.addImage({ path: "scr-hero.png", x: MAIN_X, y: TOP, w: w1, h: h1 });
  s.addImage({ path: "scr-second.png", x: MAIN_X + w1 + g, y: TOP, w: w2, h: h1 });
  s.addImage({ path: "scr-positive.png", x: MAIN_X + w1 + w2 + 2 * g, y: TOP, w: w3, h: h1 });
  label(s, "Bone on ink  ·  the default register", MAIN_X, TOP + h1 + 0.13, w1 + w2 + g, C.mute,
    { bold: false, fontSize: 7 });
  label(s, "Ink on paper  ·  light pages only", MAIN_X + w1 + w2 + 2 * g, TOP + h1 + 0.13, w3,
    C.mute, { bold: false, fontSize: 7 });
  const yd = TOP + h1 + 0.52, wd = MAIN_W, hd = wd * 100 / 400;
  s.addImage({ path: "scr-detail.png", x: MAIN_X, y: yd, w: wd, h: hd });
  label(s, "At the dot  ·  thirty-four marks across. The pentagons carry the midtones; in the "
    + "lightest passages they give way to the rosette itself.",
    MAIN_X, yd + hd + 0.13, MAIN_W, C.mute, { bold: false, fontSize: 7 });
}

divider(6);

{ // 7.1 the journey
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "7.1  The Journey",
    intro: "Five moments, for five points. Service is the work done well; hospitality is how it "
      + "feels to receive it. We compete on both, and only one of them is rare in this market.",
    foot: "Rigorous on ninety-five per cent so five per cent can be spent unreasonably. Gestures come "
      + "from the hospitality log on the card of that owner — one size fits one, never a standard list.",
  });
  const moments = [
    ["The first call", "Thirty minutes, no fee, on your operation. You leave with a plain account of where the work is getting lost, whether or not you go on."],
    ["The plan", "One page. Two prices — the cost of yes and the cost of no. Nothing you have to be taught to read."],
    ["The build", "A short word every week and a link to see the work as it grows. No surprises at the end."],
    ["The keys", "The day it goes live you get everything — the number, the messages, the records, the writing behind them — in one folder with your name on it."],
    ["The quarterly call", "What came back, what changed, what is next. The system is yours; we keep it in good order."],
  ];
  const cw = (MAIN_W - 4 * 0.18) / 5;
  moments.forEach(([h, t], i) => {
    const x = MAIN_X + i * (cw + 0.18);
    bar(s, x, TOP, cw, 0.06, VOICES[i].hex);
    label(s, `0${i + 1}`, x, TOP + 0.26, cw, VOICES[i].ink, { fontSize: 7 });
    txt(s, h, { x, y: TOP + 0.58, w: cw, h: 0.8, fontFace: SERIF, fontSize: 15, color: C.ink, lineSpacingMultiple: 1.12 });
    body(s, t, x, TOP + 1.5, cw, 3.0, { fontSize: T.caption, lineSpacingMultiple: 1.46 });
  });
}

{ // 7.2 the words
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "7.2  The Words",
    intro: "Say it the way the owner would say it. The marque vocabulary is retired: it carried an "
      + "identity the buyer had to be taught, and a roofer should not need a glossary to read a plan.",
  });
  const cols = [
    ["We say", C.sageTint, C.sageInk, "Build. System. Owner. Built for your company. The first call. Testing. The keys. Governance. Return. The plan. Five Points Digital Studio on first mention, Five Points after."],
    ["We never say", C.coralTint, C.coralInk, "Solution. Client, customer or user for the owner. Principal, commissioning, marque-grade, calibration, bespoke. Leverage. ROI. Synergy. Cutting-edge, revolutionary, game-changing. Really, truly, genuinely, actually. Unlock, empower, transform, disrupt, innovate. Pain point. Stakeholder. Touch base, circle back, reach out. Deliverable."],
    ["When in doubt", C.violetTint, C.violetInk, "Say it the way the owner would say it. Prefer silence over hype. Ask how Rolls-Royce Bespoke would treat this owner. Warmth is the default; formality earns its place. Show rather than tell. Less rather than more. Never name a competitor."],
  ];
  const cw = (MAIN_W - 2 * 0.3) / 3;
  cols.forEach(([h, bg, fg, t], i) => {
    const x = MAIN_X + i * (cw + 0.3);
    rect(s, x, TOP, cw, 5.1, bg);
    txt(s, h, { x: x + 0.26, y: TOP + 0.28, w: cw - 0.52, h: 0.5, fontFace: SERIF, fontSize: T.sub, color: fg });
    body(s, t, x + 0.26, TOP + 0.94, cw - 0.52, 4.0, { fontSize: T.caption, lineSpacingMultiple: 1.5 });
  });
  label(s, "The mechanical rules are unchanged: British English, no contractions, no em dashes, no "
    + "Oxford comma, no parentheses, Romance possessives, numerals from ten.",
    MAIN_X, TOP + 5.38, MAIN_W, C.mute, { bold: false, fontSize: 7 });
}

{ // 7.3 stationery
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "7.3  Stationery",
    intro: "The A-series is the house standard — A4 for the plan and the letter, A5 for the folder of "
      + "keys. Ceremony is retired: no lined envelope, no invitation card, no certificate.",
    foot: "The wordmark lives on covers, not on letterhead. Letterhead carries the mark and a contact "
      + "cluster in one corner, and nothing runs the full width.",
  });
  const bcW = 2.15, bcH = 2.15, rowH = 3.4;
  rect(s, MAIN_X, TOP, bcW, bcH, C.ink);
  mark(s, 0.92, MAIN_X + (bcW - 0.92) / 2, TOP + (bcH - 0.92) / 2, "bone");
  label(s, "Card front  ·  74 × 74 mm", MAIN_X, TOP + bcH + 0.14, bcW, C.mute, { fontSize: 7, bold: false });
  const b2 = MAIN_X + bcW + 0.25;
  rect(s, b2, TOP, bcW, bcH, C.bone, { color: C.rule, width: 0.5 });
  txt(s, "Five Points\nDigital Studio", { x: b2 + 0.2, y: TOP + 0.2, w: bcW - 0.4, h: 0.62, fontFace: SERIF, fontSize: 11, color: C.ink, lineSpacingMultiple: 1.1 });
  txt(s, "Martavious Spicer\nPartner\nmartavious@fivepoints.studio\n+1 470 556 3989",
    { x: b2 + 0.2, y: TOP + 1.2, w: bcW - 0.4, h: 0.9, fontFace: SANS, fontSize: 6.5, color: C.inkSoft, lineSpacingMultiple: 1.5 });
  label(s, "Card back", b2, TOP + bcH + 0.14, bcW, C.mute, { fontSize: 7, bold: false });
  const lx = b2 + bcW + 0.3, lw = 1.8;
  rect(s, lx, TOP, lw, rowH, C.white, { color: C.rule, width: 0.5 });
  mark(s, 0.36, lx + 0.16, TOP + 0.16, "ink");
  [0.9, 1.08, 1.26, 1.44, 1.62, 1.8].forEach((yy, i) => hline(s, lx + 0.16, TOP + yy, (i % 3 === 2 ? lw * 0.38 : lw - 0.32), C.ruleSoft, 0.5));
  txt(s, "Five Points Digital Studio\nDecatur, Georgia\nfivepoints.studio", { x: lx + 0.16, y: TOP + 2.82, w: lw - 0.32, h: 0.55, fontFace: SANS, fontSize: 5.5, color: C.mute, lineSpacingMultiple: 1.4 });
  label(s, "Letterhead  ·  A4", lx, TOP + rowH + 0.14, lw, C.mute, { fontSize: 7, bold: false });
  const px = MAIN_X + MAIN_W - lw;
  well(s, px, TOP, lw, rowH, "The plan  ·  A4", { inner: "ONE PAGE" });
  well(s, MAIN_X, TOP + 4.0, span(5), 1.6, "The keys  ·  the folder handed over", { inner: "A5 BOOK" });
  well(s, MAIN_X + span(5) + 0.35, TOP + 4.0, MAIN_W - span(5) - 0.35, 1.6, "With compliments  ·  DL", { inner: "SLIP" });
}

{ // 7.4 digital
  const s = bookStudy(pres, {
    page: next(), rail: RAIL, title: "7.4  Digital",
    intro: "Bone and ink are not light mode and dark mode. The register of a page is set by its "
      + "content, never by the preference of the machine.",
    foot: "Corners carry the mark radius. Hover is tonal only. Motion is fades and position moves, "
      + "200 to 400 milliseconds, and honours reduced motion.",
  });
  const sw = span(5), sh = 3.3;
  rect(s, MAIN_X, TOP, sw, sh, C.ink);
  sharpRect(s, MAIN_X, TOP + 0.02, sw, 0.28, C.inkSoft);
  mark(s, 0.19, MAIN_X + 0.14, TOP + 0.06, "bone");
  txt(s, "We bring the city\nto your door.", { x: MAIN_X + 0.34, y: TOP + 0.95, w: sw - 0.68, h: 1.1, fontFace: SERIF, fontSize: 22, color: C.bone, lineSpacingMultiple: 1.08 });
  rect(s, MAIN_X + 0.34, TOP + 2.28, 1.5, 0.34, C.bone, null, RAD_SM);
  txt(s, "Book the first call", { x: MAIN_X + 0.34, y: TOP + 2.35, w: 1.5, h: 0.24, fontFace: SANS, fontSize: 7.5, color: C.ink, align: "center", bold: true });
  label(s, "fivepoints.studio  ·  the hero", MAIN_X, TOP + sh + 0.14, sw, C.mute, { fontSize: 7, bold: false });
  const gx = MAIN_X + sw + 0.4, gw = (MAIN_W - sw - 0.4 - 0.28) / 2;
  rect(s, gx, TOP, gw, gw, C.coralTint);
  txt(s, "Never lose\nanother job\nyou could\nhave won.", { x: gx + 0.22, y: TOP + 0.28, w: gw - 0.44, h: 1.05, fontFace: SERIF, fontSize: 12, color: C.coralInk, lineSpacingMultiple: 1.32 });
  mark(s, 0.28, gx + gw - 0.5, TOP + gw - 0.5, "ink");
  label(s, "Social", gx, TOP + gw + 0.14, gw, C.mute, { fontSize: 7, bold: false });
  const ex = gx + gw + 0.28;
  rect(s, ex, TOP, gw, gw, C.white, { color: C.rule, width: 0.5 });
  mark(s, 0.26, ex + 0.2, TOP + 0.2, "ink");
  txt(s, "Martavious Spicer\nPartner", { x: ex + 0.2, y: TOP + 0.58, w: gw - 0.4, h: 0.4, fontFace: SANS, fontSize: 7, bold: true, color: C.ink, lineSpacingMultiple: 1.35 });
  txt(s, "martavious@fivepoints.studio\nfivepoints.studio", { x: ex + 0.2, y: TOP + 1.02, w: gw - 0.4, h: 0.4, fontFace: SANS, fontSize: 6, color: C.mute, lineSpacingMultiple: 1.4 });
  label(s, "Email signature", ex, TOP + gw + 0.14, gw, C.mute, { fontSize: 7, bold: false });
  well(s, gx, TOP + gw + 0.5, gw * 2 + 0.28, sh - gw - 0.5, "The journal  ·  the almanac", { inner: "ARTICLE" });
}

// ============================================================ close
{
  const s = bookPage(pres, { page: next(), dark: true, chrome: false });
  vtext(s, "FIVE POINTS DIGITAL STUDIO  ·  VERSION 4.0 / 2026", RAIL_X, TOP, TOP + 4.4, { color: C.mute });
  vline(s, RULE1_X, TOP, BOT - TOP, C.ruleDark, 0.75);
  mark(s, 1.1, CX, 1.2, "bone");
  txt(s, "We bring the city\nto your door.", {
    x: CX, y: 3.05, w: 9.4, h: 1.9, fontFace: SERIF, fontSize: T.hero, color: C.bone, lineSpacingMultiple: 1.18 });
  hline(s, CX, 5.55, 3.2, C.ruleDark, 0.75);
  txt(s, "Five Points Digital Studio  ·  Decatur, Georgia  ·  fivepoints.studio  ·  hello@fivepoints.studio", {
    x: CX, y: 5.8, w: 10, h: 0.3, fontFace: SANS, fontSize: 10, color: C.muteLight });
  txt(s, "The pillars, the systems and their prices are ruled at the kitchen bench and join this book as its final pages.", {
    x: CX, y: 6.16, w: 10, h: 0.3, fontFace: SANS, fontSize: 9, color: C.muteDark });
}

pres.writeFile({ fileName: "five-points-identity-book.pptx" })
  .then(() => console.log("identity book:", P, "pages"));
