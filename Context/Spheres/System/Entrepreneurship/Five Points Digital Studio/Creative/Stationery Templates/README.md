# Stationery Suite

Template v2. The house hand, and the second instrument of The Letterpress:
four artefacts at three trims on the Quintessence ratification of 24 July
2026 - bone paper against one ink, the mismatched serif pair, IBM Plex Mono
for metadata, colour supplied by a single voice through the `data-voice`
contract.

Where the presentation announces the house, the stationery is what the house
uses while working. It inherits the component grammar of the master framework
rather than repeating it: three components carry over, the rest is proper to
the hand.

v2 rebuilt the visual layer onto the A Friend Of Mine Bayport architecture by
operator direction, 2026-08-06 - the masthead, the text axis and the
two-column metadata footer described below. The build, the gate and the slot
discipline are unchanged from v1.

v2.1, same day, sharpened three artefacts against the reference library by
operator direction. The influence trail, so the decisions stay legible:

- **A Friend Of Mine** (venture library, canon) - the Bayport studio itself.
  The slip's total colour flood is their principle 1 executed through the
  voice system; the corner-anchored whisper clusters are their principle 5.
- **Paula Scher** (personal library, canon) - let the type be the image. The
  card front carries no mark because the wordmark set with conviction IS the
  identity; at this scale the letterforms stop being text and become space.
- **Pangram Pangram** (venture library, canon) - foundry specimen culture.
  The card annotates itself in the mono voice: the colophon line on the
  front, the crystal's asset designation QT-001 under the mark on the back.
  The foundry credit itself joins the colophon only when the licensed faces
  land and the claim becomes true.
- **Virgil Abloh** (personal library, canon) - negative space as a material.
  The slip's empty middle is the artefact; what stays empty is a decision.
- **Aesop** (venture library, canon) - the restraint arbiter. Two gestures on
  the card, none on the letterhead, one flood on the slip. Nothing else.

v2.2, same day - the operator's keep ruling. The letterhead and the
compliments slip are RATIFIED as presented. The business card is PARKED
unratified: v2.1 stands as the working draft, the card leaves this mission's
critique scope and takes its own design session later. The signature was
sent through the same Bayport pass by the same ruling: it is now the
letterhead compressed - the masthead above, and the letterhead's two-column
metadata foot below a single rule, reach on the left, house and place on the
right, in mail-safe nested tables. The flatten pass in build.py gained a
guard the same hour: any inline declaration still carrying var() resolves
through the computed style regardless of property, so no custom property can
survive into a built deliverable again.

One structural note the reviewer recorded: the signature's guillemet slots
are plain text, not `.slot` spans, unlike the rest of the suite. This is by
construction, not omission - the flatten pass ships the block's markup as
the deliverable, so a styled slot span would carry its tint into a live mail
client on the framework file. The guillemets alone mark the fields, and
`gate.py`'s slot-survivor check remains the mechanical backstop.

## Files

- `letterhead.html` - A4 house stationery. Duplicate per letter and fill.
- `compliments.html` - DL landscape slip. Finished canon, no slots.
- `card.html` - 74mm square business card, two sheets: front then back.
- `signature.html` - email signature. Builds to `signature.built.html`.
- `specimen-letter.html`, `specimen-card.html`, `specimen-signature.html` -
  filled instances. Gate evidence and visual reference; derive from the
  frameworks, never from a specimen.
- `stationery.css` - the shared grammar. Four artefacts, one stylesheet.
- `build.py` - render each artefact at its own declared trim, with the
  overflow gate and the flatten pass. `--all` builds the suite.
- `gate.py` - copy-convention gate, plus the serif, invisible-text and
  type-stack audits. `--all` gates the suite.
- `make_mail_mark.py` - generate `assets/mark-40.png` for the signature.
  Run once, and again whenever the commissioned mark is revised.
- `fonts.css` + `fonts/` - local woff2. Generated; do not hand-edit.
- `assets/` - the Quintessence mark in its register renderings.

## Rendering

```bash
uv run --with playwright python build.py --all --proof
```

```bash
uv run --with playwright python gate.py --all
```

System Chrome does the rendering and every font is local, so the render needs
no network. The overflow gate measures every sheet and refuses to write a PDF
that has lost content; trim the copy or re-space the sheet rather than raising
the tolerance.

## The trims

Each document declares its own trim in its head, and both the build and the
gate read it from there. The geometry has exactly one source of truth and it
is the document.

| Artefact | Trim | Declared as | Output |
|---|---|---|---|
| Letterhead | A4, 210 x 297mm | `210x297mm` | `letterhead.pdf` |
| With-compliments slip | DL landscape, 220 x 110mm | `220x110mm` | `compliments.pdf` |
| Business card | 74 x 74mm square, 2 sheets | `74x74mm` | `card.pdf` |
| Email signature | none | `screen` | `signature.built.html` |

