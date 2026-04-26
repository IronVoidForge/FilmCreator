# Character Taxonomy Stage Implementation Summary

## Implementation Date
2026-04-26

## Goal
Add a first-class character taxonomy stage that becomes the source of truth for character/entity type, morphology, scale, renderability, and alias confidence.

## Files Created/Modified

### New Files
1. **orchestrator/character_taxonomy.py** - Core taxonomy synthesis module
2. **tests/test_character_taxonomy.py** - Comprehensive test suite (16 tests, all passing)

### Modified Files
1. **orchestrator/cli.py** - Added `synthesize-character-taxonomy` command

## Artifacts Created

### Per-Character Taxonomy Files
- Location: `projects/<slug>/02_story_analysis/taxonomy/characters/CHAR_<id>_TAXONOMY.json`
- Schema includes:
  - character_id, display_name, entity_kind
  - primary_type, morphology, scale, sentience, renderability
  - confidence score
  - direct_evidence and associated_evidence arrays
  - conflicts and unknowns arrays
  - needs_review flag and review_reasons
  - alias_resolution object with status and confidence
  - source_files and generated_at_utc

### Index File
- Location: `projects/<slug>/02_story_analysis/taxonomy/characters/CHARACTER_TAXONOMY_INDEX.json`
- Contains summary of all character taxonomies with quick lookup

### Review Queue Files
- Location: `projects/<slug>/02_story_analysis/taxonomy/review/CHARACTER_TAXONOMY_REVIEW_QUEUE.json`
- Location: `projects/<slug>/02_story_analysis/taxonomy/review/CHARACTER_TAXONOMY_REVIEW_QUEUE.md`
- Lists all characters requiring human review with reasons

## CLI Command Added

```bash
python -m orchestrator synthesize-character-taxonomy <project_slug> [--limit N] [--force]
```

### Options
- `--limit N`: Process only first N characters from registry
- `--force`: Regenerate existing taxonomy files

### Example Usage
```bash
python -m orchestrator synthesize-character-taxonomy princess_of_mars_test --limit 5 --force
```

## Deterministic Aggregation Behavior

### Evidence Collection
1. **Direct Evidence**: Extracted from character bibles and registry
   - Entity type hints (human, humanoid_nonhuman, animal, creature, group, etc.)
   - Morphology hints (biped, quadruped, multi_legged, winged, etc.)
   - Scale hints (tiny, small, human_scale, large, giant)

2. **Associated Evidence**: Recorded separately, does NOT override primary type
   - has_mount, has_costume, has_weapon
   - Used for context but not for primary classification

### Classification Rules
1. **Direct evidence outranks associated evidence**
   - A human riding a mount remains human
   - Mount is recorded in associated_evidence only

2. **No evidence = unknown, not guessed**
   - System never infers from genre or context
   - Unknown values explicitly marked

3. **Conflicts trigger review**
   - Conflicting type hints → needs_review = true
   - Conflicting morphology → unknown + review
   - Conflicting scale → unknown + review

4. **Group entities**
   - entity_kind = "group" → primary_type = "group"
   - Always deterministic

5. **Deceased/narrative-only entities**
   - Mummified, corpse, deceased → context_only
   - renderability = "context_only"

6. **Provisional role labels**
   - entity_kind = "provisional_role" → alias_candidate
   - requires_human_review = true
   - No hardcoded target resolution

## LLM Behavior

**Status**: NOT IMPLEMENTED (TODO)

The current implementation uses only deterministic aggregation. LLM classification is structured to be added later for:
- Unknown taxonomy after deterministic pass
- Conflicting taxonomy requiring disambiguation
- Possible alias/role label resolution
- High-impact character verification

When implemented, LLM prompts must:
- Decide only from evidence provided
- Not infer from genre or book context
- Not classify from associated mounts/objects/clothing
- Use "unknown" when uncertain

## Test Results

All 16 tests passing:

