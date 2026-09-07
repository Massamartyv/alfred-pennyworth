# The Counting House

The personal finance instrument. Where the money is reckoned, monthly, without flattery. Net worth and its trajectory live in `wealth-trajectory.md`; this file governs the machinery that feeds it and the discipline that keeps it honest. Personal scope.

- Schema, formulas and the dashboard layout: `Automations/Counting House/notion-build-spec.md`.
- Live figures: Notion personal workspace, Finance Manager. Nothing numeric lives in this file.
- Supersedes the Finance Dashboard automation deleted 2026-08-11 in the Domesday truth pass.

---

## Why the last one was deleted

The prior artefact was a static HTML page rendered by hand. Its diagnosis was genuinely good – it identified the feast/famine cycle, the lifestyle gap, the business bleed, the untracked categories and the buffer fix, and it named them well. But it could not stay true. The moment it was rendered it began to age, and a dashboard that ages silently is worse than no dashboard, because it converts a known unknown into a false certainty.

The lesson is structural, not cosmetic. **An instrument must compute its numbers, never store them.** Every figure in the Counting House is a rollup or a formula over the ledger. There is no cell where a number can be typed and then quietly become wrong. That is the entire architectural constraint, and every other decision follows from it.

---

## The discipline

Munger's method, reduced to what actually operates here. Four moves, in order of how much they earn.

**Invert.** Do not ask what would make you wealthy. Ask what would reliably keep you broke, then refuse to do those things. The answer was already in the operator's own data – money arriving in lumps with no allocation step, fees paid for the privilege of a low balance, business costs on a personal card, and roughly a fifth of spending in categories that appeared in no system at all. The dashboard therefore opens with tripwires, not totals. What would ruin you goes above the fold; what would enrich you goes below it.

**Structure over discipline.** Willpower is a depreciating asset and a poor place to store a plan. Every fix in this instrument is a structural change that removes a decision rather than a resolution that requires one. The buffer is not a goal, it is a floor that other money is topped to first. Discretionary spending is not a budget line to be respected, it is the residual after five prior claims. The system is built to work on a bad week.

**Opportunity cost is the real price.** Nothing costs what it costs; it costs what the money would have become. Every category and every subscription carries a ten-year compounded column for this reason. A $60 monthly habit is not sixty dollars, it is roughly $10,400 over a decade at 8%. This is the column that changes behaviour, because it is the only one that states the price in the currency of the North Star.

**Simplicity, and the courage to leave things out.** Five tables and seven tripwires. The instrument is deliberately smaller than the operator's appetite for building it, because a finance system that becomes a project stops being a finance system. Completeness is not the goal – closing the month is the goal.

---

## The one structural fix

The diagnosis found no allocation step between receiving and spending. Everything else – the overdrafts, the fees, the negative periods – is downstream of that single missing gate. So the gate is the intervention, and it is performed on arrival rather than at month end:

**Floor, nut, reserve, stack, engine, discretionary.** In that order, every time money lands.

Discretionary is the residual, never the default. That inversion is the whole design, and if only one thing from this build survives, it should be this one.

The claims are ordered by consequence of failure rather than by size. Overhead was a single claim until the Williamsburg move and is now two, because rent and a design subscription fail differently: missing the stack costs a tool, missing the nut costs the apartment. They must not compete for the same dollar.

---

## Housing, and what the move changes

Rent arrives in this system on 2026-09 with the move to Kent Avenue in Williamsburg. It is not an adjusted figure – it is a new one. The prior audit categorised 28 months of spending across subscriptions, food, transport, Apple Cash, travel, card payments and a long tail, and carried no housing line anywhere. Nothing in the architecture has ever had to clear a fixed monthly obligation with a date on it.

That is a different risk profile, not a larger version of the same one. Income that arrives in lumps against spending that is also lumpy produces uncomfortable months. Income that arrives in lumps against an obligation due on the first produces a cliff. The buffer and the allocation step were valuable before the move; after it they are load-bearing, and the instrument gains a tripwire that goes red whenever next month's nut is not already set aside.

The honest reading is that the ledger's own diagnosis – roughly half of periods ending at or below zero – was recorded under conditions without a rent obligation. The move raises the floor the system has to clear before anything else is true. Every figure in the ladder and the engine should be reread with that in mind.

---

## Standing rules

**Separation is absolute.** Personal and venture money never mix. Venture figures are read from venture workspaces; the only venture money that appears here is a distribution after it has landed in a personal account. This extends the plugin-routing boundary to the ledger.

**Nothing untracked.** A category that cannot be seen compounds against you at full speed and cannot be argued with. Any spending that has no category is a defect, and the uncategorised queue reaching zero is a condition of closing the month.

**The month closes, or the gap shows.** An unclosed month is left visibly open rather than quietly skipped. The alarm is the absence, which is the only alarm that survives inattention.

**Done is defined.** The build is finished when the tripwires render, the untracked categories are catching transactions, and a close fits inside one pomodoro. Refinement past that point is procrastination wearing the costume of rigour.

---

## The revenue ladder

Carried forward from the prior artefact as authored, at the 40% owner distribution rate held in the Five Points Finance department file. It converts business performance into personal outcome and gives each rung a meaning.

| Monthly Recurring Revenue | Take-home at 40% | What the rung unlocks |
|---|---|---|
| $5,000 | $2,000 | Break-even. No overdrafts once the floor is set. |
| $7,000 | $2,800 | First surplus tranche routes to the contribution engine. |
| $10,000 | $4,000 | Saving and investing begin. S-Corp election triggers. |
| $15,000 | $6,000 | Wealth building proper. |
| $25,000 | $10,000 | Engine at full draw. The trajectory instrument starts moving. |
| $50,000 | $20,000 | Operating leverage proven; the model is ready to replicate. |
| $100,000 | $40,000 | The curve steepens past a single operator's ceiling. |
| $1,000,000+ | $400,000+ | Enterprise value becomes the metric, not monthly draw. |

**A correction the ladder needs.** It is a projection, not a position. It distributes 40% of net revenue from an entity whose account history showed roughly 70% of deposits arriving as transfers from personal – the business subsidised by the operator rather than the reverse. Until that direction flips, every rung is a forecast. The rung that matters is not on the table: it is the first month the business funds itself without a personal transfer. That is the real first threshold, and the Counting House should show it plainly when it arrives.

---

## Cadence

| Trigger | Action |
|---|---|
| On every deposit | Run the allocation step before spending against it |
| Weekly – Sunday | Reconcile, clear the uncategorised queue, read the tripwires |
| First of the month | Close the prior month, review the stack, cull one thing |
| First of each quarter | Read position against the wealth-trajectory benchmarks |
| Annual | Benchmark refresh per `benchmark-ledger.md` |

---

## Maintenance

- Housing entered the ledger with the 2026-09 move. The nut is load-bearing; treat it as its own claim, never as a line inside overhead.
- The opportunity-cost multiplier assumes 8% real over ten years. It appears in two formulas in the build spec; revise both together if the assumption changes.
- Figures from the deleted HTML artefact are diagnosis only. They are never entered as values – the instrument re-derives them, and where the two disagree the instrument wins.
- When the business account first funds itself without a personal transfer, record the month and retire the correction note above.

*Last updated: 2026-09-07 – founded, then amended the same day for the Williamsburg move: housing recorded as a new category rather than a changed one, the nut split out as its own claim in the allocation step.*
