// Five Points page systems, v6.
//   BOOK   – the Swiss rail system measured off the 2025 fingerprint. The identity book.
//   REPORT – the editorial system decoded from the Musicbed trend report. The capabilities deck.
// Shared tokens: palette, faces, the corner radius, the three-tier mark ladder.
const path = require("path");

// ---------------------------------------------------------------- palette
const C = {
  ink: "0F0F10", inkSoft: "1C1A17", inkDeep: "080809",
  bone: "EAE0C8", boneLight: "F4EDDD", bonePale: "FBF7EE", paper: "F8F8F8", white: "FFFFFF",
  rule: "BDB4A2", ruleSoft: "D8D2C4", ruleDark: "3A362F",
  mute: "7A7264", muteDark: "5E574C", muteLight: "9A9284",
  coral: "D96E6E", coralInk: "A72C2C", coralTint: "F6DDDD", coralDeep: "8F2020",
  priscilla: "8AACD9", priscillaInk: "305A92", priscillaTint: "DEE8F4",
  naples: "F8DC55", naplesInk: "695804", naplesTint: "FDF6D5",
  violet: "A491CD", violetInk: "6549A1", violetTint: "E6E1F1",
  sage: "8CBFA6", sageInk: "37624D", sageTint: "E3F0E9",
  earlyDawn: "FFFAE7", quarterSpanish: "F8EDE3", haze: "F1F6F5", catskill: "F1F5F9", seasalt: "F8F8F8",
  greige: "B5AFA0", wellFill: "EDEAE3", wellRule: "D8D2C4",
};
const VOICES = [
  { name: "Coral", hex: C.coral, ink: C.coralInk, tint: C.coralTint },
  { name: "Priscilla", hex: C.priscilla, ink: C.priscillaInk, tint: C.priscillaTint },
  { name: "Naples", hex: C.naples, ink: C.naplesInk, tint: C.naplesTint },
  { name: "African Violet", hex: C.violet, ink: C.violetInk, tint: C.violetTint },
  { name: "Ash Green", hex: C.sage, ink: C.sageInk, tint: C.sageTint },
];

const SERIF = "Bookmania";
const SANS = "Manrope";

// The corner radius, carried from the mark. Every panel, card, well and chip in the
// system rounds to one of two values so the whole reads as one family with the crystal.
const RAD = 0.09;      // panels, cards, wells, images
const RAD_SM = 0.05;   // chips, buttons, swatches, small tiles

const PAGE_W = 13.333, PAGE_H = 7.5;
const PHI = 1.618;

// ---------------------------------------------------------------- the mark ladder
// Reference 96 px per inch.
// The rosette is the mark, ruled 2026-09-08. The crystal is retired as a mark and
// survives only as the geometric source of the pattern pieces. Two tiers now: the
// rosette everywhere down to 20px, the pentagon core alone below that.
const T_MICRO = 20 / 96;
function markPath(sizeIn, tone = "ink") {
  const tier = sizeIn >= T_MICRO ? "primary" : "micro";
  return path.join(__dirname, `mark-${tier}-${tone}.png`);
}
// The three assets are drawn on the same 480-square canvas, so a placed mark keeps its
// optical weight across the tiers when the box is constant.
function mark(s, sizeIn, x, y, tone = "ink") {
  s.addImage({ path: markPath(sizeIn, tone), x, y, w: sizeIn, h: sizeIn });
}

