# 01 - Fallback Safety Patch

## Goal
Immediately stop overconfident wrong classifications while the taxonomy system is being built.

## Files
- `orchestrator/character_bible_fallback.py`
- `tests/test_character_bible_production_fallbacks.py`

## Required changes

1. Remove any runtime hardcoded entity-id special casing.
2. If no upstream taxonomy exists, only classify using direct identity/body evidence.
3. Associated evidence (mounts, pets, clothing, weapons, vehicles) must never redefine the subject type.
4. If evidence is weak or conflicting, return `unknown_reference` instead of confident non-human/quadruped buckets.
5. Preserve alias/context-only handling when explicit metadata exists.

## Tests
- Human riding horse != quadruped
- Human wearing alien armor != alien species
- Weak evidence => `unknown_reference`
- Direct creature evidence => creature bucket

## Validation
`python -m compileall orchestrator`
`pytest tests/test_character_bible_production_fallbacks.py -q`
