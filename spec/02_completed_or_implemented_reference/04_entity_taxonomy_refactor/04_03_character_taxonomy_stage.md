# 03 - Character Taxonomy Stage

## Goal
Create a first-class taxonomy artifact that becomes the source of truth.

## New files
- `orchestrator/character_taxonomy.py`
- `tests/test_character_taxonomy.py`

## New artifacts
- `02_story_analysis/taxonomy/characters/CHAR_<id>_TAXONOMY.json`
- `CHARACTER_TAXONOMY_INDEX.json`
- review queue files

## Schema
- `primary_type`
- `morphology`
- `scale`
- `renderability`
- `confidence`
- `conflicts`
- `alias_resolution`
- `needs_review`

## Inputs
- character registry
- chapter entity extraction outputs
- chapter summaries
- source refs

## CLI
`python -m orchestrator synthesize-character-taxonomy <slug> --limit 50 --force`

## Tests
- Human with costume remains human
- Rider remains humanoid, mount stays associated
- Group => group
- Conflicts => review queue
