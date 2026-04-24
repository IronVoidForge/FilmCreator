# Phase 12 - Character Sheet Generation and Approval

## Goal

Generate approved character reference assets from prompt-preparation bundles using a staged approach that preserves identity first, then expands pose and view coverage without breaking canon.

---

## Why This Phase Exists

The project now has stable character bibles, descriptor enrichment, prompt-preparation bundles, and review/approval plumbing.

What is still missing is the first reusable character-reference generation workflow that:

- starts from a strong portrait identity anchor
- expands to a stable full-body reference
- derives alternate views from the approved canonical reference instead of re-inventing identity each time
- preserves approval and lock state for downstream use

This phase is intentionally about **reference-sheet generation and approval**, not broad scene rendering or keyframe production.

---

## Inputs

- character bibles
- character descriptors
- prompt-preparation bundles for character references
- approval / review metadata
- existing canonical character refs when present
- style presets and local generation workflows

---

## Outputs

- character reference candidate images
- per-character review queue entries
- approved character reference manifests
- locked canonical character refs
- supporting variant refs derived from the approved canonical portrait / full-body ref

---

## Staged Generation Plan

This phase should progress in a controlled order so later variants inherit the best approved identity anchor.

### Test Slice Mode

For validation runs, the stage should support a small test slice:

- generate `2` portrait/bust candidates
- generate `2` full-body candidates from the approved portrait set
- generate `2` supporting-view candidates from the approved full-body set

This is a test flag behavior only. It is meant to exercise the approval gates and reveal quality issues quickly without running the full reference catalog.

The approval gates still apply in test slice mode:

- portrait approval is required before full-body image-to-image generation
- full-body approval is required before supporting-view generation
- rejected candidates are preserved
- canonical approved refs are still lockable

### Stage 1 - Text-to-Image Portrait

Start with a text-to-image portrait or bust reference for the character.

Purpose:

- establish face identity
- confirm core age/state/costume interpretation
- create the first canonical approval target

Preferred output:

- portrait or bust frame
- neutral or minimally posed
- clean identity read

### Stage 2 - Image-to-Image Full Body

Once a portrait is approved, generate a full-body reference using the approved portrait as the identity source.

Purpose:

- lock the body proportion
- establish silhouette and costume continuity
- keep the approved face identity stable

Preferred output:

- full-body neutral reference
- identity-preserving image-to-image pass
- minimal pose drift

### Stage 3 - Image-to-Image Supporting Views

Once the full-body reference is approved, derive the remaining views from the approved full-body or portrait reference.

Purpose:

- produce profile, 3/4, back, action, and expression variants
- keep identity stable across all views
- avoid re-solving the character from scratch for every angle

Preferred outputs:

- profile view
- 3/4 view
- back view
- action pose
- expression sheet

---

## Prompt Families This Phase Must Cover

- portrait or bust
- full-body neutral
- profile view
- 3/4 view
- back view
- action pose
- expression sheet

---

## Required Fields

Character generation prompts should include, at minimum:

- display_name
- identity_descriptor
- body_descriptor
- face_descriptor
- costume_descriptor
- posture_descriptor
- expression_descriptor
- locked_fields
- reference_mode
- reuse_policy

---

## Approval Rules

- approve the portrait before using it as the source for full-body image-to-image generation
- approve the full-body reference before using it as the source for supporting view variants
- preserve rejected candidates and their review context
- lock the canonical approved refs so they survive downstream reruns

---

## Success Criteria

- one strong portrait identity anchor can be generated and approved
- one full-body reference can be derived from the approved portrait
- additional views can be derived from the approved full-body reference
- approval and lock semantics are preserved across reruns
- the same staged workflow can be reused for future projects without book-specific logic

---

## Suggested Implementation Files

- `orchestrator/character_references.py`
- `orchestrator/reference_assets.py`
- `orchestrator/prompt_preparation.py`
- `orchestrator/cli.py` or the future `orchestrator/cli/` package
