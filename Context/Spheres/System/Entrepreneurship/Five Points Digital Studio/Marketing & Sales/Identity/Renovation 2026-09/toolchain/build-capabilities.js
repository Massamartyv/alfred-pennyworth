// Five Points Digital Studio — Capabilities, v6.
// Built on the REPORT system decoded from the Musicbed Commercial Filmmaking Trend Report:
// four-slot running head over a hairline, three wide columns, severe scale contrast between
// display and body, full-bleed colour planes, and a CTA module. Set in the Five Points faces.
const pptxgen = require("pptxgenjs");
const L = require("./lib");
const {
  C, VOICES, SERIF, SANS, RAD, RAD_SM, PAGE_W, PAGE_H,
  rect, sharpRect, hline, vline, bar, txt, label, body, well, mark, bind,
  R, reportPage,
} = L;
const { CX, COLW, GUT, TOP, TOP_TEXT, BOT, RIGHT, T, col, span, HEAD_H } = R;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Five Points Digital Studio";
pres.company = "Five Points Digital Studio";
pres.title = "Five Points Digital Studio — Capabilities";

const DOC = "Capabilities";
let P = 0;
const next = () => ++P;

// ---------------------------------------------------------------- helpers
function display(s, text, x, y, w, o = {}) {
  txt(s, text, {
    x, y, w, h: o.h || 1.5, fontFace: SERIF, fontSize: o.fontSize || T.display,
    color: o.color || C.ink, lineSpacingMultiple: R.LEAD_DISPLAY, valign: "top", ...o,
  });
}
function lead(s, text, x, y, w, h, o = {}) {
  txt(s, bind(text, w, o.fontSize || T.lead), {
    x, y, w, h, fontFace: SERIF, fontSize: T.lead, color: o.color || C.ink,
    lineSpacingMultiple: R.LEAD_LEAD, ...o,
  });
}
function para(s, text, x, y, w, h, o = {}) {
  txt(s, bind(text, w, o.fontSize || T.body), {
    x, y, w, h, fontFace: SANS, fontSize: T.body, color: o.color || C.inkSoft,
    lineSpacingMultiple: R.LEAD_BODY, ...o,
  });
}
// The Musicbed call-out: a dark tab label sitting on a light card.
function ctaModule(s, x, y, w, tab, head, sub, o = {}) {
  const tabW = Math.min(w * 0.62, 0.14 + tab.length * 0.075);
  rect(s, x, y, tabW, 0.28, o.tabFill || C.ink, null, RAD_SM);
  txt(s, tab, { x: x + 0.12, y: y + 0.055, w: tabW - 0.24, h: 0.18, fontFace: SANS,
    fontSize: T.micro, color: o.tabColor || C.bone, valign: "middle" });
  const cardY = y + 0.28;
  rect(s, x, cardY, w, o.h || 1.15, o.fill || C.white, { color: C.ruleSoft, width: 0.75 });
  const px = x + 0.26;
  txt(s, bind(head, w - 0.52, T.sub), { x: px, y: cardY + 0.2, w: w - 0.52, h: 0.4, fontFace: SERIF,
    fontSize: T.sub, color: o.headColor || C.ink, lineSpacingMultiple: 1.24 });
  para(s, sub, px, cardY + 0.6, w - 0.52, (o.h || 1.15) - 0.7, { fontSize: T.caption, color: C.mute });
}
function creditChip(s, x, y, text, dark) {
  const w = Math.max(0.9, 0.24 + text.length * 0.052);
  s.addShape("roundRect", {
    x: x + (1.5 - w), y, w, h: 0.22, rectRadius: RAD_SM,
    fill: { color: dark ? "000000" : "FFFFFF", transparency: dark ? 55 : 25 },
  });
  txt(s, text, { x: x + (1.5 - w) + 0.1, y: y + 0.03, w: w - 0.2, h: 0.16, fontFace: SANS,
    fontSize: T.micro, color: dark ? C.bone : C.inkSoft, valign: "middle", align: "center" });
}

