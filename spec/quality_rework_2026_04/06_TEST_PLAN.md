# Focused Test Plan (No Full Pipeline Required)

## Fast compile check

```bat
cd /d C:\FilmCreator_MC
python -m compileall orchestrator
```

## Targeted pytest runs

```bat
pytest tests/test_character_bible_production_fallbacks.py -q
pytest tests/test_descriptor_prompt_normalization.py -q
pytest tests/test_prompt_preparation_visual_fallbacks.py -q
pytest tests/test_quality_grading.py -q
```

## If no tests exist yet

Implement them before running pipeline validation.

## Artifact spot checks after tests pass

Use smart resume runner only after unit tests pass.

```bat
C:\FilmCreator_MC\launchers\quick_pipeline_test\00_run_quick_pipeline_test_resume_from_045.bat
```

Then inspect:

- protagonist prompt package
n- arizona mountain cave environment prompt
- one CH002 shot prompt
- QUALITY_GRADE_INDEX.json

## Expected visible wins

- shot prompts map image1/image2 correctly
- shot negatives contain fallback negatives
- cave prompts mention cave geometry
- prompts with known issues no longer score A
- silent dialogue timelines stop polluting rerun queue
