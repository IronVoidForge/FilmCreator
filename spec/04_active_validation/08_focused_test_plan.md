Status: 90%

# Focused Test Plan (No Full Pipeline Required)

## Fast compile check

```bat
cd /d C:\FilmCreator
python -m compileall orchestrator
```

## Targeted pytest runs

```bat
pytest tests/unit/test_prompt_package.py -q -p no:cacheprovider
pytest tests/unit/test_overnight_pipeline_resume_check.py -q -p no:cacheprovider
pytest tests/test_reference_assets.py tests/test_character_references.py tests/test_environment_references.py -q -p no:cacheprovider
pytest tests/test_prompt_package_lifecycle.py tests/test_artifact_lifecycle.py -q -p no:cacheprovider
pytest tests/test_cli_menu_commands.py -q -p no:cacheprovider
```

## If no tests exist yet

Implement them before running pipeline validation.

## Artifact spot checks after tests pass

Use the CLI-native smart resume runner only after unit tests pass.

```bat
python -m orchestrator resume-check princess_of_mars_test --chapters 2-3
python -m orchestrator project-status princess_of_mars_test --chapters 2-3
python -m orchestrator run-production princess_of_mars_test --mode resume --plan-only --chapters 2-3
```

Then inspect:

- protagonist prompt package
- arizona mountain cave environment prompt
- one CH002 shot prompt
- `QUALITY_GRADE_INDEX.json`
- approved reference manifest if Phase 12/13 was exercised
- prompt-package markdown for `Repair Notes`

## Expected visible wins

- shot prompts map image1/image2 correctly
- shot negatives contain fallback negatives
- cave prompts mention cave geometry
- prompts with known issues no longer score A
- silent dialogue timelines stop polluting rerun queue
- `resume-check` stops at the first actually incomplete stage instead of trusting file existence
- prompt packages missing `Repair Notes` fail parsing instead of passing silently
- approved or locked reference assets survive ordinary reruns
