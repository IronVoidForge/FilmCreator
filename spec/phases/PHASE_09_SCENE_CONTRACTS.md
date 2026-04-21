# Phase 09 — Scene Production Contracts

## Goal

Convert scenes into structured production-ready contracts.

---

## Inputs

- scene breakdowns
- character bibles
- environment bibles

---

## Outputs

- scene_contract.json
- storyboard markdown
- scene contract index + review index
- scene review queue

---

## Required Fields

- scene_id
- purpose
- emotional_arc
- characters_required
- environments_required
- continuity_constraints
- beat_list

---

## Implementation Files

```
orchestrator/scene_contracts.py
```

---

## Acceptance Criteria

- scenes clearly define production intent
- scenes bridge narrative to shot planning
- scene contracts are reusable as upstream input for shot planning

## Status

- validated via full `princess_of_mars_test` synthesis run
