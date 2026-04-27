Status: 90%

# 06 - Fallback From Taxonomy

## Files
- `orchestrator/character_bible_fallback.py`

## Goal
Fallback consumes taxonomy instead of classifying from prose.

## Mapping examples
- human -> human
- humanoid_nonhuman -> non_human_humanoid
- group -> group_or_horde
- quadruped + large -> large_quadruped
- creature small -> small_creature
- alias -> alias_redirect
- context_only -> context_only
- unknown -> unknown_reference

## Tests
- Associated mount cannot override taxonomy
- Unknown taxonomy stays conservative

