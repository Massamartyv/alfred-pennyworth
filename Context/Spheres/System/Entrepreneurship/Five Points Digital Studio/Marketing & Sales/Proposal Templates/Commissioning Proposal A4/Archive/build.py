#!/usr/bin/env python3
"""Render the McCauley commissioning proposal to A4 PDF.

Pipeline: proposal.html -> PDF via Playwright + system Chrome.
Fonts are local woff2 files loaded through fonts.css and inline @font-face.
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

RENDER = Path("/Users/martyspicer/Alfred Pennyworth/.working/discovery-architect/mccauley/render")
SRC = RENDER / "proposal.html"
OUT = RENDER / "mccauley-automation-audit-proposal.pdf"


def main() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chrome")
        page = browser.new_page()
        page.goto(SRC.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready.then(() => true)")
        page.pdf(
            path=str(OUT),
            format="A4",
            print_background=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
        )
        browser.close()
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