// ---------------------------------------------------------------- primitives
function rect(s, x, y, w, h, fill, line, radius) {
  // Omit the line key entirely when none is wanted — an empty line object is rendered
  // as an inherited theme stroke by Keynote, which draws a border nobody asked for.
  const o = { x, y, w, h };
  if (line) o.line = line;
  o.fill = fill ? { color: fill } : { type: "none" };
  if (radius === null || radius === 0) {
    s.addShape("rect", o);
  } else {
    // OOXML clamps the roundRect adjustment at half the shorter side; asking for more
    // yields a degenerate shape, so cap it here.
    const r = Math.min(radius === undefined ? RAD : radius, Math.min(w, h) / 2);
    s.addShape("roundRect", { ...o, rectRadius: r });
  }
}
function sharpRect(s, x, y, w, h, fill, line) { rect(s, x, y, w, h, fill, line, 0); }
function hline(s, x, y, w, color, width) {
  s.addShape("line", { x, y, w, h: 0, line: { color: color || C.rule, width: width || 0.75 } });
}
// A rule drawn as a filled bar rather than a line — used where a coloured cap sits on a
// panel and a stroked line would inherit the panel geometry.
function bar(s, x, y, w, h, color, radius) {
  rect(s, x, y, w, h, color, null, radius === undefined ? 0 : radius);
}
function vline(s, x, y, h, color, width) {
  s.addShape("line", { x, y, w: 0, h, line: { color: color || C.rule, width: width || 0.75 } });
}
// Bind the final two words of every line-segment with a non-breaking space so no
// paragraph can strand a single word on its last line. The house rule, enforced in code
// rather than by hand-tuning copy.
const NBSP = "\u00A0";
function bind(t, w, fontSize) {
  if (typeof t !== "string") return t;
  // Rough characters per line for this measure. Used only to decide whether binding the
  // last two words would create a token too wide for the column — which would make the
  // renderer break a word mid-glyph, a far worse fault than the runt it prevents.
  const cpl = (w && fontSize) ? (w * 72) / (fontSize * 0.50) : 60;
  let out = t.split("\n").map((seg) => {
    const i = seg.lastIndexOf(" ");
    if (i <= 0) return seg;
    const pair = seg.slice(seg.lastIndexOf(" ", i - 1) + 1);
    if (pair.length > cpl * 0.9) return seg;
    return seg.slice(0, i) + NBSP + seg.slice(i + 1);
  }).join("\n");
  // A dash never begins a line: tie it to the word it follows.
  out = out.split(" – ").join(NBSP + "– ").split(" — ").join(NBSP + "— ");
  return out;
}
function txt(s, text, o) {
  s.addText(text, { margin: 0, isTextBox: true, valign: "top", ...o });
}
function label(s, text, x, y, w, color, o = {}) {
  txt(s, String(text).toUpperCase(), {
    x, y, w, h: 0.22, fontFace: SANS, fontSize: 9, bold: true,
    color: color || C.mute, charSpacing: 1.8, ...o,
  });
}
function body(s, text, x, y, w, h, o = {}) {
  txt(s, bind(text, w, o.fontSize || 11), { x, y, w, h, fontFace: SANS, fontSize: 11,
    color: C.inkSoft, lineSpacingMultiple: 1.5, ...o });
}
function serif(s, text, x, y, w, h, o = {}) {
  txt(s, text, { x, y, w, h, fontFace: SERIF, fontSize: 22, color: C.ink,
    lineSpacingMultiple: 1.14, ...o });
}
// Rotated rail text, reading bottom to top. wrap:false is load-bearing – without it a
// long string wraps to a second column and reads as a rule struck through the words.
function vtext(s, text, cx, cyTop, cyBot, o = {}) {
  const len = cyBot - cyTop, cy = (cyTop + cyBot) / 2, h = o.h || 0.3;
  txt(s, text, {
    x: cx - len / 2, y: cy - h / 2, w: len, h, rotate: 270, wrap: false,
    fontFace: SANS, fontSize: 7, color: C.mute, charSpacing: 1.6,
    align: o.align || "left", valign: "middle", ...o,
  });
}
function well(s, x, y, w, h, caption, o = {}) {
  rect(s, x, y, w, h, o.fill || C.wellFill, { color: o.line || C.wellRule, width: 0.75 }, o.radius);
  if (o.inner !== false) {
    txt(s, (o.inner || "IMAGE").toUpperCase(), {
      x, y: y + h / 2 - 0.16, w, h: 0.32, fontFace: SANS, fontSize: 7,
      color: o.innerColor || C.mute, charSpacing: 1.6, align: "center", valign: "middle",
    });
  }
  if (caption) label(s, caption, x, y + h + 0.13, w, C.mute, { fontSize: 7, bold: false });
}

// ================================================================ BOOK system
const B = {
  RAIL_X: 0.26, RULE1_X: 0.62, RULE2_X: 3.80,
  CX: 0.82, COLW: 0.855, GUT: 0.15,
  TOP: 0.30, BOT: 7.20,
  LEFT_W: 2.865, MAIN_X: 3.95, MAIN_W: 8.87,
  T: { micro: 7, label: 9, caption: 9.5, body: 11, lead: 14, sub: 18, head: 22, display: 28, hero: 36, mega: 46 },
};
B.col = (n) => B.CX + (n - 1) * (B.COLW + B.GUT);
B.span = (n) => n * B.COLW + (n - 1) * B.GUT;
B.BAND_H = B.BOT - B.TOP;