// ================================================================ 01 cover
{
  const s = reportPage(pres, { page: next(), chrome: false });
  sharpRect(s, 0, 0, PAGE_W, PAGE_H, C.coral);
  mark(s, 0.62, PAGE_W / 2 - 0.31, 0.5, "bone");
  label(s, "The marketing consultancy that builds the systems an owner keeps", 0, 1.32, PAGE_W,
    C.coralDeep, { align: "center", bold: false, fontSize: T.micro + 0.5 });
  txt(s, "WE BRING\nTHE CITY\nTO YOUR DOOR", {
    x: 0.6, y: 1.86, w: PAGE_W - 1.2, h: 4.6, fontFace: SERIF, fontSize: 92, bold: true,
    color: C.coralDeep, align: "center", lineSpacingMultiple: 0.96,
  });
  label(s, "Five Points Digital Studio  ·  Decatur, Georgia  ·  est. 2021", 0, 6.86, PAGE_W,
    C.coralDeep, { align: "center", bold: false, fontSize: T.micro + 0.5 });
}

// ================================================================ 02 about
{
  const s = reportPage(pres, { page: next(), doc: DOC, dark: true, headFill: C.inkSoft });
  sharpRect(s, 0, HEAD_H, PAGE_W, PAGE_H - HEAD_H, C.inkSoft);
  well(s, 0, HEAD_H, PAGE_W, PAGE_H - HEAD_H, null,
    { fill: "23201C", line: "23201C", inner: false, radius: 0 });
  label(s, "The owner at his place  ·  full bleed", CX, PAGE_H - 0.52, 5.0, C.muteDark, { bold: false });
  display(s, "About", CX, TOP, 4.0, { fontSize: T.head, color: C.bone, h: 0.5 });
  label(s, "(A)", CX, TOP + 1.05, 1.0, C.muteLight, { bold: false, fontSize: T.micro });
  display(s, "Five Points is the marketing\nconsultancy for owner-operators\nwho would rather run the work\nthan chase it.",
    CX, TOP + 1.32, 5.6, { fontSize: 26, color: C.bone, h: 2.0 });
  label(s, "(B)", col(2) + 0.6, TOP + 3.55, 1.0, C.muteLight, { bold: false, fontSize: T.micro });
  display(s, "Everything we build is yours\nthe day it goes live — the number,\nthe records, the writing behind them.",
    col(2) + 0.6, TOP + 3.82, 6.0, { fontSize: 26, color: C.greige, h: 1.6 });
  creditChip(s, RIGHT - 1.66, BOT - 0.28, "Decatur, Georgia", true);
}

// ================================================================ 03 contents
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  sharpRect(s, PAGE_W / 2, HEAD_H, PAGE_W / 2, PAGE_H - HEAD_H, C.greige);
  sharpRect(s, PAGE_W / 2 + 0.9, HEAD_H + 0.55, PAGE_W / 2 - 0.9, PAGE_H - HEAD_H - 0.55, C.ink);
  display(s, "Contents", CX, TOP, 4.0, { fontSize: T.head, h: 0.5 });
  const left = [["The name", "04"], ["What we are", "05"], ["Five ways we help", "06"],
    ["Operations, in full", "07"], ["What you keep", "08"]];
  const right = [["How it works", "09"], ["Our promise", "10"], ["What stands behind it", "11"],
    ["The work", "12"], ["The first call", "13"]];
  display(s, "The studio", CX, TOP + 0.95, 4.0, { fontSize: T.sub, h: 0.4 });
  left.forEach(([t, p], i) => {
    const y = TOP + 1.55 + i * 0.42;
    txt(s, t, { x: CX, y, w: 3.2, h: 0.3, fontFace: SANS, fontSize: T.lead, color: C.ink });
    txt(s, p, { x: CX + 3.3, y, w: 0.5, h: 0.3, fontFace: SANS, fontSize: T.lead, color: C.ink, align: "right" });
  });
  const rx = PAGE_W / 2 + 1.35;
  display(s, "The work", rx, TOP + 0.95, 4.0, { fontSize: T.sub, color: C.bone, h: 0.4 });
  right.forEach(([t, p], i) => {
    const y = TOP + 1.55 + i * 0.42;
    txt(s, t, { x: rx, y, w: 3.2, h: 0.3, fontFace: SANS, fontSize: T.lead, color: C.bone });
    txt(s, p, { x: rx + 3.3, y, w: 0.5, h: 0.3, fontFace: SANS, fontSize: T.lead, color: C.bone, align: "right" });
  });
}

