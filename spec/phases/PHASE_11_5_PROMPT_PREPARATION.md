# Phase 11.5 - Prompt Preparation and Reference Pack Assembly

## Goal

Prepare compact, generation-ready prompt bundles for reference-sheet work and downstream production prompts without mutating upstream bibles or shot contracts.

---

## Why This Phase Exists

The project already has stable character bibles, environment bibles, scene contracts, and shot packages.

What is still missing is a dedicated bridge layer that:

- turns those contracts into prompt-ready bundles
- fans out reference variants for different angles, zooms, and composition needs
- keeps image-to-image consistency guidance tied to canonical traits
- avoids duplicating prompt construction logic in every later phase
- stays compatible with downstream ComfyUI prompt enhancement passes

This phase is intentionally about prompt preparation, not new world analysis.

---

## Inputs

- character bibles
- environment bibles
- scene contracts
- shot packages
- continuity state and review notes
- style profiles and generation presets
- existing prompt-package schema helpers
- existing shared prompt draft builders

---

## Outputs

- per-character reference prompt bundles
- per-environment reference prompt bundles
- per-shot production prompt bundles
- angle and zoom variant prompt bundles
- image-to-image consistency prompt bundles
- prompt package indexes
- prompt review queues
- reuse fingerprints for prompt bundles

---

## Prompt Families This Phase Must Cover

### Character Reference Prompt Families

- front view
- 3/4 view
- profile view
- back view
- full-body neutral
- bust or portrait
- action pose
- expression sheet

### Environment Reference Prompt Families

- establishing wide
- medium spatial view
- detail or prop focus
- interior layout
- exterior geography or topography
- lighting variant
- time-of-day variant

### Shot / Production Prompt Families

- primary shot prompt
- keyframe prompt
- alternate-angle prompt
- tighter zoom prompt
- interval or continuation prompt
- image-to-image correction prompt
- consistency repair prompt

### ComfyUI Prompt Enhancement Handling

- prompt-enhancer pass input
- prompt-enhancer pass output
- compact base prompt for enhancer expansion
- enhancer-safe negative prompt

---

## Required Fields

These bundles should continue to use the existing Markdown prompt-package contract, with prompt-prep-specific inputs added as needed.

### Core Fields

- title
- id
- purpose
- workflow type
- positive prompt
- negative prompt
- inputs
- continuity notes
- sources

### Prompt-Prep Inputs

- asset_id or shot_id
- source_artifact_ids
- reference_mode
- angle_profile
- zoom_profile
- lens_family
- composition_lock
- trait_lock
- image_to_image_source
- change_budget
- reuse_policy
- variant_policy
- review_notes
- prompt_enhancer_mode
- prompt_enhancer_profile

---

## Hierarchy Rules

- Do not mutate the upstream character bible, environment bible, scene contract, or shot package when preparing prompt bundles.
- Use the canonical bibles and contracts as source material, not as replaceable prompt text.
- Keep each prepared prompt compact enough to remain usable in local generation workflows.
- Prefer stable, reusable prompt families over one-off hand-authored prompt text.
- Keep main prompt bundles separate from review-only or ambiguous variant bundles.
- Keep the base prompt compact and descriptive enough for ComfyUI text prompt enhancers to expand without losing canon.
- Prefer named source metadata over named entities in the prompt body unless the on-screen text itself requires the proper noun.

---

## Artifact Locations

Use the existing `03_prompt_packages/` hierarchy where possible, with prompt-prep fan-out organized by asset or shot id.

Likely locations:

- `03_prompt_packages/characters/<asset_id>/`
- `03_prompt_packages/environments/<asset_id>/`
- `03_prompt_packages/scenes/<scene_id>/<clip_id>/`
- `03_prompt_packages/keyframes/<scene_id>/<clip_id>/`

If a dedicated reference-pack subtree becomes necessary later, add it only as a clear sub-hierarchy rather than scattering prompt drafts across unrelated folders.

---

## Implementation Files

Existing helpers to reuse:

- `orchestrator/prompt_package.py`
- `orchestrator/features/authoring/shared_prompts.py`
- `orchestrator/features/authoring/packet_parser.py`

Likely new orchestration layer:

- `orchestrator/prompt_preparation.py`
- `orchestrator/cli.py`

Potential launcher:

- `launchers/authoring/run_phase11_5_prompt_preparation.bat`

---

## Acceptance Criteria

- the phase can produce prompt-ready bundles for canonical characters
- the phase can produce prompt-ready bundles for canonical environments
- the phase can produce prompt-ready bundles for shot-level generation needs
- the phase can emit angle, zoom, and image-to-image variant prompts without bloating the prompt contract
- the same upstream contract can feed both reference-sheet generation and later prompt-driven asset generation
- review queues remain separate from main prompt bundles
- reruns reuse unchanged prompt bundles instead of rewriting everything

---

## Status

- `planned`
- evidence: stable bibles, scene contracts, shot packages, and prompt-package parsing already exist, so this bridge layer can now be added cleanly
