# Five Points renovation ledger

Rulings taken in the brand renovation.

**Reconciled 2026-09-08.** Five entries written to the Five Points Decision Log,
and `Foundation/brand-fingerprint.md` amended to version 3.5 - the rosette becomes
the Quintessence, and the field and the screen enter Layer 2. This file is now the
working record behind those entries rather than a pending queue.

One condition stands: the trademark knockout on the rosette has not been run, and
the amendment says so. Do not treat the mark as cleared until it is.

## Ruled

| Date | Ruling |
|---|---|
| 2026-09-07 | Concept: The Porch. Trades are the first wing. Magician leads. |
| 2026-09-07 | Tagline: "We bring the city to your door." |
| 2026-09-07 | Essence: "Connecting passion to possibility". Never printed. |
| 2026-09-07 | Fifth value: Hospitality. |
| 2026-09-07 | Journey: five moments, no ceremony, calls only. |
| 2026-09-07 | Name story v2 stands. Creativity of the neighbourhood is the focus, not its defiance. Auburn named and footnoted. |
| 2026-09-08 | **The mark is the rosette.** The crystal is retired as a mark. Its geometry survives as the source of the pattern pieces. |
| 2026-09-08 | Mark ladder collapses to two tiers: rosette down to 20px, pentagon core alone below. |
| 2026-09-08 | Field kit: the Rule stands. The Crop and the Arc are dead. |
| 2026-09-08 | The Overlap is centred and tiles, at two scales: a seamless repeat for large fills, the single centred motif for small surfaces. |
| 2026-09-08 | The Drift is redrawn on rotation and rhythm. |
| 2026-09-08 | Two new fields to be brought for the vacated slots, built on rhythm rather than gesture. |
| 2026-09-08 | **Field kit ruled: five fields.** The Trefoil motif, the Trefoil seamless repeat, the Rule, the Descent, Tumbling Air. The Measure is out. |
| 2026-09-08 | The Rule scaled 200%: leaves, spacing and wavelength all doubled, so it is a true zoom rather than bigger leaves on the old spacing. Wave reading is deliberate - a natural pattern invoked in a technological space. |
| 2026-09-08 | Halftone screen built: the dot is the mark. Core in the working range, rosette in the highlights, sized from measured ink. |
| 2026-09-08 | **Screen ruled:** house ruling 88 marks across the image width, resolution-independent. Every photograph in the documentation is screened. |
| 2026-09-08 | **Design system extracted** to its own package: `Apps/quintessence`, `@fivepoints/quintessence`. Real exports, tsc build. Geometry port verified byte-identical to the ruled drawing. |
| 2026-09-08 | Ruled: build a proper library first, port the rosette, then sync to Claude Design. |
| 2026-09-08 | Token contract moved out of the site into the package. `globals.css` 685 lines to 301; the site imports the package. One owner. |
| 2026-09-08 | Primitives moved into the package, decoupled from Next via `as` props, CSS modules replaced by named `q-` classes. |
| 2026-09-08 | **The crystal is out of live code.** `QuintessenceMark` renders the rosette (QT-002). Its geometry survives for FacetPlate, per the ruling. |
| 2026-09-08 | **Synced to Claude Design.** 13 components, 45 graded preview cells, into the existing Five Points project - superseding the hand-authored QT-001 system on the operator's ruling. 94 files deleted. |
| 2026-09-08 | **The Rule is cut.** Field kit stands at four: the Trefoil motif, the Trefoil repeat, Tumbling Air, the Descent. Dividers are plain hairlines. |
| 2026-09-10 | **Coral carries every context-free surface.** Operator-ruled after the alternatives were put to him. The tab icon, the home-screen icon, the Organization logo a search engine fetches and the header's hover bloom all take the lead voice, coral, because none of them stands on a surface with a voice to lend. Previously a derivation made in passing; now a ruling. |
| 2026-09-09 | **The icon set is rebuilt on the rosette.** `generate-icons.mjs` had derived from QT-001 and pinned its palette as literals, so the favicon was the last live surface carrying the retired crystal and the retired seal. It now imports geometry and colour from `@fivepoints/quintessence` and declares neither a coordinate nor a hex, which removes the drift class rather than the drift. The mark takes the lead voice. The dark-scheme core rule retired with the seal's inversion law - the core is now the voice, legible on any chrome. |
| 2026-09-09 | **The tier rule is overridden for the icon set, and only there.** `MICRO_THRESHOLD_PX` sends the mark below 20px to the core alone. Rendered and compared at 16px before ruling: the micro tier reads as a plain coral dot with no five-fold structure, the rosette holds five petals about a centre. Every icon frame is the rosette. The threshold stands unchanged for the component, which is drawn live rather than rasterised. |
| 2026-09-09 | **The five-voice seal is retired and Section 0.1 rule 3 with it.** The mark takes the voice of the surface it stands on, in two grades, alternating around the rosette - an instance of the one-voice law rather than its single exception. `mode="seal"` deleted. Accepted costs: no surface now carries all five hues, so the brand no longer renders its own name; the favicon and share card take the lead voice, coral, by derivation. |
| 2026-09-09 | **The masthead gains a visible wordmark.** "Five Points Digital Studio" beside the mark, the descriptor dropping below 30rem. The header had been mark-only since the Quintessence pass. |
| 2026-09-09 | **The ratified voices restored to the primary token names.** The families had each been renamed one rung darker at the extraction, so the mark painted contrast derivatives - the sun voice rendering as #695804, an olive-brown. Verified by resolving all five voices in both registers before and after: 70 of 110 values byte-identical, no accent, rule, tint, wash or error token among those that moved. |
| 2026-09-09 | **The no-gradient law stands unamended.** Three gradient treatments of the five-voice mark - Aurora, Sweep, Prism - were drawn, specimened on the workbench and cut. DESIGN_SYSTEM.md Section 0.1 rule 4 forbids gradient anywhere in the world including the mark, and three further rulings are reasoned from it: the header hover crossfade, the logo river's hard crop, and the diagram laws. The flat five-voice seal remains the identity's full-colour rendering. |
| 2026-09-09 | The masthead keeps the flat seal. The header pair - ink at rest, seal on hover at 32px with seam compensation 1.4 and 1.2 - is unchanged. |
| 2026-09-09 | **The workbench is the proving ground.** `src/app/workbench` in the site: every primitive, field and mark, every state, both registers. Noindexed, no shell, linked from nowhere. Rule: nothing reaches a public route before it has been seen there. |
| 2026-09-09 | Field kit application to the site is deferred by operator ruling - features and interface first, decorative surfaces after. |
| 2026-09-09 | **The mark's colour law moves into the package.** `Quintessence` gains `mode` - ink, voice, seal - and `seamCompensation`; the law itself lives in `colour-law.ts` and the site's animated rendering imports it rather than keeping a second copy. The design system now carries the identity's full-colour mark; before this it carried only the monotone one. |
| 2026-09-09 | **The data-voice contract is implemented where it is declared.** `tokens.css` described the contract but the five `[data-voice]` blocks lived in the site's `globals.css`, so the package shipped a contract it could not honour - a consumer importing the tokens alone got the `--voice` fallback for all five voices. Moved into the package; the site keeps a comment warning against re-declaring them. Caught by the design system's own voice-mode specimen, which rendered five cards in one identical olive. |
| 2026-09-09 | Claude Design re-synced: 14 files, Quintessence re-captured and re-graded, Sheet and the shared bundle re-uploaded. Both known render warns unchanged - `FONT_MISSING` for PP Neue Montreal and `RENDER_THIN` for TrefoilField - and no new warns. |
| 2026-09-09 | **The seal's core inverts with the register.** `QuintessenceMark` pinned the seal core to `--ink-900`, so on any ink-register surface the core vanished into the ground and the mark read as five detached petals around a void. Now `--surface-inverse`: obsidian on light, parchment on dark, which DESIGN_SYSTEM.md Section 12.1 already states as the mark's law and which `icon.svg` had honoured since the icon build. Caught by the workbench on its first day. |

