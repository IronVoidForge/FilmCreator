# Quality Grading Calibration Implementation Report

## 1. Files Changed

### Modified Files
- `orchestrator\quality_grading.py`

### New Files
- `tests\test_quality_grading.py`

---

## 2. Functions Changed

### orchestrator\quality_grading.py

#### New Functions Added

**`_has_prompt_semantic_issue(text: str) -> tuple[bool, list[str]]`**
- Detects semantic issues in prompt packages that should cap grade below A
- Checks for:
  - Missing required subject anchor
  - Reference conflicts
  - Image1 subject contradictions
  - Visible subject omissions
  - Missing fallback terms in shot negatives
  - Environment prompts missing architecture/lighting/mood/scale descriptors
  - Character prompts missing body_descriptor or locked_fields without fallback repair
- Returns tuple of (has_issue: bool, issues: list[str])

**`_is_silent_dialogue(payload: dict[str, Any]) -> bool`**
- Checks if dialogue is explicitly marked as silent/no dialogue expected
- Looks for `no_dialogue_expected: true` in payload or metadata
- Returns True if dialogue is intentionally silent

#### Modified Functions

**`_grader_prompt_package(text: str)`**
- Added call to `_has_prompt_semantic_issue()` to detect semantic problems
- Appends semantic issues to notes list
- Issues are used downstream to cap grade and trigger reruns

**`_grader_dialogue(payload: dict[str, Any], *, artifact_path: Path)`**
- Added `is_silent` check using `_is_silent_dialogue()`
- Modified "no dialogue events" note logic:
  - Only adds note if dialogue is NOT silent
  - Silent dialogue with no events is acceptable
  - Expected dialogue with no events still triggers note

**`_make_grade_record(...)`**
- Added prompt package semantic caps:
  - If semantic issue detected OR prompt_readiness < 80:
    - Grade capped from A to C
    - quality_score_10 capped at 7
    - rerun_recommended set to True
    - Adds semantic issue reason to rerun_reason
- Added dialogue silent mode logic:
  - Silent dialogue with no events: rerun_recommended = False, reason_bits = []
  - Expected dialogue with no events: rerun_recommended = True, adds reason
- Modified rerun_stage assignment:
  - Prompt packages with issues get `rerun_stage = "run-prompt-preparation"`
  - Other families use their spec-defined rerun_stage
- Reorganized rerun logic to handle special families (prompt_package, dialogue_timeline) separately

---

## 3. Grading Thresholds and Caps Added

### Prompt Package Grading Caps

**Grade A Prevention Triggers:**
1. Review notes mention "missing the required subject anchor"
2. Reference conflict exists
3. Image1 subject contradicts visible primary subject
4. Visible subject exists but positive prompt omits it
5. Shot negatives are missing fallback terms
6. **Prompt readiness score < 80** (new threshold)
7. Environment prompt missing 2+ of: architecture, lighting, mood, scale descriptors
8. Character prompt missing body_descriptor or locked_fields and no fallback repair

**When Triggered:**
- Grade capped from A → C
- quality_score_10 capped at 7
- rerun_recommended = True
- rerun_stage = "run-prompt-preparation"
- rerun_reason includes semantic issue description

### Dialogue Timeline Behavior

**Silent Dialogue (no_dialogue_expected: true):**
- Empty dialogue events do NOT trigger rerun
- No "no dialogue events" note added
- Treated as valid low-content artifact

**Expected Dialogue (no silent flag):**
- Empty dialogue events DO trigger rerun
- "expected dialogue but no events generated" added to rerun_reason
- Maintains existing failure behavior

---

## 4. Tests Added

### tests\test_quality_grading.py

Created 11 comprehensive tests:

1. **test_prompt_with_missing_subject_anchor_not_grade_a()**
   - Verifies prompt with "missing the required subject anchor" is detected
   - Confirms semantic issue is added to notes

2. **test_prompt_readiness_76_cannot_grade_a()**
   - Verifies prompt with readiness < 80 cannot grade A
   - Tests the new 80-point threshold

3. **test_prompt_with_image_contradiction_triggers_rerun()**
   - Verifies image1/environment contradiction detection
   - Confirms semantic issue triggers rerun recommendation

4. **test_silent_dialogue_no_events_does_not_rerun()**
   - Verifies silent dialogue with no_dialogue_expected: true passes
   - Confirms no "no dialogue events" note when silent

5. **test_empty_dialogue_without_silent_flag_reruns()**
   - Verifies expected dialogue with no events triggers rerun
   - Confirms "no dialogue events" note is added

6. **test_prompt_missing_fallback_terms()**
   - Verifies detection of missing fallback terms in shot negatives

