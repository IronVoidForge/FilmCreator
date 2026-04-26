# 10 - Fix Phase 7 Quality Routing And Taxonomy Hint Parser

Base reviewed commit: `ec7da7e72a3473a29c26de567c5a7d298cccd58a`.

## Purpose

Finish the remaining gaps after the Phase 1-6 architecture correction:

1. Implement taxonomy hint parsing so Phase 3 can actually consume Phase 2 structured chapter extraction fields.
2. Fix Phase 7 quality grading contradiction checks so they use the real taxonomy schema and real fallback bucket names.
3. Add tests that prove these issues cannot regress.

## Critical rule

Runtime logic must remain book-agnostic.

Do not hardcode project/book/entity names as runtime rules. Do not add special cases for any specific novel, character, species, planet, setting, or project slug.

Project-specific strings may appear only in fixture/artifact data, never as universal logic.

---

## Current problems

## Problem 1 - Taxonomy hint parser is a stub

In `orchestrator/character_taxonomy.py`, this function currently returns `None` for all inputs:

```python
def _parse_taxonomy_hints_from_markdown(content: str, source_path: str) -> dict[str, Any] | None:
    # For now, return None since existing breakdowns don't have structured hints
    # This will be populated when Phase 2 extraction is implemented
    return None
```

This means Phase 3 is architecturally correct but cannot yet consume structured Phase 2 hints from markdown files.

## Problem 2 - Phase 7 checks the wrong fallback bucket names

In `orchestrator/quality_grading.py`, `_taxonomy_fallback_contradictions(...)` checks for buckets like:

```python
"quadruped"
"creature"
```

But actual fallback buckets are:

```text
human
non_human_humanoid
small_quadruped
large_quadruped
small_creature
large_creature
group_or_horde
unknown_reference
context_only
alias_redirect
```

Contradictions like `taxonomy human + fallback large_quadruped` are currently missed.

## Problem 3 - Phase 7 treats morphology as a dict

The taxonomy schema uses:

```json
"morphology": "biped"
```

But `quality_grading.py` currently has logic like:

```python
morphology = taxonomy.get("morphology", {})
limb_config = morphology.get("limb_configuration", "")
```

That is wrong. Morphology is a string.

## Problem 4 - Phase 7 alias checks use the wrong shape

The standardized alias schema is:

```json
"alias_resolution": {
  "status": "canonical|alias_candidate|alias_approved|alias_rejected|role_label|unresolved|unknown",
  "canonical_target_id": null,
  "confidence": 0.0,
  "evidence": [],
  "requires_human_review": false
}
```

But `_alias_prompt_contradictions(...)` currently checks boolean fields like:

```python
alias_resolution.get("alias_candidate") or alias_resolution.get("alias_of")
```

It must check `alias_resolution["status"]`.

## Problem 5 - Phase 7 confidence check compares to string `low`

Taxonomy confidence is numeric:

```json
"confidence": 0.0
```

But `_grader_character(...)` checks:

```python
taxonomy.get("confidence") == "low"
```

This must become a numeric threshold check.

---

## Required changes

## A. Implement taxonomy hint markdown parser

### Target file

- `orchestrator/character_taxonomy.py`

### Function to implement

```python
def _parse_taxonomy_hints_from_markdown(content: str, source_path: str) -> dict[str, Any] | None:
```

### Requirements

The parser must:

1. Parse only structured Phase 2 fields.
2. Never infer taxonomy from arbitrary prose.
3. Return `None` if no structured taxonomy fields are found.
4. Accept reasonable markdown formats produced by the chapter extraction prompt.
5. Normalize values to the known enum values.
6. Clamp confidence to `0.0 <= confidence <= 1.0`.
7. Preserve evidence strings and source path.
8. Parse associated entities into a list.

### Minimum supported field formats

The parser should support all of these simple forms:

```markdown
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.85
direct_identity_evidence: explicitly called a human traveler
direct_visual_evidence: upright bipedal person
costume_or_covering_evidence: wears travel clothes
movement_evidence: walks upright
associated_entities: rides a large animal; carries a lantern
alias_or_role_evidence: none
unknowns: exact age
source_refs: CH001:P12
```

