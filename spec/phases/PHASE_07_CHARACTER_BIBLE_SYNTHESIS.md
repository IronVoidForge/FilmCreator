# Phase 07 — Character Bible Synthesis

## Goal

Transform accumulated character evidence into stable, canonical character bibles suitable for production use.

---

## Inputs

- global character registry
- chapter-local registries
- character breakdowns
- continuity summaries
- librarian retrieval
- identity refinement results

---

## Outputs

- character bible markdown
- character bible JSON
- bible index
- review queue

---

## Artifact Locations

```
02_story_analysis/bibles/characters/
```

---

## Required Fields

### Identity

- canonical_id
- display_name
- aliases

### Visual

- stable_visual_summary
- costume_signature
- physical traits

### Behavioral

- personality
- role
- voice notes

### Continuity

- constraints
- unresolved ambiguities

### Provenance

- evidence_refs
- revision_history

---

## Incremental Rules

- reuse if unchanged
- update if new evidence
- preserve locked fields

---

## Implementation Files

```
orchestrator/character_bible.py
orchestrator/character_bible_models.py
```

---

## Acceptance Criteria

- produces stable character definitions
- preserves evidence
- supports incremental updates
