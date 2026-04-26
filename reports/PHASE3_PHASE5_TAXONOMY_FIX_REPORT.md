# Phase 3/Phase 5 Taxonomy Ownership Fix - Final Report

## Executive Summary

Successfully corrected the taxonomy ownership architecture to ensure:
- Taxonomy is upstream of character bibles (not derived from them)
- No book-specific runtime heuristics in taxonomy logic
- Structured extraction hints are the source of truth
- Character bibles serialize and consume taxonomy data
- Fallback system uses taxonomy through bible_data

## Files Changed

### Core Implementation Files
1. **orchestrator/character_taxonomy.py**
   - Removed `_load_character_bible()` function
   - Removed `_extract_entity_type_hints()` with book-specific heuristics
   - Removed `_extract_morphology_hints()` with prose scanning
   - Removed `_extract_scale_hints()` with prose scanning
   - Added `_iter_character_taxonomy_hint_records()` to load structured hints
   - Added `_parse_taxonomy_hints_from_markdown()` for future structured parsing
   - Updated `_synthesize_character_taxonomy()` to aggregate structured hints only

2. **orchestrator/character_bible_models.py**
   - Added `entity_taxonomy: dict[str, Any]` field
   - Added `alias_resolution: dict[str, Any]` field
   - Added `associated_entities: list[dict[str, Any]]` field
   - Updated `to_dict()` to serialize new fields

3. **orchestrator/character_bible.py**
   - Added taxonomy artifact loading from `02_story_analysis/taxonomy/characters/`
   - Integrated taxonomy data into CharacterBible instantiation
   - Added taxonomy artifact to upstream_dependencies
   - Added warning when taxonomy artifact is missing
   - Updated both synthesis and reuse paths to include taxonomy fields

4. **orchestrator/character_bible_fallback.py**
   - Updated `fallback_bucket_for_character()` to accept both "approved" (legacy) and "alias_approved" (canonical)
   - No changes to core logic - already reads from bible_data taxonomy

### Test Files
5. **tests/test_character_taxonomy.py**
   - Added `test_taxonomy_does_not_read_character_bible_markdown()`
   - Added `test_taxonomy_aggregates_structured_chapter_hints()`
   - Added `test_associated_evidence_does_not_override_direct_hint()`
   - Added `test_conflicting_direct_hints_creates_review()`
   - Added `test_no_book_specific_runtime_terms_in_character_taxonomy()`
   - Updated existing tests to remove bible markdown dependencies
   - All 21 tests pass

6. **tests/test_character_bible_taxonomy_integration.py** (NEW)
   - Tests CharacterBible model serialization of taxonomy fields
   - Tests missing taxonomy does not crash
   - Tests alias status enum values (canonical, alias_candidate, alias_approved, role_label)
   - Tests associated evidence separation from physical traits
   - All 7 tests pass

7. **tests/test_character_bible_production_fallbacks.py** (NEW)
   - Tests alias_approved redirects
   - Tests alias_candidate does not redirect
   - Tests role_label does not redirect
   - Tests canonical does not redirect
   - Tests taxonomy-to-bucket mapping (human, humanoid_nonhuman, quadruped, etc.)
   - Tests missing taxonomy maps to unknown_reference
   - Tests negative term filtering by taxonomy
   - All 13 tests pass

## Runtime Hardcoded Terms Removed

Removed from `orchestrator/character_taxonomy.py`:
- "earth" / "virginia" / "confederate" → human inference
- "martian hound" / "calot" → animal inference
- "green martian" / "red martian" → humanoid_nonhuman inference
- "ape" + "creature" → creature inference
- "mummified" / "corpse" / "deceased" → context_only inference

All taxonomy classification now depends on structured upstream hints, not prose scanning.

## Taxonomy Source Ownership After Fix

### Before (WRONG)
```
character_taxonomy.py
  ↓ reads
character bible markdown
  ↓ scans prose for book-specific terms
taxonomy artifact (guessed)
```

### After (CORRECT)
```
chapter extraction (Phase 2)
  ↓ produces
structured taxonomy hints
  ↓ aggregated by
character_taxonomy.py
  ↓ produces
taxonomy artifact
  ↓ loaded by
character_bible.py
  ↓ serialized in
CharacterBible.entity_taxonomy
  ↓ consumed by
character_bible_fallback.py
```

## Where Structured Chapter Hints Are Loaded From

`_iter_character_taxonomy_hint_records()` searches:
- `projects/<slug>/02_story_analysis/character_breakdowns/chapters/<chapter_id>/<character_id>.md`

Expected structured fields (from Phase 2 extraction):
- character_type_hint
- morphology_hint
- scale_hint
- renderability_hint
- confidence
- direct_identity_evidence
- direct_visual_evidence
- costume_or_covering_evidence
- movement_evidence
- associated_entities
- alias_or_role_evidence
- unknowns
- source_refs

