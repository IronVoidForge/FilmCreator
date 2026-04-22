# Phase 09.5 - Scene Binding and Environment Selection

## Goal

Normalize scene-level bindings after scene contract synthesis and before shot planning so shots inherit stable scene decisions instead of guessing per-shot environments.

---

## Why This Phase Exists

Scene contracts already name cast and environments, but downstream shot planning has been forced to repair or reinterpret those choices. That creates drift:

- shot-local environment guesses
- `"None"` or `null` pseudo-canonical ids
- inconsistent environment selection across shots in the same scene
- unresolved group labels that should remain review items rather than canonical ids

This phase makes the scene the binding authority.

---

## Inputs

- scene contracts
- character bibles
- environment bibles
- character index / registry
- environment index / registry
- chapter summaries
- librarian retrieval

---

## Outputs

- `SCENE_BINDINGS.json` per scene
- scene binding review queue
- future environment request queue

Likely location:

- `projects/<project_slug>/02_story_analysis/contracts/scenes/<chapter_id>/<scene_id>_BINDINGS.json`

---

## Required Fields

- `scene_id`
- `chapter_id`
- `resolved_environment`
- `environment_binding_mode`
- `candidate_environment_ids`
- `beat_environment_overrides`
- `resolved_characters`
- `future_environment_requests`
- `binding_confidence`
- `binding_notes`

---

## Binding Modes

- `single_environment`
  - the whole scene inherits one canonical environment

- `multi_environment`
  - the scene legitimately changes location across beats and must provide explicit beat-level overrides

- `chapter_level_fallback`
  - the scene cannot confidently resolve a specific environment and temporarily falls back to chapter-level place continuity

- `review_required`
  - insufficient confidence even for chapter-level fallback

---

## Rules

- Shots must inherit scene bindings by default.
- A shot may only use a different environment when `beat_environment_overrides` explicitly says so.
- Raw unresolved labels like `None`, `null`, or generic place text may remain visible for grading, but they must not count as canonical bindings.
- If a missing environment is implied, create a future environment request instead of fabricating a canonical id.

---

## Implementation Files

```
orchestrator/scene_bindings.py
orchestrator/scene_contracts.py
orchestrator/shot_planner.py
```

---

## Acceptance Criteria

- every shot can inherit a scene-level environment without per-shot guessing
- scenes with one location remain consistent across all shots
- scenes with real location changes express them explicitly at beat level
- unresolved environments become reviewable binding failures, not fake canonical ids

## Status

- planned
