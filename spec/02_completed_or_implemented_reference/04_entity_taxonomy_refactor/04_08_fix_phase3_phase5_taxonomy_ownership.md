Status: 85%

# 09 - Fix Phase 3 / Phase 5 Taxonomy Ownership

Base reviewed commit: `f61d7f8c2030faa1d98f273223ff7c9900c3339a`.

## Purpose

Correct the Phase 3 and Phase 5 implementation so entity taxonomy ownership flows in the intended book-agnostic direction:

```text
chapter extraction taxonomy hints -> character taxonomy artifact -> character bible snapshot -> visual production fallback -> quality grading
```

The current implementation partially added these pieces, but the ownership chain is broken.

## Critical rule

Runtime logic must be book-agnostic. Do not hardcode book/project/entity names as universal rules.

Forbidden runtime heuristics include examples such as:

- `john_carter -> human`
- `protagonist -> john_carter`
- `earth/virginia/confederate -> human`
- `green martian/red martian -> humanoid_nonhuman`
- `martian hound/calot -> animal`
- any other rule that only works for a specific book/project

Project-specific strings may appear in generated artifacts and fixture data only when they are input data, not runtime logic.

---

## What is wrong now

### 1. `orchestrator/character_taxonomy.py` reads downstream bible markdown

Current code loads:

```python
project_dir / "02_story_analysis" / "bibles" / "characters" / f"CHAR_{character_id}.md"
```

That is wrong. Character taxonomy is intended to be upstream of bibles.

Correct ownership:

```text
chapter extraction / registry -> taxonomy -> bible -> fallback
```

Current wrong ownership:

```text
registry -> bible markdown -> taxonomy -> bible/fallback
```

### 2. `character_taxonomy.py` uses book-specific string heuristics

Current implementation contains checks like:

```python
if "human" in content and ("earth" in content or "virginia" in content or "confederate" in content):
    direct_hints.append("human")
if "martian hound" in content or "calot" in content:
    direct_hints.append("animal")
if "green martian" in content or "red martian" in content:
    direct_hints.append("humanoid_nonhuman")
```

These must be removed. They are not book-agnostic and they recreate the original false-confidence problem.

### 3. Character taxonomy does not consume Phase 2 structured hints

Phase 2 added `EntityTaxonomyHints` fields:

- `character_type_hint`
- `morphology_hint`
- `scale_hint`
- `renderability_hint`
- `confidence`
- `direct_identity_evidence`
- `direct_visual_evidence`
- `costume_or_covering_evidence`
- `movement_evidence`
- `associated_entities`
- `alias_or_role_evidence`
- `unknowns`
- `source_refs`

Phase 3 must aggregate these. It currently does not.

### 4. `CharacterBible` does not serialize taxonomy fields

`orchestrator/character_bible_models.py` still lacks:

```python
entity_taxonomy: dict[str, Any] = field(default_factory=dict)
alias_resolution: dict[str, Any] = field(default_factory=dict)
associated_entities: list[dict[str, Any]] = field(default_factory=list)
```

and `to_dict()` does not write them.

As a result, Phase 6 fallback-from-taxonomy has little or no structured taxonomy to consume.

### 5. Alias status vocabulary is inconsistent

Phase 6 currently redirects only when:

```python
alias_resolution.status == "approved"
```

The broader design uses statuses such as:

- `canonical`
- `alias_candidate`
- `alias_approved`
- `alias_rejected`
- `role_label`
- `unresolved`

The pipeline needs one consistent enum. Prefer `alias_approved` for fallback redirects.

---

## Required corrections

## A. Rewrite Phase 3 taxonomy source ownership

### Target file

- `orchestrator/character_taxonomy.py`

### Remove / stop using

Remove or stop calling:

- `_load_character_bible(...)`
- `_extract_entity_type_hints(... bible markdown content ...)`
- `_extract_morphology_hints(... bible markdown content ...)`
- `_extract_scale_hints(... bible markdown content ...)`

Remove any book-specific runtime string checks such as:

- `earth`
- `virginia`
- `confederate`
- `martian hound`
- `calot`
- `green martian`
- `red martian`

### New source inputs

Taxonomy synthesis must consume upstream evidence only:

1. Global character registry.
2. Phase 2 chapter/character extraction records that contain taxonomy hint fields.
3. Existing chapter summaries / character breakdowns only if they contain structured hint fields.
4. Source refs / paragraph refs already attached to those records.

Do not read character bibles.

### Required helper functions

Add helpers similar to:

