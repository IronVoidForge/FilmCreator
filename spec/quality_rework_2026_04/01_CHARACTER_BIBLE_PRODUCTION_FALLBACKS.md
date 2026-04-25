# Character Bible Production Fallbacks

## Target files

- `orchestrator/character_bible.py`
- `orchestrator/character_bible_models.py` (or equivalent bible dataclass/model file)
- `tests/test_character_bible_production_fallbacks.py`

## Problem

Some character bibles remain visually unusable because strict evidence synthesis returns many `unknown` values.

Examples already observed in project artifacts:

- `martian_mounts`
- `dead_friend`
- `former_self`

These should not poison downstream prompts.

## Goal

Preserve strict canon fields while adding a separate generated block:

```json
"visual_production_fallback": {
  "status": "generated | context_only | insufficient_context",
  "fallback_bucket": "earth_human | barsoom_humanoid | creature_or_primitive | group_or_horde | deceased_or_body | unknown_reference",
  "production_identity_descriptor": "...",
  "production_body_descriptor": "...",
  "production_face_descriptor": "...",
  "production_costume_descriptor": "...",
  "production_silhouette": "...",
  "production_movement_descriptor": "...",
  "production_state_variants": [],
  "negative_terms": [],
  "provisionality_note": "Generated for visual production because strict canon evidence is thin; not strict canon."
}
```

## Required implementation

### 1. Add unknown detection helpers

In `orchestrator/character_bible.py`, add helpers near other normalization utilities:

- `_is_unknownish(value)`
- `_needs_visual_production_fallback(bible_data)`
- `_fallback_bucket_for_character(entry, bible_data, evidence_summary)`

### 2. Add second-pass fallback synthesis

Inside `run_character_bible_synthesis(...)`, after strict bible merge and before final write:

- If prompt-critical fields are still unknownish, synthesize `visual_production_fallback`.
- Use LM path first.
- Use deterministic fallback if LM unavailable or parse fails.

### 3. Add model support

If the bible model is strict, extend it to include:

```python
visual_production_fallback: dict[str, Any] = field(default_factory=dict)
```

and ensure `to_dict()` writes it.

### 4. Context-only policy

For non-renderable entities (memory/body/reference-only), set:

```json
"status": "context_only"
```

Prompt prep can later skip reference-sheet generation.

## Do not do

- Do not overwrite canon fields.
- Do not remove unresolved ambiguities.
- Do not fabricate named lore facts.

## Unit tests

### Test 1: thin entity gets fallback

Input bible with many unknowns.

Expected:

- `visual_production_fallback` exists.
- `production_body_descriptor` non-empty.
- `status` in allowed set.

### Test 2: strong canon entity still allowed fallback but canon preserved

Input protagonist-like record with real evidence.

Expected:

- canon fields unchanged.
- fallback may exist but does not replace canon.

### Test 3: corpse/reference entity becomes context_only

Input `dead_friend` style record.

Expected:

```json
"status": "context_only"
```

### Test command

```bat
pytest tests/test_character_bible_production_fallbacks.py -q
```