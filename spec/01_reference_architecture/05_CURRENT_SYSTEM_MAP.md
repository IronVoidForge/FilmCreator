Status: 100%

# Current System Map

## Purpose

This document is the current high-level map of FilmCreator as it exists in code now.

Use it when you need to answer:

- what phases exist
- which ones are implemented
- which CLI commands are the real operator surface
- where smart resume fits
- where review, approval, locking, and artifact preservation fit
- which folders are canonical

This is a current-state map, not a historical roadmap.

---

## Canonical Project Shape

At a high level, active projects currently center on:

```text
projects/<project_slug>/
  01_source/
  02_story_analysis/
  03_prompt_packages/          (prepared prompt packages when present)
  03_reference_assets/         (Phase 12/13 queues, candidates, approvals, generation prompts)
  04_generated_assets/         (generated media output area in current Princess tree)
  05_scenes/
```

Important practical note:

- older specs and some legacy files still mention `04_references/`
- current reference-generation code uses `03_reference_assets/`

---

## Current Phase Stack

The current working stack is best understood like this:

1. Story analysis
2. Character taxonomy
3. Identity refinement
4. Character bibles
5. Environment bibles
6. Visual fallbacks
7. Scene contracts
8. Scene bindings
9. Shot packages
10. Dialogue timeline
11. Descriptor enrichment
12. Prompt preparation
13. Quality grading
14. Character references (Phase 12)
15. Environment references (Phase 13)

The first thirteen phases are the current production pipeline.

Phases 14 and 15 are reference-generation and approval layers that sit after prompt preparation and quality grading.

Later render/video stages are still tracked in specs but are not the main implemented operator path yet.

---

## Current Operator Surface

The main operator surface is now the Python CLI, with BATs acting as wrappers or fallback launch points.

Primary entrypoints:

```text
python -m orchestrator menu
python -m orchestrator project-status
python -m orchestrator run-production
python -m orchestrator run-story-analysis
python -m orchestrator run-quicktest-composite
python -m orchestrator run-production-range
python -m orchestrator clear-production
```

Reference-generation commands already in the CLI:

```text
python -m orchestrator plan-character-references
python -m orchestrator generate-character-references
python -m orchestrator register-character-reference-candidate
python -m orchestrator approve-character-reference
python -m orchestrator reject-character-reference
python -m orchestrator lock-character-reference

python -m orchestrator plan-environment-references
python -m orchestrator generate-environment-references
python -m orchestrator register-environment-reference-candidate
python -m orchestrator approve-environment-reference
python -m orchestrator reject-environment-reference
python -m orchestrator lock-environment-reference
```

The current menu/operator layer lives primarily in:

- `orchestrator/cli.py`
- `orchestrator/pipeline_menu.py`
- `orchestrator/production_pipeline.py`
- `orchestrator/production_status.py`
- `orchestrator/production_cleanup.py`
- `orchestrator/production_run_state.py`

---

## Smart Resume

Smart resume is no longer just a BAT concern.

It currently lives in:

- `orchestrator/overnight_pipeline_resume_check.py`

It is used by:

- the trusted overnight resume BAT
- production status reporting
- production pipeline planning / resume routing

Current role:

- inspect on-disk artifacts
- detect fake-success or partial outputs
- return the first incomplete stage

Current validation is strongest for:

- visual fallbacks
- descriptor enrichment
- prompt preparation
- quality grading

This means smart resume is already part of the CLI-era architecture, even though the trusted BAT still uses it too.

---

## Prompt Packages

Prompt packages are a canonical contract between authoring and downstream generation.

Core implementation:

- `orchestrator/prompt_package.py`
- `orchestrator/prompt_preparation.py`

Current schema expectations:

- `Title`
- `ID`
- `Purpose`
- `Workflow Type`
- `Positive Prompt`
- `Negative Prompt`
- `Inputs`
- `Continuity Notes`
- `Repair Notes`
- `Sources`

`Repair Notes` is now required as a heading.
The section may be empty, but older prompt markdown without that heading is no longer current-schema-valid.

---

## Reference Assets

Phase 12 and Phase 13 now use a structured reference-asset system.

Core implementation:

- `orchestrator/reference_assets.py`
- `orchestrator/character_references.py`
- `orchestrator/environment_references.py`

Current behavior includes:

- planning queues
- chapter filtering
- candidate registration
- approval
- rejection
- locking
- approved manifests
- generation prompt package writing
- prompt variant and booster metadata

Canonical reference-asset root:

```text
projects/<project_slug>/03_reference_assets/
```

---

## Artifact Lifecycle / Reuse

The minimal shared lifecycle core is now implemented.

Core implementation:

- `orchestrator/artifact_lifecycle.py`

Current coverage:

1. Approved reference assets
2. Prepared prompt package lifecycle sidecars

What it provides:

- `ArtifactMetadata`
- `is_locked(...)`
- `mark_stale(...)`
- `merge_preserving_locked_fields(...)`
- `write_artifact_with_metadata(...)`

Current practical guarantees:

- locked approved references survive ordinary later approvals
- locked prompt packages survive normal reruns without markdown overwrite

This is the current foundation for broader reuse protection across later artifact families.

---

## Review / Approval / Locking

Review and approval are partially implemented already, even though the full generic review model spec is not finished.

Currently real in code:

- reference candidate approval
- reference candidate rejection
- reference candidate locking
- approved reference manifests
- lifecycle-aware preservation of locked approved references

This means reference assets are currently the most mature review-and-lock artifact family.

---

## Launchers vs CLI

The migration direction is:

- CLI is the long-term source of truth
- BATs are wrappers, transition tools, or trusted fallback entrypoints

Still-relevant launchers:

- trusted overnight resume BAT
- cleanup launchers
- `quicktest_phase/`
- `menu/` wrappers

Archived/obsolete launchers are no longer the main execution model.

In particular, old sentinel-only resume launchers should not be treated as trustworthy.

---

## Testing Status

The project now has focused non-destructive coverage around several cross-cutting systems:

- CLI/menu/operator routing
- production planning / status / cleanup
- Phase 12/13 reference-generation static validation
- artifact lifecycle core
- prompt package lifecycle sidecars
- smart resume validation
- prompt package schema enforcement

This means a meaningful amount of operator and schema hardening can now be tested without running Comfy or rerunning the full pipeline.

---

## Current Truths

If you need the short version of how to think about the project right now:

1. The CLI is now the primary control surface.
2. Smart resume belongs to the CLI era, not just BATs.
3. Prompt packages are a strict schema contract now.
4. Reference assets use `03_reference_assets`, not old `04_references`.
5. Artifact lifecycle protection has started and is already real for prompt packages and reference assets.
6. Review/approval/locking is most mature in Phase 12/13 reference assets.
7. The broad later render/video pipeline is still a later-system area, not the main currently validated operator path.

---

## Related Specs

- `00_SPEC_STATUS_INDEX.md`
- `01_reference_architecture/03_CLI_PIPELINE_ORCHESTRATOR_SPEC.md`
- `03_active_current_blockers/01_smart_resume_validation.md`
- `03_active_current_blockers/02_artifact_lifecycle_and_reuse.md`
- `03_active_current_blockers/05_review_and_approval_model.md`
- `04_active_validation/01_prompt_package_schema.md`
- `05_reference_generation_next/01_phase_12_character_sheet_generation_and_approval.md`
- `05_reference_generation_next/02_phase_13_environment_reference_generation_and_approval.md`
