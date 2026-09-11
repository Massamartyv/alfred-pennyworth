#!/usr/bin/env python3
"""Check a marque presentation against the house copy conventions.

    uv run --with playwright python gate.py                  # deck.html
    uv run --with playwright python gate.py --src other.html

Checks the RENDERED text, not the source: the stylesheet is full of custom
properties that look like double hyphens and CSS functions that look like
parentheses, so the only trustworthy copy is what the browser lays out.

Enforces the fingerprint punctuation gate, V6: no em dashes, no double
hyphens, no parentheses, no contractions, no possessive apostrophe-s, no plus
sign as a conjunction, no exclamation marks, no Oxford comma. Fails on any
unfilled guillemet slot, which makes it the last check before a send. Fails
on runts: a single short word stranded alone on the last line of a paragraph.

Also audits the serif discipline: any element rendering the display serif at
a computed weight above 400 fails, because the face carries the emphasis and
the setting must not.

Exit status is 0 when clean, 1 when anything is found, so it can gate a send.
Note the unfilled framework fails the slot check by design; a client instance
must pass clean.
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

# The serif carries no weight above 400 anywhere in the system. Audit the
# computed style of every element that renders text in the serif stack.
SERIF_WEIGHT = """
() => {
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    if (!el.textContent || !el.textContent.trim()) continue;
    const cs = getComputedStyle(el);
    const family = cs.fontFamily.toLowerCase();
    if (family.includes('editorial') || family.includes('sentient')) {
      const weight = parseInt(cs.fontWeight, 10);
      if (weight > 400) {
        out.push({tag: el.tagName, cls: el.className.toString().slice(0, 40), weight});
      }
    }
  }
  return out;
}
"""


# Invisible text. A register that redefines colour tokens without re-asserting
# the literal colour property can leave text the same colour as its ground --
# present in the DOM, unreadable on the sheet, and undetectable through
# innerText. Walk every element carrying its own text, resolve its effective
# background by climbing to the first opaque ancestor fill, and fail anything
# whose contrast falls below 1.6:1. Elements at cumulative opacity below 0.5
# (the ghost lines) are exempt: their lightness is deliberate. The threshold
# catches invisibility, not taste; legibility judgement stays with review.
INVISIBLE = """
() => {
  const lum = (r, g, b) => {
    const f = v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };
  const parse = c => {
    const m = c.match(/rgba?\\(([\\d.]+),\\s*([\\d.]+),\\s*([\\d.]+)(?:,\\s*([\\d.]+))?\\)/);
    return m ? {r: +m[1], g: +m[2], b: +m[3], a: m[4] === undefined ? 1 : +m[4]} : null;
  };
  const out = [];
  for (const el of document.querySelectorAll('body *')) {
    const own = Array.from(el.childNodes).some(n => n.nodeType === 3 && n.textContent.trim());
    if (!own) continue;
    let node = el, alpha = 1, bg = null;
    while (node && node !== document.documentElement) {
      const cs = getComputedStyle(node);
      alpha *= parseFloat(cs.opacity);
      if (!bg) {
        const b = parse(cs.backgroundColor);
        if (b && b.a > 0.9) bg = b;
      }
      node = node.parentElement;
    }
    if (alpha < 0.5 || !bg) continue;
    const fg = parse(getComputedStyle(el).color);
    if (!fg) continue;
    const l1 = lum(fg.r, fg.g, fg.b), l2 = lum(bg.r, bg.g, bg.b);
    const ratio = (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
    if (ratio < 1.6) {
      out.push({
        text: el.textContent.trim().slice(0, 32),
        cls: el.className.toString().slice(0, 30),
        ratio: Math.round(ratio * 100) / 100,
      });
    }
  }
  return out;
}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--src", type=pathlib.Path, default=HERE / "deck.html")
    args = parser.parse_args()

    src = args.src.resolve()
    if not src.exists():
        print(f"No such document: {src}", file=sys.stderr)
        return 1

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(src.as_uri())
        page.wait_for_load_state("networkidle")
        page.evaluate("document.fonts.ready")
        text = page.evaluate("() => document.body.innerText")
        runts = page.evaluate(RUNTS)
        heavy_serifs = page.evaluate(SERIF_WEIGHT)
        invisible = page.evaluate(INVISIBLE)
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

    if heavy_serifs:
        failures += 1
        print(f"  {'serif above 400':<26} FOUND  {len(heavy_serifs)}")
        for hit in heavy_serifs[:6]:
            print(f"  {'':<26}   <{hit['tag'].lower()} class={hit['cls']!r}> at {hit['weight']}")
    else:
        print(f"  {'serif above 400':<26} clean")

    if invisible:
        failures += 1
        print(f"  {'invisible text':<26} FOUND  {len(invisible)}")
        for hit in invisible[:6]:
            print(
                f"  {'':<26}   {hit['text']!r} class={hit['cls']!r}"
                f" contrast {hit['ratio']}:1"
            )
    else:
        print(f"  {'invisible text':<26} clean")

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