and markdown bullet forms:

```markdown
- character_type_hint: human
- morphology_hint: biped
- scale_hint: human_scale
- renderability_hint: renderable
- confidence: 0.85
- direct_identity_evidence: explicitly called a human traveler
- associated_entities: rides a large animal; carries a lantern
```

and display-label forms:

```markdown
- character_type: human
- morphology: biped
- scale: human_scale
- renderability: renderable
```

### Field aliases

Support these aliases:

- `character_type_hint`, `character_type`, `primary_type_hint`, `type_hint`
- `morphology_hint`, `morphology`
- `scale_hint`, `scale`
- `renderability_hint`, `renderability`
- `confidence`, `taxonomy_confidence`
- `direct_identity_evidence`, `identity_evidence`
- `direct_visual_evidence`, `visual_evidence`
- `costume_or_covering_evidence`, `costume_evidence`, `equipment_evidence`
- `movement_evidence`
- `associated_entities`, `associated_entity_evidence`
- `alias_or_role_evidence`, `alias_evidence`, `role_evidence`
- `unknowns`
- `source_refs`, `source_references`

### Valid enum values

Use the same enum values from Phase 2 helpers:

`character_type_hint`:

- `human`
- `humanoid_nonhuman`
- `animal`
- `creature`
- `group`
- `object`
- `machine`
- `abstract`
- `unknown`

`morphology_hint`:

- `biped`
- `quadruped`
- `multi_legged`
- `serpentine`
- `winged`
- `constructed`
- `amorphous`
- `unknown`

`scale_hint`:

- `tiny`
- `small`
- `human_scale`
- `large`
- `giant`
- `unknown`

`renderability_hint`:

- `renderable`
- `context_only`
- `alias_or_role`
- `unknown`

### Normalization

Normalize:

- lowercase
- trim spaces
- replace spaces and hyphens with underscores
- invalid values become `unknown`

### Return shape

Return a dict like:

```json
{
  "character_type_hint": "human",
  "morphology_hint": "biped",
  "scale_hint": "human_scale",
  "renderability_hint": "renderable",
  "confidence": 0.85,
  "direct_identity_evidence": "explicitly called a human traveler",
  "direct_visual_evidence": "upright bipedal person",
  "costume_or_covering_evidence": "wears travel clothes",
  "movement_evidence": "walks upright",
  "associated_entities": ["rides a large animal", "carries a lantern"],
  "alias_or_role_evidence": "none",
  "unknowns": "exact age",
  "source_refs": ["CH001:P12"],
  "source_path": "..."
}
```

### No prose inference

This parser must not classify by scanning body prose. It should only parse explicit structured fields.

For example, if markdown contains prose:

```markdown
The traveler rides a huge beast and walks into town.
```

but no structured fields, return `None`.

---

## B. Fix quality grading taxonomy/fallback contradiction checks

### Target file

- `orchestrator/quality_grading.py`

### Add bucket family constants

Add constants near the helper functions:

```python
HUMAN_BUCKETS = {"human"}
NON_HUMAN_HUMANOID_BUCKETS = {"non_human_humanoid"}
QUADRUPED_BUCKETS = {"small_quadruped", "large_quadruped"}
CREATURE_BUCKETS = {"small_creature", "large_creature"}
GROUP_BUCKETS = {"group_or_horde"}
NON_RENDER_BUCKETS = {"context_only", "alias_redirect"}
UNKNOWN_BUCKETS = {"unknown_reference"}
BIOLOGICAL_NON_HUMAN_BUCKETS = NON_HUMAN_HUMANOID_BUCKETS | QUADRUPED_BUCKETS | CREATURE_BUCKETS
```

### Fix `_taxonomy_fallback_contradictions(...)`

Rules:

1. `primary_type == "human"` contradicts fallback buckets in:
   - `non_human_humanoid`
   - `small_quadruped`
   - `large_quadruped`
   - `small_creature`
   - `large_creature`

