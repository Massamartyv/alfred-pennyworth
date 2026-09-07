# The Counting House – Notion Build Spec

The executable schema for the personal Finance Manager. Five databases and one dashboard page, built in the Notion personal workspace. This file is the build instruction; `Context/Spheres/System/Personal Finance/counting-house.md` is the doctrine it serves.

**Scope:** Personal. The separation rule holds – venture money is read through venture workspaces and never enters these tables except as a distribution landing in a personal account.

**Provenance:** supersedes `Automations/Finance Dashboard/`, deleted 2026-08-11 in the Domesday truth pass. That artefact was a hand-rendered HTML snapshot with no live wiring; its diagnosis was sound and is carried forward, its figures are not. Every number below is a slot the instrument computes, never a value typed in.

---

## Definition of done

The build is finished – not iterated further – when all five conditions hold:

1. The five databases exist with the properties in this spec.
2. The previously untracked categories are seeded and receiving transactions, housing among them.
3. Every account carries a Minimum Floor and a Last Reconciled date.
4. The dashboard page renders the seven tripwires above the fold.
5. A monthly close takes under 25 minutes end to end – one pomodoro.

Anything beyond this is decoration and is explicitly out of scope. The instrument earns its keep by being closed every month, not by being beautiful.

---

## Database 1 – Accounts

The balance-sheet primitives. Referenced in `wealth-trajectory.md` as the Account Manager; that name is retired in favour of Accounts.

| Property | Type | Definition |
|---|---|---|
| Account | Title | Institution and product, e.g. "Chase Total Checking" |
| Institution | Text | Bank or custodian |
| Type | Select | Checking, Savings, Credit, Investment, Loan, Cash |
| Scope | Select | Personal, Five Points, Marty Gras, Paradigm, Lillie and Lynette, Atlas |
| Balance | Number, dollar | Last reconciled balance, entered positive for all types |
| Signed Balance | Formula | Liabilities carried negative so net worth is one sum |
| Counts Toward Net Worth | Checkbox | Default checked; unchecked for pass-through accounts |
| Minimum Floor | Number, dollar | The untouchable balance for this account |
| Floor Breach | Formula | Tripwire 1 feed |
| Fee Waiver Minimum | Number, dollar | Balance at which the account stops charging a service fee |
| Fee Exposure | Formula | Whether the account is currently paying an avoidable fee |
| Last Reconciled | Date | Set on every reconciliation |
| Stale | Formula | Tripwire 7 feed – true past 14 days |
| Transactions | Relation | → Transactions |

**Formulas.**

```
Signed Balance
if(prop("Type") == "Credit" or prop("Type") == "Loan", -abs(prop("Balance")), prop("Balance"))

Floor Breach
if(prop("Minimum Floor") > 0 and prop("Balance") < prop("Minimum Floor"), "⚠ Below floor", "✓ Intact")

Fee Exposure
if(prop("Fee Waiver Minimum") > 0 and prop("Balance") < prop("Fee Waiver Minimum"), "⚠ Paying to be poor", "✓ Waived")

Stale
dateBetween(now(), prop("Last Reconciled"), "days") > 14
```

**Views.** Net Worth (grouped by Type, sum of Signed Balance) · Floors (filtered to breaches) · Reconciliation Queue (sorted by Last Reconciled ascending).

---

## Database 2 – Transactions

The atomic ledger. Everything else is a rollup of this table.

| Property | Type | Definition |
|---|---|---|
| Description | Title | As it appears on the statement |
| Date | Date | Transaction date, not posting date |
| Amount | Number, dollar | Negative for outflow, positive for inflow |
| Account | Relation | → Accounts |
| Category | Relation | → Categories |
| Direction | Formula | Inflow or Outflow |
| Is Fee | Checkbox | Any bank fee, overdraft, interest charge or late penalty |
| Account Scope | Rollup | Scope, via Account |
| Category Kind | Rollup | Kind, via Category |
| Misrouted | Formula | Tripwire 4 feed – business spend sitting on a personal account |
| Month | Formula | YYYY-MM, the join key to Monthly Close |
| Sphere | Relation | → Sphere Manager, per the relational-backbone rule |

**Formulas.**

```
Direction
if(prop("Amount") >= 0, "Inflow", "Outflow")

Misrouted
prop("Category Kind") == "Business" and prop("Account Scope") == "Personal"

Month
formatDate(prop("Date"), "YYYY-MM")
```

**Views.** This Month · Uncategorised (Category is empty – the queue that must reach zero at close) · Misrouted · Fees · By Category.

---

## Database 3 – Categories

Where the invisible money becomes visible. The seeded untracked categories are the point of this table.