7. **test_environment_missing_descriptors()**
   - Verifies detection of missing architecture/lighting/mood/scale

8. **test_character_missing_body_descriptor()**
   - Verifies detection of missing body_descriptor or locked_fields

9. **test_silent_dialogue_with_metadata()**
   - Verifies no_dialogue_expected can be in metadata block

10. **test_reference_conflict_detected()**
    - Verifies reference conflict detection

11. **test_visible_subject_omitted()**
    - Verifies detection when visible subject exists but prompt omits it

---

## 5. Command Results

### Compilation Check
```
cd /d C:\FilmCreator_MC
python -m compileall orchestrator
```

**Result:** ✅ SUCCESS
```
Compiling 'orchestrator\quality_grading.py'...
```
No syntax errors detected.

### Test Execution
```
pytest tests\test_quality_grading.py -q
```

**Result:** ✅ SUCCESS
```
11 passed in 0.02s
```

All tests pass on first run.

---

## 6. Remaining Risks

### Low Risk Items

1. **Semantic Issue Detection Patterns**
   - Current implementation uses string matching on review notes
   - Risk: If review note wording changes, detection may miss issues
   - Mitigation: Patterns are broad (e.g., "missing fallback" not exact match)
   - Recommendation: Monitor review note consistency in prompt preparation

2. **Environment Descriptor Threshold**
   - Requires 2+ missing descriptors from [architecture, lighting, mood, scale]
   - Risk: Single missing descriptor won't trigger cap
   - Mitigation: Threshold is intentionally lenient to avoid false positives
   - Recommendation: Adjust to 1+ if too many weak prompts pass

3. **Prompt Readiness Threshold (80)**
   - New hard threshold may be too strict or too lenient
   - Risk: May need calibration after observing real distribution
   - Mitigation: Threshold is based on spec requirement
   - Recommendation: Monitor prompt_readiness distribution in next quality index

### Medium Risk Items

4. **Silent Dialogue Metadata Location**
   - Checks both root level and metadata block for no_dialogue_expected
   - Risk: If flag is placed elsewhere, won't be detected
   - Mitigation: Two common locations are checked
   - Recommendation: Document canonical location in dialogue synthesis spec

5. **Rerun Stage Assignment**
   - Prompt packages with issues route to "run-prompt-preparation"
   - Risk: If prompt preparation stage name changes, routing breaks
   - Mitigation: Stage name matches spec requirement
   - Recommendation: Keep stage names stable or add stage name registry

### No Identified High Risks

The implementation:
- Does not modify existing grading logic for other families
- Does not silence real failures (only distinguishes silent vs expected dialogue)
- Uses minimal helper functions as required
- Maintains backward compatibility for non-prompt/non-dialogue families

---

## 7. Expected Behavior Changes

### Before Implementation
- 173/173 prompt packages graded A despite average readiness 76
- Empty dialogue timelines always triggered rerun warnings
- Semantic issues in prompts did not affect grade

### After Implementation
- Prompt packages with readiness < 80 cannot grade A (capped to C)
- Prompt packages with semantic issues cannot grade A (capped to C)
- Silent dialogue timelines with no events do not trigger reruns
- Expected dialogue timelines with no events still trigger reruns
- Rerun queue will include prompt packages with semantic issues
- Rerun stage for prompt issues points to "run-prompt-preparation"

---

## 8. Integration Notes

### No Pipeline Changes Required
- Changes are isolated to quality grading logic
- No modifications to prompt preparation, dialogue synthesis, or other stages
- Smart resume runner will automatically use new grading logic

### Next Steps
1. Run smart resume to regenerate quality index with new grading
2. Inspect QUALITY_GRADE_INDEX.json for prompt package grade distribution
3. Verify prompt packages with known issues now grade C or below
4. Confirm silent dialogue timelines no longer pollute rerun queue
5. Review rerun queue for semantic issue descriptions

### Validation Artifacts to Check
After running smart resume:
- `02_story_analysis/grading/QUALITY_GRADE_INDEX.json`
- `02_story_analysis/grading/review/QUALITY_RERUN_QUEUE.json`
- Prompt package grades (should see more C/D/F grades)
- Dialogue timeline rerun count (should decrease if silent shots exist)

---

## Implementation Summary

✅ All required semantic checks implemented
✅ Prompt readiness threshold (80) enforced
✅ Silent dialogue mode implemented
✅ Grade capping logic added (A → C for issues)
✅ Rerun routing to prompt-preparation stage
✅ 11 comprehensive tests added
✅ All tests passing
✅ No syntax errors
✅ Minimal code changes (2 new helpers, 3 modified functions)
✅ No breaking changes to existing families

The quality grading system is now stricter and more useful, addressing the core issue where 173/173 prompt packages incorrectly graded A.
