# 02 - Chapter Entity Extraction

## Goal
Make chapter extraction the first structured source of entity taxonomy evidence.

## Locate producing modules
Use repo search locally:

`findstr /S /I /N "chapter summary chapter_summ" orchestrator\*.py`
`findstr /S /I /N "character_breakdown entity_mentions" orchestrator\*.py`

## New output fields per mention
- `character_type_hint`
- `morphology_hint`
- `scale_hint`
- `renderability_hint`
- `confidence`
- `direct_identity_evidence`
- `direct_visual_evidence`
- `associated_entities[]`
- `alias_or_role_evidence`
- `source_refs[]`

## Prompt rules
Separate:
- what the entity IS
n- what it WEARS/USES
- what it RIDES/OWNS
- what is nearby

If uncertain, output `unknown` with reason.

## Tests
- Rider + mount separated correctly
- Role label captured as alias candidate
- Group of warriors => group
- Animal mount => animal/creature
