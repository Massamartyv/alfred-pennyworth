# Suite Two skill selection - blast radius, not fire frequency

The operation brief requires the three additions beyond the two migrated skills to be
justified "on blast radius, not on guesswork about fire frequency, because no telemetry
exists yet to know which skills fire most." That telemetry - the skill-fire ledger - is
Whetstone slate item 3, a separate dispatch not yet built (see the handoff for the
dependency note). Selection here runs on a different axis entirely: what does a wrong
routing decision cost, independent of how often the skill is invoked.

The two migrated skills anchor two ends of a spectrum already: `ui-ux-pro-max` writes
nothing external (a misroute costs a wasted design pass, nothing more), and
`journey-planner` writes Notion project state gated behind an explicit Preview step. The
three additions were chosen to cover the blast-radius territory those two do not:

| Skill | Write surface / domain | Cost of a false trigger | Cost of a false skip |
|---|---|---|---|
| `offer-creator` | Live Stripe writes (`mcp__stripe-fivepoints__stripe_api_write`) | A malformed or premature offer enters the pricing system | Pricing work drifts unstructured, off the Hormozi discipline |
| `switchboard` | Live Five Points CRM + active dialling queue | Prospect writes misfire mid-pipeline, corrupting the ladder position | A call runs with no brief and no logged outcome - the flywheel's single source of truth breaks |
| `therapist` | No external write; personal-scope sensitive interior-work domain | An uninvited crossing into psychologically loaded territory | Emotional processing that should have been held goes unattended |

`offer-creator` and `switchboard` are the only two skills in the full 32-skill roster wired
to a live, non-Notion external write inside the sample considered (Stripe and the Five
Points CRM respectively) - both were read during selection alongside `email-copy`,
`sales-copy` and `social-copy`, which are external-facing but sit behind Navigation Rule
3's send-confirmation gate, which buffers their blast radius relative to a skill that
writes directly on trigger. `therapist` was chosen over `dr-thompkins` as the sensitive-
domain representative because it carries no external write at all (Fullscript and Strava
tools on `dr-thompkins` are read-only) - it is the cleanest instance of "the harm is in the
register, not the artifact," which is a distinct failure mode from a write mistake and
worth its own coverage rather than a second write-surface skill.

This selection is provisional by the brief's own admission. Once the fire-frequency
telemetry exists, the honest move is to re-run this selection against actual fire counts
and see whether blast radius and frequency point the same direction - they may not.
