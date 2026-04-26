# 11 - Final Cleanup Before Cross-Book Validation

Base reviewed commit: `21ced09b8fc51e4c69e70d43bb38d2955ee1cbd8`.

## Purpose

Before validating the entity taxonomy refactor on a second public-domain project, fix the remaining small but important issues found in code review.

This spec is intentionally focused. It does not redesign the taxonomy system. It closes the last known gaps before cross-book validation.

## Critical rule

Runtime logic must remain book-agnostic.

Do not add project-specific, book-specific, species-specific, planet-specific, or character-specific rules.

Forbidden examples as runtime logic:

- `john_carter`
- `barsoom`
- `green_martian`
- `martian_leader`
- `watch_dog`
- `wizard_of_oz`
- `dorothy`
- any other project-specific entity or setting name

Project/book strings may appear only in test fixture data or generated project artifacts, not in reusable runtime rules.

---

## Review summary

The architecture is now mostly correct:

- taxonomy no longer reads character bible markdown
- taxonomy parser now reads structured fields only
- character bibles serialize taxonomy fields
- fallback is taxonomy-driven
- quality grading has taxonomy/fallback contradiction checks

Remaining code issues:

1. Phase 2 wiring is not proven. The helper exists, but actual chapter extraction must be verified to emit structured taxonomy fields.
2. `world_refinement.py` still contains project-specific weak/generic role tokens.
3. Character bible LLM synthesis prompt does not appear to receive taxonomy context directly.
4. `quality_grading.py` has inconsistent alias rerun-stage routing.
5. Taxonomy artifacts should preserve evidence strings, not only hint labels.

---

# Fix 1 - Prove and enforce Phase 2 taxonomy hint output

## Files to inspect

Find the actual chapter extraction / chapter summary / character breakdown writer:

```bat
findstr /S /I /N "character_breakdowns chapter_breakdowns chapter_summaries" orchestrator\*.py orchestrator\features\*.py
findstr /S /I /N "format_entity_taxonomy_markdown parse_entity_taxonomy_hints EntityTaxonomyHints" orchestrator\*.py orchestrator\features\*.py tests\*.py
findstr /S /I /N "Physical Description Costume/Silhouette Prompt Phrases" orchestrator\*.py orchestrator\features\*.py
```

Likely relevant file family:

- `orchestrator/features/authoring/entity_taxonomy.py`
- the module that writes `02_story_analysis/character_breakdowns/chapters/<chapter>/<character_id>.md`
- prompt module such as `orchestrator/features/authoring/shared_prompts.py`, if present

## Required behavior

The generated per-character chapter breakdown markdown must include a structured section that `character_taxonomy.py` can parse.

Minimum required fields:

```markdown
# Entity Type Hints

- character_type: human|humanoid_nonhuman|animal|creature|group|object|machine|abstract|unknown
- morphology: biped|quadruped|multi_legged|serpentine|winged|constructed|amorphous|unknown
- scale: tiny|small|human_scale|large|giant|unknown
- renderability: renderable|context_only|alias_or_role|unknown
- confidence: 0.00

## Direct Identity Evidence
<evidence or blank>

## Direct Visual Evidence
<evidence or blank>

## Costume/Equipment
<evidence or blank>

## Movement
<evidence or blank>

## Associated Entities
<semicolon or comma separated associated entities>

## Alias/Role Evidence
<evidence or blank>

## Unknowns
<unknowns or blank>

## Source References
<source refs or blank>
```

This must be emitted into the actual artifact path that `character_taxonomy.py` reads:

```text
02_story_analysis/character_breakdowns/chapters/<chapter_id>/<character_id>.md
```

If the current project writes a different path, either:

1. update taxonomy reader to match the real path, or
2. update the writer to also create the expected per-character markdown file.

Do not leave a mismatch.

## Prompt requirements

The chapter extraction prompt must explicitly say:

- classify what the entity itself appears to be
- do not confuse associated entities with the subject
- riding/owning/wearing/carrying something does not change entity type
- if uncertain, use `unknown` and explain the missing evidence
- confidence is required
- associated entities must be listed separately

## Tests

Add/update tests for the writer/parser round trip:

1. Generated markdown from `format_entity_taxonomy_markdown(...)` is parseable by `_parse_taxonomy_hints_from_markdown(...)`.
2. The real character breakdown writer includes the `# Entity Type Hints` section.
3. A sample chapter breakdown with a humanoid riding a mount results in:
   - subject type hint remains humanoid/person/unknown from direct evidence
   - mount is recorded under associated entities
   - no quadruped classification is assigned to the rider
4. Prose-only markdown still returns `None` from the taxonomy parser.

Suggested tests:

- `tests/test_chapter_entity_extraction_schema.py`
- `tests/test_character_taxonomy.py`

---

# Fix 2 - Remove project-specific generic role tokens from world refinement

## Target file

- `orchestrator/world_refinement.py`

## Current issue

`_GENERIC_ROLE_TOKENS` currently includes project/chapter-specific values such as:

