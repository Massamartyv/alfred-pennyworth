---
file_type: reference
document_type: design_tokens
scope: cross-venture
last_updated: 2026-09-10
source: Extracted from retired alfred-os/ BabylonJS scene on 2026-04-23; remapped to the nine departments 2026-09-10
---

# Department Colours

The canonical colour palette for the nine departments. The original seven colours were extracted from the retired `alfred-os/` visualisation (BabylonJS Pokémon-world scene), where each studio was represented as a Pokémon-type colour. This is the design-token reference for any UI work that surfaces department activity – dashboards, monitoring displays, briefing visuals.

Applies across every venture (Five Points, Atlas, Martywood, Paradigm, Lillie and Lynette, and any future addition) because the nine-department model is cross-venture.

---

## Palette

| Department | Hex | RGB (0–255) | Normalised (0.0–1.0) | Visual Feel | Provenance |
|---|---|---|---|---|---|
| Foundation | `#84CC16` | 132, 204, 22 | 0.52, 0.80, 0.09 | Lime. Community, giving, rootedness. | Recommendation, 2026-04-23 |
| Administration | `#D3A673` | 211, 166, 115 | 0.83, 0.65, 0.45 | Tan. Structure, paper, foundation. | Source scene |
| Finances | `#05B5D4` | 5, 181, 212 | 0.02, 0.71, 0.83 | Cyan. Cool, liquidity, numbers. | Source scene, from Finance |
| Business Development | `#21C55E` | 33, 196, 94 | 0.13, 0.77, 0.37 | Green. Pipeline, expansion, life. | Source scene, from Growth |
| Marketing & Sales | `#FF6B36` | 255, 107, 54 | 1.00, 0.42, 0.21 | Burnt orange. Heat, expression, output energy. | Source scene, from Creative |
| Operations | `#EBB208` | 235, 178, 8 | 0.92, 0.70, 0.03 | Amber. Throughput, delivery, motion. | Source scene |
| Product Development | `#A854F7` | 168, 84, 247 | 0.66, 0.33, 0.97 | Violet. Thinking, depth, the offer made. | Source scene, from Strategy |
| Human Resources | `#F472B6` | 244, 114, 182 | 0.96, 0.45, 0.71 | Rose. People, warmth, culture. | Recommendation, 2026-09-10 |
| Knowledge Base | `#6B7280` | 107, 114, 128 | 0.42, 0.45, 0.50 | Graphite grey. Library, reference. | Recommendation, 2026-04-23 |

**Default (unmatched / fallback):** `#A8A88F` – 168, 168, 143 – muted olive-grey for anything that does not cleanly map to a department.

**Retired:** Production slate `#94A3B8` – 148, 163, 184. Production folded into Operations and Product Development on 2026-09-10; the colour is held here should a design pass want it back.

Colours marked as recommendations were not extracted from the source scene. Adjust them if a design pass revisits the palette.

---

## Variant Derivations

For UI states that need depth (hover, active, disabled, darkened):

- **Dark (60%)**: multiply each RGB channel by 0.6. Used for backgrounds in the original scene.
- **Light (tint)**: blend with white at 20–40%. Used for subtle backgrounds or inactive states.

The original scene used the dark variant for base-colour backgrounds and the full variant for accents and particle FX.

---

## Usage Notes

- These colours are a design-token reference, not a strict brand palette. Ventures still carry their own brand colours for external-facing work (Five Points, Martywood have their own fingerprints).
- When an internal dashboard or briefing needs to distinguish departments at a glance, this palette is the default.
- The colours are deliberately high-contrast against each other so multi-department activity reads clearly. Graphite and the olive-grey fallback sit closest; pair Knowledge Base with a label wherever the two could meet.

---

*This palette is preserved because the finished creative work of selecting and pairing distinct colours took real effort. The `alfred-os/` visualisation that originated it has been retired, but the colour system itself survives as a reusable reference. Renamed from `studio-colours.md` at The Restoration, 2026-09-10.*