```python
def _iter_character_taxonomy_hint_records(project_dir: Path, character_id: str, registry_entry: dict[str, Any]) -> list[dict[str, Any]]:
    """Return structured taxonomy hint records from chapter extraction / character breakdown outputs."""
```

This helper should search known upstream locations for records for the character and collect only structured fields, not infer from arbitrary prose.

The exact file locations must be discovered in repo by the local agent with commands such as:

```bat
findstr /S /I /N "character_type_hint morphology_hint renderability_hint" projects\*\02_story_analysis\*.json projects\*\02_story_analysis\*.md orchestrator\*.py orchestrator\features\*.py
findstr /S /I /N "character_breakdowns chapter_breakdowns" orchestrator\*.py orchestrator\features\*.py
```

Expected possible upstream paths include, but are not limited to:

- `02_story_analysis/character_breakdowns/chapters/...`
- `02_story_analysis/chapter_summaries/...`
- any authoring extraction output that Phase 2 updated

If no structured records exist yet for a project, taxonomy should produce `unknown` / `needs_review`, not guess from bible prose.

### Aggregation rules

1. Direct hints outrank associated evidence.
2. Associated evidence must not alter primary type.
3. Confidence should be weighted by hint confidence and source count.
4. Conflicting direct hints produce `needs_review = true`.
5. No direct hints produce `primary_type = unknown`, `confidence = 0.0`, `needs_review = true`.
6. Do not default to any genre/species based on book context.
7. Alias/role evidence should populate `alias_resolution`, not silently merge.

### Output schema

Keep/ensure these fields:

```json
{
  "character_id": "...",
  "display_name": "...",
  "entity_kind": "individual|group|provisional_role|unknown",
  "primary_type": "human|humanoid_nonhuman|animal|creature|group|object|machine|abstract|unknown",
  "morphology": "biped|quadruped|multi_legged|serpentine|winged|constructed|amorphous|unknown",
  "scale": "tiny|small|human_scale|large|giant|unknown",
  "sentience": "person|animal|monster|object|abstract|unknown",
  "renderability": "renderable|context_only|alias_redirect_candidate|unknown",
  "confidence": 0.0,
  "direct_evidence": [],
  "associated_evidence": [],
  "conflicts": [],
  "unknowns": [],
  "needs_review": false,
  "review_reasons": [],
  "alias_resolution": {
    "status": "canonical|alias_candidate|alias_approved|alias_rejected|role_label|unresolved|unknown",
    "canonical_target_id": null,
    "confidence": 0.0,
    "evidence": [],
    "requires_human_review": false
  },
  "source_files": [],
  "generated_at_utc": "..."
}
```

---

## B. Fix Phase 5 CharacterBible taxonomy serialization

### Target files

- `orchestrator/character_bible_models.py`
- `orchestrator/character_bible.py`

### Model changes

Add to `CharacterBible`:

```python
entity_taxonomy: dict[str, Any] = field(default_factory=dict)
alias_resolution: dict[str, Any] = field(default_factory=dict)
associated_entities: list[dict[str, Any]] = field(default_factory=list)
```

Add these fields to `to_dict()`.

### Synthesis changes

In `run_character_bible_synthesis(...)` or the relevant per-character bible packaging function:

1. Load taxonomy artifact for `character_id` if it exists.
2. Copy taxonomy snapshot into `entity_taxonomy`.
3. Copy `taxonomy["alias_resolution"]` into `alias_resolution`.
4. Copy associated evidence into `associated_entities`.
5. Add taxonomy artifact path as an upstream dependency in metadata when present.
6. If taxonomy is missing, do not crash. Use `{}` and add a warning/review note.

Character bible prompt should receive taxonomy context and must be instructed:

- Use taxonomy as the primary source for entity type/morphology/renderability.
- Do not override taxonomy from associated entities.
- Keep associated entities separate from the character body.
- If taxonomy confidence is low, preserve uncertainty.
- Do not silently merge aliases.

---

## C. Standardize alias status enum

Use this enum across taxonomy, world refinement, bible snapshots, and fallback:

- `canonical`
- `alias_candidate`
- `alias_approved`
- `alias_rejected`
- `role_label`
- `unresolved`
- `unknown`

Rules:

- `alias_candidate` never redirects fallback automatically.
- `role_label` never redirects automatically.
- `alias_approved` redirects fallback if `canonical_target_id` is present.
- `canonical` means render as its own entity.

Update `character_bible_fallback.py` so alias redirect checks `alias_approved`. For backward compatibility only, it may also accept old `approved` temporarily, but tests should assert `alias_approved`.

---

