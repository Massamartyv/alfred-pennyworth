#!/usr/bin/env python3
"""Check a commissioning document against the house copy conventions.

    uv run --with playwright python gate.py                  # proposal.html
    uv run --with playwright python gate.py --src other.html

Checks the RENDERED text, not the source. Checking the source gives false
positives on every count, because the stylesheet is full of custom properties
that look like double hyphens and CSS functions that look like parentheses.
The only trustworthy copy is what the browser lays out, so the document is
loaded and `document.body.innerText` is what gets graded.

Enforces the fingerprint punctuation gate, V6: no em dashes, en dashes only,
no contractions, no parentheses, no Oxford comma, no exclamation marks, and
Romance possessives rather than an apostrophe-s.

Also fails on any unfilled `«SLOT»`, which is the one mistake a client-ready
instance must never ship with.

And it fails on runts. A runt is a single short word stranded alone on the last
line of a paragraph. It reads as a defect before it reads as a word, and on
these pages there is too much white space around it to hide. `text-wrap: pretty`
in the stylesheet prevents most of them; this catches the rest, by walking the
laid-out text character by character and reading the final line back verbatim
rather than inferring it from a width.

Note the neighbouring terms, because they are routinely confused: a WIDOW is a
paragraph's last line pushed alone to the top of the next page or column, and an
ORPHAN is a paragraph's first line stranded alone at the foot of one. Fixed
sheets with `overflow: hidden` cannot produce either, so runts are the only one
of the three this document can suffer.

Exit status is 0 when clean, 1 when anything is found, so it can gate a send.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).parent

CHECKS = {
    "em dash": r"—",
    "double hyphen": r"--",
    "parentheses": r"[()]",
    "contraction": r"\b\w+['’](?:t|re|ve|ll|d|m)\b",
    "possessive apostrophe-s": r"\b\w+['’]s\b",
    "plus as conjunction": r"\s\+\s",
    "exclamation mark": r"!",
    "Oxford comma": r",\s+(?:and|or)\s+\w+\s*[.;]",
    "unfilled slot": r"«[^»]*»",
}

# Walk each paragraph character by character and record the y of every glyph. A
# change in y is a line break, so the tail after the final change is the last
# line, read back verbatim. Measuring the width of the last line instead would
# only tell you it is short, not whether it is one word or two.
RUNTS = """
() => {
  const out = [];
  for (const p of document.querySelectorAll('p')) {
    const walker = document.createTreeWalker(p, NodeFilter.SHOW_TEXT);
    const chars = [];
    let n;
    while ((n = walker.nextNode())) {
      for (let i = 0; i < n.textContent.length; i++) {
        const r = document.createRange();
        r.setStart(n, i); r.setEnd(n, i + 1);
        chars.push({c: n.textContent[i], y: Math.round(r.getBoundingClientRect().top)});
      }
    }
    if (chars.length < 2) continue;
    const lastY = chars[chars.length - 1].y;
    let start = chars.length - 1;
    while (start > 0 && chars[start - 1].y === lastY) start--;
    const lastLine = chars.slice(start).map(o => o.c).join('').trim();
    const lines = new Set(chars.map(o => o.y)).size;
    if (lines > 1 && lastLine.split(/\\s+/).filter(Boolean).length === 1) {
      out.push({lastLine, opening: p.textContent.trim().slice(0, 40)});
    }
  }
  return out;
}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", type=pathlib.Path, default=HERE / "proposal.html")
    args = parser.parse_args()

    src = args.src.resolve()
    if not src.exists():
        print(f"No such document: {src}", file=sys.stderr)
        return 1

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        page = browser.new_page(viewport={"width": 794, "height": 1123})
        page.goto(src.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        text = page.evaluate("() => document.body.innerText")
        runts = page.evaluate(RUNTS)
        browser.close()

    text = re.sub(r"\s+", " ", text)

    failures = 0
    print(f"{src.name} · {len(text)} characters of visible copy\n")
    for name, pattern in CHECKS.items():
        hits = re.findall(pattern, text)
        if hits:
            failures += 1
            shown = sorted(set(hits))[:8]
            print(f"  {name:<26} FOUND  {shown}")
        else:
            print(f"  {name:<26} clean")

    if runts:
        failures += 1
        print(f"  {'runt':<26} FOUND  {len(runts)}")
        for runt in runts:
            print(f"  {'':<26}   {runt['lastLine']!r} ends [{runt['opening']}...]")
    else:
        print(f"  {'runt':<26} clean")

    print(
        f"\n  en dashes {text.count(chr(8211))} · "
        f"middle dots {text.count(chr(183))}"
    )

    if failures:
        print(f"\n{failures} check(s) failed. Not ready to send.", file=sys.stderr)
        return 1

    print("\nClean against the house conventions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
