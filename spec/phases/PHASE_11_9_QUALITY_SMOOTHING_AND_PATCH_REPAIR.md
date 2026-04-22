# Phase 11.9 - Quality Smoothing and Patch Repair

## Goal

Repair low-grade or incomplete artifacts by patching only the missing or weak fields, using narrow context packs, instead of rerunning whole synthesis families.

---

## Why This Phase Exists

Quality grading can already detect:

- `unknown`
- `None`
- `null`
- unresolved canonical ids
- missing prompt data
- thin scene and shot fields

The next step is not always a full rerun. Many artifacts only need a small amount of missing data filled in. This phase performs those focused repairs.

---

## Inputs

- quality rerun queue
- focus fields from grading
- source artifact JSON
- scene contract / scene binding context when relevant
- chapter summary
- relevant character or environment bible
- previous scene or previous chapter context when required

---

## Outputs

- patched artifacts
- smoothing run manifest
- smoothing review queue
- repair notes / provenance updates

---

## Repair Rules

- patch only fields named in `focus_fields`
- preserve existing good fields
- never overwrite clearly supported/book-backed fields with speculative values
- allow generated or inferred fields to be completed best-effort
- escalate context in this order:
  - artifact itself
  - direct dependencies
  - current scene
  - previous scene
  - previous chapter

---

## Family Guidance

- characters
  - fill missing generated visual buckets only

- environments
  - fill missing generated spatial and material buckets only

- scenes
  - repair missing binding fields, unresolved scene-level cast/environment choices, and thin production-intent fields

- shots
  - repair missing shot-level fields, but inherit scene environment from scene bindings rather than choosing a new one

- dialogue
  - repair missing scene binding, missing primary/supporting shot mapping, and thin delivery metadata

---

## Implementation Files

```
orchestrator/quality_smoother.py
orchestrator/quality_grading.py
orchestrator/selective_rerun.py
```

---

## Acceptance Criteria

- low-grade artifacts can be improved without full-family reruns
- smoothing uses tight context packs
- repaired artifacts retain prior strong fields
- scene and shot environment continuity is preserved during repair

## Status

- planned