The card is a deliberate carve-out from the A-series standard, per the
fingerprint, to preserve cardholder compatibility.

## The axis

Every artefact is built on two vertical lines: a narrow mark column at the
outer margin, and the text axis indented from it. The mark sits alone in its
column. The identification, everything the reader reads, and the metadata
footer all sit on the axis. Nothing is centred except the one bled moment on
the card front.

This is the architecture of the A Friend Of Mine Bayport stationery -
operator-directed 2026-08-06 - which is the same case study the fingerprint's
seven AFOM execution principles were extracted from. The suite therefore
reads as one system across three trims, and any document added to The
Letterpress later can join it by adopting the same four variables:
`--margin-x` for the mark column, `--axis` for the text, `--margin-r` and
`--margin-b` for the outer edges. Each document sets them for its own trim.

## Inherited components

Three of the twelve, reduced to what a working document needs. The rest of
the master grammar - the poster cover, the thesis essay, the interstitial -
belongs to documents that argue, and stationery does not argue.

| ID | As inherited here | Where |
|----|-------------------|-------|
| LP-01 | The mark discipline: one colour per rendering, the register variant chosen by ground | all four |
| LP-02 | The running head, become the masthead: mark in its column, identification on the axis | letterhead, compliments, card back |
| LP-07 | The action card, reduced to the marque eyebrow in the footer grid | letterhead, compliments |

## Slot register

Every instance field is a `«GUILLEMET SLOT»` set in mono on a voice tint, so
anything unfilled is impossible to miss in a proof. `gate.py` fails on any
survivor, which makes it the last check before a send.

| Slot | Where |
|------|-------|
| `«DD MONTH YYYY»` | letterhead, the date line |
| `«PRINCIPAL NAME»` `«HOUSE OR COMPANY»` `«CITY»` | letterhead, the address block |
| `«THE SALUTATION»` `«THE CLOSE»` | letterhead, the opening and the sign-off |
| `«THE LETTER – FIRST/SECOND/THIRD MOVEMENT»` | letterhead, the three body paragraphs |
| `«NAME»` `«TITLE»` | letterhead sign-off, card back, signature |
| `«EMAIL»` | card back, signature |

The with-compliments slip carries no slots at all. It is finished canon: the
only thing that ever changes on it is written by hand in ink, which is the
point of the object. It therefore passes the gate as shipped and serves as
its own specimen.

## Design decisions worth knowing

**One voice, one attribute.** `<body data-voice="coral">` sets the whole
artefact. Swap in `cornflower`, `sun`, `lavender` or `sage` and every tint,
rule and accent follows - including the email signature, which is flattened
from the same tokens at build time. One voice per artefact, absolute.

**The wordmark appears on working documents.** AFOM principle 3 in the
fingerprint reads "the wordmark lives on covers, not on letterhead."
The Bayport letterhead that principle was extracted from carries its
wordmark at the top of every sheet, beside the mark, above the address. The
principle misreports its own source. The suite follows the artefact rather
than the transcription, on operator direction; the delta is staged for the
canon amendment along with the serif weight.

**The footer is a grid, not a cluster.** Two columns on the axis, each
carrying two groups: identification and reach on the left, standing and
descriptor on the right. It does not run the full width of the sheet, so
AFOM principle 5 - corner-anchored contact typography, nothing running full
width - survives intact.

**The compliments slip floods the voice.** It is the ceremonial piece, the
one that travels with a gift or a returned document, so it takes AFOM
principle 1 whole: a total flood of the voice's deep grade, the message set
tonally in the light grade at display size - the tonal register is the
gesture, which is why it only works large - the whisper clusters in the
tint, and the mark in parchment per the one-colour-per-rendering rule on
dark grounds. One voice per surface holds absolutely: no second hue touches
the object. The letterhead stays bone because it is the working surface, and
the slip is the one full-voice object in the hand.

**The card front is a typographic composition, and the one symmetric
moment.** The two words are set larger than the card, each line cropped by
the trim on both edges, the lines offset against each other so the letters
enter one edge deeper than they leave the other. The tagline sits in the
band the leading opens between the lines - the one surface in the suite
where the tagline appears - and the colophon whispers at the foot in the
mono voice. No mark on this face: the wordmark set with conviction is the
identity, and the mark holds the back with its designation beneath it.
Offsets and crops are measured against rendered widths, not assumed. The
bleed lives inside its own clipping box rather than overflowing the sheet,
because the sheet's overflow is what the build's gate measures: an
intentional bleed must never be indistinguishable from a guillotined line.
Note that a line wider than its box does not centre its overflow;
`text-align: center` anchors it left and spills right only. Centring is done
by construction.

