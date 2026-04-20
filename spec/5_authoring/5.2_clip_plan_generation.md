# 5.2 Clip Plan Generation

## Goal

Define how the legacy clip-planning layer should evolve into the new shot-planning architecture.

This spec is now a **compatibility and bridge spec**.
It no longer defines the final production-planning abstraction.

The long-term architecture is:

- analysis outputs
- character and environment bibles
- scene production contracts
- shot packages
- dialogue and edit timeline

Legacy clip planning remains useful, but only as:

- a predecessor to shot packages
- a compatibility layer for older prompt and render flows
- an import source when the new shot package does not yet exist

---

## Design Principles

- `clip` may remain a valid legacy runtime unit, but should not be treated as the final planning abstraction.
- The new primary planning abstraction is the **shot package**.
- Existing clip planning logic should be reused where helpful, but adapted through compatibility adapters rather than treated as canonical forever.
- New planning architecture should prefer scene contracts and canonical bibles over raw analysis files.
- The pipeline should preserve already-working clip-generation paths while introducing stronger upstream contract layers.

---

## Updated Working Interpretation

- `clip = cut` remains acceptable in current implementation.
- Legacy clip plans are still useful render-facing planning artifacts.
- Future shot packages should supersede clip plans as the canonical production-planning unit.
- When both exist, shot packages should be the source of truth and legacy clip plans should become derived or compatibility artifacts.
- The system should remain file-first before any future SQLite synchronization layer.

---

## Legacy Responsibilities That Remain Useful

A clip or shot planning artifact may still describe:

- shot purpose
- opening-frame intent
- motion beat structure
- starting continuity source
- composition type
- continuity mode
- dependency policy
- fallback strategy
- required refs
- expected prompt-package targets

These responsibilities remain valid, but they should now be understood as part of the **future shot package contract**.

---

## Updated Architectural Role

### Old model

```text
scene analysis -> clip plan -> prompt writing
```

### New model

```text
scene analysis
-> character / environment bibles
-> scene production contracts
-> shot packages
-> prompt writing
```

### Temporary compatibility model

```text
scene contract -> shot package -> legacy clip plan adapter -> existing prompt/render paths
```

This compatibility model is the preferred migration strategy.

---

## Recommended Future Contract Split

### Scene contract owns

- scene purpose
- emotional arc
- scene-level beat ordering
- required characters
- required environments
- continuity constraints
- broad shot opportunities

### Shot package owns

- shot/clip purpose
- camera intent
- composition
- visible entities
- opening-state and continuity mode
- motion beat structure
- required refs
- prompt seed summary

### Legacy clip plan adapter may still emit

- clip-scoped prompt file expectations
- clip-scoped render output expectations
- compatibility naming for existing runners

---

## Existing Useful Planning Fields To Preserve

The following concepts remain useful and should carry forward into shot-package design:

- `Scene Purpose`
- `Clip Purpose`
- `Duration Seconds`
- `Start Mode`
- `Composition Type`
- `Continuity Mode`
- `Starting Keyframe Strategy`
- `Dependency Policy`
- `Fallback Strategy`
- `Look Continuity Policy`
- `Required Refs`
- `Visible Character Assets`
- `Opening Keyframe Intent`
- `Cut Motion Intent`
- `Interval Beats`
- `Continuity Rules`
- `Axis And Eyeline Rules`

These should inform the future shot package schema rather than be discarded.

---

## What Should Change Going Forward

### Clip plan should no longer be the only bridge

The bridge is now:

- scene contract
- then shot package
- then prompt writing

### Shot package should become the canonical planning artifact

The legacy clip plan should eventually become:

- a derived artifact
- or an adapter output

### New prompt writing should prefer shot packages

Prompt writers should eventually prefer:

- character bibles
- environment bibles
- scene contracts
- shot packages

rather than raw scene analysis and legacy clip-plan assumptions.

---

## Migration Requirements

### Requirement 1 — preserve existing runtime value

Existing clip plan fields should not be broken just to satisfy a cleaner architecture.

### Requirement 2 — add a compatibility adapter

Recommended implementation file:

```text
orchestrator/legacy_clip_plan_adapter.py
```

This module should:

- read a canonical shot package
- emit a legacy clip-plan-shaped artifact when needed
- keep old prompt/render flows usable during migration

### Requirement 3 — do not bury new logic in old clip-planning files

New shot-planning architecture should live in new modules, not as another layer of special cases in legacy clip planning.

---

## Suggested Future Implementation Files

### New canonical planning files

```text
orchestrator/scene_contracts.py
orchestrator/shot_planning.py
orchestrator/shot_package_writer.py
orchestrator/legacy_clip_plan_adapter.py
```

### Existing files likely to be touched

```text
orchestrator/story_authoring.py
orchestrator/cli.py
orchestrator/prompt_package.py
orchestrator/runner.py
```

---

## Updated Commands

### Current / transitional

- `python -m orchestrator plan-scene <project_slug> --scene <scene_id>`
- `python -m orchestrator plan-clip <project_slug> --scene <scene_id> --clip <clip_id>`

### Preferred future direction

- `python -m orchestrator build-scene-contracts <project_slug> [--scene ...]`
- `python -m orchestrator build-shot-packages <project_slug> [--scene ...]`
- optional compatibility export:
  - `python -m orchestrator export-legacy-clip-plan <project_slug> --scene <scene_id> --shot <shot_id>`

---

## Acceptance

This spec is considered satisfied when:

- useful legacy clip-planning concepts are preserved in the new architecture
- shot packages become the canonical planning artifact
- prompt writing can consume shot packages directly
- existing legacy clip-oriented flows remain usable through an adapter during transition
- the system no longer depends on clip planning being the only bridge between analysis and prompt writing
