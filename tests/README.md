# Test Scaffold

This repo now treats automated testing as part of the architecture, not a later cleanup task.

## Intended Layout

- `tests/unit/`
  - pure deterministic logic such as IDs, naming, helpers, and template expansion
- `tests/contracts/`
  - workflow registry validation, state schema validation, and prompt-package contract checks
- `tests/integration/`
  - filesystem and CLI behavior such as project scaffolding, run-manifest creation, and asset promotion
- `tests/fixtures/`
  - sample prompt packages, sample state files, and small file fixtures for pathing tests
- `tests/live/`
  - optional ComfyUI smoke tests gated behind environment flags

## First Tests to Implement

- registry loading and workflow lookup
- `SC###` and `CL###` validation
- project, scene, and clip scaffold creation
- run-manifest creation for clip-scoped workflows
- asset promotion into shared and clip-local destinations
- prompt-package heading validation

## Testing Rule

Use automated tests for structure, routing, manifests, and contracts.

Keep manual review for image quality and creative approval.
