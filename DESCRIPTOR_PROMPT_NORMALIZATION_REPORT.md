# Descriptor Prompt Normalization Implementation Report

## Executive Summary

Successfully implemented descriptor prompt normalization to ensure prompt preparation consumes the best prompt-facing descriptor values. The implementation establishes a clear precedence hierarchy where reference_repair values outrank generic generated values while preserving canon-backed supported values.

---

## 1. Files Changed

### Modified Files
- `orchestrator\prompt_preparation.py`
  - Updated `_prompt_field_text()` function to reorder field precedence

### New Files
- `tests\test_descriptor_prompt_normalization.py`
  - Comprehensive test suite with 10 test cases

---

## 2. Functions Changed

### `_prompt_field_text(descriptor, repair, field_name, *fallback_values)`

**Location:** `orchestrator\prompt_preparation.py` (line ~330)

**Change:** Reordered the precedence of field value sources in the `_prompt_text()` call.

**Before:**
```python
return _prompt_text(
    supported.get(field_name),
    generated.get(field_name),
    field_values.get(field_name),
    repair.get(field_name),
    *fallback_values,
)
```

**After:**
```python
return _prompt_text(
    supported.get(field_name),
    repair.get(field_name),
    generated.get(field_name),
    field_values.get(field_name),
    *fallback_values,
)
```

**Rationale:** This change ensures that `reference_repair` values are consulted immediately after supported values but before generic generated placeholders, allowing repaired fields to override weak generated content while still respecting evidence-backed canon.

---

## 3. Field Precedence Behavior

### New Precedence Order (Highest to Lowest)

1. **Supported field values** (`supported_field_values`)
   - Evidence-backed, canon-grounded values
   - Highest priority - never overridden
   - Source: Character/environment bibles, contracts, explicit evidence

2. **Reference repair** (`reference_repair`)
   - Repaired prompt-facing values
   - Fills gaps with stronger context than generic generation
   - Source: `character_descriptor_repair.py`, `environment_descriptor_repair.py`

3. **Generated field values** (`generated_field_values`)
   - LLM-inferred or heuristic-generated values
   - Used when no stronger source exists
   - Source: Descriptor enrichment LLM passes

4. **Raw field values** (`field_values`)
   - Unclassified field values
   - Legacy or direct field assignments
   - Lower priority than structured sources

5. **Fallback arguments** (`*fallback_values`)
   - Last resort values
   - Only used when all other sources are empty/None
   - Typically project-level defaults or generic placeholders

### Behavior Guarantees

- **Canon preservation:** Supported values always win
- **Repair dominance:** Repair beats generic generated placeholders
- **Graceful degradation:** Falls through to next level if current level is None/empty
- **No data loss:** All sources remain available; only selection order changes

---

## 4. Tests Added

### Test Suite: `tests\test_descriptor_prompt_normalization.py`

**Total Tests:** 10

#### Core Precedence Tests

1. **test_repair_outranks_generic_generated**
   - Validates repair value beats generated value
   - Scenario: Generic generated body vs. specific repaired body
   - Expected: Repair wins

2. **test_supported_outranks_repair**
   - Validates supported value beats repair value
   - Scenario: Canon face from evidence vs. repaired face
   - Expected: Supported wins

3. **test_fallback_fills_missing_generated_field_only**
   - Validates fallback only used when all else missing
   - Scenario: Empty descriptor with fallback costume
   - Expected: Fallback wins

4. **test_fallback_does_not_overwrite_supported_value**
   - Validates fallback never overrides supported
   - Scenario: Canon posture vs. fallback posture
   - Expected: Supported wins

#### Extended Precedence Tests

5. **test_generated_outranks_raw_field_values**
   - Validates generated beats raw field values
   - Expected: Generated wins over raw

6. **test_repair_outranks_raw_field_values**
   - Validates repair beats raw field values
   - Expected: Repair wins over raw

7. **test_full_precedence_chain**
   - Validates full chain with all values present
   - Expected: Supported wins when all sources compete

8. **test_repair_wins_when_no_supported**
   - Validates repair wins when supported missing
   - Expected: Repair beats generated/raw/fallback

#### Edge Case Tests

