# 4.2 ComfyUI Client and Workflow Patching

## Goal

Patch known workflow controls at runtime and submit the job to ComfyUI consistently.

## Responsibilities

- Load the canonical workflow JSON
- Patch prompt text
- Patch input image paths
- Patch save prefix and exposed controls
- Submit the job
- Wait for completion
- Capture output metadata

## Rules

- The default execution target is one configured local ComfyUI runtime.
- Multiple launchers or ports only count as separate runtimes if they point at different base, user, input, and output directories.
- Patch points come from the workflow registry, not from hardcoded runner logic.
- Unknown patch points must fail loudly rather than silently ignoring requested changes.
- Every job should capture enough metadata to re-run it later.
- When local hardware cannot comfortably host both a local authoring LM and ComfyUI together, the system should treat them as separate phases instead of assuming concurrent execution.
- Hosted or proprietary render APIs are out of scope for the required product-core behavior.

## Acceptance

- The same patcher can operate on multiple workflows as long as the registry defines the patch points.