```python
"narrator_ch002"
"prisoner_ch008"
"martian_leader"
"watch_dog"
```

These must not be reusable runtime rules.

## Required change

Replace `_GENERIC_ROLE_TOKENS` with a purely generic, book-agnostic set.

Allowed examples:

```python
_GENERIC_ROLE_TOKENS = {
    "narrator",
    "protagonist",
    "stranger",
    "man",
    "woman",
    "boy",
    "girl",
    "child",
    "person",
    "creature",
    "beast",
    "leader",
    "chieftain",
    "warrior",
    "prisoner",
    "guard",
    "friend",
    "enemy",
    "former_self",
}
```

But `_is_generic_role_label(...)` must remain evidence-aware:

- If taxonomy has high confidence and known primary_type, do not treat as weak solely because token is generic.
- If registry has stable canonical evidence and multiple mentions, do not treat as weak solely because token is generic.
- If role-token appears with chapter suffix, strip the suffix generically rather than hardcoding chapter-specific token names.

## Add helper if needed

```python
def _strip_variant_suffixes(value: str) -> str:
    """Remove generic suffixes such as _ch###, _main, _### for weak-role comparison."""
```

Use existing regex helpers if already present.

## Tests

Update `tests/unit/test_world_refinement.py`:

1. `martian_leader` or any project-specific token is not present in `_GENERIC_ROLE_TOKENS`.
2. `narrator_ch002` normalizes to `narrator` through suffix stripping, not static hardcoding.
3. High-confidence taxonomy prevents generic role weakening.
4. Low-confidence role label still goes to review.

Do not use John Carter-specific assertions. Use synthetic IDs:

- `leader_ch002`
- `watcher_ch008`
- `named_leader`
- `generic_prisoner`

---

# Fix 3 - Add taxonomy context to character bible LLM synthesis prompt

## Target file

- `orchestrator/character_bible.py`

## Current issue

The character bible JSON carries taxonomy fields, and fallback sees taxonomy. However, the LLM synthesis prompt itself still appears to receive only `ENTRY` and `EVIDENCE`.

This allows the LLM to write prose that may conflict with taxonomy or fold associated entities into the character body.

## Required change

Pass taxonomy context into the LLM synthesis prompt.

### Update function signatures if needed

Change:

```python
def _llm_synthesis(entry: dict, evidence_summary: list[str]) -> dict[str, Any] | None:
```

To something like:

```python
def _llm_synthesis(
    entry: dict,
    evidence_summary: list[str],
    *,
    entity_taxonomy: dict[str, Any] | None = None,
    alias_resolution: dict[str, Any] | None = None,
    associated_entities: list[dict[str, Any]] | list[str] | None = None,
) -> dict[str, Any] | None:
```

Then update the call site in `run_character_bible_synthesis(...)`.

### Prompt must include

```text
ENTITY_TAXONOMY:
<json>

ALIAS_RESOLUTION:
<json>

ASSOCIATED_ENTITIES:
<json>
```

### Prompt rules to add

```text
TAXONOMY RULES:
- Treat ENTITY_TAXONOMY as the source of truth for entity type, morphology, scale, and renderability.
- Do not override taxonomy based on associated entities.
- Associated entities describe things near/owned/ridden/carried/worn by the character, not the character's own body.
- Keep associated entities out of physical_build and physical_traits unless evidence explicitly says they are part of the entity's body.
- If taxonomy confidence is low or primary_type is unknown, preserve uncertainty rather than guessing.
- Do not silently merge aliases. Alias resolution belongs to identity refinement.
```

### Deterministic path

If deterministic synthesis is used, also pass or preserve taxonomy in the final `CharacterBible` object. The current serialization already supports this, but verify no code path drops it.

## Tests

Add/update `tests/test_character_bible_taxonomy_integration.py`:

1. LLM prompt builder or `_llm_synthesis` input includes `ENTITY_TAXONOMY`.
2. Prompt includes rule: associated entities must not override body/type.
3. Prompt includes rule: do not silently merge aliases.
4. CharacterBible output still serializes taxonomy fields.

If direct prompt inspection is hard because the LLM client is called inline, monkeypatch/mock `LMStudioClient.chat_completion` and capture `user_prompt`.

---

# Fix 4 - Make Phase 7 alias rerun routing consistent

## Target file

- `orchestrator/quality_grading.py`

## Current issue

`_alias_prompt_contradictions(...)` emits:

```python
"rerun_stage": "refine-identities"
```

But `_rerun_stage_for_contradiction(...)` maps:

```python
"alias_render_contradiction": "run-world-refinement"
```

The routing should use the actual CLI command consistently.

## Required change

Inspect `orchestrator/cli.py` and use the actual command. If the command is `refine-identities`, update the map to:

```python
"alias_render_contradiction": "refine-identities"
```

Ensure any references to `run-world-refinement` are removed unless that is a real CLI command.

## Tests

Update `tests/test_quality_grading.py`:

