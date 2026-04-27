Status: 90%

# 05 - Character Bible Taxonomy Integration

## Files
- `orchestrator/character_bible.py`
- `orchestrator/character_bible_models.py`
- tests for character bible

## Add model fields
- `entity_taxonomy`
- `alias_resolution`
- `associated_entities`

## Synthesis behavior
Taxonomy is primary source for entity type/morphology.
Associated entities remain separate and never become body traits.

## Tests
- Mount remains associated entity
- Human remains human despite exotic clothing
- Alias candidate preserved, not silently merged

