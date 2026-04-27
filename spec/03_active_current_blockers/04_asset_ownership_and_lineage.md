Status: 45%

# Asset Ownership and Lineage

## Purpose

Define a clean ownership model for FilmCreator so the relational database and file hierarchy do not collapse into spaghetti.

This spec is the canonical guide for:

- what is a structural child
- what is a shared asset
- what should be linked, not nested
- how prompts, dialogue, and reference sheets inherit lineage

---

## Core Principle

Not every important entity should become a parent/child folder or a direct foreign-key child.

Use structural ownership only where the hierarchy is real:

- project
- chapter
- scene
- shot
- clip

Use shared-asset linkage for things that recur across that hierarchy:

- characters
- environments
- key items
- prompts
- dialogue records
- reference sheets

---

## Structural Ownership Rules

### Project

The project owns:

- all chapters
- all shared assets
- all scene, shot, clip, and prompt artifacts
- all generated media and review records

### Chapter

A chapter owns:

- scene analysis outputs
- chapter summaries
- chapter-level continuity state
- chapter-scoped mentions of shared assets

### Scene

A scene owns:

- scene contracts
- scene storyboard / beat outputs
- shot package generation inputs
- scene-level review records

### Shot

A shot owns:

- shot packages
- keyframe prompt bundles
- alternate angle / zoom bundles
- prompt-prep variants
- shot-specific review records
- explicit shot lineage links to the previous and next shot within the same scene

### Clip

A clip owns:

- legacy render-stage prompt packages
- dialogue bindings
- motion segments
- approval state for generated assets

---

## Shared Asset Rules

Characters, environments, and key items are project-owned shared assets.

They are not direct children of scenes or shots.

Instead, they receive many-to-many links to:

- chapters they appear in
- scenes they appear in
- shots they appear in
- prompt bundles that depend on them
- media assets that depict them

That keeps repeated assets canonical without forcing a fake tree structure.

---

## Key Link Tables

Use link tables instead of scattered nullable columns whenever an entity can appear in many places.

Recommended link classes:

- `asset_mentions`
- `asset_artifact_links`
- `prompt_subject_links`
- `prompt_owner_links`
- `dialogue_bindings`
- `reference_bindings`

These should record:

- asset kind
- asset id
- artifact kind
- artifact id
- relationship type
- source evidence
- confidence or review state

---

## Prompt Ownership Rules

Every prompt package should know:

- who owns it
- what it is primarily about
- which assets it depends on
- what variant role it serves

Prompt packages should not become a pile of nullable foreign keys for every possible asset type.

Use a small owner/subject contract instead:

- owner type
- owner id
- primary subject type
- primary subject id
- variant role
- source fingerprints
- dependency links

This is especially important for:

- keyframe prompt bundles
- reference-sheet prompts
- alternate-angle prompts
- image-to-image repair prompts

Shot prompt bundles should also preserve adjacent-shot lineage explicitly:

- previous shot id
- current shot id
- next shot id

That lets the generation workflow traverse the scene tree without needing direct image-path references in the prompt text.

---

## Dialogue Ownership Rules

Dialogue is not just a timeline entry.

It should also be captured as a clip-level or shot-level record with:

- speaker
- utterance text
- source span
- timing estimate
- binding to the owning clip or shot

That makes dialogue searchable and reusable without hiding it inside a single timeline blob.

---

## Key Item Rules

Key items are canonical shared assets when they:

- recur across chapters
- matter for continuity
- have a stable visible identity
- should later become reference-sheet candidates

Examples:

- unique rings
- signature swords
- distinctive armor sets
- emblems or sigils
- relics or devices

---

## Acceptance Criteria

- characters, environments, and key items remain project-owned shared assets
- scenes own scene contracts and shot planning inputs
- shots own shot packages and keyframe prompt bundles
- clips own dialogue bindings and motion records
- prompts are linked to owners and subjects without a spaghetti of direct foreign keys
- database traversal remains obvious and queryable

