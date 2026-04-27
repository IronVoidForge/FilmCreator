Status: 100%

# Phase 12/13 Real Run Checklist

## Purpose

This is the operator checklist to use once the current Phase 1-11 pipeline run finishes and we are ready to do the first small real Phase 12/13 image-generation slice.

This checklist assumes:

- prompt preparation and quality grading have completed
- smart resume is available from the CLI
- Phase 12/13 static validation, approval flow, locking, and lifecycle protection are already implemented

---

## Before You Start

Run a read-only resume check first:

```powershell
python -m orchestrator resume-check princess_of_mars_test --chapters 2-3
```

Confirm:

- the current run is complete through prompt preparation / quality grading
- there is no unexpected resume failure earlier in the pipeline

Optional richer status view:

```powershell
python -m orchestrator project-status princess_of_mars_test --chapters 2-3
```

---

## Character Reference Validation Slice

Start with one small character slice:

```powershell
python -m orchestrator generate-character-references princess_of_mars_test --chapters 2-3 --variant bust_portrait --limit 1 --test-slice --execute --prompt-variant raw
```

Then compare alternate prompt variants:

```powershell
python -m orchestrator generate-character-references princess_of_mars_test --chapters 2-3 --variant bust_portrait --limit 1 --test-slice --execute --prompt-variant character_clean
python -m orchestrator generate-character-references princess_of_mars_test --chapters 2-3 --variant bust_portrait --limit 1 --test-slice --execute --prompt-variant character_readability
python -m orchestrator generate-character-references princess_of_mars_test --chapters 2-3 --variant bust_portrait --limit 1 --test-slice --execute --prompt-variant character_polish
```

Inspect:

- `projects/princess_of_mars_test/03_reference_assets/characters/*/REFERENCE_CANDIDATES.json`
- `projects/princess_of_mars_test/03_reference_assets/characters/APPROVED_CHARACTER_REFERENCES.json`
- generated prompt packages under `generation_prompts/`

Approve one candidate:

```powershell
python -m orchestrator approve-character-reference princess_of_mars_test --candidate-id <candidate_id>
```

Lock the approved candidate:

```powershell
python -m orchestrator lock-character-reference princess_of_mars_test --candidate-id <candidate_id>
```

Success means:

- a candidate image is registered
- the approved manifest is updated
- the locked approved reference survives normal later approvals

---

## Environment Reference Validation Slice

Run one small environment slice:

```powershell
python -m orchestrator generate-environment-references princess_of_mars_test --chapters 2-3 --variant establishing_wide --limit 1 --test-slice --execute --prompt-variant raw
```

Then compare alternate prompt variants:

```powershell
python -m orchestrator generate-environment-references princess_of_mars_test --chapters 2-3 --variant establishing_wide --limit 1 --test-slice --execute --prompt-variant environment_clean
python -m orchestrator generate-environment-references princess_of_mars_test --chapters 2-3 --variant establishing_wide --limit 1 --test-slice --execute --prompt-variant environment_readability
python -m orchestrator generate-environment-references princess_of_mars_test --chapters 2-3 --variant establishing_wide --limit 1 --test-slice --execute --prompt-variant environment_polish
```

Inspect:

- `projects/princess_of_mars_test/03_reference_assets/environments/*/REFERENCE_CANDIDATES.json`
- `projects/princess_of_mars_test/03_reference_assets/environments/APPROVED_ENVIRONMENT_REFERENCES.json`
- generated prompt packages under `generation_prompts/`

Approve one candidate:

```powershell
python -m orchestrator approve-environment-reference princess_of_mars_test --candidate-id <candidate_id>
```

Lock it:

```powershell
python -m orchestrator lock-environment-reference princess_of_mars_test --candidate-id <candidate_id>
```

---

## What To Check Manually

For both character and environment runs:

- output images are actually produced
- queue entries show the right chapter slice
- prompt variant and booster metadata are present
- approved manifests point at the chosen candidate
- locked candidates remain canonical after normal follow-up operations

---

## If Something Looks Wrong

Use these read-only checks first:

```powershell
python -m orchestrator resume-check princess_of_mars_test --chapters 2-3
python -m orchestrator project-status princess_of_mars_test --chapters 2-3
```

Then inspect:

- `PROMPT_PREPARATION_INDEX.json`
- `VISUAL_FALLBACKS.json`
- `DESCRIPTOR_INDEX.json`
- `QUALITY_GRADE_INDEX.json`

Do not start by rerunning the full upstream pipeline unless the resume checker says an earlier stage is actually incomplete.
