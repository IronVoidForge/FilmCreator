Status: 90%

# 1.3 Workflow Catalog and Registry

## Goal

Keep workflow selection declarative instead of hardcoded in orchestration logic.

## Canonical Workflow Names

- `workflows/stills/text_to_image/klein4b_text_to_image_api.json`
- `workflows/stills/single_ref_continuation/klein_single_image_edit_api.json`
- `workflows/stills/two_ref_insert/klein_multi_image_edit_flattened_api.json`
- `workflows/stills/four_ref_scene_build/klein_multi_image_edit_4_image_scene_build_api.json`

Motion workflow source graphs may live beside the still catalog, but they are not registry-backed until an API-exported workflow and patch-point contract exist.

## Registry Rules

- Each workflow entry must declare `id`, `filename`, `supported_stages`, and `output_scope`.
- Each workflow entry must declare required and optional image slots.
- Each workflow entry must declare known patch points for prompt text, save prefix, and exposed controls.
- Unknown patch points may be marked as pending, but they must be called out explicitly.

## Acceptance

- The runner can resolve a stage to a workflow without an if-else chain.
- A human can inspect the registry and understand what inputs a job needs.
- Workflow filename changes only require registry updates, not runner rewrites.

