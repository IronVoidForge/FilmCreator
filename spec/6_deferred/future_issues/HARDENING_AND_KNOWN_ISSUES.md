# Future Hardening And Known Issues

## Purpose

This document records current weaknesses that should be improved in future passes, without tying the fixes to any specific book, chapter, or scene.

The goal is to keep the pipeline:

- path-agnostic
- chapter-agnostic
- scene-agnostic
- book-agnostic
- reusable across future projects

---

## Current Issue Classes

### 1. Shot prompt assembly can still leak thin data into prose

Observed failure class:

- missing anchors can produce awkward prompt fragments
- optional fields can collapse into broken clauses
- placeholder-like content can leak into final prompt text

Why this matters:

- prompt text should remain readable even when a source field is missing
- a weak field should route to review, not create malformed output

Generic fix direction:

- keep prompt assembly clause-based
- require validation before rendering
- block or review prompt bundles when critical anchors are missing
- sanitize each clause before join

### 2. Dialogue timeline artifacts may still be structurally thin

Observed failure class:

- some dialogue artifacts contain no events
- some shot-level dialogue outputs are empty by design but still need to grade cleanly
- the grading layer must accept both project-level dialogue timelines and list-shaped shot dialogue artifacts

Why this matters:

- empty or list-shaped dialogue outputs should be handled as valid low-content artifacts, not as exceptions
- the review queue should distinguish between:
  - genuinely missing dialogue
  - intentionally empty dialogue for a shot
  - malformed dialogue payloads

Generic fix direction:

- keep dialogue synthesis tolerant of list-shaped payloads
- grade list payloads as a supported artifact shape
- surface no-event dialogue as a quality issue, not a runtime failure
- add explicit review notes for unresolved speakers and empty event sets

### 3. Descriptor enrichment still depends on upstream evidence quality

Observed failure class:

- some entities have incomplete physical or stylistic detail
- prompt prep can only surface what the upstream evidence and synthesis layers provide

Why this matters:

- downstream prompt quality should not depend on hand-written special casing
- missing details should be visible as gaps, not silently invented

Generic fix direction:

- keep descriptor enrichment evidence-driven
- mark thin fields clearly
- prefer review notes over silent inference
- only promote stable values into locked canonical fields

### 4. Review routing needs to stay conservative

Observed failure class:

- some prompt families are ready for generation
- some should be review-only
- not every weak artifact should be auto-corrected

Why this matters:

- conservative review routing prevents broken prompts from escaping into generation
- review-only outputs are useful when source data is partial

Generic fix direction:

- keep family-specific required fields
- route weak artifacts to review rather than forcing them through
- preserve the artifact for audit
- keep review notes descriptive and reusable

### 5. Future reference-asset growth should remain sliceable

Observed failure class:

- reference planning can grow broad quickly
- full inventories are useful, but they are not always the right execution target

Why this matters:

- large catalogs should be reducible to small testable slices
- future phases need to be testable without full-registry reruns

Generic fix direction:

- support per-family limits
- support selective entity subsets
- keep approval and lock states separate from planning
- allow future keyframe and asset phases to consume only approved subsets

---

## Dialogue-Specific Proposed Fixes

These are the next dialogue improvements that should be done in a generic way for any project.

### A. Support multiple dialogue payload shapes

Current need:

- project-level dialogue timelines are dict-shaped
- shot-level dialogue artifacts may be list-shaped

Proposed fix:

- normalize dialogue payload access through a shared helper
- treat list-shaped shot dialogue as a supported artifact shape
- treat dict-shaped timeline summaries as a supported artifact shape

### B. Separate dialogue grading from dialogue synthesis assumptions

Current need:

- grading should not assume that every dialogue file contains events
- synthesis should not require every shot to have non-empty dialogue

Proposed fix:

- make the grader understand:
  - chapter-level timelines
  - shot-level dialogue files
  - empty event sets
- preserve rerun recommendations for low-content dialogue without throwing errors

### C. Distinguish missing dialogue from intentionally empty dialogue

Current need:

- an empty `DIALOGUE.json` can mean the shot simply has no dialogue
- it should not be conflated with a runtime failure

Proposed fix:

- record a clear reason such as:
  - no dialogue events
  - unresolved speakers
  - low completeness
- keep the file shape valid so the grading and rerun queue remain reliable

### D. Keep dialogue warnings generic and project-neutral

Current need:

- warnings should describe the failure class, not the story content

Proposed fix:

- use generic messages like:
  - no dialogue events
  - unresolved speakers
  - weak scene binding
  - low evidence coverage

---

## Hardening Principles To Preserve

- never hardcode a specific book title into pipeline logic
- never hardcode a specific chapter or scene into validation logic
- never assume one project’s naming conventions are universal
- never convert a review-only artifact into a forced success
- never let a blank field create broken prompt prose
- never let a list-shaped payload crash a dict-shaped grader

---

## Suggested Follow-Up Files

- `spec/6_deferred/future_issues/SHOT_PROMPT_HARDENING_NOTES.md`
- `spec/6_deferred/future_issues/DIALOGUE_TIMELINE_REPAIR_NOTES.md`
- `spec/6_deferred/future_issues/REFERENCE_ASSET_SLICING_NOTES.md`

