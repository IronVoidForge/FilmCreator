Status: 70%

# 4.3 Output Routing Logging and Manifests

## Goal

Make output placement and run history deterministic and reproducible.

## Rules

- `output_scope` decides whether a job writes to project, scene, or clip space.
- Candidate generations land in the stage folder for that scope.
- Each run writes a manifest with project, scene, clip, workflow, prompt, refs, seed, outputs, and timestamp.
- Logs belong near the work they describe and can also be mirrored to project-level `logs/`.

## Acceptance

- A clip artifact cannot accidentally land in a project-shared folder.
- A successful run can be reproduced from its manifest without guesswork.

