# Entity Taxonomy Usage Guide

## Overview

Chapter entity extraction now emits structured, book-agnostic entity type hints with confidence scores. This provides the earliest structured source of character/entity taxonomy evidence in the FilmCreator pipeline.

## Quick Start

### Parsing Entity Taxonomy from Character Records

```python
from orchestrator.features.authoring.entity_taxonomy import parse_entity_taxonomy_hints

# From a character extraction record
record_fields = {
    "asset_id": "warrior_leader",
    "character_type_hint": "humanoid_nonhuman",
    "morphology_hint": "biped",
    "scale_hint": "human_scale",
    "renderability_hint": "renderable",
    "confidence": "0.75",
    "direct_identity_evidence": "described as a tall warrior",
    "associated_entities": "mount, weapon",
}

hints = parse_entity_taxonomy_hints(record_fields)

print(f"Type: {hints.character_type_hint}")  # humanoid_nonhuman
print(f"Morphology: {hints.morphology_hint}")  # biped
print(f"Confidence: {hints.confidence}")  # 0.75
print(f"Associated: {hints.associated_entities}")  # ['mount', 'weapon']
```

### Formatting for Markdown Output

```python
from orchestrator.features.authoring.entity_taxonomy import (
    parse_entity_taxonomy_hints,
    format_entity_taxonomy_markdown,
)

hints = parse_entity_taxonomy_hints(record_fields)
markdown = format_entity_taxonomy_markdown(hints)

# Produces:
# # Entity Type Hints
# 
# - character_type: humanoid_nonhuman
# - morphology: biped
# - scale: human_scale
# - renderability: renderable
# - confidence: 0.75
# 
# ## Direct Identity Evidence
# described as a tall warrior
# 
# ## Associated Entities
# mount, weapon
```

## Field Reference

### Core Taxonomy Hints

| Field | Type | Valid Values | Default |
|-------|------|--------------|---------|
| character_type_hint | str | human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown | unknown |
| morphology_hint | str | biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown | unknown |
| scale_hint | str | tiny, small, human_scale, large, giant, unknown | unknown |
| renderability_hint | str | renderable, context_only, alias_or_role, unknown | unknown |
| confidence | float | 0.0 to 1.0 | 0.0 |

### Evidence Fields

| Field | Type | Purpose |
|-------|------|---------|
| direct_identity_evidence | str | What the source says the entity IS |
| direct_visual_evidence | str | Physical appearance details |
| costume_or_covering_evidence | str | Clothing, armor, equipment worn |
| movement_evidence | str | How the entity moves |
| associated_entities | list[str] | Nearby entities (mounts, weapons, companions) |
| alias_or_role_evidence | str | Role labels, titles, alternate names |
| unknowns | str | Explanation of what's missing/uncertain |
| source_refs | list[str] | Source paragraph/chapter references |

## Common Patterns

### Pattern 1: Rider + Mount Separation

**Source Text:** "The leader dismounted from an eight-legged mount."

**Correct Extraction:**

```python
# Leader record
leader = {
    "asset_id": "leader",
    "character_type_hint": "humanoid_nonhuman",  # or human/unknown
    "morphology_hint": "biped",  # NOT quadruped or multi_legged
    "associated_entities": "eight_legged_mount",
}

# Mount record (separate)
mount = {
    "asset_id": "eight_legged_mount",
    "character_type_hint": "animal",
    "morphology_hint": "multi_legged",
    "scale_hint": "large",
}
```

### Pattern 2: Human with Exotic Clothing

**Source Text:** "A man wearing ornate alien robes and a jeweled headpiece."

**Correct Extraction:**

```python
character = {
    "asset_id": "robed_man",
    "character_type_hint": "human",  # NOT alien or humanoid_nonhuman
    "morphology_hint": "biped",
    "direct_identity_evidence": "described as a man",
    "costume_or_covering_evidence": "ornate alien robes, jeweled headpiece",
}
```

### Pattern 3: Group Entity

**Source Text:** "A group of warriors charged forward."

**Correct Extraction:**

```python
group = {
    "asset_id": "warrior_group",
    "character_type_hint": "group",
    "morphology_hint": "unknown",  # groups don't have single morphology
    "renderability_hint": "context_only",  # or renderable if described
    "direct_identity_evidence": "a group of warriors",
}
```

