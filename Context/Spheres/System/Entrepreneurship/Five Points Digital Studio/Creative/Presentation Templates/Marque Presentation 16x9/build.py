#!/usr/bin/env python3
"""Render the marque presentation to a 16:9 PDF, with an overflow gate.

    uv run --with playwright python build.py                # render deck.html
    uv run --with playwright python build.py --src other.html
    uv run --with playwright python build.py --proof        # also write PNGs

Pipeline: HTML -> PDF via Playwright driving system Chrome. Fonts are local
woff2 files loaded through fonts.css, so the render needs no network and is
reproducible years from now.

THE OVERFLOW GATE. Every sheet is a fixed 1280 x 720 px surface with
overflow: hidden, so copy that grows past the sheet is silently guillotined
rather than reported. The build measures each sheet before writing the PDF
and refuses to write one that has lost content. Fix the copy or the spacing;
do not raise the tolerance.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent

# 16:9 at 96 CSS px per inch. The viewport matches the sheet exactly so the
# measurement pass and the PDF pass see one identical layout.
SHEET_PX = {"width": 1280, "height": 720}

# One CSS pixel of slack for sub-pixel rounding; anything past a whole pixel
# is real lost content.
TOLERANCE_PX = 1

MEASURE = """
() => Array.from(document.querySelectorAll('.sheet')).map((sheet, i) => ({
  page: i + 1,
  clientHeight: sheet.clientHeight,
  scrollHeight: sheet.scrollHeight,
  clientWidth: sheet.clientWidth,
  scrollWidth: sheet.scrollWidth,
}))
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", type=pathlib.Path, default=HERE / "deck.html")
    parser.add_argument("--out", type=pathlib.Path, default=None)
    parser.add_argument(
        "--proof",
        action="store_true",
        help="write per-sheet PNG proofs beside the PDF",
    )
    args = parser.parse_args()

    src = args.src.resolve()
    if not src.exists():
        print(f"No such document: {src}", file=sys.stderr)
        return 1

    out = args.out or src.with_suffix(".pdf")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        page = browser.new_page(viewport=SHEET_PX)
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

        print(f"{len(sheets)} sheets measured")
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
                f"\nRefusing to render: content is clipped on sheet {pages}.\n"
                "Trim the copy or re-space the sheet, then build again.",
                file=sys.stderr,
            )
            browser.close()
            return 2

        if args.proof:
            proof_dir = out.parent / "proof" / src.stem
            proof_dir.mkdir(parents=True, exist_ok=True)
            for index in range(len(sheets)):
                target = proof_dir / f"sheet-{index + 1:02d}.png"
                page.locator(".sheet").nth(index).screenshot(path=str(target))
                print(f"  proof {target.name}")

        # @page in the stylesheet declares the 1280 x 720 px sheet;
        # prefer_css_page_size hands that declaration to the PDF engine.
        page.pdf(
            path=str(out),
            prefer_css_page_size=True,
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        browser.close()

    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
