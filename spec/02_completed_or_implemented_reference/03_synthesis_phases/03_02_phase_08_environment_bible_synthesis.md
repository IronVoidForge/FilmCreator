# Phase 08 — Environment Bible Synthesis

## Goal

Create canonical, reusable environment definitions for production.

---

## Inputs

- environment registries
- chapter descriptions
- scene usage
- continuity summaries

---

## Outputs

- environment bible markdown
- environment bible JSON

---

## Required Fields

- canonical_id
- display_name
- environment_type
- visual_summary
- layout_notes
- lighting
- mood
- recurring_elements
- constraints

---

## Implementation Files

```
orchestrator/environment_bible.py
```

---

## Acceptance Criteria

- consistent environment descriptions across scenes
- reusable references for shot planning

---

## Status

- `validated`
- evidence: `synthesize-environment-bibles` is available through `orchestrator/cli.py`, `orchestrator/environment_bible.py` exists, and the authoring/full-book launchers already route through this phase; full reruns have produced stable environment bible artifacts and review queues
- next revision required: keep tightening hierarchy-aware environment reuse and chapter-local alias resolution
