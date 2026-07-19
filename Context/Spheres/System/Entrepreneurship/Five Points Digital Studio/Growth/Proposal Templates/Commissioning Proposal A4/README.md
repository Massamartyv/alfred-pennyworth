# Commissioning Proposal - A4 Template

Version 1 reference implementation, seeded from the McCauley Electrical
commission of July 2026. Six-page A4 commissioning document on the brand
fingerprint: Parchment flood, Fraunces display with Space Grotesk body via the
local woff2 files, Burnt Orange eyebrows, Emerald rules, ghost folio numerals,
corner-anchored contact clusters and the marque eyebrow.

## Files

- `proposal.html` - the document. Duplicate per client and replace the copy;
  the page grammar (cover, conversation, evidence, commission, two prices,
  next) generalizes across offers.
- `build.py` - Playwright + system Chrome render to A4 PDF. Update the RENDER
  path per engagement.
- `fonts.css` + `fonts/` - local font subsets with unicode ranges.

## Per-client personalization

The `.spine` block on the cover (six-stripe pride flag, full-height left edge)
is a McCauley-specific personalization honoring the client's own brand
identity. Remove the block, or replace it with a client-specific detail, for
other commissions. The rest of the palette is fingerprint-locked.

## Page discipline

Every page is a fixed 297mm sheet with `overflow: hidden` - content that grows
must be trimmed or re-spaced, and every render gets a visual page-by-page pass
before it ships. Copy conventions per the fingerprint: no contractions, en
dashes only, British spelling, numerals for 10 and above.