| Property | Type | Definition |
|---|---|---|
| Category | Title | |
| Kind | Select | Fixed, Variable, Discretionary, Business, Transfer, Income, Fee |
| Previously Untracked | Checkbox | Honesty column – was this invisible before the Counting House? |
| Monthly Target | Number, dollar | Zero means untargeted, not unlimited |
| Actual This Month | Rollup | Sum of Amount from Transactions, filtered to current month |
| Variance | Formula | Target minus actual |
| Annualised | Formula | Actual × 12 |
| Ten-Year Opportunity Cost | Formula | What this category costs if the money compounded instead |

**Formulas.**

```
Variance
prop("Monthly Target") - abs(prop("Actual This Month"))

Annualised
abs(prop("Actual This Month")) * 12

Ten-Year Opportunity Cost
round(prop("Annualised") * 14.4866)
```

The 14.4866 multiplier is the future value of a ten-year annuity at 8% – `((1.08^10) - 1) / 0.08`. It converts a monthly habit into the number it actually costs. This is the single most useful column in the build: it is what turns an abstraction into a decision.

**Seed rows – the ones that were tracked nowhere.** Housing leads the list: the prior audit of 28 months carried no housing line at all, so rent enters this system as a new category rather than a changed one.

| Category | Kind | Previously Untracked |
|---|---|---|
| Housing – Rent | Fixed | ✓ – no housing line existed in the prior audit |
| Housing – Utilities and Internet | Fixed | ✓ – as above |
| Housing – Renter's Insurance | Fixed | ✓ – as above |
| Apple Cash and Cash App Sends | Discretionary | ✓ |
| Uber Rides and Eats | Variable | ✓ |
| Food – Groceries and Dining | Variable | ✓ |
| Travel | Variable | ✓ |

Seed the remainder as they appear. Do not pre-build a taxonomy – categories earn their existence by catching a real transaction.

---

## Database 4 – Recurring

The subscription stack. Built to be culled, not admired.

| Property | Type | Definition |
|---|---|---|
| Service | Title | |
| Amount | Number, dollar | As charged |
| Cadence | Select | Monthly, Quarterly, Annual |
| Monthly Equivalent | Formula | Normalised for comparison |
| Annual Cost | Formula | Monthly equivalent × 12 |
| Ten-Year Cost | Formula | Compounded opportunity cost |
| Scope | Select | Personal, or the owning venture |
| Account Charged | Relation | → Accounts |
| Misrouted | Formula | Venture tool billed to a personal account |
| Started | Date | |
| Last Used | Date | Updated on the monthly review, honestly |
| Verdict | Select | Keep, Kill, Downgrade, Undecided |
| Zombie | Formula | Unused past 60 days and still undecided |

**Formulas.**

```
Monthly Equivalent
if(prop("Cadence") == "Annual", prop("Amount") / 12,
  if(prop("Cadence") == "Quarterly", prop("Amount") / 3, prop("Amount")))

Annual Cost
prop("Monthly Equivalent") * 12

Ten-Year Cost
round(prop("Annual Cost") * 14.4866)

Misrouted
prop("Scope") != "Personal" and prop("Account Charged").map(current.prop("Scope")).includes("Personal")

Zombie
dateBetween(now(), prop("Last Used"), "days") > 60 and prop("Verdict") == "Undecided"
```

**Views.** The Stack (sorted by Ten-Year Cost descending – the cull order) · Zombies · Misrouted · Kill List.

---

## Database 5 – Monthly Close

One row per month. This table is what makes the instrument maintained rather than merely built – an unclosed month is a visible gap, and the gap is the alarm.

| Property | Type | Definition |
|---|---|---|
| Month | Title | YYYY-MM |
| Period | Date | First to last of the month |
| Opening Net Worth | Number, dollar | Carried from prior close |
| Closing Net Worth | Number, dollar | Sum of Signed Balance at close |
| Delta | Formula | The only number that matters over time |
| Income | Rollup | Sum of inflows |
| Spend | Rollup | Sum of outflows |
| Retained | Formula | Income minus spend |
| Retention Rate | Formula | Retained as a share of income |
| Fees Burned | Rollup | Sum where Is Fee |
| Closing Liquid | Number, dollar | Checking and cash at close |
| Ended Negative | Formula | The feast/famine counter |
| Untracked Share | Formula | Share of spend in previously untracked categories |
| Nut | Number, dollar | Rent, utilities and insurance for the month |
| Nut Reserved | Checkbox | Next month's nut set aside in full |
| Nut Coverage | Formula | Closing liquid divided by the nut, in months |
| Allocation Performed | Checkbox | Was the allocation step run on every deposit this month |
| Closed | Checkbox | |
| Closed On | Date | |
| Note | Text | One line. What actually happened. |

**Formulas.**

```
Delta
prop("Closing Net Worth") - prop("Opening Net Worth")

Retained
prop("Income") - abs(prop("Spend"))

Retention Rate
if(prop("Income") > 0, prop("Retained") / prop("Income"), 0)

Ended Negative
prop("Closing Liquid") <= 0

Nut Coverage
if(prop("Nut") > 0, prop("Closing Liquid") / prop("Nut"), 0)
```