**The signature is generated, never hand-written.** Mail clients strip style
blocks, webfonts and custom properties, so the signature cannot ship as
authored. The source therefore names no hue and no face directly: it writes
inline rules against the token sheet, and `build.py` resolves them through
`getComputedStyle` into `signature.built.html`. That generated file is what
gets pasted into the client. Never hand-edit it; it is overwritten on every
build. The consequence worth having: the mail artefact obeys the voice
contract like everything else, and a voice change regenerates it.

**The mail stack is the one sanctioned exception.** Mail clients have Arial
and not much else, so the signature runs `--font-mail` where every other
surface runs the three ratified stacks. The fingerprint already specifies
Arial for this artefact. The exception is declared as a token rather than
written ad hoc, and `gate.py` confines it: the mail stack is permitted on the
signature and fails anywhere else, and any family belonging to no declared
stack fails everywhere.

**The register variants carry literal colour, not `currentColor`.** The
upstream `mark.svg` in the design system fills with `currentColor`, which is
correct for inline SVG where the host sets `color`. Loaded through an `<img>`
tag the SVG becomes an isolated document, `currentColor` resolves to black
regardless of the root fill, and a parchment mark renders ink. Both register
variants here therefore carry their literal hex. Never copy `currentColor`
geometry into a variant meant for an `<img>`.

**The mail mark is a raster, generated from the vector.** Every other surface
takes the mark as SVG. Mail clients are the exception, so `make_mail_mark.py`
renders `assets/mark-40.png` from `mark-ink.svg` at 3x and lets the browser
downsample, and it refuses to write the file if the mark did not arrive. The
stage it renders is a real file rather than injected markup, because a page
on an `about:blank` origin cannot load a `file://` subresource and the
failure is silent - a structurally valid PNG that no client can decode.

**The wordmark sits at serif 400.** The fingerprint's Layer 3 specifies
Medium 500 for the wordmark. The Quintessence ratification caps the serif at
400 and `gate.py` enforces the cap, so the cap governs. The drift is recorded
in the canon amendment staged for Release.

**No street address and no telephone.** The studio publishes an email and a
website; the proposal template has always carried exactly those two lines,
and the suite follows it. The telephone slot was dropped from the card in v2
rather than left as a field nobody can fill - a card that carries a number
the studio does not answer is worse than a card that does not. If the house
takes a published line, add it to the footer grid in `stationery.css` once
and every artefact inherits it. The footer's right column carries Decatur,
Georgia, which the presentation cover already publishes, so the suite is
consistent with what is already in the world.

**The signature mark must be hosted before the signature ships.** The `src`
is a relative local path, which is correct for the proof and wrong for a live
signature: it breaks the moment the block leaves this folder, and most
clients will not embed a local file on paste. Replace it with an absolute
https URL on the studio domain before the block goes into anyone's mail
client. This is the last mile and it is not yet built.

## Copy conventions

Per the brand fingerprint quality gate V6, enforced against the rendered
text: no em dashes - en dashes only - no contractions, no parentheses, no
Oxford comma, no exclamation marks, no possessive apostrophe-s, British
spelling, numerals for 10 and above, the middle dot separates metadata.
`gate.py` enforces all of it, plus runts, the serif weight ceiling of 400, an
invisible-text audit and the type-stack audit. The gate cannot judge copy
quality or layout taste; the behavioural review tier owns that.

## Deriving an instance

1. Duplicate the framework file. Keep the stylesheet link.
2. Declare the voice on `<body data-voice="...">`. One voice.
3. Fill every slot. Leave nothing guillemetted.
4. Build with `--proof` and read the proof sheet with your eyes. The gate
   cannot see an image that failed to load, a mark rendered in the wrong
   register or a letter that reads badly.
5. Gate it. A client-facing instance passes clean or it does not go out.

## Open

- The signature mark needs hosting at an absolute https URL on the studio
  domain. Until then the signature is proof-only and must not be pasted into
  a live mail client.
- The licensed PP files are pending; drop them into `fonts/` under their real
  family names and the suite upgrades itself.
- Printed production is unspecified: the fingerprint calls for 540gsm duplex
  card with painted edges, 120gsm uncoated letterhead and edge painting in
  the opposite colour. No printer is engaged and no stock is proofed.
- A published telephone line, if the house wants one.
- The envelope range - DL, C5 and C4 - is specified in the fingerprint and
  not yet drawn. It needs no build script, only a printer specification.
- Behavioural review pass, validation contract A6, pending for the specimens.
