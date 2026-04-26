# World Refinement Taxonomy Integration - Implementation Summary

## Files Changed

### 1. orchestrator/world_refinement.py
**Changes:**
- Replaced `_WEAK_CHARACTER_NAMES` with `_GENERIC_ROLE_TOKENS` (removed book-specific names like "martian_leader", "watch_dog", "dead_friend")
- Added `_taxonomy_cache` to WorldIdentityRefiner.__init__
- Added `_load_taxonomy()` method to load character taxonomy files
- Added `_is_generic_role_label()` method with evidence-aware detection
- Added `_check_taxonomy_conflicts()` method to detect type conflicts
- Updated `_cluster_member_summary()` to include taxonomy data in evidence
- Updated `_maybe_character_candidate()` to use generic role detection
- Updated `_rank_entity_candidate()` to use generic role detection
- Updated `_validate_decision()` to check taxonomy conflicts before merge
- Updated `_build_classification_prompt()` to include guardrails for LLM

### 2. tests/unit/test_world_refinement.py
**Changes:**
- Rewrote all tests to match new implementation
- Added `test_generic_role_label_with_no_taxonomy_creates_review_candidate()`
- Added `test_taxonomy_conflict_blocks_merge()`
- Fixed registry path assertions to use refined registry

## Weak-Name Hardcoding Removed

**Before:**
```python
_WEAK_CHARACTER_NAMES = {
    "narrator",
    "narrator_main",
    "narrator_ch002",
    "protagonist",
    "former_self",
    "dead_friend",        # Book-specific
    "prisoner",
    "prisoner_ch008",
    "chieftain",          # Book-specific
    "martian_leader",     # Book-specific
    "watch_dog",          # Book-specific
}
```

**After:**
```python
_GENERIC_ROLE_TOKENS = {
    "protagonist",
    "narrator",
    "stranger",
    "man",
    "woman",
    "boy",
    "girl",
    "child",
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

**Detection Logic:**
Now uses `_is_generic_role_label()` which checks:
1. Is the root token in generic role tokens?
2. Does taxonomy show high confidence (>= 0.7) and known type? → NOT generic
3. Does taxonomy show canonical alias status? → NOT generic
4. Is entity canonical with 3+ chapter mentions? → NOT generic
5. Otherwise → IS generic role label

## Taxonomy Loading Behavior

**Implementation:**
- Loads from `{project_dir}/02_story_analysis/taxonomy/characters/CHAR_{character_id}_TAXONOMY.json`
- Uses in-memory cache (`_taxonomy_cache`) to avoid repeated file reads
- Returns `None` if file missing or unreadable
- Does NOT crash if taxonomy missing - gracefully degrades to existing behavior

**Usage:**
- Called in `_cluster_member_summary()` to include taxonomy in evidence
- Called in `_maybe_character_candidate()` for generic role detection
- Called in `_rank_entity_candidate()` for scoring
- Called in `_validate_decision()` for conflict checking

## Merge Guardrails Added

**Taxonomy Conflict Detection:**
Blocks or forces human review when:
1. **Primary type conflicts:**
   - human vs animal
   - human vs object
   - animal vs object

2. **Entity kind conflicts:**
   - group vs individual

3. **Renderability conflicts:**
   - context_only vs renderable

4. **Low confidence:**
   - Any taxonomy with confidence < 0.5

**LLM Guardrails:**
Added to classification prompt:
- "Do not merge if taxonomy primary_type conflicts (human vs animal, group vs individual, object vs person)"
- "Do not merge generic role labels without high-confidence evidence"
- "If taxonomy confidence is low or conflicts exist, flag_for_human_review"
- "If uncertain, flag_for_human_review"

## Tests Added/Updated

**New Tests:**
1. `test_generic_role_label_with_no_taxonomy_creates_review_candidate()` - Verifies generic role labels without taxonomy go to human review
2. `test_taxonomy_conflict_blocks_merge()` - Verifies human vs animal conflict blocks merge

**Updated Tests:**
1. `test_refine_world_dry_run_writes_artifacts_without_mutating_registries()` - Updated to work with new implementation
2. `test_refine_world_applies_safe_merge_and_preserves_provenance()` - Fixed registry path
3. `test_refine_world_retries_empty_completion_once()` - Updated to work with new implementation

**All tests pass:** 5/5

## Command Results

```bash
cd /d C:\FilmCreator_MC
python -m compileall orchestrator\world_refinement.py
# Compiling 'orchestrator\\world_refinement.py'...

pytest tests\unit\test_world_refinement.py -q
# .....
# 5 passed in 0.10s
```

## Compatibility Risks

**Low Risk:**
1. **Missing taxonomy files** - System gracefully degrades to existing behavior
2. **Malformed taxonomy files** - Caught by try/except, returns None
3. **Generic role tokens** - More conservative than old hardcoded list
4. **Taxonomy conflicts** - May increase human review queue initially, but prevents bad merges

**Migration Notes:**
- Existing projects without taxonomy will work unchanged
- Projects with taxonomy will get enhanced conflict detection
- No breaking changes to registry format or API
- LLM prompt includes new guardrails but maintains same output schema

## Evidence Summary

**Taxonomy data included in candidate evidence:**
```json
{
  "taxonomy": {
    "primary_type": "human",
    "morphology": "biped",
    "scale": "human_scale",
    "renderability": "renderable",
    "confidence": 0.9,
    "needs_review": false,
    "alias_resolution": {
      "status": "canonical",
      "confidence": 1.0
    }
  }
}
```

This enables LLM and human reviewers to make informed merge decisions based on entity type, not just name similarity.