**Views.** Trailing 12 · Open Months (Closed unchecked – must never exceed one) · Negative Endings.

---

## The dashboard page

One page, six sections, in this order. The order is the argument: what would keep you broke comes before what would make you rich.

### I. The Tripwires

Seven binary states across the top, each green or red at a glance. No numbers, no nuance – a tripwire that requires interpretation is not a tripwire.

| # | Tripwire | Red when | Source |
|---|---|---|---|
| 1 | Buffer intact | Any account below its Minimum Floor | Accounts → Floor Breach |
| 2 | Nut reserved | Next month's rent and utilities not yet set aside in full | Monthly Close → Nut Reserved |
| 3 | No fees burned | Any fee this month | Monthly Close → Fees Burned > 0 |
| 4 | Nothing misrouted | Business spend on a personal account | Transactions → Misrouted |
| 5 | Everything visible | Uncategorised transactions outstanding | Transactions → Uncategorised |
| 6 | Allocation performed | A deposit landed without being split | Monthly Close → Allocation Performed |
| 7 | Books current | Any account unreconciled past 14 days | Accounts → Stale |

Tripwire 2 is new as of the Williamsburg move and is the one that changes the risk profile. Rent is the first obligation in this system with a hard date and a consequence that is not financial. It is reserved a month ahead or the tripwire is red.

### II. Position

Net worth as the sum of Signed Balance, and the percentile it buys. Alongside it, **months of nut covered** – liquid divided by the monthly nut. With a lease in place this is the honest runway figure and it replaces a general overhead runway. This section wires the slot that `wealth-trajectory.md` has been holding open – both frames, demographic and overall US, read against the benchmark table in that file. Also: liquid runway in months, and the trailing contribution rate against the engine.

### III. The Allocation Step

The structural fix, and the reason the rest exists. The diagnosis was that money arrives in lumps and disperses within days because no allocation step sits between receiving and spending. So the step is made explicit and is performed on arrival, not at month end:

1. **Floor** – top every account to its Minimum Floor before anything else moves.
2. **Nut** – next month's rent and utilities, reserved in full.
3. **Reserve** – tax and known irregulars.
4. **Stack** – the month's cullable recurring costs.
5. **Engine** – the contribution to the wealth trajectory.
6. **Discretionary** – what remains, and only what remains.

Discretionary is the residual, never the default. That single inversion is the whole design.

The claims are ordered by consequence of failure, not by size. Overhead was one claim before the move and is now two, because rent and Adobe fail differently: missing the stack costs a tool, missing the nut costs the apartment. They do not belong in the same bucket and must not compete for the same dollar.

### IV. The Stack

Recurring, sorted by Ten-Year Cost descending, with verdicts. Reviewed monthly. The cull is the exercise, not the inventory.

### V. The Gap

Overhead against revenue, and the threshold ladder – what each level of business MRR converts to at the 40% owner distribution. The ladder is carried forward from the prior artefact as the operator authored it, with one correction noted in the doctrine file: it is a projection, not a position.

### VI. The Month

The current Monthly Close row, the trailing 12, and the retention-rate trend.

---

## Cadence

| Trigger | Action | Ceiling |
|---|---|---|
| On every deposit | Run the allocation step before spending against it | 5 minutes |
| Weekly – Sunday, with the reconnection batch | Reconcile balances, clear the uncategorised queue, read the tripwires | 15 minutes |
| First of the month | Close the prior month, review the stack, cull one thing | 25 minutes |
| First of each quarter | Read position against the wealth-trajectory benchmarks | 15 minutes |
| Annual – September and late year | Benchmark refresh per `benchmark-ledger.md` | Per the ledger runbook |

---

## Build order

Build in this sequence; each step depends on the one above.

1. Categories – seed the four untracked, add Kind and the opportunity-cost formula.
2. Accounts – every account, with Minimum Floor and Fee Waiver Minimum set.
3. Transactions – relations to both, then import history.
4. Recurring – the stack, with Account Charged wired.
5. Monthly Close – open the current month.
6. The dashboard page – tripwires first, then the rest.

---

## Maintenance

- Figures inherited from the deleted HTML artefact are diagnosis only and are never entered as values. The instrument re-derives everything.
- The opportunity-cost multiplier assumes 8% real. Revise here if that assumption changes; it appears in two formulas.
- Housing entered the system with the Williamsburg move, 2026-09. It is the first hard-dated obligation this ledger has carried; treat the nut as load-bearing rather than as another category.
- Venture money enters only as a distribution landing in a personal account. If a venture figure is needed, read the venture workspace – never mirror it here.

*Last updated: 2026-09-07 – authored, then amended the same day for the Williamsburg move: housing seeded as a Fixed category, the nut split out of overhead as its own claim, tripwire 2 added, nut coverage added to Position and Monthly Close.*
