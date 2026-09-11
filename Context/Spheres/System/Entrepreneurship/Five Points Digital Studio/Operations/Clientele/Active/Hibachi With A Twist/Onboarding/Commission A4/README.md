# Hibachi With A Twist - A Five Points Commission

Two documents, sent together. Both A4, both on the Quintessence design system,
both in the coral voice.

- `proposal.html` - five pages. What was built, what comes with it, what it
  costs and how the last steps run.
- `statement.html` - one page. Statement FP-2026-003, the money.

An instance of `Marketing & Sales/Proposal Templates/Commissioning Proposal A4/`. Read that
README for the system rules and the render pipeline.

**Status is not recorded here.** Whether these have been signed, sent or paid
lives in the Five Points Notion workspace.

## The commercial shape

| | |
|---|---|
| Commission | $7,000 |
| Due | $3,500 on receipt to commission; $3,500 balance at go-live |
| Method | Zelle to 470-556-3989, note FP-2026-003 |

Two bodies of work, the website and the staff portal, settled as one commission
at the standard rate. Both are named on both documents so the client can see
what the figure covers.

**Operator ruling of 12 August 2026, superseding the ruling of 31 July.** The
earlier draft carried a 50% returning-client reduction to $3,750. It was
withdrawn because the scope grew by an entire auth-backed scheduling portal
after the reduction was struck, and the portal is folded into the full price
rather than invoiced separately. The documents were never sent and the client
never saw the earlier figure, so nothing was retracted. The returning-client
reduction remains available as a studio instrument; it was not applied here.

**Operator ruling of 16 August 2026: settlement staged 50/50.** Half on receipt
commissions the work; the balance falls due at go-live, and the domain cutover
happens the day it arrives. The staging is the concession already given.

**Operator ruling of 16 August 2026, late evening: commission set at $7,000,**
matching the 2022 engagement level and its shape ($3,500 up front, $3,500 on
completion). The client disputes the 2022 figure ($1,700 by her recollection);
the price stands on the 2026 scope regardless. Negotiation opens and holds at
$7,000. A $3,500 walk-away floor exists as an operator-only contingency, never
pre-offered.

The statement is dated the day it is issued. If the send slips past 16 August
2026, change the date and re-run the build and the gate before it goes.

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

```bash
uv run --with playwright python gate.py --src statement.html
```

Run the gate against both before either goes anywhere. Proofs are namespaced by
document under `proof/`.

## Notes on this instance

The statement runs tight against the A4 sheet. The build gate refused three
times before the copy came down far enough, and the payment note is one
paragraph rather than two for that reason. Adding a line anywhere above the
footer will clip it again, so re-run the build after any edit.

Voice is coral, which is both the studio default and the nearest of the five to
the rosewood the kitchen already uses. Do not substitute the client brand red
into the document; the surface belongs to the studio.