2. `primary_type == "humanoid_nonhuman"` contradicts fallback buckets in:
   - `small_quadruped`
   - `large_quadruped`
   - `small_creature`
   - `large_creature`
   unless morphology explicitly supports non-humanoid creature form. For the current schema, morphology is a string. If `morphology == "biped"`, quadruped/creature buckets are contradictions.

3. `primary_type == "animal"` or `primary_type == "creature"` contradicts fallback bucket `human`, unless taxonomy has low confidence and review status says unresolved. Keep this simple and testable.

4. `primary_type == "group"` contradicts any singular individual bucket:
   - `human`
   - `non_human_humanoid`
   - `small_quadruped`
   - `large_quadruped`
   - `small_creature`
   - `large_creature`

5. `renderability == "context_only"` contradicts any renderable visual bucket:
   - `human`
   - `non_human_humanoid`
   - `small_quadruped`
   - `large_quadruped`
   - `small_creature`
   - `large_creature`
   - `group_or_horde`

6. Unknown taxonomy should not generate contradictions by itself; it should be handled by low-confidence/missing-taxonomy checks.

### Treat morphology as a string

Replace any code that assumes morphology is a dict.

Use:

```python
morphology = str(taxonomy.get("morphology", "unknown")).strip().lower()
```

---

## C. Fix quality grading alias checks

### Target function

- `_alias_prompt_contradictions(...)`

### Required behavior

Use:

```python
status = str(alias_resolution.get("status", "unknown")).strip().lower()
```

Rules:

- `alias_candidate` + separate visual reference without approval => contradiction/review recommendation.
- `role_label` + separate visual reference without approval => contradiction/review recommendation.
- `unresolved` + separate visual reference => review recommendation.
- `alias_approved` should not be a contradiction if prompt uses/redirects to canonical target.
- `canonical` should not be a contradiction.

Because prompt package structures can vary, this helper should be defensive. Detect visual rendering attempts from any of these if present:

- `visual_references`
- `reference_asset_ids`
- `subject_reference`
- `character_reference_id`
- `render_as_separate_character`

---

## D. Fix confidence handling

### Target code

- `_grader_character(...)`

Replace:

```python
taxonomy.get("confidence") == "low"
```

with numeric handling:

```python
try:
    confidence = float(taxonomy.get("confidence", 0.0) or 0.0)
except (TypeError, ValueError):
    confidence = 0.0
```

Rules:

- If taxonomy exists and confidence < 0.5 and `needs_review` is true, add rerun/review recommendation.
- If taxonomy exists and primary_type == unknown, recommend `synthesize-character-taxonomy` only if structured hints exist or taxonomy stage should be rerun; otherwise mark review/unknown without pretending rerun will invent facts.

---

## E. Improve rerun routing specificity

Ensure contradiction records include:

- `type`
- `severity`
- `detail`
- `rerun_stage`

Use stage mapping:

- taxonomy missing/conflicting/low confidence -> `synthesize-character-taxonomy`
- bible missing taxonomy snapshot -> `synthesize-character-bibles`
- fallback contradicts taxonomy -> `synthesize-character-bibles`
- prompt contradicts taxonomy/bible -> `synthesize-prompt-preparation`
- unresolved alias/role label rendered separately -> `refine-identities` or `run-world-refinement` depending actual CLI command name in this repo

Check actual CLI command names in `orchestrator/cli.py` before choosing.

---

## F. Tests to add/update

## 1. `tests/test_character_taxonomy.py`

Add parser tests:

### `test_parse_taxonomy_hints_from_markdown_colon_format`

Input markdown with colon fields.

Expected parsed dict:

- `character_type_hint == "human"`
- `morphology_hint == "biped"`
- `scale_hint == "human_scale"`
- `renderability_hint == "renderable"`
- `confidence == 0.85`
- associated entities parsed into list
- source path preserved

### `test_parse_taxonomy_hints_from_markdown_bullet_format`

