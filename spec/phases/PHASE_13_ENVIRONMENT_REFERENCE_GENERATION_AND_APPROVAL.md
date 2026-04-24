# Phase 13 - Environment Reference Generation and Approval

## Goal

Generate approved environment reference assets from prompt-preparation bundles using a staged approach that preserves spatial identity before expanding lighting and sub-location variants.

---

## Why This Phase Exists

The project now has stable environment bibles, descriptor enrichment, prompt-preparation bundles, and review/approval plumbing.

What is still missing is the first reusable environment-reference generation workflow that:

- starts from a strong establishing view
- expands to a stable spatial reference
- derives detail, lighting, and mood variants from the approved canonical environment
- preserves approval and lock state for downstream use

This phase is intentionally about **reference-sheet generation and approval**, not shot keyframes or final scene renders.

---

## Inputs

- environment bibles
- environment descriptors
- prompt-preparation bundles for environment references
- approval / review metadata
- existing canonical environment refs when present
- style presets and local generation workflows

---

## Outputs

- environment reference candidate images
- per-environment review queue entries
- approved environment reference manifests
- locked canonical environment refs
- supporting variants derived from the approved canonical establishing view

---

## Staged Generation Plan

### Test Slice Mode

For validation runs, the stage should support a small test slice:

- generate `2` establishing-view candidates
- generate `2` spatial-reference candidates from the approved establishing-view set
- generate `2` supporting-variant candidates from the approved spatial-reference set

This is a test flag behavior only. It is meant to exercise the approval gates and reveal quality issues quickly without running the full environment catalog.

The approval gates still apply in test slice mode:

- establishing-view approval is required before spatial image-to-image generation
- spatial-reference approval is required before supporting variants
- rejected candidates are preserved
- canonical approved refs are still lockable

### Stage 1 - Text-to-Image Establishing View

Start with a text-to-image establishing image for the environment.

Purpose:

- establish spatial identity
- confirm scale, layout, and landmark interpretation
- create the first canonical approval target

Preferred output:

- wide establishing view
- clear layout read
- minimally ambiguous geography

### Stage 2 - Image-to-Image Spatial Reference

Once an establishing view is approved, derive a stable spatial reference using the approved image as the source.

Purpose:

- lock the environment’s spatial identity
- preserve layout and major landmarks
- reduce drift before variant generation

Preferred output:

- medium spatial view or stabilized wide
- identity-preserving image-to-image pass
- minimal layout drift

### Stage 3 - Image-to-Image Supporting Variants

Once the spatial reference is approved, derive supporting variants from the approved canonical environment.

Purpose:

- produce detail, lighting, mood, and sub-location references
- keep the environment canon stable across variants

Preferred outputs:

- detail focus
- sub-location or prop focus
- lighting variant
- time-of-day variant

---

## Prompt Families This Phase Must Cover

- establishing wide
- medium spatial view
- detail focus
- sub-location focus
- lighting variant
- time-of-day variant

---

## Required Fields

Environment generation prompts should include, at minimum:

- display_name
- layout_descriptor
- scale_descriptor
- architecture_descriptor
- landmark_descriptor
- lighting_descriptor
- mood_descriptor
- locked_fields
- reference_mode
- reuse_policy

---

## Approval Rules

- approve the establishing view before using it as the source for spatial image-to-image generation
- approve the spatial reference before using it as the source for supporting variants
- preserve rejected candidates and their review context
- lock the canonical approved refs so they survive downstream reruns

---

## Success Criteria

- one strong establishing environment reference can be generated and approved
- one stabilized spatial reference can be derived from the approved establishing view
- supporting environment variants can be derived from the approved spatial reference
- approval and lock semantics are preserved across reruns
- the same staged workflow can be reused for future projects without book-specific logic

---

## Suggested Implementation Files

- `orchestrator/environment_references.py`
- `orchestrator/reference_assets.py`
- `orchestrator/prompt_preparation.py`
- `orchestrator/cli.py` or the future `orchestrator/cli/` package
