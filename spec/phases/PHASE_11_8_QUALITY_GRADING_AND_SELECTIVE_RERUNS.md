# Phase 11.8 - Quality Grading and Selective Reruns

## Goal

Grade all synthesis outputs for completeness, evidence support, prompt readiness, and inference load, then produce selective rerun manifests for the lowest quality items instead of rerunning the whole project.

---

## Why This Phase Exists

The synthesis pipeline can now produce:

- character bibles
- environment bibles
- scene contracts
- shot packages
- dialogue timelines
- descriptor records
- prompt bundles

Those artifacts are useful, but they are not always equally strong. Some are fully grounded. Some are thin but acceptable. Some depend heavily on LLM inference and should be revisited once more evidence or better synthesis rules exist.

This phase creates a consistent grading layer so the project can answer:

- which outputs are complete enough to keep
- which outputs need review
- which outputs should be regenerated
- which outputs should be left alone because they are already strong or explicitly locked

This is the phase that enables targeted reruns instead of broad, expensive rebuilds.

---

## Design Principle

Do not treat every artifact the same.

Instead:

- score each artifact family using the same rubric
- separate completeness from evidence quality
- separate LLM-heavy inference from source-backed fact coverage
- prefer rerunning only the weak artifacts and their dependents
- preserve locked or reviewed outputs unless a downstream dependency truly requires regeneration

This phase should not invent new canon. It should classify quality and produce actionable rerun plans.

---

## Inputs

- character bibles
- environment bibles
- scene contracts
- shot packages
- dialogue timelines
- descriptor records
- prompt bundles
- review queues
- evidence references and provenance maps
- artifact lifecycle metadata when available
- dependency graphs or stale markers when available

---

## Outputs

- per-artifact grade records
- per-family quality summaries
- low-grade review queues
- selective rerun manifests
- rerun priority lists
- dependency-aware rebuild notes
- grade history for future trend comparison

---

## Grading Model

Each artifact should be scored in a small number of stable dimensions.

### Core Dimensions

- `completeness`
  - how much of the expected schema is filled
  - how many required fields are present
  - how many major fields remain unknown or empty

- `evidence_support`
  - how much of the artifact is grounded in source text, registries, or downstream canon
  - whether the important claims are backed by provenance

- `consistency`
  - whether the artifact contradicts its own source material
  - whether it conflicts with known continuity or sibling artifacts

- `prompt_readiness`
  - how usable the artifact is for later prompt assembly or image generation
  - whether the core visual / narrative instructions are compact and clear

- `inference_load`
  - how much of the artifact depends on LLM judgment rather than explicit source support
  - this is not automatically bad, but high inference load with low evidence should be flagged

### Optional Supporting Dimensions

- `continuity_risk`
- `review_density`
- `dependency_impact`
- `manual_lock_status`

### Suggested Grade Bands

- `A`
  - high completeness
  - strong evidence
  - low contradiction risk
  - safe to reuse as-is

- `B`
  - solid overall
  - small gaps or some inference-heavy areas
  - may need selective improvement, not a full rewrite

- `C`
  - usable but noticeably thin
  - should be queued for review or selective rerun

- `D`
  - weak or incomplete
  - should usually be rerun unless locked or intentionally provisional

- `F`
  - failed, malformed, or unusable
  - must be regenerated or repaired

---

## Rerun Rules

The grading layer should emit a rerun plan rather than immediately changing artifacts.

Recommended rerun triggers:

- completeness below the project threshold
- evidence support below the project threshold
- prompt readiness below the project threshold
- contradiction or continuity risk above the project threshold
- unresolved review flags on a canonical artifact
- stale or dependency-invalid artifacts

Recommended exclusions:

- locked artifacts
- intentionally provisional artifacts that are already marked for later human review
- artifacts that are low evidence but still structurally correct and intentionally sparse

The rerun manifest should identify:

- artifact type
- canonical id
- chapter / scene / shot / item scope when relevant
- reason for rerun
- suggested rerun stage
- dependency fan-out

---

## Artifact Contract

Each graded record should carry:

- canonical_id
- display_name
- entity_type
- source_phase
- grade_band
- completeness_score
- evidence_support_score
- consistency_score
- prompt_readiness_score
- inference_load_score
- review_status
- rerun_recommended
- rerun_scope
- rerun_reason
- evidence_refs
- dependency_refs
- lock_status
- grade_notes

Scores can be represented as:

- normalized integers from `0` to `100`
- or a fixed `0.0` to `1.0` scale

The exact scale should remain stable across phases.

---

## Review Behavior

This phase should make it easy to answer three separate questions:

1. Is the artifact good enough to keep?
2. If not, why not?
3. What is the smallest useful rerun that can improve it?

That means the output should avoid vague warnings and instead point to concrete remediation categories such as:

- fill missing visual buckets
- tighten evidence sourcing
- remove contradictory or stale claims
- re-run downstream prompt preparation only
- re-run the upstream synthesis stage for this artifact family

---

## Suggested Rerun Scope Levels

The rerun manifest should support more than one level of rebuild:

- single artifact
- entity family
- chapter-scoped cluster
- scene-scoped cluster
- shot chain
- dependent prompt bundle only

This allows the pipeline to rerun the minimum needed surface area.

---

## Artifact Locations

Likely locations:

- `02_story_analysis/grading/`
- `02_story_analysis/grading/reports/`
- `02_story_analysis/grading/manifests/`
- `02_story_analysis/grading/review/`

Potential downstream rerun queue locations:

- `02_story_analysis/reruns/`
- `03_prompt_packages/reruns/`

---

## Implementation Files

Likely orchestration additions:

- `orchestrator/quality_grading.py`
- `orchestrator/selective_rerun.py`
- `orchestrator/cli.py`

Potential launcher:

- `launchers/multi_chapter/run_quality_grading_and_selective_reruns.bat`

---

## Acceptance Criteria

- every major synthesis family can be graded consistently
- low-quality artifacts can be identified without rerunning everything
- rerun manifests are specific enough to drive targeted rebuilds
- locked artifacts are protected from unnecessary regeneration
- quality grades can be compared across runs over time

---

## Status

- `implemented`
- evidence: the `grade-artifacts` CLI now scans the synthesis outputs, scores them, and writes a project-grade index plus rerun queue without modifying the source artifacts
