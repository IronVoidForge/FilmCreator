# Multi-Chapter World Model Migration Plan

## Goal

Transition FilmCreator from single-chapter analysis to a persistent, evolving, searchable story-world system while preserving:

- Markdown-first authoring
- tagged packet LLM outputs
- forgiving local parsers
- auditability and debuggability

---

## Core Principles

- Do NOT overwrite character data — evolve it
- Preserve uncertainty instead of hallucinating
- Track identity, not just mentions
- Separate canonical facts from contextual states
- All LLM outputs are tagged Markdown packets
- All structure is derived locally (Markdown → JSON → optional DB)

---

## NEW: Phase 0 – Full Book Ingestion

### Goal

Convert a raw full book into clean chapter source files.

### Required Features

- detect and skip table of contents
- detect chapter headers (roman, numeric, inconsistent formats)
- ignore front matter (preface, introduction)
- preserve chapter order and titles

### Outputs

```
01_source/book/raw_book.txt
01_source/book/book_manifest.md
01_source/book/book_parse_report.md
01_source/chapters/CH001.md
01_source/chapters/CH002.md
```

### Verification

- TOC is not duplicated into chapter files
- chapter count matches expectation
- chapter order is correct
- ambiguous boundaries are reported

### Suggested Functions

- `parse_full_book_to_chapters(raw_text)`
- `detect_table_of_contents(block)`
- `extract_chapter_boundaries(lines)`
- `write_book_manifest(chapters)`
- `write_parse_report(anomalies)`

---

## Phase 1 – Persistent World State (Minimum Viable)

### Character Registry

Each character becomes persistent:

- canonical_id
- aliases
- first_seen_chapter
- last_seen_chapter
- is_fully_identified
- confidence

### Chapter Processing Loop

For each chapter:

1. Load world state
2. Run character extraction (split pipeline)
3. Merge into registry
4. Write updated world files

### Verification

- characters persist across chapters
- aliases resolve consistently
- no duplicate canonical IDs unless unresolved

### Suggested Functions

- `load_world_state(project)`
- `update_world_from_chapter(chapter)`
- `merge_character(candidate, registry)`

---

## Phase 2 – Layered Descriptions

### Description Layers

- innate (always true)
- chapter_specific
- forward_from

### Verification

- later chapters modify state without overwriting history
- forward-from changes propagate correctly

### Suggested Functions

- `apply_layered_description(character, update)`
- `resolve_character_state_at_chapter(character, chapter_id)`

---

## Phase 3 – Confidence and Clarification

### Features

- confidence scoring
- unresolved character tracking
- deferred clarification

### Verification

- weak characters do not pollute canonical registry
- later chapters can resolve earlier uncertainty

### Suggested Functions

- `score_character_confidence(character)`
- `generate_clarification_request(character)`
- `resolve_clarification(character, new_data)`

---

## Phase 4 – Revision + Retcon Handling

### Features

- revision log
- contradiction detection

### Verification

- conflicting traits are logged
- no silent overwrites

### Suggested Functions

- `detect_contradictions(character)`
- `write_revision_entry(character, change)`

---

## Phase 5 – Timeline Awareness

### Features

- character evolution timeline
- environment state timeline
- scene-state snapshots

### Verification

- scenes use only prior knowledge
- no future leakage

### Suggested Functions

- `build_chapter_snapshot(chapter_id)`
- `build_scene_snapshot(scene_id)`
- `resolve_state_for_prompt(scene_id)`

---

## Phase 6 – Environment Continuity

### Features

- persistent environment registry
- evolving state (damage, time, weather)

### Verification

- environments update consistently across chapters

---

## Phase 7 – Prompt Integration

### Features

- prompts reference snapshot state
- no forward contamination

### Verification

- prompts differ correctly between chapters
- continuity errors are minimized

---

## Searchability Layer (Pre-SQLite)

### File-Based Indexing

Generate JSON indexes from Markdown:

```
world/indexes/character_index.json
world/indexes/environment_index.json
```

### Suggested Functions

- `build_character_index_json()`
- `build_environment_index_json()`
- `search_character(name_or_alias)`

---

## SQLite Migration (Final Phase)

### When to Start

ONLY after:

- multi-chapter system works
- schemas stabilize
- queries become painful in file form

### Role of SQLite

- query layer
- not initial source of truth

### Suggested Functions

- `db_init()`
- `db_sync_from_files()`
- `query_character_timeline()`

---

## Implementation Order (Final)

1. Book ingestion (Phase 0)
2. Chapter loop + world registry (Phase 1)
3. Layered descriptions (Phase 2)
4. Clarification system (Phase 3)
5. Revision + contradictions (Phase 4)
6. Timeline + snapshots (Phase 5)
7. Environment continuity (Phase 6)
8. Prompt integration (Phase 7)
9. JSON indexing layer
10. SQLite migration

---

## End State

A system that:

- parses entire books
- builds persistent characters and environments
- evolves them over time
- generates scenes from correct historical state
- remains debuggable and inspectable
- can later be accelerated by SQLite without architectural rewrites
