# Phase 11 - Dialogue, Timing, and Edit Timeline

## Goal

Add temporal structure and dialogue alignment to scene and shot sequences, and carry extracted dialogue into downstream production artifacts.

## Current Status

Validated for baseline dialogue extraction and timeline writing. The next revision is about stronger scene-first and shot-second binding.

---

## Inputs

- shot packages
- scene contracts
- scene bindings
- chapter analysis outputs
- dialogue-bearing scene or clip notes when available

---

## Outputs

- dialogue_timeline.json
- edit_timeline.json
- clip dialogue notes
- shot-to-dialogue bindings
- scene-bound dialogue events
- clip-level dialogue text or excerpt artifacts

---

## Required Fields

### Dialogue

- speaker
- text
- scene_id
- shot_id
- supporting_shot_ids
- timing_estimate
- clip_id
- dialogue_source_ref

### Timeline

- shot order
- duration
- transitions

---

## Binding Rules

- Dialogue must bind to scenes first.
- After scene binding, each dialogue line must map to one or more shots.
- Each line should carry:
  - `primary_shot_id`
  - `supporting_shot_ids`
- Dialogue mapping may use adjacent lines and nearby scene context, but it should not bypass the scene contract hierarchy.

---

## Prompt / Schema Updates Required

- Dialogue extraction and timeline prompts should explicitly target scene binding before shot mapping.
- Downstream prompt-preparation should be able to consume delivery and shot-binding metadata without re-deriving line placement.

---

## Implementation Files

```
orchestrator/dialogue_timeline.py
```

---

## Acceptance Criteria

- dialogue aligns to scenes first, then to shots
- timeline can drive video assembly
