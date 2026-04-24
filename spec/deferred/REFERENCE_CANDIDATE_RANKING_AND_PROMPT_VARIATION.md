# Deferred: Reference Candidate Ranking and Prompt Variation System

## Purpose

Phase 12 and Phase 13 should eventually preserve manual review data across many generations so we can learn which prompt styles, workflow settings, seeds, and quality modifiers produce the best reusable references.

This is deferred because the current priority is validating that generation, review, approval, locking, and downstream reuse work end-to-end.

## Goals

- Preserve every candidate, including rejected candidates.
- Let the user manually rank and tag candidates during review.
- Track prompt text, booster bundle, workflow, seed, model, and key settings for every candidate.
- Make it possible to compare a few hundred generations and identify repeatable winning prompt/settings combinations.
- Keep the system file-first. Do not require SQLite for the first implementation.

## Candidate Review Fields

Each reference candidate should eventually support additional review metadata:

```json
{
  "manual_rank": 1,
  "manual_score": 8,
  "review_decision": "approved | rejected | hold | regenerate",
  "review_tags": [
    "good_face",
    "too_dark",
    "weak_costume_visibility",
    "strong_silhouette",
    "bad_hands"
  ],
  "reviewer_notes": "Strong face, but the shirt blends into shadow.",
  "prompt_style_tags": [
    "studio_reference",
    "clean_lighting",
    "quality_booster_v1"
  ],
  "workflow_id": "still.t2i.klein.distilled",
  "seed": 12345,
  "steps": 20,
  "cfg": null,
  "model": "flux",
  "source_reference_image": "",
  "created_at": "...",
  "reviewed_at": "..."
}
```

## Review Tag Vocabulary

Start with a small controlled vocabulary. Allow freeform notes, but keep common tags consistent.

### Positive Tags

- `good_face`
- `good_identity`
- `good_costume_read`
- `good_body_read`
- `good_silhouette`
- `good_lighting`
- `good_environment_layout`
- `good_spatial_read`
- `good_detail_read`
- `usable_for_downstream`

### Negative Tags

- `too_dark`
- `too_bright`
- `underexposed`
- `overexposed`
- `bad_face`
- `identity_drift`
- `bad_hands`
- `bad_anatomy`
- `weak_costume_visibility`
- `cropped_subject`
- `wrong_age`
- `wrong_species`
- `wrong_environment`
- `muddy_details`
- `overstylized`
- `not_reference_sheet`

## Ranking Behavior

Manual rankings should be per asset and per variant family.

Example:

- John Carter / bust portrait candidate A: rank 1
- John Carter / bust portrait candidate B: rank 2
- John Carter / full body candidate A: rank 1

A lower rank number means better. `manual_score` can use 1-10 for coarse comparison across unrelated subjects.

## Aggregation Reports

Future reporting should answer:

- Which booster bundles appear most often in approved candidates?
- Which negative tags appear most often per workflow?
- Which seeds/settings produce repeatable quality?
- Which prompt families fail most often?
- Which variants are most likely to need regeneration?

Suggested outputs:

```text
03_reference_assets/reports/REFERENCE_CANDIDATE_RANKINGS.json
03_reference_assets/reports/REFERENCE_CANDIDATE_RANKINGS.md
03_reference_assets/reports/PROMPT_STYLE_PERFORMANCE.md
```

## First Implementation Plan

1. Extend candidate JSON records with optional review metadata fields.
2. Add CLI commands:
   - `rank-character-reference`
   - `rank-environment-reference`
   - `tag-reference-candidate`
3. Preserve rejected candidates forever unless manually purged.
4. Add reports that summarize tags, rankings, workflow IDs, seeds, and booster bundle IDs.
5. Later, allow the prompt preparation system to choose booster bundles based on past winning tags.

## Non-Goals For First Pass

- No SQLite.
- No automatic ML ranking.
- No deleting rejected candidates.
- No hidden scoring that replaces user judgment.

## Acceptance Criteria

- Every candidate can be ranked manually.
- Rejected candidates keep their prompt/settings metadata.
- Approved and locked candidates retain review history.
- Reports can show which prompt variations produce the best user-ranked outputs.
