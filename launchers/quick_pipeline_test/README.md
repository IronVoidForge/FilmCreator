# Quick Pipeline Test

Run these in order for a compact downstream validation:

1. `00_clear_downstream_artifacts.bat`
2. `01_run_scene_contracts.bat`
3. `02_run_scene_bindings.bat`
4. `03_run_shot_packages.bat`
5. `04_run_dialogue_timeline.bat`
6. `05_run_descriptor_enrichment.bat`
7. `06_run_prompt_preparation.bat`
8. `07_run_quality_grading.bat`

Non-interactive full run:
- `00_run_quick_pipeline_test_auto.bat`

Recommended project:
- `princess_of_mars_test`

Recommended slice:
- chapters `2-3`

Each stage can be run independently if you only want to skip one part of the pipeline.

This skips Phase 1 ingest/book-summary work, preserves bibles, and exercises the same post-bible stages as the larger downstream runner on a smaller slice.

Optional bible refresh steps for a tiny slice of canonical entities:
- `08_run_character_bibles.bat`
- `09_run_environment_bibles.bat`

These use a small `--limit` and are self-contained within the quick-test folder.

The auto launcher defaults to:
- project slug `princess_of_mars_test`
- chapters `2-3`
- character limit `3`
- environment limit `3`
- bibles off unless you pass `1` for the optional include flags
