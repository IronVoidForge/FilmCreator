# Workflow Home

These are the canonical still-workflow families the orchestrator should reference.

- `text_to_image/klein4b_text_to_image_api.json`
  - shared project-level character and environment generation
- `single_ref_continuation/klein_single_image_edit_api.json`
  - clip-level anchor and interval generation from a prior approved frame
- `two_ref_insert/klein_multi_image_edit_flattened_api.json`
  - clip-level two-reference scene insertion or still-fix generation
- `four_ref_scene_build/klein_multi_image_edit_4_image_scene_build_api.json`
  - clip-level scene build using environment, character, and optional continuity refs
- `three_ref_scene_build/`
  - reserved for a dedicated 3-image API workflow family that has not been registered yet

For now each family folder contains one preferred canonical JSON. Later model variants can live beside it in the same family folder.

## Current Mapping

- `text_to_image/klein4b_text_to_image_api.json`
  - synced to `current_workflows/Klein4b_text_to_image_API.json`
- `single_ref_continuation/klein_single_image_edit_api.json`
  - synced to `current_workflows/KleinSingleImageEdit_API.json`
- `two_ref_insert/klein_multi_image_edit_flattened_api.json`
  - synced to `current_workflows/KleinMultiImageEdit- flattened_API.json`
- `four_ref_scene_build/klein_multi_image_edit_4_image_scene_build_api.json`
  - synced to `current_workflows/KleinMultiImageEdit - 4 images_API.json`

These canonical files are now API exports intended for ComfyUI `/prompt` submission.
The larger editor-graph JSON files are still kept in `current_workflows/` as editable source graphs.

## Motion Workflow Source

- `../video/cut_motion_wan_longlook/wan22_longlook_cut_motion_graph.json`
  - synced to `current_workflows/LongLook - Wan2.2.json`
  - kept as a source graph for Wan 2.2 cut-motion work
  - not yet registered for orchestrator runs because it still needs an API-exported version and patch-point mapping

## Remaining Current Workflow Files

- `current_workflows/Double Image.json`
- `current_workflows/Single image.json`
- `current_workflows/KleinMultiImageEdit- flattened.json`
- `current_workflows/MultiImageEdit1_optional_refs_4input.json`
- `current_workflows/SingleImageNextScene.json`
- `current_workflows/text_to_image_klein4b.json`