1. `alias_candidate` rendered separately routes to `refine-identities`.
2. `_rerun_stage_for_contradiction("alias_render_contradiction")` returns `refine-identities`.
3. `alias_approved` with target does not create contradiction.

---

# Fix 5 - Preserve taxonomy evidence strings

## Target file

- `orchestrator/character_taxonomy.py`

## Current issue

The parser captures rich fields such as:

- `direct_identity_evidence`
- `direct_visual_evidence`
- `costume_or_covering_evidence`
- `movement_evidence`
- `source_refs`

But the synthesized taxonomy artifact currently stores `direct_evidence` mostly as hint labels, such as `human`, instead of evidence text.

## Required change

When aggregating records in `_synthesize_character_taxonomy(...)`, preserve evidence strings.

Suggested output structure:

```json
"direct_evidence": [
  {
    "type_hint": "human",
    "morphology_hint": "biped",
    "scale_hint": "human_scale",
    "renderability_hint": "renderable",
    "confidence": 0.9,
    "direct_identity_evidence": "explicitly called a human traveler",
    "direct_visual_evidence": "upright bipedal person",
    "costume_or_covering_evidence": "wears travel clothes",
    "movement_evidence": "walks upright",
    "source_path": "...",
    "source_refs": ["CH001:P12"]
  }
]
```

Associated evidence should similarly preserve context:

```json
"associated_evidence": [
  {
    "associated_entities": ["rides a large animal"],
    "source_path": "...",
    "source_refs": ["CH001:P12"]
  }
]
```

If backward compatibility requires `direct_evidence` to remain a list of strings, add new fields instead:

- `direct_evidence_records`
- `associated_evidence_records`

But prefer richer records if existing tests can be updated safely.

## Tests

Update `tests/test_character_taxonomy.py`:

1. Parsed markdown evidence strings appear in taxonomy artifact.
2. Associated entity evidence appears in associated evidence records.
3. `source_path` and `source_refs` are preserved.
4. Direct hint labels still drive taxonomy classification.

---

# Validation commands

Run targeted tests only:

```bat
cd /d C:\FilmCreator_MC
python -m compileall orchestrator
pytest tests/test_character_taxonomy.py -q
pytest tests/test_chapter_entity_extraction_schema.py -q
pytest tests/test_character_bible_taxonomy_integration.py -q
pytest tests/test_character_bible_production_fallbacks.py -q
pytest tests/test_quality_grading.py -q
pytest tests/unit/test_world_refinement.py -q
```

If `tests/test_chapter_entity_extraction_schema.py` does not exist, create it or run the equivalent Phase 2 test file.

Do not run the full auto pipeline yet.

---

# Required spot-check before cross-book validation

After tests pass, regenerate chapter extraction for a tiny current-project slice and inspect one actual character breakdown markdown file.

Required manual check:

```bat
findstr /S /I /N "Entity Type Hints character_type morphology renderability confidence" projects\princess_of_mars_test\02_story_analysis\character_breakdowns\chapters\*.md
```

If this finds nothing, Phase 2 is still not wired and cross-book validation is premature.

Then run:

```bat
python -m orchestrator synthesize-character-taxonomy princess_of_mars_test --limit 10 --force
python -m orchestrator synthesize-character-bibles princess_of_mars_test --limit 10 --force
python -m orchestrator grade-artifacts princess_of_mars_test --family character_bible
```

Inspect:

```bat
findstr /S /I /N "\"primary_type\": \"unknown\"" projects\princess_of_mars_test\02_story_analysis\taxonomy\characters\*.json
findstr /S /I /N "\"entity_taxonomy\"" projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_*.json
findstr /S /I /N "\"fallback_bucket\"" projects\princess_of_mars_test\02_story_analysis\bibles\characters\CHAR_*.json
```

---

# Cross-book validation gate

After the above fixes and spot-check pass, validate on a second project.

Recommended books:

- `wizard_of_oz`
- `frankenstein`
- `treasure_island`

Validation should check:

1. No contamination from the current Princess of Mars project.
2. Taxonomy is driven by that book's chapter extraction hints.
3. Expected broad classifications make sense.
4. Fallback buckets follow taxonomy.
5. Quality grading catches contradictions.

Do not rely only on `findstr` contamination checks. Also spot-check actual entities semantically.

---

# Completion report required

Return:

1. Files changed.
2. Confirmation Phase 2 writer emits structured taxonomy hints.
3. Example generated character breakdown snippet showing `# Entity Type Hints`.
4. World refinement token cleanup summary.
5. Character bible prompt taxonomy-context proof.
6. Quality rerun routing fix proof.
7. Taxonomy evidence preservation proof.
8. Test results.
9. Tiny current-project spot-check results.
10. Whether cross-book validation is approved.

## Approval gate

This cleanup is complete only when:

- actual chapter breakdown artifacts include structured taxonomy hint fields
- world refinement has no project-specific weak-role tokens
- character bible LLM prompt includes taxonomy context and rules
- alias rerun routing is consistent
- taxonomy artifacts preserve evidence strings/source refs
- all targeted tests pass