// ================================================================ 04 the name
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "The Name", CX, TOP - 0.06, 5.4, { h: 1.4 });
  para(s, "Atlanta began where a railway stopped and grew where five streets met. That intersection "
    + "is the point every address in the city counts from.\n\nThe station beneath it is the one place "
    + "where every line meets. Whoever you are and wherever you are going, if you need to change "
    + "direction in this city, you do it here.\n\nAnd two miles east, the neighbourhood that borrowed "
    + "its name was made into the most creative corner of the city by independent owners, one door at "
    + "a time. No brand made it. Independent people made it by being unmistakably themselves, and the "
    + "city came to them.",
    CX, TOP + 1.75, COLW, 3.4);
  lead(s, "We took the name for all three: the point everything counts from, five disciplines in one "
    + "place and the conviction that a business unmistakably itself will bring the city to its door.",
    col(2), TOP - 0.02, COLW, 1.1);
  para(s, "Five Points Digital Studio was founded on 5 May 2021 — the fifth day of the fifth month — "
    + "at the far end of Decatur Street, the road that leaves the intersection heading east.\n\n"
    + "That is the whole of our trade, and it is still best done on a porch, by the people who live "
    + "there.", col(2), TOP + 1.3, COLW, 1.6);
  well(s, col(2), TOP + 3.15, COLW, 2.0, null, { inner: "FIVE POINTS STATION" });
  well(s, col(3), TOP - 0.02, COLW, 2.6, null, { inner: "THE DISTRICT, ONE DOOR AT A TIME" });
  para(s, "The first grocery in Atlanta opened there in 1845, the first post office in 1846, the first "
    + "mayor was elected there in 1848. A block north, Auburn Avenue sets off east — the street John "
    + "Wesley Dobbs named, and which Fortune in 1956 called the wealthiest Black street in the world.\n\n"
    + "In 1928 Atlanta raised those streets a storey and a half on viaducts, and the merchants moved "
    + "upstairs and kept trading on top of their own ground floor. The original storefronts are still "
    + "down there. This is a city that has always built on what it already had.",
    col(3), TOP + 2.85, COLW, 2.6);
}

// ================================================================ 05 what we are
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "A marketing consultancy\nthat builds the systems\nan owner keeps.", CX, TOP - 0.06, 8.2, { h: 2.2 });
  lead(s, "Five disciplines under one roof, AI-first — made for the owner-operator who would rather "
    + "run the work than chase it.", col(3), TOP + 0.02, COLW, 1.0, { align: "right" });
  hline(s, CX, TOP + 2.55, RIGHT - CX, C.rule, 0.75);
  const cards = [
    ["Eighty", "A marketing consultancy whose systems the owner keeps. Everything we build is yours the day it goes live: the number, the records, the writing behind them, the accounts in your name."],
    ["Twenty", "AI-first, on five pillars. The tools became cheap enough for a two-van company to own outright, and we build with them rather than renting them back to you."],
    ["For whom", "Owner-operators with two to twenty on the crew, who still answer the phone some days and buy with their own money. The trades are the first wing of the house, not the whole of it."],
  ];
  cards.forEach(([h, t], i) => {
    const x = col(i + 1);
    label(s, `0${i + 1}`, x, TOP + 2.8, 1.0, C.mute, { fontSize: T.micro });
    display(s, h, x, TOP + 3.1, COLW, { fontSize: T.sub, h: 0.4 });
    para(s, t, x, TOP + 3.62, COLW, 1.8);
  });
}

