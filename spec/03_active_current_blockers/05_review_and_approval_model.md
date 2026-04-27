Status: 55%

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
- request_regeneration_with_notes
- shortlist_for_operator
- mark_reviewed_no_decision

---

## Rework Semantics

A rework request should include:

- target artifact id
- reason
- optional fields or sections needing revision
- whether downstream artifacts should be marked stale immediately

For visual candidates, a rework request should also support:

- structured rejection tags
- freeform operator notes
- source frame id if the candidate came from image-to-image
- whether to keep the same source frame
- whether to keep the same seed
- whether to generate more candidates before changing upstream artifacts

The LLM may be asked to write repair prompt details from these notes, but that repair output is a generation variant. It should not rewrite the canonical source artifact unless the operator explicitly requests upstream repair.

## Visual Candidate Review Queues

Later still/video phases need candidate queues in addition to synthesis review queues:

```text
projects/<project_slug>/06_reviews/reference_candidates_queue.json
projects/<project_slug>/06_reviews/frame_candidates_queue.json
projects/<project_slug>/06_reviews/video_takes_queue.json
projects/<project_slug>/06_reviews/repair_requests/
```

For Phase 14 frame candidates, the queue item must record whether the candidate blocks downstream I2V generation. A dependent next-shot opener should stay blocking until one candidate is approved.

For future automatic image review, the queue may include an `auto_review` object with scores and reject reasons, but human approval remains required for production assets unless a future explicit lazy mode is enabled.

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
- a visual candidate can be rejected with tags and notes
- a regeneration request can preserve the original canonical prompt and create a repair variant

