# Review and Approval Model

## Purpose

Define how human review, approval, rejection, locking, and rework requests work across FilmCreator artifacts.

This spec extends the existing render-stage review ideas upward into:

- character bibles
- environment bibles
- scene contracts
- shot packages
- dialogue timelines
- generated asset bundles

---

## Design Principles

### Review must happen at natural breakpoints

The pipeline should not force users to inspect every low-level artifact in real time.
Instead, it should present review at natural boundaries.

### Approval is explicit

An artifact should not be treated as approved just because it exists.

### Rejection should preserve context

Rejected artifacts should not disappear.
They should remain available for audit and comparison.

### Locked artifacts survive reruns

Once an artifact is approved and locked, normal reruns should not overwrite it.

---

## Review Breakpoints

Recommended breakpoints:

1. After chapter analysis
2. After character and environment bible synthesis
3. After scene contract generation
4. After shot planning
5. After dialogue timeline generation
6. After prompt-preparation and reference-pack generation
7. After character, environment, and key-item reference generation
8. After keyframe generation
9. After audio generation
10. After video assembly

---

## Approval States

Recommended states:

- `unreviewed`
- `reviewed`
- `approved`
- `rejected`
- `approved_locked`

---

## Review Queue Artifacts

Suggested locations:

```text
projects/<project_slug>/reviews/character_queue.json
projects/<project_slug>/reviews/environment_queue.json
projects/<project_slug>/reviews/key_item_queue.json
projects/<project_slug>/reviews/scene_queue.json
projects/<project_slug>/reviews/shot_queue.json
projects/<project_slug>/reviews/audio_queue.json
projects/<project_slug>/reviews/video_queue.json
```

Suggested fields:

- artifact_id
- artifact_type
- reason_for_review
- severity
- current_status
- suggested_action
- downstream_impact

---

## Review Actions

Recommended actions:

- approve
- approve_and_lock
- reject
- request_rework
- mark_reviewed_no_decision

---

## Rework Semantics

A rework request should include:

- target artifact id
- reason
- optional fields or sections needing revision
- whether downstream artifacts should be marked stale immediately

---

## Suggested Implementation Files

```text
orchestrator/review_queue.py
orchestrator/artifact_lifecycle.py
orchestrator/review_tools.py
```

---

## Acceptance Criteria

- at least one synthesis artifact can be reviewed and approved
- approved artifacts can be locked
- rejections are preserved with context
