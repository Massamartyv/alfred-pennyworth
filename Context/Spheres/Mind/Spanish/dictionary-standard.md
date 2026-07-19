# Language Dictionary Standard

Governs how vocabulary enters every language bank in Notion. Spanish (Spanish Language Bank) is live; Japanese and Arabic inherit this standard when they activate. First application: the Spanish Language Bank under the Spanish Dictionary resource page.

---

## The entry unit: the lemma

One database row per lemma – the dictionary citation form. Never a row per inflected form.

| Word class | Citation form | Example |
|---|---|---|
| Verb | Infinitive | empezar, not empezamos |
| Noun | Singular | año, not años |
| Adjective | Masculine singular | movido, not movida |
| Phrase / idiom | Fixed form | ¿qué tal? |

If an irregular inflected form deserves its own attention (fue, tuve), it lives inside the lemma's page content or as a child page beneath it – never as a sibling row.

## Conjugations: child pages, not rows

Full conjugation material lives in child pages inside the verb's page:

- One child page per verb, titled `Conjugación – {verb}`
- Tables grouped by mood and tense, one toggle per tense
- Light starter (present tense only) may live directly in the page body until the child page is warranted

The existing `Conjugations` and `Root Word` self-relations remain for cross-linking the rare inflected form that earns its own card. The default is content, not rows.

## Universal core (every language bank)

| Property | Type | Rule |
|---|---|---|
| Word | Title | The lemma, capitalized |
| Type | Select | Word / Phrase / Phonetics |
| Part of Speech | Multi-select | In the target language (Verbo, Sustantivo...) |
| Translation | Text | Terse English gloss – the flashcard answer (empezar → "to begin"). Primary meaning field going forward |
| Definition | Text | Richer usage note – register, nuance, stem-change flags. Optional; use when the terse gloss is not enough |
| Example Sentence | Text | A real sentence from actual use – never invented after the fact |
| Comfort Level | Select | Unknown / Difficult / Hesitation / Easy / Known – set at capture from observed behavior, updated on review |
| Last Review | Date | Feeds the Next Review formula (spaced repetition) |

## Language layer (added per language, never shared)

| Language | Additional properties |
|---|---|
| Spanish (live) | Gender (Masculino/Femenino), Prefix (El/La/Los/Las) |
| Japanese (future) | Kanji, Kana, Romaji, Politeness register |
| Arabic (future) | Root (triliteral), Script, Transliteration |

A new language bank copies the universal core and adds only its layer. Nothing else.

## Capture rules

1. Batch at session end – never mid-conversation.
2. Dedupe on lemma before creating (query the bank first).
3. Example sentence comes from the conversation where the word surfaced.
4. Comfort Level reflects observed behavior at capture: asked about it = Difficult; newly introduced = Unknown; produced with effort = Hesitation.

## Resolved decisions (2026-07-08)

1. **Translation is a text field, not a relation.** A `Translation` text property was added to the Spanish Language Bank and is now the primary meaning field – terse, flashcard-ready. The legacy `English` relation to the separate English bank is deprecated: leave it empty on new entries. It doubled page count and slowed capture for no gain at this scale.
2. **No backfill batch job.** The 35 sparse 2023 entries are left as-is. Dedupe-on-lemma means a word resurfacing in a live session enriches its existing row rather than duplicating, so the bank heals organically through use. Accent pairs (Como/Cómo, Que/Qué) are distinct lemmas and stay as separate entries.

---

*Last updated: 2026-07-08 – v1.1, Translation field added and both open decisions resolved.*