## Open

- **`globals.css` still declares 52 custom properties and its own
  `[data-register="ink"]` block, which `tokens.css` also declares.** The
  8 September extraction was not complete. `globals.css` is imported after
  the package tokens, so the site runs on its own copy wherever the two
  overlap - which means the design system and the site can disagree without
  anything failing. Wants a proper reconciliation pass, not a guess.
- **The icon set still ships the retired crystal.** `scripts/generate-icons.mjs`
  is written for QT-001 and derives from the site's own geometry module, not
  the package. `public/marks/logo.svg` is a crystal asset. The favicon is a
  visible surface carrying a mark the ruling retired on 8 September.
- Trademark knockout on the rosette before anything is written to the fingerprint.
- Trades photography. The binding constraint on the screen; the library is four AI stock frames, two watermarked, none of the trades.
- Kitchen bench: pillar systems, names, prices, guarantees.
- Sales-room deck and proposal deck, both unbuilt.
- Copy transcript from the operator, to make both decks reflect the pains solved.

## Implementation state

- `lib.js` markPath flipped to the two-tier ladder; every consumer routes through
  `mark()` so the whole system follows.
- `marks.py` now emits `mark-primary-{ink,bone}.png` (the rosette).
- `ruled.py` is the canonical ruled system - four fields and the screen. Anything a
  deck draws, it draws from there.
- `assets.py` generates every field and screened asset both decks consume.
- All five mark plates redrawn for the rosette; the ladder plate now shows two tiers.
- Identity book REBUILT: 42 pages. New section 6.0 The Field (four pages), Application
  renumbered to 7.0, mark copy rewritten off the crystal, photography section rebuilt
  on screened imagery.
- Capabilities deck NOT yet rebuilt. The remaining open item.
- `Apps/quintessence` is the design system: mark, four fields, seven primitives,
  the token contract and the type suite. Built, committed, synced.
- The screen stays a build-time image treatment and is deliberately not a
  component; it belongs in a tooling package.
