# Commissioning Proposal - A4

Template v2. Six-page A4 commissioning document on the Quintessence
ratification of 24 July 2026: bone paper against one ink, the mismatched serif
pair, IBM Plex Mono for indices and metadata, and colour supplied by a single
voice through the `data-voice` contract.

Built from the design system at `~/.claude/skills/five-points-design/`, which
is the imported mirror of the Claude Design project
`de001169-e481-46a4-be13-6eb348868e6f`. Read that system first; this document
only records what is specific to the proposal.

## What changed from v1

v1 was a McCauley Electrical instance wearing the word "template". Its copy,
its electrical one-line plates and its $1,000 / $2,000 / $3,000 doors were all
that one engagement, and its palette and faces belong to a direction that has
since been retired. It is preserved in `Archive/` and should not be reopened
for a new client.

| | v1 | v2 |
|---|---|---|
| Display face | Fraunces 300 | PP Editorial New 400, interim Sentient |
| Body face | Space Grotesk | PP Neue Montreal, interim General Sans |
| Datum face | none | IBM Plex Mono |
| Accent | Burnt Orange eyebrows, Emerald rules | one voice, coral by default, via `data-voice` |
| Page index | 58pt ghosted display numeral | mono index numeral in the margin |
| Cover masthead | the numeral 5 | the Quintessence at 19mm |
| Cover spine | six-stripe pride flag | neutral five-tone ramp |
| Doors | three ad-hoc prices | the Survey, the Commission, the Evolution |
| Two prices | yes first | no first, so the ledger anchors the fee |
| Overflow | eyeballed | gated in the build, page by page |

## Files

- `proposal.html` - the document. Duplicate per client and replace the slots.
- `build.py` - render to A4 PDF, with the overflow gate. `--proof` also writes
  per-page PNGs to `proof/`.
- `localize_fonts.py` - pull the three faces into `fonts/`, cut the static
  instances and write `fonts.css`. Run once per checkout - see Fonts below.
- `fonts.css` + `fonts/` - local static faces plus their variable cutting
  sources. Generated; do not hand-edit.
- `Archive/` - v1, retired.

## Rendering

Playwright is not installed system-wide and a venv inside a template would be
copied into every client folder, so the build runs through an ephemeral
environment:

```bash
uv run --with playwright python build.py --proof
```

System Chrome does the rendering, and every font is local, so the render needs
no network and reproduces years from now.

**The overflow gate.** Each page is a fixed 297mm sheet with `overflow:
hidden`, which means copy that grows past the sheet is silently guillotined
rather than reported. `build.py` measures every sheet and refuses to write a
PDF that has lost content. When it refuses, trim the copy or re-space the page.
Do not raise the tolerance. Page 5 in particular sits closest to its ceiling.

## Fonts

**Never ship a variable font into a Chrome-rendered PDF.** Chrome's
`page.pdf()` embeds variable fonts as Type 3 glyph procedures with bad
bounding boxes. Chrome itself, poppler and macOS Preview render the result
fine, but strict viewers - pdf.js, and therefore Firefox and much of the
browser-preview world - draw the words overlapping and stacked on top of one
another. The defect shipped undetected for exactly that reason.

`localize_fonts.py` therefore treats the Fontshare variable files as cutting
sources only. It pins static instances with fontTools at the weights the
stylesheet requests - Sentient 400 roman and italic, General Sans 400 and
600 - and `fonts.css` serves only those statics as TTF, which Chrome embeds
as healthy CID TrueType. The `*-200_700-*.woff2` files stay in `fonts/` for
re-cutting and are never served.

```bash
uv run --with "fonttools[woff]" python localize_fonts.py
```

The corollary: every weight the document can request, including by
inheritance, must exist as a real face. A missing weight makes Chrome
synthesise it, and synthetic bold embeds as Type 3 through the same path.
The guillemet slots inside semibold headings did exactly that until IBM
Plex Mono 600 joined 400 and 500. If a new rule starts asking for a weight
or style not yet served, add it to `INSTANCES` in `localize_fonts.py` - or
to the Google URL for the mono - and re-run.

Diagnose any built PDF with `pdffonts proposal.pdf`. A `Type 3` row is the
defect; a healthy sheet reads `CID TrueType` throughout. The rule applies
to the licensed PP files when they land - if they arrive as variable fonts,
cut statics before they enter `fonts/`.

## Per-client personalisation

Every client-specific field is a `«GUILLEMET SLOT»`, set in mono on a coral
tint so that anything unfilled is impossible to miss in the proof. The register:

