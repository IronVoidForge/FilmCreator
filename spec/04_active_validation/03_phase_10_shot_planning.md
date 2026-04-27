Status: 85%

# Phase 10 - Shot Planning and Shot Packages

## Goal

Break scenes into ordered, generation-ready shot packages that inherit authoritative scene bindings.

---

## Inputs

- scene contracts
- scene bindings
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
- target_seconds

---

## Binding Rules

- The shot planner must inherit environment from the scene binding artifact by default.
- The shot planner must not pick a fresh environment per shot unless the scene binding explicitly declares multiple beat-level environments.
- Unresolved cast or environment labels may be preserved as review information, but they must not be treated as canonical.
- If a scene uses chapter-level environment fallback, every shot in that scene must inherit the same fallback state consistently.

---

## Prompt / Schema Updates Required

- Shot-planning prompts should receive the scene-bound environment, not a loose environment list.
- Prompt packets should refer to shot environment as inherited context, not a field the LLM is expected to rediscover.
- `target_seconds` should remain first-class in the shot schema because downstream timing and dialogue mapping depend on it.

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
- the environment remains consistent across shots in a single-location scene
- environment drift cannot occur from per-shot freeform guessing

---

## Status

- `validated`
- evidence: `synthesize-shot-packages` runs end to end for `princess_of_mars_test` and writes per-shot packages plus indexes and review queues
- next revision required: inherit scene bindings and stop per-shot environment discovery

