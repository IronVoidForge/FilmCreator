# Phase 11 — Dialogue, Timing, and Edit Timeline

## Goal

Add temporal structure and dialogue alignment to shot sequences, and carry extracted dialogue into clip-level artifacts for downstream assembly.

---

## Inputs

- shot packages
- scene contracts
- chapter analysis outputs
- dialogue-bearing scene or clip notes when available

---

## Outputs

- dialogue_timeline.json
- edit_timeline.json
- clip dialogue notes
- shot-to-dialogue bindings
- clip-level dialogue text or excerpt artifacts

---

## Required Fields

### Dialogue

- speaker
- text
- shot_id
- timing_estimate
- clip_id
- dialogue_source_ref

### Timeline

- shot order
- duration
- transitions

---

## Implementation Files

```
orchestrator/dialogue_timeline.py
```

---

## Acceptance Criteria

- dialogue aligns to shots
- timeline can drive video assembly
