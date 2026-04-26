# DESCRIPTOR QUALITY IMPROVEMENTS - IMPLEMENTATION COMPLETE

## Files Changed
- `orchestrator/descriptor_enrichment.py` (+56 lines)

## Changes Applied

### 1. Added 4 New Helper Functions (after line 400)
- `_looks_like_entity_association(text: str) -> bool`
  - Detects entity/relationship references in text
  - Filters patterns: "(nearby)", "next to", "Protagonist", capitalized names
  
- `_filter_entity_associations(values: list[str]) -> list[str]`
  - Removes entity associations from accessory/costume lists
  
- `_is_generic_group_filler(field_name: str, value: Any) -> bool`
  - Detects generic group filler text
  - Patterns: "varied hair", "species-consistent", "where applicable"
  
- `_should_suppress_group_field(field_name: str, value: Any, supported_values: dict) -> bool`
  - Determines if group field should be suppressed
  - Requires evidence for: hair_color, eye_color, face_shape, skin_tone, facial_hair

### 2. Modified `_character_specific_generated_default` (line ~524)
**BEFORE:**
```python
collective_defaults = {
    "height": "varied heights within a broad martial group",
    "hair_color": "varied hair coloring where applicable",
    "eye_color": "varied but species-consistent eyes",
    "face_shape": "varied face shapes across the group",
    # ... 8 generic portrait fields
}
```

**AFTER:**
```python
collective_defaults = {
    # Only group-appropriate fields
    "costume_materials": "repeatable martial fabrics...",
    "posture": "disciplined group-ready posture",
    # ... no individual portrait fields
}
# Suppress individual portrait fields for groups
if field_name in {"height", "build", "skin_tone", "hair_color", 
                  "hair_style", "eye_color", "face_shape", "facial_hair"}:
    return None
```

### 3. Modified `_sanitize_character_fields` (line ~2185)
**BEFORE:**
```python
for field_name in ["recurring_accessories", "distinctive_features", ...]:
    cleaned = _coerce_string_list(base_fields.get(field_name, []))
```

**AFTER:**
```python
# Filter entity associations from accessory fields
accessory_fields = ["recurring_accessories", "costume_layers", "held_items"]
for field_name in accessory_fields:
    raw_list = _coerce_string_list(base_fields.get(field_name, []))
    filtered = _filter_entity_associations(raw_list)  # NEW
```

### 4. Added Group Filler Suppression in `_base_character_descriptor` (line ~2441)
**AFTER** `_sanitize_character_fields(base_fields, field_origin)`:
```python
profile = _character_profile(base_fields, evidence_summary, char_id, ...)
if profile["is_collective"]:
    supported_values = {k: v for k, v in base_fields.items() 
                       if field_origin.get(k) in EXPLICIT_ORIGINS}
    fields_to_check = list(base_fields.keys())
    for field_name in fields_to_check:
        if _should_suppress_group_field(field_name, base_fields.get(field_name), 
                                       supported_values):
            base_fields.pop(field_name, None)
            field_origin.pop(field_name, None)
            review_flags.append(f"suppressed_generic_group_filler_{field_name}")
```

## Expected Results

### PART A - Entity Association Filtering
**BEFORE:**
```yaml
recurring_accessories:
  - "Protagonist (nearby)"
  - "standing beside John Carter"
```

**AFTER:**
```yaml
recurring_accessories: []
# Filtered out - these are relationships, not accessories
```

### PART B - Group Filler Suppression
**BEFORE:**
```yaml
hair_color: "varied hair coloring where applicable"
eye_color: "varied but species-consistent eyes"
face_shape: "varied face shapes across the group"
```

**AFTER:**
```yaml
# Fields suppressed - no evidence support
# review_flags includes: suppressed_generic_group_filler_hair_color
```

## Validation Steps
1. Run descriptor enrichment on CH002-CH003
2. Check character descriptors for groups (e.g., "Tharks", "warriors")
3. Verify:
   - No "(nearby)" or character names in recurring_accessories
   - No generic "varied hair/eye/face" fields for groups
   - review_flags show suppression tracking

## Prompt Prep Impact
No changes needed to `prompt_preparation.py` - cleaner source descriptors automatically improve prompt quality.

## Git Status
```
M orchestrator/descriptor_enrichment.py
```

## Implementation Notes
- Minimal surgical changes - no descriptor system rewrite
- 4 new functions, 3 function modifications
- Total: +56 lines
- All changes are backward compatible
- Filtering happens at strategic points in the pipeline