Input markdown with bullet fields.

Expected same parsing.

### `test_parse_taxonomy_hints_from_markdown_display_labels`

Input fields:

```markdown
- character_type: animal
- morphology: quadruped
- scale: large
- renderability: renderable
```

Expected normalized hint keys.

### `test_parse_taxonomy_hints_returns_none_without_structured_fields`

Input prose only. Expected `None`.

### `test_parse_taxonomy_hints_invalid_values_become_unknown`

Input invalid values. Expected enum fields normalized to `unknown`.

### `test_parse_taxonomy_hints_confidence_clamped`

Input confidence `2.0` -> `1.0`; input `-1` -> `0.0`.

### `test_taxonomy_aggregates_parsed_markdown_hints`

Create temp character breakdown markdown with structured fields. Run taxonomy. Expected taxonomy uses those fields.

## 2. `tests/test_quality_grading.py`

Add tests for Phase 7 bugs:

### `test_human_taxonomy_large_quadruped_fallback_contradiction`

Payload:

```json
entity_taxonomy.primary_type = human
visual_production_fallback.fallback_bucket = large_quadruped
```

Expected:

- contradiction detected
- rerun recommended
- rerun stage `synthesize-character-bibles`

### `test_human_taxonomy_large_creature_fallback_contradiction`

Same for `large_creature`.

### `test_humanoid_nonhuman_biped_small_creature_contradiction`

Taxonomy:

```json
primary_type = humanoid_nonhuman
morphology = biped
```

Fallback:

```json
fallback_bucket = small_creature
```

Expected contradiction.

### `test_group_taxonomy_individual_fallback_contradiction`

Group taxonomy + human fallback. Expected contradiction.

### `test_context_only_taxonomy_renderable_fallback_contradiction`

Renderability context_only + human fallback. Expected contradiction.

### `test_alias_candidate_prompt_visual_reference_recommends_refinement`

Alias status alias_candidate and prompt package has visual refs. Expected rerun/review route to identity/world refinement.

### `test_role_label_prompt_visual_reference_recommends_refinement`

Same for role_label.

### `test_alias_approved_does_not_flag_when_target_present`

Alias approved with target. Expected no alias contradiction.

### `test_low_confidence_numeric_taxonomy_routes_to_taxonomy`

Confidence 0.2, needs_review true. Expected rerun/review recommendation for taxonomy.

### `test_morphology_string_does_not_crash`

Taxonomy morphology is a string. Expected no AttributeError.

---

## G. Validation commands

Run:

```bat
cd /d C:\FilmCreator_MC
python -m compileall orchestrator
pytest tests/test_character_taxonomy.py -q
pytest tests/test_quality_grading.py -q
pytest tests/test_character_bible_taxonomy_integration.py -q
pytest tests/test_character_bible_production_fallbacks.py -q
```

Do not run full auto pipeline yet.

---

## H. Tiny slice validation

After tests pass, create or use a small structured markdown fixture in the project character breakdowns and run:

```bat
python -m orchestrator synthesize-character-taxonomy princess_of_mars_test --limit 5 --force
python -m orchestrator grade-artifacts princess_of_mars_test --family character_bible
```

Expected:

- taxonomy parser reads structured fields when present
- prose-only files produce unknown/needs_review rather than guesses
- quality grading detects real bucket contradictions using actual bucket names
- quality grading does not crash on string morphology

---

## I. Completion report required

Return:

1. Files changed.
2. Parser formats supported.
3. Proof parser does not infer from prose.
4. Quality contradiction fixes made.
5. Alias status handling fixes.
6. Numeric confidence handling.
7. Test results.
8. Tiny-slice validation results.
9. Remaining risks.

## Approval gate

This fix is complete only when:

- `_parse_taxonomy_hints_from_markdown(...)` is implemented and tested.
- Quality grading uses real fallback bucket names.
- Quality grading treats morphology as a string.
- Quality grading checks `alias_resolution.status`.
- Quality grading treats confidence as numeric.
- All targeted tests pass.
