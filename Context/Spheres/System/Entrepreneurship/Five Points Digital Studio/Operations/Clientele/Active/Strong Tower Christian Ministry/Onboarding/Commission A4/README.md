# Strong Tower Christian Ministry - A Five Points Commission

Two documents, sent together. Both A4, both on the Quintessence design system,
both in the cornflower voice.

- `proposal.html` - five pages. What was built, what comes with it, what it
  costs and how the last steps run.
- `statement.html` - one page. Statement FP-2026-002, the money.

An instance of `Marketing & Sales/Proposal Templates/Commissioning Proposal A4/`. Read that
README for the system rules and the render pipeline.

**Status is not recorded here.** Whether these have been signed, sent or paid
lives in the Five Points Notion workspace.

## Build

```bash
uv run --with playwright python build.py --proof
```

```bash
uv run --with playwright python build.py --src statement.html --proof
```

```bash
uv run --with playwright python gate.py
```

Run the gate against both before either goes anywhere. Proofs are namespaced by
source, so `proof/proposal/` and `proof/statement/` do not collide.

## What the proposal says

Revision 2, operator-directed. The job is to formalise an engagement that is
nearly complete, not to win one. The Goodsons came to Five Points already
knowing what they needed, the build ran early and fast, and the site is close to
finished. So the document reads as a map rather than a pitch.

| Page | Carries |
|---|---|
| 1 | Cover. "A home worthy of the house", the Quintessence at 19mm. No image |
| 2 | What this is. Why a paper like this arrives late, and on purpose |
| 3 | What was built. The inventory on the ink field: 12 pages, five ministries, four rails |
| 4 | The commission. What comes with it, $7,500, the terms, what the church owns |
| 5 | How this finishes. The last details, the keys, the move, the handoff |

## What changed at revision 2

- **No image on the cover.** The threshold plate is gone and the title block
  drops to sit nearer the centre of the sheet.
- **The diagnosis page is gone, and so is the price of no.** The client has
  lived the problem and already came to us to solve it, so arguing the pain back
  at them reads as a sales document rather than a record. Six pages became five.
- **The tile numerals are retired** and each tile name now sits level with its
  facet. That returned a whole row to every tile, and the tiles are taller than
  the template default so the extra height reads as air rather than a void
  beneath the row. The facets are identical across the three, because these are
  peers and the nested version implied a ranking.
- **Plain language throughout**, pitched at a ninth-grade reading level. Short
  sentences, common words, no industry vocabulary. The house punctuation rules
  still bind, so the register is plain but not casual.

## The statement

One page. Total $7,500.00, with $3,750.00 due now to begin and $3,750.00 at
handoff, matching the terms printed on page 4 of the proposal.

- **Zelle is the preferred rail**, to 470-556-3989, referencing FP-2026-002.
  That is the personal number from the Notion contact card, set by operator
  ruling of 2026-07-30. The 678-557-9692 number on FP-2026-001 was wrong and
  should not be carried into any future statement.
- **Stripe is named as the alternative** for card and bank transfer, with no
  live payment link. Nothing was created in the Stripe account.
- Numbering follows FP-2026-001, the Renegade Golf statement of 15 July 2026.
- The issuer block, the terms format and the creed carry over from that
  statement. Its Fraunces and Emerald design does not; this one is rebuilt on
  the current system.

## Verified 2026-07-30

- Proposal: all five sheets clear the overflow gate at zero pixels.
- Statement: one sheet, clear at zero pixels.
- Both pass the house punctuation gate clean on the rendered text.
- Page count taken from the repository, not the prior draft: 12 `page.tsx`
  routes, so both documents say 12.

## Confirm before sending

- FP-2026-002 assumes FP-2026-001 was the only statement issued this year.
- The proposal names strongtowercm.org as the destination while the site still
  serves from the Vercel preview. Page 5 makes the move a step, so this is
  correct as written.