// ================================================================ 06 five ways
{
  const s = reportPage(pres, { page: next(), doc: DOC, bg: C.greige, headFill: "C3BDAF" });
  display(s, "Five ways\nwe help", CX, TOP - 0.06, 4.4, { h: 1.6 });
  lead(s, "Five pillars, for five points. Every one of them is built for your company and priced on "
    + "the first call, from your own numbers.", col(2), TOP + 0.02, COLW, 1.0);
  const pillars = [
    ["Operations", "The systems that run the business while the owner works — the phone answered at any hour, the lead texted back in a minute, the old list called in your name."],
    ["Development", "Your website and the tools behind it, built to be kept. Fast, plain and yours from the day it goes live."],
    ["Creative", "Your brand and how it appears everywhere it appears — the mark, the truck, the estimate, the page."],
    ["Market Presence", "How the city finds you — the search listing, the pages, the posts and the ads, run so that the phone rings."],
    ["Consulting", "The plan. What to do first, what to leave alone, and what it is worth, in your own numbers."],
  ];
  pillars.forEach(([h, t], i) => {
    const y = TOP + 1.95 + i * 0.92;
    hline(s, CX, y, RIGHT - CX, "9A9484", 0.75);
    label(s, `0${i + 1}`, CX, y + 0.2, 0.6, C.muteDark, { fontSize: T.micro });
    display(s, h, CX + 0.7, y + 0.14, 3.0, { fontSize: T.sub, h: 0.36 });
    para(s, t, col(2), y + 0.16, span(2), 0.62, { color: "3D3830" });
  });
}

// ================================================================ 07 operations
{
  const s = reportPage(pres, { page: next(), doc: DOC, dark: true, headFill: C.inkSoft });
  display(s, "OPERATIONS", CX, TOP - 0.1, 8.0, { fontSize: 62, color: C.bone, bold: true, h: 1.1 });
  lead(s, "THE PHONE IS THE WHOLE BUSINESS.\nEVERYTHING ELSE IS DOWNSTREAM OF IT.",
    col(3), TOP + 0.06, COLW, 0.9, { color: C.bone, align: "right", fontSize: T.lead, fontFace: SANS });
  display(s, "Never lose another job\nyou could have won.", CX, TOP + 1.35, 3.9, { fontSize: T.sub, color: C.bone, h: 0.8 });
  para(s, "A missed call is not a missed call. It is a job that went to whoever picked up first, and "
    + "you will never see the invoice you did not write.\n\nMost owners already run an unpaid version "
    + "of this work — the after-hours rotation, the voicemail checked at eleven at night, the family "
    + "member drafted into dispatch. We build the system that does it properly, in your name, and hand "
    + "you the keys.", CX, TOP + 2.35, COLW, 2.4, { color: C.greige });
  well(s, col(2), TOP + 1.35, span(2), 3.05, null,
    { fill: "23201C", line: "3A362F", inner: "THE VAN, THE YARD, THE PHONE", innerColor: C.muteDark });
  creditChip(s, RIGHT - 1.66, TOP + 3.98, "Atlanta, 2026", true);
  const three = [["Speed to lead", "The web lead or missed call that waits an hour and goes to the next number."],
    ["After-hours capture", "The two-in-the-morning storm call that hits voicemail and never calls back."],
    ["Database activation", "The old customers and dead quotes nobody has called since."]];
  three.forEach(([h, t], i) => {
    const x = col(i + 1);
    hline(s, x, TOP + 4.75, COLW, C.ruleDark, 0.75);
    display(s, h, x, TOP + 4.95, COLW, { fontSize: 15, color: C.bone, h: 0.3 });
    para(s, t, x, TOP + 5.35, COLW, 0.7, { color: C.mute, fontSize: T.caption });
  });
}

// ================================================================ 08 what you keep
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "Everything we build is yours\nthe day it goes live.", CX, TOP - 0.06, 8.6, { h: 1.5 });
  lead(s, "Most agencies charge by the month and take the keys with them when the engagement ends.",
    col(3), TOP + 0.02, COLW, 1.0, { align: "right" });
  const keeps = [
    ["The number", "The phone line, the text-back number, the accounts — in your name, not ours."],
    ["The records", "Every call, every message, every booking, kept where you can read them."],
    ["The writing", "The words the system uses, the pages, the plan — the whole of it, handed across."],
    ["The right to leave", "Thirty days after it goes live, if you would rather not keep it, we unplug it and refund the setup."],
  ];
  const cw = (RIGHT - CX - 3 * 0.3) / 4;
  keeps.forEach(([h, t], i) => {
    const x = CX + i * (cw + 0.3);
    rect(s, x, TOP + 1.95, cw, 2.85, C.priscillaTint);
    label(s, `0${i + 1}`, x + 0.26, TOP + 2.2, 1.0, C.priscillaInk, { fontSize: T.micro });
    display(s, h, x + 0.26, TOP + 2.5, cw - 0.52, { fontSize: T.sub, h: 0.6 });
    para(s, t, x + 0.26, TOP + 3.24, cw - 0.52, 1.4);
  });
  ctaModule(s, CX, TOP + 4.95, span(2), "The Owner's Keys",
    "Stop governance whenever you like.",
    "The system keeps running. Nothing switches off, and the number stays yours.", { h: 0.85 });
}

