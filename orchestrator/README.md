# Orchestrator Scaffold

This folder holds the machine-readable contracts that the future runner should use.

- `registry/workflow_registry.json` maps workflow IDs to canonical JSON files, expected inputs, output scope, and known patch points.
- `templates/prompt_package_template.md` defines the Markdown format that both humans and the authoring layer should produce.
- `templates/*.template.json` defines the state and manifest shapes the runner should read and write.

The intent is to keep orchestration code thin:

- load state
- resolve the correct workflow
- patch prompt and image inputs
- send the job to ComfyUI
- write outputs into the project -> scene -> clip hierarchy
- log the run for reproducibility

Starter CLI commands are now scaffolded:

- `python -m orchestrator init-project <project_slug>`
- `python -m orchestrator init-scene <project_slug> <scene_id>`
- `python -m orchestrator init-clip <project_slug> <scene_id> <clip_id>`
- `python -m orchestrator list-workflows`
- `python -m orchestrator plan-run <project_slug> <workflow_id> <stage> <prompt_file> --scene SC001 --clip CL001`
- `python -m orchestrator promote-asset <project_slug> <source> <target> --scene SC001 --clip CL001`
- `python -m orchestrator run-still <project_slug> <stage> <prompt_file> [--workflow-id ...] [--scene SC001] [--clip CL001] [--asset-id hero] [--ref slot=path] [--execute]`
- `python -m orchestrator plan-batch <project_slug> <stage> --scene SC001 --clip CL001 [--prompt-file ...] [--batch-size 4]`
- `python -m orchestrator run-batch <batch_manifest> [--ref image1=...] [--seed-base 1000] [--execute]`

`run-still` prepares and validates by default. It writes a manifest plus a patched workflow preview into the run log, and only submits to ComfyUI when `--execute` is passed.

`plan-batch` is the authoring-side split point for review-driven stages. It generates style-profile prompt variants from one canonical base prompt and writes a master batch manifest. `run-batch` is the render-side split point that prepares or executes every candidate in that manifest against ComfyUI.

Current limitation:

- The canonical workflows are now API exports, but some image-edit workflows still contain baked-in example `LoadImage` filenames for optional refs.
- `run-still` warns about missing optional refs and auto-reuses the resolved continuity source for `image2`.
- The four-ref keyframe path now auto-fills `image3` and `image4` with safe fallbacks when they are omitted, so a two-ref smoke run can still prepare cleanly.
- The current four-ref and two-ref workflow exports do not expose a registered negative-prompt patch point yet, so negative prompt text is preserved in prompt packages but not injected into those workflows.
