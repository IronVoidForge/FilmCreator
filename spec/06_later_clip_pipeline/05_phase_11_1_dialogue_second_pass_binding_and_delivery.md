Status: 25%

# Phase 11.1 - Dialogue Second Pass Binding and Delivery

## Goal

Run a second dialogue pass after baseline dialogue extraction to improve scene binding, shot mapping, speaker attribution, and delivery intent without rerunning the whole dialogue timeline from scratch.

---

## Why This Phase Exists

The first dialogue pass is allowed to be conservative. It can leave:

- unresolved speakers
- scene-only bindings
- weak shot assignment
- thin delivery notes

That is acceptable for baseline extraction, but not strong enough for production planning. This second pass exists to repair those weak areas with tighter context and scene-aware evidence.

---

## Inputs

- baseline dialogue timeline
- scene contracts
- scene bindings
- shot packages
- chapter summaries
- relevant character bibles
- dialogue enrichment outputs when available
- previous scene context when current-scene evidence is thin

---

## Outputs

- patched dialogue events
- dialogue second-pass review queue
- delivery and binding confidence updates
- scene-level dialogue binding summaries

---

## Responsibilities

- resolve ambiguous speakers using scene-bound cast instead of chapter-wide guessing
- bind dialogue to scenes first, then to one or more shots
- assign:
  - `primary_shot_id`
  - `supporting_shot_ids`
- improve delivery intent:
  - `delivery_style`
  - `emotion`
  - `volume`
  - `tempo`
  - `subtext` when support exists

---

## Context Rules

- start with the current dialogue event, current scene contract, current scene bindings, and current shot list
- if the current scene is insufficient, include the previous scene
- if the previous scene is still insufficient, include the previous chapter summary
- do not widen context further unless explicitly required

---

## Repair Rules

- preserve already-good speaker assignments
- preserve already-good shot bindings
- patch only unresolved or low-confidence fields
- never fabricate a canonical speaker outside the scene-bound cast unless the evidence clearly requires it
- do not collapse narration and dialogue into the same category

---

## Implementation Files

```
orchestrator/dialogue_second_pass.py
orchestrator/dialogue_timeline.py
orchestrator/dialogue_enrichment.py
```

---

## Acceptance Criteria

- unresolved speakers decrease materially after the second pass
- scene bindings are stronger than the baseline range-based heuristic
- dialogue-to-shot mapping supports one-to-many shot coverage
- delivery metadata becomes production-usable without overwriting strong existing fields

## Status

- planned

