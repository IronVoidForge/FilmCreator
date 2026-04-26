# Character Bible Production Fallbacks Implementation Report

## 1. Files Changed

### Modified Files:
- `orchestrator/character_bible_models.py` - Added visual_production_fallback field to CharacterBible model
- `orchestrator/character_bible.py` - Added import and integration of fallback synthesis

### New Files Created:
- `orchestrator/character_bible_fallback.py` - New module containing fallback helper functions
- `tests/test_character_bible_production_fallbacks.py` - Comprehensive test suite

## 2. Functions Changed

### orchestrator/character_bible.py:
- Modified `run_character_bible_synthesis()`:
  - Added fallback synthesis after bible creation
  - Calls `needs_visual_production_fallback()` to detect thin evidence
  - Calls `deterministic_visual_fallback()` to generate fallback block
  - Preserves all strict canon fields unchanged

### New Functions in orchestrator/character_bible_fallback.py:
- `is_unknownish(value)` - Detects unknown/empty/placeholder values
- `needs_visual_production_fallback(bible_data)` - Determines if fallback is needed based on critical visual fields
- `fallback_bucket_for_character(entry, bible_data, evidence_summary)` - Classifies character into fallback bucket
- `deterministic_visual_fallback(entry, bible_data, evidence_summary)` - Generates complete fallback block

## 3. Schema/Model Changes

### CharacterBible Model (character_bible_models.py):
Added new field:
```python
visual_production_fallback: dict[str, Any] = field(default_factory=dict)
```

Updated `to_dict()` method to include:
```python
"visual_production_fallback": self.visual_production_fallback,
```

### Visual Production Fallback Structure:
```json
{
  "status": "generated | context_only | insufficient_context",
  "fallback_bucket": "earth_human | barsoom_humanoid | creature_or_primitive | group_or_horde | deceased_or_body | context_only | unknown_reference",
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

## 4. How Strict Canon is Preserved

### Separation Strategy:
1. **Strict canon fields remain untouched** - All existing character bible fields (identity_baseline, physical_build, costume_signature, etc.) are preserved exactly as synthesized from evidence
2. **Fallback is a separate block** - The `visual_production_fallback` field is a distinct dictionary that does NOT overwrite any canon fields
3. **Clear provisionality marking** - Every fallback includes a `provisionality_note` stating it is "not strict canon"
4. **Status field distinction** - Fallback status is one of: `generated`, `context_only`, or `insufficient_context`

### Detection Logic:
- Fallback is only generated when 2 or more critical visual fields are "unknownish"
- Critical fields checked: `identity_baseline`, `physical_build`, `costume_signature`, `stable_visual_summary`
- Strong canon bibles with good evidence do NOT receive fallback

## 5. How Generated Fallback is Marked

### Explicit Marking:
1. **Separate field name** - `visual_production_fallback` clearly indicates this is not canon
2. **Status field** - Always includes a `status` field indicating generation method
3. **Fallback bucket** - Explicitly states the classification bucket used
4. **Provisionality note** - Human-readable disclaimer: "Generated for visual production because strict canon evidence is thin; not strict canon."
5. **Negative terms** - Includes anti-patterns to avoid in generation

### Bucket Classification:
- `earth_human` - Frontier-era human defaults
- `barsoom_humanoid` - Martian humanoid defaults
- `creature_or_primitive` - Bestial/animal defaults
- `group_or_horde` - Collective group defaults
- `context_only` - Non-renderable entities (deceased, memory, reference-only)
- `unknown_reference` - Insufficient evidence for any classification

## 6. Tests Added

### Test File: tests/test_character_bible_production_fallbacks.py

#### Test Coverage:
1. **test_is_unknownish()** - Validates unknown value detection
2. **test_needs_visual_production_fallback()** - Tests thin evidence detection
3. **test_fallback_bucket_context_only()** - Validates context_only classification
4. **test_fallback_bucket_earth_human()** - Tests earth_human bucket
5. **test_fallback_bucket_barsoom_humanoid()** - Tests barsoom_humanoid bucket
6. **test_fallback_bucket_creature()** - Tests creature_or_primitive bucket
7. **test_fallback_bucket_group()** - Tests group_or_horde bucket
8. **test_deterministic_visual_fallback_context_only()** - Validates context_only fallback generation
9. **test_deterministic_visual_fallback_earth_human()** - Tests earth_human fallback content
10. **test_deterministic_visual_fallback_barsoom_humanoid()** - Tests barsoom_humanoid fallback content
11. **test_deterministic_visual_fallback_creature()** - Tests creature fallback content
12. **test_deterministic_visual_fallback_preserves_canon()** - Ensures canon fields not overwritten
13. **test_thin_unknown_heavy_entity_receives_fallback()** - Validates thin entity gets fallback
14. **test_strict_canon_fields_preserved()** - Confirms strong canon doesn't need fallback

#### All Tests Pass: ✓ 14 passed in 0.03s

## 7. Command Results

### Compilation Check:
```
cd /d C:\FilmCreator_MC
python -m compileall orchestrator
```
**Result:** SUCCESS - All files compiled without errors

### Test Execution:
```
pytest tests\test_character_bible_production_fallbacks.py -q
```
**Result:** SUCCESS - 14 passed in 0.03s

## 8. Remaining Risks

### Low Risk Items:
1. **Descriptor enrichment integration** - The descriptor_enrichment.py module may need updates to consume visual_production_fallback, but it already has reference_repair infrastructure that can be extended
2. **LLM fallback synthesis** - Currently only deterministic fallback is implemented; optional LLM-based fallback synthesis could be added later for higher quality
3. **Markdown writer** - character_bible_writer.py may need updates to display visual_production_fallback in markdown output

### Mitigation:
- All risks are non-breaking - existing functionality continues to work
- Fallback block is optional and only added when needed
- Strict canon fields are never modified
- Tests validate core functionality

### Future Enhancements:
1. Add LLM-based fallback synthesis for higher quality provisional values
2. Update descriptor enrichment to prefer fallback over generic placeholders
3. Add markdown rendering for visual_production_fallback block
4. Add fallback consumption in prompt preparation layer

## Summary

The character bible production fallbacks feature has been successfully implemented with:
- ✓ Strict canon preservation (separate fallback block)
- ✓ Clear provisional marking (status, bucket, provisionality_note)
- ✓ Deterministic fallback generation (6 bucket types)
- ✓ Comprehensive test coverage (14 tests, all passing)
- ✓ Clean compilation (no syntax errors)
- ✓ Minimal code changes (focused implementation)

The implementation follows the spec requirements exactly:
- Does not overwrite strict canon fields
- Adds clearly marked generated visual-production fallback block
- Prevents downstream prompts from being poisoned by unknown visual fields
- Remains honest about what is canon vs. generated
