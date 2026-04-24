# Quick Pipeline Test

Run these in order for a compact downstream validation:

1. `00_clear_downstream_artifacts.bat`
2. `00_run_quick_pipeline_test.bat`
3. `01_refresh_descriptor_enrichment.bat`
4. `02_refresh_prompt_preparation.bat`
5. `03_run_downstream_slice_test.bat`
6. `04_run_quality_grading.bat`

Recommended project:
- `princess_of_mars_test`

Recommended slice:
- chapters `2-3`

This skips the early ingest/book-summary phases and focuses on the post-bible pipeline, prompt preparation, and a small downstream validation slice.

The reset step clears downstream artifacts only and preserves upstream chapter summaries.