function bookPage(pres, opts = {}) {
  const s = pres.addSlide();
  const dark = !!opts.dark;
  s.background = { color: dark ? C.ink : (opts.bg || C.paper) };
  const rc = dark ? C.ruleDark : C.rule;
  const mc = dark ? C.muteLight : C.mute;
  if (opts.chrome !== false) {
    vline(s, B.RULE1_X, B.TOP, B.BAND_H, rc, 0.75);
    txt(s, String(opts.page).padStart(3, "0"), {
      x: B.RAIL_X - 0.25, y: B.TOP - 0.02, w: 0.5, h: 0.3, rotate: 270, wrap: false,
      fontFace: SANS, fontSize: 7, color: mc, charSpacing: 1.6, align: "center", valign: "middle",
    });
    vtext(s, opts.rail || "BRAND FINGERPRINT", B.RAIL_X, B.BOT - 2.6, B.BOT, { color: mc, align: "left" });
    if (opts.rule2 !== false) vline(s, B.RULE2_X, B.TOP, B.BAND_H, rc, 0.75);
  }
  return s;
}

function bookStudy(pres, opts) {
  const s = bookPage(pres, opts);
  label(s, opts.title, B.CX, B.TOP + 0.02, B.LEFT_W, opts.dark ? C.bone : C.ink, { fontSize: B.T.label });
  if (opts.intro) {
    body(s, opts.intro, B.CX, B.TOP + 0.46, B.LEFT_W, 4.2, {
      fontFace: SERIF, fontSize: 11.5, lineSpacingMultiple: 1.42,
      color: opts.dark ? "C9BC9C" : C.inkSoft,
    });
  }
  if (opts.foot) {
    const fy = opts.footY || (B.BOT - 1.55);
    body(s, opts.foot, B.CX, fy, B.LEFT_W, B.BOT - fy, {
      fontSize: opts.footSize || B.T.caption, lineSpacingMultiple: opts.footLead || 1.4,
      color: opts.dark ? C.muteLight : C.muteDark,
    });
  }
  return s;
}

// ================================================================ REPORT system
// Decoded from the Musicbed trend report: a four-slot running head over a hairline,
// three wide columns, and severe scale contrast between display and body.
const R = {
  HEAD_H: 0.26,
  CX: 0.556, COLW: 3.80, GUT: 0.417,
  TOP: 0.86,          // first display baseline zone
  TOP_TEXT: 1.06,     // first body element on a page with no display head
  BOT: 6.95,
  T: { mega: 54, display: 43, head: 26, sub: 17, lead: 12.5, body: 9.5, caption: 8, micro: 7 },
  LEAD_BODY: 1.68, LEAD_DISPLAY: 1.05, LEAD_LEAD: 1.3,
};
R.col = (n) => R.CX + (n - 1) * (R.COLW + R.GUT);
R.span = (n) => n * R.COLW + (n - 1) * R.GUT;
R.RIGHT = R.CX + R.span(3);   // 12.79

function reportPage(pres, opts = {}) {
  const s = pres.addSlide();
  const dark = !!opts.dark;
  s.background = { color: dark ? C.ink : (opts.bg || C.paper) };
  if (opts.chrome === false) return s;
  const bandFill = opts.headFill || (dark ? C.inkSoft : C.seasalt);
  const fg = dark ? C.bone : C.ink;
  sharpRect(s, 0, 0, PAGE_W, R.HEAD_H, bandFill);
  hline(s, 0, R.HEAD_H, PAGE_W, dark ? C.ruleDark : C.ink, 0.75);
  const slots = [
    [opts.brand || "Five Points Digital Studio", R.col(1), 3.2, "left"],
    [opts.doc || "Capabilities", R.col(2), 3.6, "left"],
    ["2026", R.col(3), 2.0, "left"],
    [`pg ${opts.page}`, R.RIGHT - 1.4, 1.4, "right"],
  ];
  slots.forEach(([t, x, w, align]) => {
    txt(s, t, { x, y: 0.055, w, h: 0.16, fontFace: SANS, fontSize: R.T.micro + 0.5,
      color: fg, align, valign: "middle" });
  });
  return s;
}

module.exports = {
  C, VOICES, SERIF, SANS, RAD, RAD_SM, PAGE_W, PAGE_H, PHI,
  markPath, mark, T_MICRO,
  rect, sharpRect, hline, vline, bar, txt, label, body, serif, vtext, well, bind,
  B, bookPage, bookStudy,
  R, reportPage,
};