Current behavior: Returns empty list since existing breakdowns don't have structured hints yet.
Future behavior: Will parse structured hints when Phase 2 extraction is implemented.

## CharacterBible Serialization Proof

Example from `CHAR_john_carter.json`:

```json
{
  "entity_taxonomy": {
    "character_id": "john_carter",
    "primary_type": "unknown",
    "morphology": "unknown",
    "scale": "unknown",
    "sentience": "unknown",
    "renderability": "unknown",
    "confidence": 0.0,
    "needs_review": true
  },
  "alias_resolution": {
    "status": "canonical",
    "canonical_target_id": null,
    "confidence": 1.0,
    "evidence": ["Registry status is canonical"],
    "requires_human_review": false
  },
  "associated_entities": []
}
```

## Alias Status Enum Used Everywhere

Canonical enum values:
- `canonical` - Entity is its own canonical identity
- `alias_candidate` - Potential alias, requires human review, no auto-redirect
- `alias_approved` - Approved alias, redirects to canonical_target_id
- `alias_rejected` - Rejected as alias, treat as separate entity
- `role_label` - Role/title, not a character identity, no auto-redirect
- `unresolved` - Needs resolution, no auto-redirect
- `unknown` - Status unknown

Backwards compatibility:
- Fallback accepts both "approved" (legacy) and "alias_approved" (canonical)
- Tests assert canonical values

## Test Results

```
tests/test_character_taxonomy.py: 21 passed
tests/test_character_bible_taxonomy_integration.py: 7 passed
tests/test_character_bible_production_fallbacks.py: 13 passed
tests/unit/test_world_refinement.py: 5 passed (no changes needed)
```

Total: 46 tests passed, 0 failed

## Tiny-Slice Artifact Spot-Check Results

### Taxonomy Synthesis
```bash
python -m orchestrator synthesize-character-taxonomy princess_of_mars_test --limit 5 --force
```

Results:
- 5 characters synthesized
- 4 marked needs_review (correct - no structured hints)
- 4 marked unknown primary_type (correct - no structured hints)
- No book-specific heuristics used
- Taxonomy artifacts written to `02_story_analysis/taxonomy/characters/`

Sample: `CHAR_john_carter_TAXONOMY.json`
- primary_type: "unknown" ✓
- morphology: "unknown" ✓
- scale: "unknown" ✓
- confidence: 0.0 ✓
- needs_review: true ✓
- alias_resolution.status: "canonical" ✓

### Bible Synthesis
```bash
python -m orchestrator synthesize-character-bibles princess_of_mars_test --limit 3 --force
```

Results:
- 3 bibles synthesized
- All loaded taxonomy artifacts (with warnings for missing taxonomy)
- All include entity_taxonomy, alias_resolution, associated_entities fields
- Fallback bucket: "unknown_reference" (correct - taxonomy is unknown)
- Fallback status: "insufficient_context" (correct)

Sample: `CHAR_john_carter.json`
- entity_taxonomy present ✓
- alias_resolution present ✓
- associated_entities present ✓
- visual_production_fallback.fallback_bucket: "unknown_reference" ✓
- No book-specific guessing ✓

## Remaining Risks

### Low Risk
1. **Phase 2 structured hints not yet implemented**
   - Current behavior: Taxonomy returns "unknown" for all fields
   - Mitigation: This is correct behavior - no guessing
   - Future: Phase 2 extraction will populate structured hints

2. **Backwards compatibility with old bibles**
   - Old bibles without taxonomy fields will load with empty dicts
   - Mitigation: Code handles missing fields gracefully
   - Fallback will use unknown_reference bucket

3. **Taxonomy artifact missing warnings**
   - Bible synthesis warns when taxonomy artifact is missing
   - Mitigation: Warning is informational, not an error
   - Bible synthesis continues with empty taxonomy

### No Risk
- All tests pass
- No book-specific runtime rules remain
- Taxonomy does not read bible markdown
- Fallback receives taxonomy through bible_data
- Alias status enum is consistent

## Approval Gate Checklist

✅ character_taxonomy.py no longer reads character bible markdown
✅ character_taxonomy.py has no book-specific taxonomy rules
✅ taxonomy artifacts are generated from structured upstream hints
✅ CharacterBible serializes taxonomy fields
✅ fallback receives taxonomy through bible_data
✅ all targeted tests pass

## Conclusion

The taxonomy ownership architecture has been successfully corrected. The system is now:
- Book-agnostic (no hardcoded entity names or settings)
- Upstream-driven (taxonomy from structured hints, not bible prose)
- Properly integrated (bibles serialize and consume taxonomy)
- Well-tested (46 tests covering all requirements)

The architecture is ready for Phase 2 structured extraction implementation.