// ================================================================ 09 how it works
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "How it works", CX, TOP - 0.06, 5.0, { h: 1.0 });
  lead(s, "Five moments. No ceremony, no travel, no surprises at the end.", col(3), TOP + 0.02, COLW, 0.8, { align: "right" });
  const moments = [
    ["The first call", "Thirty minutes, no fee, on your operation. You leave with a plain account of where the work is getting lost in your business — whether or not you go on."],
    ["The plan", "One page. Two prices, the cost of yes and the cost of no. Nothing you have to be taught to read."],
    ["The build", "A short word every week and a link to see the work as it grows."],
    ["The keys", "The day it goes live you get everything, in one folder with your name on it."],
    ["The quarterly call", "What came back, what changed, what is next. The system is yours; we keep it in good order."],
  ];
  moments.forEach(([h, t], i) => {
    const y = TOP + 1.35 + i * 1.02;
    hline(s, CX, y, RIGHT - CX, C.ruleSoft, 0.75);
    rect(s, CX, y + 0.24, 0.16, 0.16, VOICES[i].hex, null, RAD_SM);
    label(s, `0${i + 1}`, CX + 0.34, y + 0.22, 0.6, C.mute, { fontSize: T.micro });
    display(s, h, CX + 1.05, y + 0.16, 2.8, { fontSize: T.sub, h: 0.36 });
    para(s, t, col(2), y + 0.18, span(2), 0.72);
  });
}

// ================================================================ 10 the promise
{
  const s = reportPage(pres, { page: next(), doc: DOC, bg: C.greige, headFill: "C3BDAF" });
  display(s, "Our promise", CX, TOP - 0.06, 5.0, { h: 1.0 });
  lead(s, "Three guarantees, written to the price of each system and named on the plan.",
    col(3), TOP + 0.02, COLW, 0.8, { align: "right" });
  const gs = [
    ["The Owner's Keys", "Everything is yours the day it goes live — the number, the messages, the records, the writing behind them. Stop governance whenever you like and the system keeps running.", C.sageTint, C.sageInk],
    ["The Recovered Job", "If, inside ninety days of going live, the system has not booked at least one job you would otherwise have missed, governance runs free until it does.", C.naplesTint, C.naplesInk],
    ["The Walkaway", "Thirty days after going live, if you would rather not keep it, we unplug it and refund the setup. The number stays yours.", C.coralTint, C.coralInk],
  ];
  gs.forEach(([h, t, bg, fg], i) => {
    const x = col(i + 1);
    rect(s, x, TOP + 1.35, COLW, 3.3, bg);
    label(s, `0${i + 1}`, x + 0.3, TOP + 1.62, 1.0, fg, { fontSize: T.micro });
    display(s, h, x + 0.3, TOP + 1.95, COLW - 0.6, { fontSize: T.sub, h: 0.4 });
    para(s, t, x + 0.3, TOP + 2.52, COLW - 0.6, 1.9);
  });
  para(s, "All three are conditional on the tracking that makes them measurable. None of them is "
    + "stated as a warranty of revenue.", CX, TOP + 4.9, span(2), 0.5, { color: "3D3830" });
}

