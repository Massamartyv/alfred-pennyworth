#!/usr/bin/env python3
"""Render a stationery artefact to PDF at its own trim, with an overflow gate.

    uv run --with playwright python build.py --src letterhead.html
    uv run --with playwright python build.py --all --proof
    uv run --with playwright python build.py --src card.html --proof

Pipeline: HTML -> PDF via Playwright driving system Chrome. Fonts are local
woff2 files loaded through fonts.css, so the render needs no network and is
reproducible years from now.

THE TRIM DECLARATION. The suite spans three paper trims and one screen
artefact, so no single page size can live in this script. Each document
declares its own in its head:

    <meta name="trim" content="210x297mm">   letterhead
    <meta name="trim" content="220x110mm">   with-compliments slip
    <meta name="trim" content="74x74mm">     business card
    <meta name="trim" content="screen">      email signature

The build reads that declaration and sizes the viewport and the PDF from it,
so the geometry has exactly one source of truth and it is the document.

THE OVERFLOW GATE. Every sheet is a fixed surface with overflow: hidden, so
copy that grows past the trim is silently guillotined rather than reported.
The build measures each sheet before writing the PDF and refuses to write one
that has lost content. Fix the copy or the spacing; do not raise the
tolerance.

THE FLATTEN PASS. A screen-trim document writes no PDF. Instead the block
between the SIGNATURE markers is flattened - custom properties resolved to
literal values through getComputedStyle - and written beside the source as
<stem>.built.html. Mail clients cannot resolve var(), so the source stays
token-pure and the generated file carries the resolved values. Change the
voice on the source, rebuild, and the deliverable follows.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent

# The suite, in the order a principal meets it.
SUITE = ["letterhead.html", "compliments.html", "card.html", "signature.html"]

# 96 CSS px per inch is Chrome's layout constant; mm-declared sheets resolve
# exactly once at this viewport, with no reflow between measuring and writing.
PX_PER_MM = 96 / 25.4

# One CSS pixel of slack for sub-pixel rounding on mm-declared boxes; anything
# past a whole pixel is real lost content.
TOLERANCE_PX = 1

# A screen artefact has no trim to measure against, so the stage is given room
# and the sheet is measured by its own content box.
SCREEN_PX = {"width": 900, "height": 600}

MEASURE = """
() => Array.from(document.querySelectorAll('.sheet')).map((sheet, i) => ({
  page: i + 1,
  clientHeight: sheet.clientHeight,
  scrollHeight: sheet.scrollHeight,
  clientWidth: sheet.clientWidth,
  scrollWidth: sheet.scrollWidth,
}))
"""

# Resolve every inline custom-property reference on the marked block to the
# literal value Chrome computed, and hand back the flattened markup.
#
# The styles must be read from the LIVE nodes. A detached clone has no
# computed style -- getComputedStyle returns empty strings for everything --
# so the walk pairs each live element with its clone by index and copies the
# resolved values across. Anything the browser declines to compute as a
# shorthand falls back to the value the source declared.
FLATTEN = """
() => {
  const walk = document.createTreeWalker(document.body, NodeFilter.SHOW_COMMENT);
  let start = null, end = null, node;
  while ((node = walk.nextNode())) {
    if (node.nodeValue.includes('SIGNATURE START')) start = node;
    if (node.nodeValue.includes('SIGNATURE END')) end = node;
  }
  if (!start || !end) return null;

  // The properties that must survive the trip into a mail client.
  const KEEP = ['font-family', 'font-size', 'font-weight', 'color',
                'line-height', 'padding', 'border-collapse', 'display', 'border'];

  const roots = [];
  for (let n = start.nextSibling; n && n !== end; n = n.nextSibling) {
    if (n.nodeType === 1) roots.push(n);
  }
  if (!roots.length) return null;

  const resolve = (live, clone) => {
    const declared = live.getAttribute('style');
    if (declared) {
      const computed = getComputedStyle(live);
      const out = [];
      for (const chunk of declared.split(';')) {
        const prop = chunk.split(':')[0].trim();
        if (!prop) continue;
        const raw = live.style.getPropertyValue(prop);
        // Any raw value still carrying var() must resolve through the
        // computed style regardless of property -- mail clients cannot
        // resolve custom properties, so a survivor is a broken deliverable.
        const value = (KEEP.includes(prop) || raw.includes('var('))
          ? (computed.getPropertyValue(prop) || raw)
          : raw;
        if (value) out.push(`${prop}:${value}`);
      }
      clone.setAttribute('style', out.join(';'));
    }
    const liveKids = live.querySelectorAll('*');
    const cloneKids = clone.querySelectorAll('*');
    for (let i = 0; i < liveKids.length; i++) {
      const declaredKid = liveKids[i].getAttribute('style');
      if (!declaredKid) continue;
      const computedKid = getComputedStyle(liveKids[i]);
      const out = [];
      for (const chunk of declaredKid.split(';')) {
        const prop = chunk.split(':')[0].trim();
        if (!prop) continue;
        const raw = liveKids[i].style.getPropertyValue(prop);
        // Same var() guard as the root pass above; keep the two in step.
        const value = (KEEP.includes(prop) || raw.includes('var('))
          ? (computedKid.getPropertyValue(prop) || raw)
          : raw;
        if (value) out.push(`${prop}:${value}`);
      }
      cloneKids[i].setAttribute('style', out.join(';'));
    }
  };

  const shell = document.createElement('div');
  for (const live of roots) {
    const clone = live.cloneNode(true);
    resolve(live, clone);
    shell.appendChild(clone);
  }
  return shell.innerHTML;
}
"""


def read_trim(src: pathlib.Path) -> str:
    """Pull the trim declaration out of the document head."""
    match = re.search(
        r'<meta\s+name=["\']trim["\']\s+content=["\']([^"\']+)["\']',
        src.read_text(),
        re.IGNORECASE,
    )
    if not match:
        raise SystemExit(
            f"{src.name} declares no trim. Add "
            '<meta name="trim" content="WxHmm"> to its head.'
        )
    return match.group(1).strip()


def trim_to_px(trim: str) -> dict[str, int]:
    match = re.fullmatch(r"(\d+(?:\.\d+)?)x(\d+(?:\.\d+)?)mm", trim)
    if not match:
        raise SystemExit(f"Unreadable trim {trim!r}. Expected WxHmm or 'screen'.")
    width, height = float(match.group(1)), float(match.group(2))
    return {"width": round(width * PX_PER_MM), "height": round(height * PX_PER_MM)}


def build_one(page, src: pathlib.Path, proof: bool) -> int:
    trim = read_trim(src)
    is_screen = trim == "screen"

    page.set_viewport_size(SCREEN_PX if is_screen else trim_to_px(trim))
    page.goto(src.as_uri())
    page.wait_for_load_state("networkidle")
    page.evaluate("document.fonts.ready")

    sheets = page.evaluate(MEASURE)
    overflowing = [
        sheet
        for sheet in sheets
        if sheet["scrollHeight"] - sheet["clientHeight"] > TOLERANCE_PX
        or sheet["scrollWidth"] - sheet["clientWidth"] > TOLERANCE_PX
    ]

    print(f"\n{src.name} · trim {trim} · {len(sheets)} sheet(s)")
    for sheet in sheets:
        over_y = sheet["scrollHeight"] - sheet["clientHeight"]
        over_x = sheet["scrollWidth"] - sheet["clientWidth"]
        state = "CLIPPED" if sheet in overflowing else "ok"
        print(
            f"  sheet {sheet['page']:>2}  {state:>7}"
            f"  vertical {over_y:+d}px  horizontal {over_x:+d}px"
        )

    if overflowing:
        pages = ", ".join(str(sheet["page"]) for sheet in overflowing)
        print(
            f"\nRefusing to render {src.name}: content is clipped on sheet {pages}.\n"
            "Trim the copy or re-space the sheet, then build again.",
            file=sys.stderr,
        )
        return 2

    if proof:
        proof_dir = src.parent / "proof" / src.stem
        proof_dir.mkdir(parents=True, exist_ok=True)
        for index in range(len(sheets)):
            target = proof_dir / f"sheet-{index + 1:02d}.png"
            page.locator(".sheet").nth(index).screenshot(path=str(target))
            print(f"  proof {target.name}")

    if is_screen:
        flattened = page.evaluate(FLATTEN)
        if flattened is None:
            print(
                f"  {src.name} declares a screen trim but carries no "
                "SIGNATURE START/END markers; nothing to flatten.",
                file=sys.stderr,
            )
            return 2
        built = src.with_suffix(".built.html")
        built.write_text(
            "<!-- Generated by build.py from "
            f"{src.name}. Do not hand-edit; rebuild instead. -->\n"
            f"{flattened.strip()}\n"
        )
        print(f"  wrote {built.name}")
        return 0

    out = src.with_suffix(".pdf")
    width, height = trim.replace("mm", "").split("x")
    page.pdf(
        path=str(out),
        width=f"{width}mm",
        height=f"{height}mm",
        print_background=True,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
    )
    print(f"  wrote {out.name}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", type=pathlib.Path, default=None)
    parser.add_argument(
        "--all", action="store_true", help="build every artefact in the suite"
    )
    parser.add_argument(
        "--proof", action="store_true", help="write per-sheet PNG proofs"
    )
    args = parser.parse_args()

    if args.all:
        targets = [HERE / name for name in SUITE]
    elif args.src:
        targets = [args.src.resolve()]
    else:
        parser.error("give --src <file> or --all")

    missing = [target for target in targets if not target.exists()]
    if missing:
        for target in missing:
            print(f"No such document: {target}", file=sys.stderr)
        return 1

    failures = 0
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        page = browser.new_page()
        for target in targets:
            failures += 1 if build_one(page, target, args.proof) else 0
        browser.close()

    if failures:
        print(f"\n{failures} artefact(s) failed to build.", file=sys.stderr)
        return 2

    print(f"\nBuilt {len(targets)} artefact(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