1. ✅ test_path_helpers - Path helper functions work correctly
2. ✅ test_human_with_exotic_clothing_remains_human - Costume doesn't change type
3. ✅ test_rider_remains_humanoid_mount_is_associated - Mount is associated evidence
4. ✅ test_mount_entity_becomes_animal - Direct mount evidence → animal
5. ✅ test_group_entity_becomes_group_type - Group entity → group type
6. ✅ test_deceased_entity_becomes_context_only - Deceased → context_only
7. ✅ test_ambiguous_role_label_requires_review - Role labels need review
8. ✅ test_conflicting_type_hints_create_review - Conflicts trigger review
9. ✅ test_no_evidence_becomes_unknown - No evidence → unknown
10. ✅ test_sentience_determination - Sentience derived from primary_type
11. ✅ test_morphology_conflict_detection - Morphology conflicts detected
12. ✅ test_scale_conflict_detection - Scale conflicts detected
13. ✅ test_taxonomy_synthesis_complete - Full synthesis works
14. ✅ test_run_character_taxonomy_empty_registry - Handles empty registry
15. ✅ test_run_character_taxonomy_with_limit - Limit parameter works
16. ✅ test_book_agnostic_no_hardcoded_names - No book-specific hardcoding

## Validation Results

### Test Project: princess_of_mars_test
- Total registry entries: 57
- Synthesized: 57
- Needs review: 33 (58%)
- Unknown count: 32 (56%)

### Sample Classifications

**john_carter**:
- primary_type: human
- morphology: unknown
- scale: unknown
- sentience: person
- renderability: renderable
- confidence: 1.0
- direct_evidence: ["human"]
- associated_evidence: ["has_costume", "has_weapon"]

**woola** (Martian hound):
- primary_type: animal
- morphology: quadruped
- scale: large
- sentience: animal
- renderability: renderable
- confidence: 1.0
- direct_evidence: ["animal"]
- associated_evidence: ["has_costume"]

**mummified_woman**:
- primary_type: context_only
- morphology: unknown
- scale: unknown
- sentience: unknown
- renderability: context_only
- confidence: 1.0
- direct_evidence: ["context_only"]

**sola** (Green Martian):
- primary_type: humanoid_nonhuman
- morphology: unknown
- scale: unknown
- sentience: person
- renderability: renderable
- confidence: 1.0
- direct_evidence: ["humanoid_nonhuman"]

**apache_warriors**:
- primary_type: group
- entity_kind: group
- scale: large
- renderability: renderable
- confidence: 1.0

**colossal_ape_creature**:
- primary_type: creature
- morphology: unknown
- scale: large
- sentience: monster
- renderability: renderable
- confidence: 1.0

## Book-Agnostic Verification

✅ **No hardcoded character names** - Test verifies no book-specific names in logic
✅ **No genre assumptions** - System doesn't infer from "Mars" or "Barsoom"
✅ **No title-specific rules** - Works for any project
✅ **Evidence-based only** - All classifications from actual text evidence

## Compatibility Risks

### Low Risk
- New module, doesn't modify existing pipelines
- Reads from existing character registry and bibles
- Writes to new taxonomy directory structure
- CLI command is additive

### Integration Points
- Reads: `02_story_analysis/world/CHARACTER_REGISTRY.json`
- Reads: `02_story_analysis/bibles/characters/CHAR_*.md`
- Writes: `02_story_analysis/taxonomy/characters/` (new)
- Writes: `02_story_analysis/taxonomy/review/` (new)

### Future Integration
- World refinement will consume taxonomy artifacts
- Character bible synthesis may reference taxonomy
- Fallback system will use renderability flags
- Quality grading may route based on taxonomy

## Next Steps

1. **Phase 04**: Integrate taxonomy into world_refinement.py
2. **Phase 05**: Integrate taxonomy into character_bible.py
3. **Phase 06**: Update fallback system to use renderability
4. **Phase 07**: Add quality grading routing based on taxonomy
5. **Optional**: Add LLM classification for unknown/conflicting cases

## Summary

The character taxonomy stage is fully implemented with:
- ✅ Deterministic aggregation logic
- ✅ Book-agnostic design
- ✅ Comprehensive test coverage
- ✅ CLI integration
- ✅ Review queue generation
- ✅ Evidence-based classification
- ✅ Conflict detection
- ✅ No hardcoded assumptions

The system successfully classifies characters into appropriate types while maintaining strict evidence-based reasoning and flagging ambiguous cases for human review.
