#!/usr/bin/env python3
"""Render the mail mark: assets/mark-40.png, from assets/mark-ink.svg.

    uv run --with playwright python make_mail_mark.py

Run once, and again whenever the commissioned mark is revised. Generated
output; never hand-edit the PNG.

Why a raster at all. Every other surface in the suite takes the mark as SVG,
which is the correct format and scales without loss. Mail clients are the
exception: SVG support across them is patchy enough that the fingerprint
specifies a PNG for this one artefact. So the signature gets a raster, and it
is generated from the same vector every other surface uses rather than
exported by hand into a parallel truth.

Rendered at 3x and downsampled by the browser to 40px so the seam channels of
the crystal survive the reduction. The background stays transparent: the mark
renders ink, and a mail client in dark mode composites it on its own ground.

THE STAGE IS A REAL FILE, deliberately. Handing the markup to set_content
leaves the page on an about:blank origin, and Chrome refuses to load a
file:// subresource from there - so the mark silently fails to arrive and the
screenshot captures a broken-image placeholder instead of the crystal. The
resulting PNG is structurally valid, passes every CRC, and is unreadable. The
stage is therefore written beside the mark and navigated to, so the SVG and
the page share one origin. Do not swap this back to set_content.
"""

from __future__ import annotations

import pathlib
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent
SOURCE = HERE / "assets" / "mark-ink.svg"
TARGET = HERE / "assets" / "mark-40.png"

SIZE = 40
SCALE = 3


def main() -> int:
    if not SOURCE.exists():
        print(f"No such mark: {SOURCE}", file=sys.stderr)
        return 1

    stage = HERE / "_mail-mark-stage.html"
    stage.write_text(
        "<!DOCTYPE html><html><head><meta charset=\"utf-8\"><style>"
        "* { margin: 0; padding: 0; }"
        "html, body { background: transparent; }"
        f"#stage {{ width: {SIZE}px; height: {SIZE}px; }}"
        "#stage img { width: 100%; height: 100%; display: block; }"
        "</style></head><body>"
        f'<div id="stage"><img src="{SOURCE.name}" alt=""></div>'
        "</body></html>"
    )
    # The stage sits in assets/ so the relative src resolves beside the mark.
    stage_in_assets = SOURCE.parent / stage.name
    stage.rename(stage_in_assets)

    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(channel="chrome")
            page = browser.new_page(
                viewport={"width": SIZE, "height": SIZE},
                device_scale_factor=SCALE,
            )
            page.goto(stage_in_assets.as_uri())
            page.wait_for_load_state("networkidle")

            arrived = page.evaluate(
                "() => { const i = document.images[0];"
                " return i && i.complete && i.naturalWidth > 0; }"
            )
            if not arrived:
                print(
                    f"The mark did not load from {SOURCE.name}; refusing to "
                    "write a blank PNG.",
                    file=sys.stderr,
                )
                browser.close()
                return 2

            page.locator("#stage").screenshot(
                path=str(TARGET), omit_background=True
            )
            browser.close()
    finally:
        stage_in_assets.unlink(missing_ok=True)

    print(f"Wrote {TARGET.relative_to(HERE)} at {SIZE}px, {SCALE}x device scale.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
