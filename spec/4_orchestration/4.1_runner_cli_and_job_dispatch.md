# 4.1 Runner CLI and Job Dispatch

## Goal

Provide a manual local-first runner that can execute still-image stages before the authoring layer is automated.

## Required Commands

- Run a shared character reference job
- Run a shared environment reference job
- Run a clip scene-build job
- Run a clip anchor or interval job
- Promote an approved asset

## Dispatch Rules

- Resolve the project, scene, and clip context from arguments or state.
- Resolve the workflow from the registry.
- Resolve the latest approved continuity source from clip state for continuation jobs.
- Validate required prompt files and image refs before execution.
- Route outputs according to the declared output scope.
- Authoring and rendering are separate local phases; the runner must not require LM Studio to remain loaded while ComfyUI executes a render job.
- Hosted or proprietary generation APIs are not required for the core pipeline.

## Acceptance

- A human can run the still-image pipeline locally without editing workflow JSONs by hand.
