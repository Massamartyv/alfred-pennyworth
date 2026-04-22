# Finance Dashboard

Visual finance overview – revenue streams, expenses, projections, cash position.

## Current State

**Static HTML artefact.** `finance-dashboard.html` is a snapshot rendered by hand. Not connected to live data. Not scheduled. Not interactive.

## Target State

Automation build pending. The intent is to pull live data from:

- Personal Notion workspace – Finances database (income, expenses, subscriptions, transactions)
- Five Points Notion workspace – revenue tracking
- Stripe (Five Points) – invoices, MRR, payouts
- Bank account integrations (TBD)

And render a refreshed dashboard on a schedule (daily or weekly). The script would replace the current static HTML with a generated version that reflects live state.

## Scope

**Personal.** The dashboard spans both personal and business finances but is owned by the personal operator (Martavious) for visibility. Data isolation rules still apply – personal and Five Points data are read from separate sources and kept in separate sections of the output.

## Next Moves

1. Design the data model – what metrics, what time windows, what comparisons
2. Choose rendering path – static HTML regeneration, React SPA, or dedicated dashboard platform
3. Wire data sources – Notion MCP for both workspaces, Stripe MCP for Five Points
4. Schedule – cron or scheduled-tasks MCP for recurring runs
5. Notification – iMessage summary when thresholds are breached

Pending a dedicated build session.