### Pattern 4: Role Label Only

**Source Text:** "The captain ordered the retreat."

**Correct Extraction:**

```python
captain = {
    "asset_id": "captain",
    "character_type_hint": "unknown",
    "morphology_hint": "unknown",
    "renderability_hint": "alias_or_role",
    "confidence": "0.2",
    "alias_or_role_evidence": "referred to as 'the captain'",
    "unknowns": "No physical description; only role label provided",
}
```

### Pattern 5: Unknown with Explanation

**Source Text:** "The entity approached silently."

**Correct Extraction:**

```python
entity = {
    "asset_id": "silent_entity",
    "character_type_hint": "unknown",
    "morphology_hint": "unknown",
    "scale_hint": "unknown",
    "renderability_hint": "unknown",
    "confidence": "0.1",
    "movement_evidence": "approached silently",
    "unknowns": "No identity or physical description provided; only movement mentioned",
}
```

## Integration Points

### In Character Extraction (story_authoring.py)

```python
# After parsing character record
from orchestrator.features.authoring.entity_taxonomy import (
    parse_entity_taxonomy_hints,
    format_entity_taxonomy_markdown,
)

for raw_character in character_records:
    # ... existing field extraction ...
    
    # Parse taxonomy hints
    taxonomy_hints = parse_entity_taxonomy_hints(raw_character.fields)
    
    # Optionally append to markdown
    taxonomy_section = format_entity_taxonomy_markdown(taxonomy_hints)
    character_markdown = f"{markdown}\n\n{taxonomy_section}"
    
    # Store in registry/bible
    # ...
```

### In Character Registry

```python
# Extend registry entry with taxonomy
registry_entry = {
    "canonical_id": canonical_id,
    "asset_id": asset_id,
    "aliases": aliases,
    # ... existing fields ...
    "taxonomy": taxonomy_hints.to_dict(),
}
```

### In Character Bible

```markdown
# Character Bible: warrior_leader

## Identity
- character_id: `warrior_leader`
- status: `canonical`

## Entity Type Hints
- character_type: humanoid_nonhuman
- morphology: biped
- scale: human_scale
- renderability: renderable
- confidence: 0.75

## Direct Identity Evidence
Described as a tall warrior with commanding presence.

## Associated Entities
- mount: eight_legged_beast
- weapon: energy_lance
```

## Validation

### Safe Defaults

The parser provides safe defaults for all fields:

```python
# Empty record
hints = parse_entity_taxonomy_hints({})

assert hints.character_type_hint == "unknown"
assert hints.morphology_hint == "unknown"
assert hints.confidence == 0.0
assert hints.associated_entities == []
```

### Invalid Values

Invalid hint values automatically fall back to "unknown":

```python
record = {
    "character_type_hint": "invalid_type",
    "morphology_hint": "not_a_real_morphology",
}

hints = parse_entity_taxonomy_hints(record)

assert hints.character_type_hint == "unknown"
assert hints.morphology_hint == "unknown"
```

### Confidence Clamping

Confidence is automatically clamped to [0.0, 1.0]:

```python
record_high = {"confidence": "1.5"}
record_low = {"confidence": "-0.3"}

hints_high = parse_entity_taxonomy_hints(record_high)
hints_low = parse_entity_taxonomy_hints(record_low)

assert hints_high.confidence == 1.0
assert hints_low.confidence == 0.0
```

## Best Practices

### DO:
✅ Separate entity identity from equipment/clothing/mounts
✅ Use "unknown" with explanation when uncertain
✅ Record associated entities separately
✅ Provide confidence scores based on evidence quality
✅ Use book-agnostic taxonomy values
✅ Explain unknowns in the unknowns field

### DON'T:
❌ Conflate rider with mount morphology
❌ Change species based on clothing
❌ Use book-specific taxonomy values
❌ Guess details without source evidence
❌ Omit confidence scores
❌ Leave unknowns unexplained

## Testing

Run the test suite:

```bash
pytest tests/test_chapter_entity_extraction_schema.py -v
```

Expected output: 17 tests passing, covering:
- Parsing and defaulting
- Rider/mount separation
- Clothing vs. species
- Group entities
- Animal mounts
- Role labels
- Unknown entities
- Markdown formatting
- Book-agnostic validation
