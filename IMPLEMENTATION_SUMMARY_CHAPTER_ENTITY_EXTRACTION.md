# Chapter Entity Extraction Implementation Summary

## Implementation Date
2025-01-XX

## Specification
spec/refactor_entity_taxonomy/02_CHAPTER_ENTITY_EXTRACTION.md

## Goal
Upgrade chapter summary/chapter extraction to emit structured, book-agnostic entity type hints with confidence. This becomes the earliest structured source of character/entity taxonomy evidence.

## Files Changed

### 1. orchestrator/features/authoring/shared_prompts.py
**Changes:**
- Updated `character_extraction_user_prompt()` to include new entity taxonomy fields in record_fields list:
  - character_type_hint
  - morphology_hint
  - scale_hint
  - renderability_hint
  - confidence

- Added comprehensive entity taxonomy rules to body_requirements:
  - Identify what the entity itself appears to be, not what it wears or rides
  - Do not confuse nearby/associated things with the entity
  - Separate rider from mount classification
  - Clothing doesn't change species/type
  - Defined allowed values for each hint type (book-agnostic)
  - Confidence scoring (0.0 to 1.0)
  - Use "unknown" with explanation when uncertain

- Updated example output format to include the new fields with sample values

**Allowed Values (Book-Agnostic):**
- character_type_hint: human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown
- morphology_hint: biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown
- scale_hint: tiny, small, human_scale, large, giant, unknown
- renderability_hint: renderable, context_only, alias_or_role, unknown

### 2. orchestrator/features/authoring/entity_taxonomy.py (NEW)
**Purpose:** Parser and defaulting helpers for entity taxonomy hints

**Key Components:**
- `EntityTaxonomyHints` dataclass: Structured representation of entity taxonomy data
  - All core hint fields (character_type, morphology, scale, renderability, confidence)
  - Evidence fields (direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence)
  - Associated data (associated_entities, alias_or_role_evidence, unknowns, source_refs)
  - to_dict() method for serialization

- Valid hint sets as constants:
  - VALID_CHARACTER_TYPE_HINTS
  - VALID_MORPHOLOGY_HINTS
  - VALID_SCALE_HINTS
  - VALID_RENDERABILITY_HINTS

- `parse_entity_taxonomy_hints()`: Parse hints from record fields with safe defaults
  - Normalizes hint values to valid options
  - Defaults to "unknown" for invalid/missing values
  - Clamps confidence to [0.0, 1.0]
  - Parses comma-separated lists for associated_entities and source_refs

- `format_entity_taxonomy_markdown()`: Format hints as human-readable markdown
  - Concise section for entity type hints
  - Conditional sections for evidence fields (only if present)
  - Clean formatting for downstream consumption

### 3. tests/test_chapter_entity_extraction_schema.py (NEW)
**Purpose:** Comprehensive test coverage for entity taxonomy extraction

**Test Classes:**
1. **TestEntityTaxonomyParsing**: Core parsing functionality
   - Complete hints parsing
   - Missing fields default to unknown
   - Invalid values default to unknown
   - Confidence clamping
   - List parsing (associated_entities, source_refs)

2. **TestRiderMountSeparation**: Critical separation logic
   - Rider remains biped even when riding a mount
   - Mount is classified separately as animal/multi_legged
   - Associated entities link them without conflating types

3. **TestHumanWearingExoticClothing**: Clothing vs. species
   - Human wearing exotic clothing remains human
   - Costume recorded separately in costume_or_covering_evidence

4. **TestGroupOfWarriors**: Group entity handling
   - Group classified as "group" character_type
   - Appropriate renderability (context_only)

5. **TestAnimalMount**: Animal classification
   - Animal/creature type with appropriate morphology
   - Scale and renderability hints

6. **TestRoleLabel**: Role/alias handling
   - Role labels captured in alias_or_role_evidence
   - Renderability set to alias_or_role
   - No hardcoded canonical targets

