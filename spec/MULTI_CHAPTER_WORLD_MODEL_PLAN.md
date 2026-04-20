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

## Phase B Foundation (NEW)

Before multi-chapter world modeling begins, Phase B establishes:

- canonical character registry
- canonical environment registry
- provisional identity handling
- chapter-level continuity state

These artifacts live under:

```
02_story_analysis/world/
```

They are the required foundation for all later multi-chapter logic.

Current status:

- The canonical character and environment registries are in use.
- Chapter continuity summaries and world snapshots are being written per chapter.
- The latest full `princess_of_mars_test` run completed `28/28` chapters with `0` failures using the Gemma 4 IT model and the repair-first retry policy.
- The remaining improvement work is mostly about speed and context-window headroom, not basic correctness.

---

## Resilient Run Orchestration

Book-level chapter analysis is now continue-on-failure by default.

The manifest run writes:

- `02_story_analysis/runs/BOOK_RUN_latest.json`
- `02_story_analysis/runs/BOOK_RUN_<timestamp>.json`
- `02_story_analysis/runs/failed_chapters.json`
- `02_story_analysis/runs/FAILED_CHAPTERS_REPORT.md`

The latest failed-chapter list can be retried without rerunning the full manifest.

---

## Phase 0 – Full Book Ingestion

### Goal

Convert a raw full book into clean chapter source files.

### Outputs

```
01_source/book/raw_book.txt
01_source/book/book_manifest.md
01_source/chapters/CH001.md
```

---

## Phase 1 – Persistent World State (Built on Phase B)

### Character Registry

Each character becomes persistent:

- canonical_id
- aliases
- first_seen_chapter
- last_seen_chapter
- status (canonical vs provisional)
- resolution_reason

### Environment Registry

- canonical_id
- aliases
- state notes

---

## Phase 2 – Layered Descriptions

### Description Layers

- innate (always true)
- chapter_specific
- forward_from

---

## Phase 3 – Confidence and Clarification

### Features

- confidence scoring
- unresolved character tracking
- deferred clarification

---

## Phase 4 – Revision + Retcon Handling

### Features

- revision log
- contradiction detection

---

## Phase 5 – Timeline Awareness

### Features

- character evolution timeline
- environment state timeline
- scene-state snapshots

---

## Phase 6 – Environment Continuity

### Features

- persistent environment registry
- evolving state (damage, time, weather)

---

## Phase 7 – Prompt Integration

### Features

- prompts reference snapshot state
- no forward contamination

---

## SQLite Migration (Final Phase)

### When to Start

ONLY after:

- multi-chapter system works
- schemas stabilize

---

## End State

A system that:

- parses entire books
- builds persistent characters and environments
- evolves them over time
- generates scenes from correct historical state
