Status: 20%

# Phase 11.6 - Key Item Index and Reference Pack Assembly

## Goal

Identify, consolidate, and describe story-significant items that need continuity tracking or future reference-sheet generation.

---

## Why This Phase Exists

Some artifacts are not characters and not environments, but still behave like canonical assets:

- unique rings
- named swords
- distinctive armor sets
- emblems
- tools with repeated plot significance
- relics or devices that must stay visually consistent

These items need their own index so they can be referenced, tracked, and later turned into prompt-ready reference bundles without being lost inside character or environment files.

---

## Inputs

- chapter analysis outputs
- scene contracts
- shot packages
- character and environment bibles where items are mentioned
- continuity summaries
- librarian retrieval
- existing prop / item mentions in markdown sources

---

## Outputs

- key item registry
- per-item markdown reference notes
- per-item JSON contracts
- key item index
- key item review queue
- chapter mention links
- reference-sheet eligibility flags

---

## Required Fields

### Identity

- canonical_id
- display_name
- aliases or alternate names
- item_kind

### Visual and Functional

- stable_visual_summary
- material / construction notes
- functional_role
- recurring appearance notes

### Continuity

- chapter_mentions
- scene_mentions
- unresolved ambiguities
- locked traits

### Provenance

- evidence_refs
- source chapters
- revision history

### Reference Eligibility

- reference_sheet_candidate
- multi_angle_candidate
- image_to_image_candidate
- review_status

---

## Inclusion Rules

- Include items that recur across chapters.
- Include items that need visual consistency for story continuity.
- Include items that are named or clearly canonical in the source material.
- Exclude incidental background props unless they become story-significant later.
- Prefer stable, reusable identifiers over scene-local labels.

---

## Artifact Locations

Likely locations:

- `02_story_analysis/key_items/`
- `02_story_analysis/key_items/indices/`
- `02_story_analysis/key_items/review/`
- `03_prompt_packages/key_items/<item_id>/` if later prompt-prep fan-out is needed

---

## Implementation Files

Likely new orchestration layer:

- `orchestrator/key_item_index.py`
- `orchestrator/cli.py`

Potential launcher:

- `launchers/authoring/run_phase11_6_key_items.bat`

---

## Acceptance Criteria

- repeated story-significant items are indexed consistently
- visually important items have stable descriptive records
- the index can be used later for prompt-preparation and reference-sheet generation
- incidental props do not flood the main index
- review queues remain separate from canonical entries

---

## Status

- `planned`
- evidence: the project already tracks characters, environments, scenes, and shots, so this is the right time to add a dedicated canonical item layer