7. **TestUnknownEntity**: Unknown handling
   - Unknown type with low confidence
   - Explanation in unknowns field

8. **TestMarkdownFormatting**: Output formatting
   - Complete hints formatted correctly
   - Minimal hints formatted without empty sections

9. **TestValidHintSets**: Book-agnostic validation
   - No book-specific terms in hint sets
   - All hint sets include "unknown"

**Test Results:** 17 tests, all passing

## Prompt Changes

### Key Additions to Character Extraction Prompt:

```
Entity taxonomy rules:
- identify what the entity itself appears to be, not what it wears or rides
- do not confuse nearby/associated things with the entity
- if source says a person rides a mount, classify the person separately from the mount
- if source says a character wears foreign/alien/exotic clothing, do not change their species/type
- character_type_hint: human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown
- morphology_hint: biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown
- scale_hint: tiny, small, human_scale, large, giant, unknown
- renderability_hint: renderable, context_only, alias_or_role, unknown
- confidence: 0.0 to 1.0 for each type/morphology/renderability hint
- if uncertain, use unknown and explain the missing evidence in the markdown section
```

## Parser/Defaulting Changes

**Safe Defaults:**
- All hint fields default to "unknown" if missing or invalid
- Confidence defaults to 0.0 and is clamped to [0.0, 1.0]
- Lists (associated_entities, source_refs) default to empty lists
- Text fields default to empty strings

**Normalization:**
- Hint values normalized to lowercase with underscores
- Invalid values automatically fall back to "unknown"
- Comma-separated lists parsed and trimmed

## Backward Compatibility

**Existing Outputs:**
- New fields are additive; existing character extraction continues to work
- Old markdown outputs remain valid
- JSON schema is extended, not replaced
- Parser handles missing new fields gracefully

**Migration Path:**
- Existing character breakdowns can be re-extracted to gain taxonomy hints
- Old breakdowns without hints will parse with "unknown" defaults
- No breaking changes to downstream consumers

## Downstream Compatibility Risks

**Low Risk:**
- New fields are optional and default safely
- Existing code that doesn't use taxonomy hints is unaffected
- Markdown formatting is backward compatible

**Medium Risk:**
- Character registry may need updates to store/merge taxonomy hints
- Character bible generation may want to include taxonomy sections
- Shared prompt generation could leverage taxonomy for better prompts

**Recommended Follow-up:**
1. Update character registry to store taxonomy hints
2. Update character bible templates to include entity type sections
3. Update character matching to consider taxonomy hints
4. Add taxonomy hint visualization to review tools

## Validation Results

```bash
# Compilation check
python -m compileall orchestrator
# Result: Success, no syntax errors

# New tests
pytest tests/test_chapter_entity_extraction_schema.py -v
# Result: 17 passed in 0.04s

# Existing tests
pytest tests -q -k "chapter or extraction or breakdown"
# Result: 24 passed, 101 deselected in 0.63s
```

## Critical Rules Enforced

✅ No hardcoded book-specific entity names (John Carter, Barsoom, etc.)
✅ No hardcoded book titles or species names
✅ No special handling for single project examples
✅ No assumptions about fantasy/sci-fi entities being non-human
✅ No assumptions about animal/mount shapes from specific books
✅ Book-agnostic taxonomy vocabulary
✅ Separation of entity identity from equipment/clothing/mounts
✅ Unknown values with explanations when uncertain

## Next Steps

1. **Integration Testing:** Run full chapter extraction on test project to verify LLM compliance
2. **Registry Updates:** Extend character/entity registry to store taxonomy hints
3. **Bible Updates:** Add taxonomy sections to character bible templates
4. **Matching Updates:** Leverage taxonomy hints in character matching logic
5. **Visualization:** Add taxonomy hint display to review/debug tools

## Notes

- The implementation is minimal and focused per the implicit instruction
- All code is production-ready and tested
- Documentation is inline and comprehensive
- The schema is extensible for future taxonomy refinements
