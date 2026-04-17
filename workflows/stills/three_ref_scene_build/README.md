# Three Ref Scene Build

This family is reserved for a dedicated 3-image API workflow.

Intended use:

- `image_1`
  - base environment or scene plate
- `image_2`
  - primary character reference
- `image_3`
  - continuity, costume, or secondary character reference

Why this exists:

- the current 4-image API workflow still works, but leaving optional image slots empty can preserve baked example `LoadImage` filenames from the exported workflow
- a dedicated 3-image API workflow will be safer and easier to reason about for regular scene-build work

Next step:

- paste or export a ComfyUI API workflow for the 3-image version here
- once that file exists, register it as a canonical workflow family in `orchestrator/registry/workflow_registry.json`
