# Implementation Summary: Quality Grading Contradiction Detection & Rerun Routing

## Files Changed

### orchestrator/quality_grading.py
- Added 5 helper functions for contradiction detection:
  - `_taxonomy_fallback_contradictions()` - Detects taxonomy/fallback bucket mismatches
  - `_negative_term_contradictions()` - Detects negative_terms contradicting taxonomy
  - `_alias_prompt_contradictions()` - Detects alias entities rendered as separate characters
  - `_renderability_prompt_contradictions()` - Detects context_only entities with render prompts
  - `_rerun_stage_for_contradiction()` - Maps contradiction types to rerun stages

- Modified `_grader_character()`:
  - Returns 7 values instead of 6 (added contradictions list)
  - Checks taxonomy vs fallback contradictions
  - Checks negative_terms contradictions
  - Checks low confidence taxonomy without review notes
  - Adds contradiction details to notes

- Modified `_make_grade_record()`:
  - Handles contradictions from character grading
  - Applies grade caps for high severity contradictions (A→B+, B→C)
  - Sets rerun_recommended=True for high severity contradictions
  - Routes to correct rerun stage based on contradiction type
  - Initializes empty contradictions list for non-character families

### tests/test_quality_grading.py
- Added 13 new tests:
  - `test_taxonomy_fallback_contradiction_human_nonhuman()` - Human + non_human_humanoid
  - `test_taxonomy_fallback_contradiction_humanoid_quadruped()` - Humanoid + quadruped
  - `test_taxonomy_fallback_no_contradiction_humanoid_quadruped_with_morphology()` - Valid case
  - `test_negative_term_contradiction_human()` - Human + "human proportions"
  - `test_negative_term_contradiction_quadruped()` - Quadruped + "four-legged"
  - `test_alias_prompt_contradiction()` - Alias rendered separately
  - `test_alias_prompt_no_contradiction_with_approval()` - Valid approved case
  - `test_renderability_prompt_contradiction()` - Context-only + render
  - `test_rerun_stage_mapping()` - Correct stage routing
  - `test_character_grading_with_contradictions()` - Integration test
  - `test_character_grading_correct_taxonomy_fallback()` - Valid case
  - `test_character_grading_low_confidence_no_review()` - Low confidence detection
  - `test_character_grading_missing_taxonomy_no_crash()` - Graceful handling

## Contradiction Checks Added

### 1. Taxonomy/Fallback Mismatches
- **Human + non_human_humanoid/creature/quadruped**: High severity, rerun bibles
- **Humanoid + quadruped/creature**: High severity unless morphology supports it

### 2. Negative Term Contradictions
- **Human taxonomy + "human proportions" in negative_terms**: High severity
- **Quadruped taxonomy + "four-legged" in negative_terms**: High severity

### 3. Alias Contradictions
- **Alias candidate rendered separately without approval**: Medium severity, rerun world-refinement

### 4. Renderability Contradictions
- **Context-only + visual_references in prompt**: High severity, rerun prompt-preparation

### 5. Low Confidence Taxonomy
- **Confidence=low without review_notes**: Medium severity, rerun taxonomy

## Rerun Routing Behavior

| Contradiction Type | Rerun Stage |
|-------------------|-------------|
| taxonomy_fallback_mismatch | synthesize-character-bibles |
| negative_term_contradiction | synthesize-character-bibles |
| alias_render_contradiction | run-world-refinement |
| renderability_prompt_contradiction | run-prompt-preparation |
| taxonomy_missing | synthesize-character-taxonomy |
| low_confidence_taxonomy | synthesize-character-taxonomy |

## Grade Cap Behavior

- **High severity contradictions**: Grade capped at B+ (max quality_score_10 = 7)
  - A/A+/A- → B+
  - B/B+/B- → C
- **Medium severity contradictions**: Rerun recommended but no aggressive cap
- **Contradictions added to notes**: All contradiction details appear in grade record notes

## Validation Results

```
Command: python -m compileall orchestrator\quality_grading.py
Result: ✓ Compiled successfully

Command: pytest tests\test_quality_grading.py -q
Result: ✓ 24 passed in 0.04s
```

## Remaining Risks

### 1. Real-World Data Edge Cases
- **Risk**: Taxonomy morphology field variations not covered
- **Mitigation**: Tests cover common patterns; field is checked with case-insensitive substring match

### 2. Contradiction Severity Tuning
- **Risk**: Grade caps may be too aggressive or too lenient
- **Mitigation**: High severity only for clear structural contradictions; medium for review-worthy issues

### 3. Missing Taxonomy Detection
- **Risk**: Current implementation only checks if taxonomy exists in bible, not if taxonomy index file exists
- **Mitigation**: Spec mentions checking taxonomy_index_path.exists() but this requires file system access during grading; deferred to future enhancement

### 4. Prompt Package Contradictions
- **Risk**: Prompt packages are markdown files, not JSON; alias/renderability checks need prompt metadata
- **Mitigation**: Current implementation checks character bibles; prompt-level checks would require parsing prompt metadata sections

### 5. Associated Entity Term Contradictions
- **Risk**: Spec mentions "associated entity terms appear as character's own body descriptor" but no clear field mapping
- **Mitigation**: Not implemented; requires clarification on which fields contain "body descriptors" vs "associated entity terms"

### 6. Bible Missing Taxonomy Snapshot
- **Risk**: Spec mentions checking if bible.entity_taxonomy exists when taxonomy stage has run
- **Mitigation**: Not implemented; requires tracking which stages have been run (stage execution metadata)

## Implementation Notes

- **No book-specific hardcoding**: All checks use structured fields only
- **Graceful degradation**: Missing taxonomy doesn't crash; returns empty contradictions
- **Actionable rerun reasons**: Each contradiction includes specific detail message
- **Structured contradiction format**: Type, severity, detail, rerun_stage for downstream processing
- **Backward compatible**: Non-character families continue to work with empty contradictions list