9. **test_empty_descriptor_uses_fallback**
   - Validates None descriptor falls to fallback
   - Expected: Fallback wins with null descriptor

10. **test_none_values_skip_to_next_precedence**
    - Validates None values skip to next level
    - Expected: Generated wins after None supported/repair

---

## 5. Command Results

### Compilation Check
```
Command: python -m compileall orchestrator
Status: SUCCESS
Output: Compiling 'orchestrator\\prompt_preparation.py'...
```

**Result:** No syntax errors. Module compiles cleanly.

### Test Execution
```
Command: pytest tests\test_descriptor_prompt_normalization.py -q
Status: SUCCESS
Output: 10 passed in 0.05s
```

**Result:** All 10 tests pass. Precedence logic validated.

---

## 6. Remaining Risks

### Low Risk Items

1. **Descriptor enrichment integration**
   - **Risk:** Descriptor enrichment already stores `reference_repair`, but this implementation assumes the repair module populates it correctly
   - **Mitigation:** Existing repair modules (`character_descriptor_repair.py`, `environment_descriptor_repair.py`) already write to `reference_repair`
   - **Status:** No changes needed; integration already exists

2. **Visual production fallback ingestion**
   - **Risk:** Spec mentions character bibles may have `visual_production_fallback` block
   - **Current state:** Not implemented in this pass (deferred to spec 01_CHARACTER_BIBLE_PRODUCTION_FALLBACKS.md)
   - **Mitigation:** Descriptor enrichment can be extended later without breaking current precedence
   - **Status:** Acknowledged; not blocking

3. **Prompt-facing field aliases**
   - **Risk:** Spec mentions alias mapping for prompt-facing fields
   - **Current state:** Fields already exist in codebase with canonical names
   - **Mitigation:** No aliases needed; fields are already consistently named
   - **Status:** No action required

### No Risk Items

1. **Backward compatibility:** Change only affects precedence order; no data structures modified
2. **Performance:** No performance impact; same number of lookups, just reordered
3. **Data integrity:** No data loss; all sources remain available

---

## 7. Implementation Notes

### Design Decisions

1. **Minimal change approach:** Only modified the argument order in one function call
2. **No structural changes:** Preserved all existing data structures and interfaces
3. **Test-first validation:** Created comprehensive test suite before running pipeline

### Alignment with Spec

- ✅ Repair values now outrank generic generated values
- ✅ Supported values still outrank repair values
- ✅ Fallback fills missing fields only
- ✅ Fallback does not overwrite supported values
- ✅ No evidence-supported fields erased
- ✅ No fallback data moved into supported fields

### Future Enhancements (Out of Scope)

The following items are mentioned in related specs but not implemented here:

1. **Character bible production fallback block** (spec 01)
   - Descriptor enrichment can ingest `visual_production_fallback` from bibles
   - Would populate generated fields when missing
   - Does not affect current precedence logic

2. **Environment/shot prompt injection** (spec 03)
   - Bucket-specific environment positive context
   - Shot image role mapping fixes
   - Separate from descriptor field precedence

3. **Quality grading calibration** (spec 04)
   - Prompt package grading tightening
   - Dialogue timeline semantics
   - Downstream from prompt preparation

---

## 8. Validation Summary

| Validation Step | Status | Details |
|----------------|--------|---------|
| Syntax check | ✅ PASS | No compilation errors |
| Unit tests | ✅ PASS | 10/10 tests passing |
| Precedence logic | ✅ PASS | All precedence rules validated |
| Canon preservation | ✅ PASS | Supported values never overridden |
| Repair dominance | ✅ PASS | Repair beats generated |
| Fallback safety | ✅ PASS | Fallback only fills gaps |

---

## 9. Conclusion

The descriptor prompt normalization implementation is **complete and validated**. The change is minimal, focused, and preserves all existing behavior while establishing the correct precedence for prompt-facing descriptor values.

**Key Achievement:** Repaired fields now correctly outrank generic generated placeholders, ensuring stronger prompt-facing context reaches the generation layer without compromising canon integrity.

**Next Steps:** This implementation is ready for integration. The prompt preparation layer now correctly consumes descriptor fields in the intended precedence order. Future work on character bible production fallbacks (spec 01) can build on this foundation without requiring changes to the precedence logic.
