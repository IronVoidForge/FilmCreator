# Fallback Bucket Refactor

Base review commit: `a68a008d1561c2442b13ac6d94c797f53abcecdb`.

## Problem

`visual_production_fallback` is now populated, but buckets are still too book-specific or semantically wrong.

Observed issues:

- `protagonist` appears to be the story role/alias for `john_carter`; it should redirect to the canonical visual character rather than render as its own visual character.
- `martian_mounts` was classified as humanoid even though mounts should be quadruped/creature morphology.
- Green Martian / four-armed humanoid characters should not be classified as beasts.
- Fallback text should add prompt-facing details from canon fields and bucket defaults, never conflict with canon and never overwrite canon.

## Target files

- `orchestrator/character_bible_fallback.py`
- `tests/test_character_bible_production_fallbacks.py`

Avoid touching downstream prompt/descriptor/quality code for this task.

## Required bucket enum

Use reusable morphology / production buckets:

- `alias_redirect`
- `context_only`
- `human`
- `non_human_humanoid`
- `small_quadruped`
- `large_quadruped`
- `small_creature`
- `large_creature`
- `group_or_horde`
- `unknown_reference`

Remove or stop emitting old book-specific buckets:

- `earth_human`
- `barsoom_humanoid`
- `creature_or_primitive`

Book/story context such as Barsoom, Green Martian, Apache, Mars, Thark, or frontier Earth belongs in descriptor text or evidence basis, not in bucket names.

## Classification priority

Implement classification in this order:

1. Alias/role redirect.
2. Context-only narrative/deceased/non-renderable.
3. Group/horde.
4. Quadruped/mount/beast.
5. Non-human humanoid.
6. Human.
7. Creature.
8. Unknown reference.

## Specific expected outcomes

- `protagonist` -> `alias_redirect` to `john_carter`.
- `john_carter` -> `human`.
- `apache_warriors` -> `group_or_horde`.
- `martian_leader`, `chieftain`, `tars_tarkas`, `sola`, green Martian / red Martian humanoids -> `non_human_humanoid`.
- `martian_mounts`, `woola`, watchdog/watch dog/hound/mount entities -> `large_quadruped` or `large_creature` depending evidence.
- ape / colossal creature entities -> `large_creature` unless clear humanoid evidence exists.
- `dead_friend` -> `context_only`.

## Canon additive fallback text

`deterministic_visual_fallback(...)` should build production fields from canon first, then bucket defaults.

Rules:

- `production_identity_descriptor`: prefer `identity_baseline`, then `stable_visual_summary`, then bucket default.
- `production_body_descriptor`: combine `physical_build` and useful `physical_traits`; add bucket default only if needed.
- `production_face_descriptor`: use distinguishing face/anatomy features when present; add bucket default only if needed.
- `production_costume_descriptor`: prefer `costume_signature`; use bucket default only if unknown.
- `production_silhouette`: combine `distinguishing_features`, `physical_build`, and bucket silhouette default.
- `production_movement_descriptor`: prefer `movement_language`; use bucket default only if unknown.
- `production_state_variants`: prefer canon `state_variants`; use bucket defaults only if unknown.

Fallback text must never conflict with canon. It should add to thin fields, not replace strong fields.

## Unknown detection

`is_unknownish(...)` should treat these as unknown:

- `Unknown.`
- `unknown`
- `[]`
- `[ ]`
- `['unknown']`
- `['[]']`
- empty list
- `None`
- `not specified`
- `unspecified`

Do not treat useful text as unknown just because it contains the word `unknown` in a longer explanatory sentence.

## Tests

Update `tests/test_character_bible_production_fallbacks.py`.

Required tests:

1. `protagonist` redirects to `john_carter`.
2. `john_carter` is `human`.
3. `martian_mounts` is quadruped/creature, not humanoid.
4. Green Martian chieftain is `non_human_humanoid`.
5. Martian leader fallback preserves canon specifics such as 15ft/four arms/armlet.
6. Dead friend is `context_only`.
7. Ape/colossal creature is `large_creature`.
8. Unknownish handling catches `Unknown.`, `[]`, `['unknown']`, and `['[]']`.

## Validation

```bat
cd /d C:\FilmCreator_MC
python -m compileall orchestrator
pytest tests\test_character_bible_production_fallbacks.py -q
```

Do not run the full auto pipeline for this spec.
