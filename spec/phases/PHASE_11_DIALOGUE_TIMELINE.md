# Phase 11 — Dialogue, Timing, and Edit Timeline

## Goal

Add temporal structure and dialogue alignment to shot sequences.

---

## Inputs

- shot packages
- scene contracts

---

## Outputs

- dialogue_timeline.json
- edit_timeline.json

---

## Required Fields

### Dialogue

- speaker
- text
- shot_id
- timing_estimate

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