## D. Keep Phase 6 fallback-from-taxonomy; do not reintroduce prose scanning

`orchestrator/character_bible_fallback.py` is directionally correct after Phase 6.

Keep:

- taxonomy-to-bucket mapping
- conservative `unknown_reference` fallback
- negative-term filtering

Do not reintroduce:

- broad prose scanning
- book-specific string heuristics
- ID-specific special cases

---

## E. Tests to add/update

### 1. `tests/test_character_taxonomy.py`

Add or update tests:

#### Test: taxonomy does not read bible markdown

Create a temp project with a fake character bible markdown containing misleading text, but no structured extraction hints.

Expected:

- taxonomy remains `unknown`
- `needs_review = true`
- no classification is derived from bible markdown

#### Test: taxonomy aggregates structured chapter hints

Create structured hint records for one character:

```json
{
  "character_type_hint": "human",
  "morphology_hint": "biped",
  "scale_hint": "human_scale",
  "renderability_hint": "renderable",
  "confidence": 0.9,
  "direct_identity_evidence": "explicitly called a human traveler",
  "associated_entities": ["rides a large animal"]
}
```

Expected:

- `primary_type = human`
- `morphology = biped`
- `scale = human_scale`
- associated evidence does not change type

#### Test: associated evidence does not override direct hint

Direct hint says humanoid/person. Associated entity says mount/animal.

Expected:

- primary type remains humanoid/person hint
- associated evidence is recorded separately

#### Test: conflict creates review

One direct hint says human, another says animal.

Expected:

- `primary_type = unknown` or conservative resolution
- `needs_review = true`
- conflicts list non-empty

#### Test: no book-specific runtime terms

Inspect `orchestrator/character_taxonomy.py` source text and assert it does not contain book-specific literals such as:

- `john_carter`
- `barsoom`
- `green martian`
- `red martian`
- `confederate`
- `virginia`
- `calot`

Use lowercase source text for this assertion.

### 2. `tests/test_character_bible_taxonomy_integration.py`

Create if missing.

Required tests:

1. CharacterBible model serializes `entity_taxonomy`, `alias_resolution`, and `associated_entities`.
2. Character bible synthesis loads taxonomy artifact and includes taxonomy snapshot.
3. Missing taxonomy does not crash and emits warning/review note.
4. Associated evidence appears in `associated_entities`, not as physical body traits.
5. Alias candidate is preserved as candidate, not auto-redirected.
6. Alias approved is serialized with target and available to fallback.

### 3. `tests/test_character_bible_production_fallbacks.py`

Update alias tests:

- `alias_approved` redirects.
- `alias_candidate` does not redirect.
- old `approved` compatibility may be accepted only if intentionally kept.

Ensure fallback tests use structured taxonomy, not prose/ID heuristics.

### 4. `tests/unit/test_world_refinement.py`

Update if needed so alias enum matches:

- alias candidate -> review / not auto merge
- alias approved -> safe redirect/merge only when produced by refinement approval flow

---

## F. Validation commands

Run:

```bat
cd /d C:\FilmCreator_MC
python -m compileall orchestrator
pytest tests/test_character_taxonomy.py -q
pytest tests/test_character_bible_taxonomy_integration.py -q
pytest tests/test_character_bible_production_fallbacks.py -q
pytest tests/unit/test_world_refinement.py -q
```

Do not run full auto pipeline yet.

---

## G. Small slice artifact validation

After tests pass, run a tiny slice only:

```bat
python -m orchestrator synthesize-character-taxonomy princess_of_mars_test --limit 5 --force
python -m orchestrator synthesize-character-bibles princess_of_mars_test --limit 5 --force
```

Then inspect:

- taxonomy files contain no bible-derived guesswork
- unknowns remain unknown when no structured hints exist
- bibles include taxonomy snapshot fields
- fallback buckets use taxonomy fields

---

## H. Completion report required

Return a report with:

1. Files changed.
2. Runtime hardcoded terms removed.
3. Explanation of taxonomy source ownership after fix.
4. How structured chapter hints are loaded.
5. CharacterBible field serialization proof.
6. Alias status enum used everywhere.
7. Test results.
8. Tiny-slice artifact spot-check results.
9. Remaining risks.

## Approval gate

This fix is complete only when:

- `character_taxonomy.py` no longer reads character bible markdown.
- `character_taxonomy.py` contains no book-specific taxonomy rules.
- taxonomy artifacts are generated from structured upstream hints.
- CharacterBible serializes taxonomy fields.
- fallback receives taxonomy via bible data.
- all targeted tests pass.

