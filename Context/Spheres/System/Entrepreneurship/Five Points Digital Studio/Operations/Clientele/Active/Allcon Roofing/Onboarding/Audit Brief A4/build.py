#!/usr/bin/env python3
"""Render the commissioning proposal to A4 PDF, with an overflow gate.

    python3 build.py                      # render proposal.html beside itself
    python3 build.py --src path/to.html   # render a client instance elsewhere
    python3 build.py --proof              # also write per-page PNG proofs

Pipeline: HTML -> PDF via Playwright driving system Chrome. Fonts are local
woff2 files loaded through fonts.css, so the render needs no network and is
reproducible years from now. Run localize_fonts.py once first.

THE OVERFLOW GATE. Every page is a fixed 297mm sheet with overflow: hidden,
which means copy that grows past the sheet is not reported by anything -- it
is silently guillotined, and the first person to notice is the client holding
the paper. So the build measures each sheet before it writes the PDF and
refuses to write one that has lost content. Fix the copy or the spacing; do
not raise the tolerance.

The proof pass writes one PNG per sheet for the page-by-page visual read.
Screenshots come from Chrome itself, not from an embedded preview pane, so
what they show is what prints.
"""

from __future__ import annotations

import argparse
import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent

# A4 at 96 CSS px per inch. Chrome lays the document out at this viewport so
# that mm-declared sheets resolve exactly once, with no reflow between the
# measurement pass and the PDF pass.
A4_PX = {"width": 794, "height": 1123}

# One CSS pixel of slack. Sub-pixel rounding on mm-declared boxes routinely
# leaves a fractional overhang that neither prints nor clips; anything past
# a whole pixel is real lost content.
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
    parser.add_argument("--src", type=pathlib.Path, default=HERE / "proposal.html")
    parser.add_argument("--out", type=pathlib.Path, default=None)
    parser.add_argument(
        "--proof",
        action="store_true",
        help="write per-page PNG proofs beside the PDF",
    )
    args = parser.parse_args()

    src = args.src.resolve()
    if not src.exists():
        print(f"No such document: {src}", file=sys.stderr)
        return 1

    out = args.out or src.with_suffix(".pdf")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        page = browser.new_page(viewport=A4_PX)
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
                f"  page {sheet['page']}  {state:>7}"
                f"  vertical {over_y:+d}px  horizontal {over_x:+d}px"
            )

        if overflowing:
            pages = ", ".join(str(sheet["page"]) for sheet in overflowing)
            print(
                f"\nRefusing to render: content is clipped on page {pages}.\n"
                "Trim the copy or re-space the page, then build again.",
                file=sys.stderr,
            )
            browser.close()
            return 2

        if args.proof:
            # Namespaced by source stem: a folder holding both a proposal and a
            # statement would otherwise have the second render silently
            # overwrite the proofs of the first.
            proof_dir = out.parent / "proof" / src.stem
            proof_dir.mkdir(parents=True, exist_ok=True)
            for index in range(len(sheets)):
                target = proof_dir / f"page-{index + 1:02d}.png"
                page.locator(".sheet").nth(index).screenshot(path=str(target))
                print(f"  proof {target.name}")

        page.pdf(
            path=str(out),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        browser.close()

    print(f"\nWrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