// ================================================================ 11 proof
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "What stands\nbehind it", CX, TOP - 0.06, 4.4, { h: 1.6 });
  lead(s, "Not a pitch. A pattern — the systems themselves, running in the names of the companies "
    + "that own them.", col(2), TOP + 0.02, COLW, 1.0);
  const stats = [["2021", "Founded in Decatur, Georgia, on the fifth day of the fifth month. Five years of systems that are still running."],
    ["5", "Organisations on the roll — school districts, universities and a city government among them — and each still runs what was built."],
    ["1", "Partner on every job. The person you meet on the first call is the person who builds and the person who answers for it."]];
  stats.forEach(([n, t], i) => {
    const x = col(i + 1);
    txt(s, n, { x, y: TOP + 1.9, w: COLW, h: 1.2, fontFace: SERIF, fontSize: 68, color: C.ink });
    hline(s, x, TOP + 3.2, COLW, C.rule, 0.75);
    para(s, t, x, TOP + 3.42, COLW, 1.2);
  });
  sharpRect(s, 0, TOP + 4.9, PAGE_W, PAGE_H - (TOP + 4.9), C.coral);
  txt(s, "Never lose another job you could have won.", {
    x: CX, y: TOP + 5.18, w: 9.0, h: 0.6, fontFace: SERIF, fontSize: 30, color: C.coralDeep });
  txt(s, "The promise we make to the trades, where the phone is the whole business.", {
    x: CX, y: TOP + 5.75, w: 9.0, h: 0.3, fontFace: SANS, fontSize: T.caption, color: C.coralDeep });
}

// ================================================================ 12 the work
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "The work", CX, TOP - 0.06, 5.0, { h: 1.0 });
  lead(s, "A body of systems built for owner-operators and the organisations that serve them. Each "
    + "one still runs in the name of the company that owns it.", col(3), TOP + 0.02, COLW, 1.0, { align: "right" });
  // modular gallery, Musicbed proportions
  well(s, CX, TOP + 1.35, span(2), 2.35, "Speed to lead  ·  a roofing company in DeKalb", { inner: "CASE STUDY" });
  well(s, col(3), TOP + 1.35, COLW, 2.35, "After-hours capture  ·  HVAC, south metro", { inner: "CASE STUDY" });
  well(s, CX, TOP + 4.1, COLW, 1.95, "Database reactivation  ·  garage doors", { inner: "CASE STUDY" });
  well(s, col(2), TOP + 4.1, COLW, 1.95, "Website engineering  ·  a church in East Point", { inner: "CASE STUDY" });
  well(s, col(3), TOP + 4.1, COLW, 1.95, "Brand identity  ·  a window trade", { inner: "CASE STUDY" });
}

// ================================================================ 13 the first call
{
  const s = reportPage(pres, { page: next(), doc: DOC });
  display(s, "Thirty minutes.\nNo fee. On your\noperation, not ours.", CX, TOP - 0.06, span(2), { h: 2.6 });
  para(s, "You leave with a plain account of where the work is getting lost in your business — the "
    + "lead that waits, the call that comes at night, the list nobody calls — whether or not you go "
    + "on.\n\nIf you do, the plan follows on one page with two prices on it: the cost of yes and the "
    + "cost of no, both in your own numbers.", CX, TOP + 3.05, COLW, 2.0);
  ctaModule(s, col(3), TOP - 0.02, COLW, "Book the first call",
    "hello@fivepoints.studio",
    "fivepoints.studio  ·  Decatur, Georgia\n+1 470 556 3989", { h: 1.35 });
  well(s, col(3), TOP + 1.85, COLW, 2.9, null, { inner: "THE KITCHEN TABLE" });
  well(s, col(2), TOP + 3.05, COLW, 2.0, null, { inner: "THE PLAN, ONE PAGE" });
}

// ================================================================ 14 close
{
  const s = reportPage(pres, { page: next(), chrome: false });
  sharpRect(s, 0, 0, PAGE_W, PAGE_H, C.ink);
  mark(s, 1.0, CX, 1.35, "bone");
  txt(s, "We bring the city\nto your door.", {
    x: CX, y: 3.05, w: 9.4, h: 2.1, fontFace: SERIF, fontSize: 46, color: C.bone, lineSpacingMultiple: 1.2 });
  hline(s, CX, 5.5, 3.2, C.ruleDark, 0.75);
  txt(s, "Five Points Digital Studio  ·  Decatur, Georgia  ·  fivepoints.studio  ·  hello@fivepoints.studio", {
    x: CX, y: 5.76, w: 10, h: 0.3, fontFace: SANS, fontSize: 10, color: C.muteLight });
  label(s, "Capabilities  ·  2026", CX, 6.16, 6, C.muteDark, { bold: false });
}

pres.writeFile({ fileName: "five-points-capabilities.pptx" })
  .then(() => console.log("capabilities:", P, "pages"));
