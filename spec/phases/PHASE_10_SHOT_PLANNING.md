# Phase 10 — Shot Planning and Shot Packages

## Goal

Break scenes into ordered, generation-ready shot packages.

---

## Inputs

- scene contracts
- character bibles
- environment bibles

---

## Outputs

- per-shot JSON and markdown packages under `projects/<project_slug>/02_story_analysis/contracts/shots/`
- `SHOT_PACKAGE_INDEX.json`
- `SHOT_PACKAGE_INDEX.md`
- `SHOT_PACKAGE_REVIEW_INDEX.json`
- `SHOT_PACKAGE_REVIEW_INDEX.md`
- `review/SHOT_PACKAGE_REVIEW_QUEUE.json`
- `review/SHOT_PACKAGE_REVIEW_QUEUE.md`

---

## Required Fields

- shot_id
- scene_id
- shot_type
- camera_description
- composition
- characters_in_frame
- environment
- prompt_seed

---

## Implementation Files

```
orchestrator/shot_planner.py
```

---

## Acceptance Criteria

- shots are ordered and coherent
- prompts can be generated directly
- the planner writes review queues without mutating upstream scene contracts

---

## Status

- `validated`
- evidence: `synthesize-shot-packages` runs end to end for `princess_of_mars_test` and writes 383 shot packages across 124 scene contracts
