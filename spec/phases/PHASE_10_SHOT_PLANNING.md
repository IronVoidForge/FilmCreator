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

- shot_package.json

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
