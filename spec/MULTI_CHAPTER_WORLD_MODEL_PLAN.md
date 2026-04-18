# Multi-Chapter World Model Migration Plan

## Goal
Transition FilmCreator from single-chapter analysis to a persistent, evolving story-world system that maintains continuity across all chapters.

---

## Core Principles
- Do NOT overwrite character data — evolve it
- Preserve uncertainty instead of hallucinating
- Track identity, not just mentions
- Separate canonical facts from contextual states

---

## Phase 1 – Persistent World State (Minimum Viable)

### Character Registry
Each character becomes a persistent entity:
- canonical_id
- aliases
- first_seen_chapter
- last_seen_chapter
- is_fully_identified

### Chapter Processing Loop
For each chapter:
1. Load existing character index
2. Extract new characters
3. Match to existing characters
4. Update or create entries

### Alias Resolution
- Normalize names
- Match fuzzy aliases
- Allow LLM-assisted merge decisions

---

## Phase 2 – Layered Descriptions

### Description Layers
- innate (always true)
- chapter_specific
- forward_from (state changes after a point)

Example:
- CH001: cavalry uniform
- CH005+: Martian armor

---

## Phase 3 – Confidence and Clarification

### Confidence System
- score based on description completeness
- track missing fields

### Deferred Clarification
- do not force early answers
- resolve later if data appears

---

## Phase 4 – Revision + Retcon Handling

### Revision Log
- track when facts change
- mark superseded fields

### Contradiction Detection
- detect conflicting descriptions
- flag for resolution or user input

---

## Phase 5 – Timeline Awareness

### Character Evolution Timeline
Track:
- first appearance
- costume changes
- injuries
- transformations

### Scene-State Snapshotting
Before generating a scene:
- freeze character state at that timeline point

---

## Phase 6 – Environment Continuity

- persistent environment families
- evolving state (damage, time of day, etc.)

---

## Phase 7 – Prompt Integration

- prompts reference character state at scene time
- no future information leakage

---

## Additional Enhancements

### Visual Anchor Extraction
- face shape
- silhouette
- color palette

### Stability Profiles
- track how stable a character is visually

### Foreshadow Tracking
- unresolved narrative threads
- later payoff detection

---

## Data Storage Strategy

### Recommended Structure
- characters/
  - CHARACTER_INDEX.md
  - character_id.md
- timeline/
- revisions/

---

## Risks
- increased complexity
- more LLM calls
- harder debugging

---

## Recommended Implementation Order

1. Persistent character registry
2. Alias resolution
3. Layered descriptions
4. Deferred clarification
5. Timeline + forward states
6. Revision + contradiction handling

---

## End State

A searchable, persistent world model that:
- maintains continuity
- supports long-form storytelling
- drives consistent visual generation