| Slot | Where |
|---|---|
| `«DD MONTH YYYY»` | cover date line |
| `«PRINCIPAL»` | cover, page 2 |
| `«PRACTICE»` | cover, page 2, footers on pages 2 to 5 |
| `«CITY»` | cover |
| `«THE FOUNDING PROPOSITION»` | page 2 |
| `«THE EVIDENCE OF DEMAND»` | page 2 |
| `«FINDING ONE»`, `«FINDING TWO»` | page 3 headings |
| `«WHAT WAS FOUND, WHAT IT COSTS, IN TWO SENTENCES»` | page 3, twice |
| `«THE SMALL THINGS FOUND WRONG»` | page 3, finding 03 |
| `«THE INACTION LEDGER, IN FIGURES»` | page 5 |
| `«$197 – $19,700»` | page 5 price line |
| `«BOOKING LINK»`, `«N»` | page 6 |

The cover title reads "Excellence at volume." by default. It is a working
default, not a fixture, and it is the first thing to replace.

Everything else is studio-side canon and changes rarely: the wall, the three
doors, the guarantee, the two-prices logic and the three next steps. That is
deliberate. The argument of the studio is the same for every premium operator
near one million in revenue, and a proposal that re-argues it from scratch each
time is a proposal that does not believe it.

**Search for `«` before sending.** A live slot in a client document is the one
failure this template can still produce.

## Design decisions worth knowing

**One voice, one attribute.** `<body data-voice="coral">` sets the whole
document. Swap in `cornflower`, `sun`, `lavender` or `sage` and every rule,
numeral, bullet, facet and well follows, because no rule in the document names
a hue. Coral is the lead voice and holds the accent role by default. One voice
per surface is absolute, and the document is one surface, so never mix two.

**The neutral spine.** The five voices meet in exactly one place, the mark, so
the default cover spine is five tones of the neutral ramp rather than five
voices. An identity spine - pride, pan-African or similar - is a themed
substitution, wider than the default, and reserved for identity-owned clients
per the standing ruling. It is not the house default.

**The mark at 19mm.** The cover carries the Quintessence in place of the text
wordmark, per the fingerprint amendment of 2026-07-21, with the studio name
held in the cover footer line so the mark never carries identification alone.
19mm resolves to roughly 72 CSS px, which sits between the UI grade at 48 and
the sign grade at 96 on the mark size ladder, so it takes the full crystal at
stroke-width 2.5 verbatim. Do not thicken the stroke to make the seams close:
they are meant to stay open at this grade and they resolve at print resolution
even though they turn to noise in a screen-scale raster. Only below 26px does
the mark change form, and there it becomes the reduction in `favicon.svg`.

**One ink field.** Page 4 is the document's only inversion, declared with
`data-register="ink"`. The pull quote on page 3 therefore takes the quieter
device, a voice-tint well with an ink rule, rather than a second flood.

**Two figures step outside the reading measure.** The price line and the
schedule table are set to 152mm rather than the 122mm measure. A price that
wraps stops reading as a figure, and a three-column schedule held to 122mm
falls to 46mm in its last column and wraps four deep.

**Deliberate deviation, one.** On the ink register the ratified `--border` is
`rgba(bone, 0.14)`, which is tuned for a backlit display and disappears when
printed on obsidian, taking the door edges with it. `--rule-on-ink` raises it
to `0.30`. Nothing else departs from the token sheet.

**Headroom.** Pages 3, 5 and 6 render with space at the foot. That is
deliberate: the slots on those pages are the ones that grow most when real
client copy replaces them. Do not fill the space with new material, and let the
gate tell you when the copy has grown too far.

## Copy conventions

Per the brand fingerprint, quality gate V6, and enforced against the rendered
text rather than the source: no em dashes, en dashes only. No contractions. No
parentheses. No Oxford comma. No exclamation marks. Romance possessives, "the
live conditions of the practice" and not the other way round. British spelling.
Numerals for 10 and above. The middle dot separates metadata.

Note that the design system README permits the em dash for a considered aside.
The fingerprint bans it. The fingerprint governs.

`gate.py` enforces all of it, plus one more thing: it fails on any unfilled
`«SLOT»`, which makes it the last check before a send.

```bash
uv run --with playwright python gate.py
```

It grades the rendered text rather than the source, and it exits non-zero when
anything is found. Note that the template itself fails the slot check by
design; a client instance must pass clean.

## Open

- The fingerprint amendment of 2026-07-21 describes the cover glyph as "the
  founder-approved nav adaptation, flat single colour with the seam-rounding
  paired stroke". That adaptation is not in the design system, so the cover here
  renders the standard `mark.svg` at the sign-grade stroke. Reconcile when the
  adaptation surfaces.
- The licensed PP files are pending. Drop them into `fonts/` under their real
  family names and the document upgrades itself, because every stack already
  names PP first.
- The ceremonial seal is deliberately absent. It belongs to the countersigned
  commissioning agreement, not to a proposal.
