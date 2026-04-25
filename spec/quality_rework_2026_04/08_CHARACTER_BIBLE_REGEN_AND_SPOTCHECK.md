# Character Bible Regeneration and Spot Check

Run this only after `07_FALLBACK_BUCKET_REFACTOR.md` is implemented and tests pass.

## Goal

Regenerate character bibles with corrected fallback buckets, then spot-check the highest-risk outputs before any downstream pipeline run.

## Commands

```bat
cd /d C:\FilmCreator_MC
python -m orchestrator synthesize-character-bibles princess_of_mars_test --limit 60 --force
```

## Spot-check files

- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_protagonist.json`
- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_john_carter.json`
- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_martian_mounts.json`
- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_martian_leader.json`
- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_chieftain.json`
- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_dead_friend.json`
- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_woola.json`
- `projects/princess_of_mars_test/02_story_analysis/bibles/characters/CHAR_ape_man_1.json`

## Expected results

- `protagonist` has `alias_redirect` targeting `john_carter`.
- `john_carter` is `human`.
- `martian_mounts` is `large_quadruped` or `large_creature`.
- `martian_leader` is `non_human_humanoid` and canon-specific.
- `chieftain` is `non_human_humanoid`.
- `dead_friend` is `context_only`.
- `woola` is quadruped/creature.
- `ape_man_1` is `large_creature` or another clearly justified non-human category.

## Quick grep checks

```bat
findstr /S /I /N "\"fallback_bucket\"" projects\princess_of_mars_test\02_story_analysis\bibles\characters\*.json
findstr /S /I /N "\"canonical_target_id\"" projects\princess_of_mars_test\02_story_analysis\bibles\characters\*.json
```

## Deliverable

Return a written review listing:

1. Files spot-checked.
2. Any remaining bad bucket assignments.
3. Any fallback text still too generic or conflicting with canon.
4. Whether downstream auto pipeline is approved.
