Status: 60%

# Phase 14/16 - Review Queue, Prompt Repair, and Auto Image Review

## Goal

Define how FilmCreator presents generated visual candidates for human review, captures what is wrong, asks the LLM to produce repair prompt details, and later uses automatic image review to reduce the number of low-quality candidates a human must inspect.

This spec covers still candidates from Phase 14 and video candidates from Phase 16.

## Phase Placement

Review queue and repair apply after candidate generation:

- Phase 12 character reference candidates
- Phase 13 environment reference candidates
- Phase 14 opening keyframe / alternate-angle opener candidates
- Phase 16 video take candidates

Auto image review is later and optional. It should not be required for the first full pipeline validation pass.

## Inputs Already Available By Phase

Phase 12/13 candidate review has:

- reference generation prompt package
- candidate image path
- candidate metadata
- source character/environment bible
- descriptor fields
- prompt variant / booster metadata

Phase 14 candidate review has:

- shot package
- prepared shot prompt package
- approved refs when available
- candidate still path
- frame strategy
- source frame metadata when image-to-image was used
- workflow id and seed

Phase 16 video review has:

- approved opener frame
- I2V prompt package
- video take path
- source opener metadata
- duration / frame count
- workflow id and seed

No review phase should need to re-read the full source book. It should use the already-produced artifacts and allow a targeted repair note when those artifacts are insufficient.

## Review Queue Artifact

Suggested root:

```text
projects/<project>/06_reviews/
```

Suggested files:

```text
06_reviews/reference_candidates_queue.json
06_reviews/frame_candidates_queue.json
06_reviews/video_takes_queue.json
06_reviews/selected/
06_reviews/rejected/
06_reviews/repair_requests/
```

Queue item shape:

```json
{
  "review_item_id": "CH001_SC001_SH002_OPENER_C003_REVIEW",
  "phase": "phase_14_frame_generation",
  "artifact_type": "opening_keyframe_candidate",
  "candidate_id": "CH001_SC001_SH002_OPENER_C003",
  "candidate_path": "projects/.../candidate_003.png",
  "scene_id": "CH001_SC001",
  "shot_id": "SH002",
  "strategy": "previous_last_frame_reframe",
  "source_frame_id": "CH001_SC001_SH001_LAST_APPROVED",
  "status": "unreviewed",
  "priority": "normal",
  "blocking_downstream": true,
  "suggested_action": "approve_one_or_request_regen"
}
```

## Human Review Actions

The operator should be able to:

- approve candidate
- approve and lock candidate
- reject candidate
- request more candidates
- request prompt repair and regenerate
- mark candidate as usable but not preferred
- compare candidates from different seeds or prompt variants

For dependent I2V sequences, approving the opener may unblock the next video generation job.

## Rejection Tags

Use structured tags so repair can be targeted:

```text
wrong_identity
wrong_costume
wrong_environment
wrong_camera_angle
wrong_zoom_or_crop
bad_reframe
bad_composition
too_dark
too_bright
weak_face
bad_hands
missing_key_prop
continuity_break
too_generic
style_drift
motion_bad
video_artifacts
```

The operator can add freeform notes:

```text
The character is correct, but the camera needs to be lower and closer.
Keep the same body pose and room layout from the source frame.
Do not turn this into a wide shot.
```

## LLM Prompt Repair

When the operator asks for repair, the system should send the LLM a narrow context packet:

- original prompt package
- candidate metadata
- rejection tags
- operator notes
- relevant descriptor fields
- source frame role when applicable

The LLM should not rewrite the canonical source artifacts. It should produce a repair patch for the next generation prompt.

Repair output:

```json
{
  "repair_id": "CH001_SC001_SH002_OPENER_REPAIR_001",
  "target_candidate_id": "CH001_SC001_SH002_OPENER_C003",
  "repair_summary": "Tighten camera to lower medium-close reverse angle while preserving pose and room layout.",
  "positive_prompt_additions": [
    "lower camera height, medium-close reverse angle",
    "preserve the same pose, wardrobe, prop positions, and room layout from the source frame"
  ],
  "negative_prompt_additions": [
    "wide establishing shot",
    "changed costume",
    "different room layout"
  ],
  "fields_to_emphasize": [
    "camera_angle",
    "shot_size",
    "continuity_from_previous_shot"
  ],
  "regeneration_strategy": "same_source_frame_new_seed"
}
```

Repair prompt variants are temporary generation prompts. They do not replace the canonical prepared prompt package unless a separate upstream artifact repair is explicitly requested.

## Automatic Image Review

Auto image review is a later assist, not the first gate.

Purpose:

- generate many candidates cheaply
- automatically reject obvious failures
- rank the remaining candidates
- present only the best subset to the operator

Auto review should classify:

- subject visible
- identity likely correct
- environment likely correct
- camera roughly matches request
- frame is not blank/corrupt
- image is not unreadably dark/bright
- major anatomy or artifact issues
- continuity compatibility with source frame when applicable

Auto review result:

```json
{
  "auto_review_status": "shortlisted",
  "auto_score_100": 82,
  "auto_reject_reasons": [],
  "rubric": {
    "identity": "good",
    "environment": "fair",
    "camera_match": "good",
    "composition": "good",
    "continuity": "fair",
    "image_quality": "good"
  }
}
```

Hard rule:

- Auto review may shortlist or reject obvious failures.
- Auto review must not approve final production assets without human confirmation unless the operator explicitly enables a future lazy mode.

## First Implementation Boundary

Do first:

- human review queues
- approve/reject/regenerate with notes
- LLM repair patch generation
- candidate metadata preserving source frame / seed / prompt variant

Do later:

- automatic vision review
- lazy mode auto-selection
- GUI review surface

## Acceptance Criteria

- The operator can choose one approved still from several candidates.
- The operator can explain what is wrong and request a repair prompt.
- Repair prompts preserve canonical prompt packages and write variant metadata.
- Dependent next-shot I2V jobs stay blocked until a required opener is approved.
- Future auto review can rank candidates without replacing human final approval.
