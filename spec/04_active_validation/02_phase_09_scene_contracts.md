Status: 85%

# Phase 09 - Scene Production Contracts

## Goal

Convert scenes into structured production-ready contracts that act as the binding authority for cast, place, and scene-local dialogue context.

---

## Inputs

- scene breakdowns
- character bibles
- environment bibles
- character index / registry candidates
- environment index / registry candidates
- librarian retrieval

---

## Outputs

- scene_contract.json
- storyboard markdown
- scene contract index + review index
- scene review queue
- future environment request queue entries when the indexed library is insufficient

---

## Required Fields

- scene_id
- purpose
- emotional_arc
- characters_required
- environments_required
- resolved_characters
- resolved_environment
- environment_binding_mode
- candidate_environment_ids
- future_environment_requests
- continuity_constraints
- beat_list

---

## Binding Rules

- The scene contract must choose characters from the character index whenever possible.
- The scene contract must choose environments from the environment index whenever possible.
- The scene contract must not invent a canonical environment id when no indexed environment fits.
- If the scene appears to take place inside a more specific area of a known environment, emit:
  - `subenvironment_label`
  - `subenvironment_parent_environment_id`
- If the scene appears to require an environment not present in the current index, emit a future environment request rather than a fake canonical binding.
- Default to one canonical environment per scene.
- Only allow multiple environment bindings inside a scene when the scene explicitly changes place across beats.

---

## Prompt / Schema Updates Required

- The scene-contract synthesis prompt should become selector-first rather than freeform naming.
- Prompt packets should include:
  - character candidate ids and display names
  - environment candidate ids and display names
  - explicit instruction to choose from candidates first
  - explicit instruction to emit a future environment request instead of fabricating canon
- The scene contract JSON schema should carry the new binding fields so downstream phases can inherit rather than guess.

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
- the chosen environment is authoritative at scene level
- cast and environment choices come from indexed candidates unless explicitly marked as future requests
- freeform scene labels do not masquerade as canonical bindings

## Status

- validated for baseline synthesis
- next revision required: strengthen selector-first binding and future environment request emission

