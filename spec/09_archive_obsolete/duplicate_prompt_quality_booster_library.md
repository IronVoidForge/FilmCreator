# Deferred: Generic Prompt Quality Booster Libraries

## Purpose

Create reusable, generic prompt booster bundles that can be applied at generation time without changing the canonical base prompt packages.

The base prompt should stay story-specific and clean. Boosters should be optional variations used for A/B testing and quality improvement.

## Design Rule

Boosters are grouped by generation use case, not by story, character, or world.

Use separate libraries for:

- Character references
- Environment references
- Scene/keyframe assembly
- Experimental aesthetic polish

Do not put specific subject details into boosters. Avoid words like `human`, `male`, `princess`, `armor`, `desert`, or any project-specific term. Those belong in the base prompt package.

## Injection Point

Boosters should be injected at generation time when temporary generation prompt packages are written.

Current good injection points:

```text
orchestrator/character_references.py::_write_generation_prompt_package
orchestrator/environment_references.py::_write_generation_prompt_package
```

Future scene/keyframe injection should happen in the Phase 14 generation prompt writer, not in prompt preparation.

## Variation Strategy

Each base prompt can produce controlled variants:

1. `raw` — no boosters
2. `clean` — clean readability bundle only
3. `readability` — clean + subject readability bundles
4. `polish` — clean + readability + light polish bundle

This creates comparable generations while preserving the raw baseline.

## Tracking Requirements

Every generated candidate should eventually record:

```json
{
  "prompt_variant_id": "readability",
  "booster_bundle_ids": [
    "character_reference_clean_v1",
    "character_face_readability_v1"
  ],
  "base_prompt_path": "...",
  "generation_prompt_path": "...",
  "workflow_id": "...",
  "seed": 12345
}
```

Manual rankings can later reveal which bundles actually improve results.

## Library Files

Initial generic libraries live under:

```text
spec/prompt_boosters/character_reference_boosters.json
spec/prompt_boosters/environment_reference_boosters.json
spec/prompt_boosters/scene_assembly_boosters.json
spec/prompt_boosters/experimental_boosters.json
```

These are specs first. Runtime code can later load them into `orchestrator/prompt_boosters.py`.

## First Runtime Plan

1. Add `orchestrator/prompt_boosters.py`.
2. Load bundle JSON by ID.
3. Append selected bundle positive terms to the positive prompt.
4. Append selected bundle negative terms to the negative prompt.
5. Write temporary generation prompt packages with the selected booster metadata.
6. Record booster metadata on generated candidates.

## Non-Goals

- No automatic prompt optimization yet.
- No giant keyword spam lists.
- No subject-specific boosters.
- No permanent mutation of prepared prompt packages.

## Acceptance Criteria

- A raw generation can be compared against boosted variants.
- Character, environment, and scene boosters are separate.
- Candidate metadata records which bundle IDs were used.
- Manual review can later compare bundle performance.
