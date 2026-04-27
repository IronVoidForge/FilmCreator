Status: 85%

# Multi-Chapter World Model Plan (Updated)

## Goal

Evolve FilmCreator from chapter-level analysis into a persistent, synthesis-driven story world that supports:

- canonical characters and environments
- continuity-aware scene contracts
- downstream shot and production generation
- non-destructive iteration across full books

---

## Core Principles

- Do NOT overwrite â€” always evolve
- Preserve uncertainty instead of forcing incorrect merges
- Separate identity from description
- Separate canonical truth from contextual state
- Track evidence and revisions
- All structure is derived locally (Markdown â†’ JSON â†’ optional DB)
- Synthesis stages must be explainable and auditable

---

## Current Reality (Post-Refactor)

The system now reliably produces:

- chapter summaries
- character and environment extraction
- scene decomposition
- global and local registries
- chapter continuity state and summaries
- resilient book-level runs with failure isolation

This is no longer the problem space.

The problem space is now:

â†’ turning this data into stable, reusable production assets

---

## Foundational Layer (Already in Place)

### Canonical Identity (Phase B)

Artifacts:

```
02_story_analysis/world/
```

Includes:

- CHARACTER_REGISTRY.json
- ENVIRONMENT_REGISTRY.json
- chapter-local registries
- continuity state files

This is the required base for all synthesis work.

---

## World Model Evolution Path

### Stage 1 â€“ Evidence Accumulation (complete enough)

- extraction from chapters
- accumulation in registries
- continuity tracking

### Stage 2 â€“ Identity Refinement (partially complete)

- duplicate detection
- alias resolution
- provisional identity handling

This remains a standalone batch step and should not be fused into ingest.

### Stage 3 â€“ Canonical Synthesis (NEW PRIMARY FOCUS)

#### Character Bible Synthesis

- merge all evidence into canonical character representations
- preserve uncertainty and conflicting descriptions
- produce stable visual and narrative contracts

#### Environment Bible Synthesis

- merge location evidence
- define spatial, visual, and mood consistency
- support reuse across scenes

Outputs become the canonical world layer.

---

### Stage 4 â€“ Scene Production Contracts

Scenes become production-ready units:

- narrative purpose
- emotional beats
- required characters
- required environments
- continuity constraints

This stage bridges analysis â†’ filmmaking.

---

### Stage 5 â€“ Shot-Level World Interaction

Shots reference world state:

- character bibles
- environment bibles
- continuity state

Shots become the first fully generation-ready units.

---

### Stage 6 â€“ Timeline and State Evolution

Add temporal awareness:

- character evolution
- environment changes
- scene state transitions

This supports long-form coherence.

---

### Stage 7 â€“ Production Asset Integration

World model feeds:

- character sheets
- environment references
- keyframes
- video generation

---

## Artifact Layers

The world model should be thought of as layered:

1. raw extraction (chapter-level)
2. registries (identity accumulation)
3. refined identities (post-pass)
4. synthesized bibles (canonical layer)
5. scene contracts (contextual layer)
6. shot packages (generation layer)

Each layer builds on the previous one and should not overwrite it.

---

## Persistence Strategy

### File-First (Current)

- Markdown for review
- JSON for contracts
- media for outputs

### Future SQLite Layer

Only after stabilization:

- read-optimized
- file-synced
- non-destructive

---

## Key Design Constraints

### Non-destructive evolution

Later chapters must:

- add detail
- refine understanding
- never erase prior evidence

### Snapshot correctness

Each scene must:

- reference only valid past state
- avoid forward contamination

### Explainability

Every synthesized element should be traceable back to:

- chapters
- scenes
- specific evidence

---

## End State Vision

A system that can:

- ingest full books
- build evolving world models
- synthesize production-ready character and environment bibles
- generate scene and shot contracts
- drive full audiovisual generation pipelines
- preserve and reuse work across iterative runs

---

## What This Enables Next

With this model in place, FilmCreator becomes:

- a production planning system, not just an analysis tool
- a reusable world builder across chapters
- a stable foundation for consistent visual generation

The next steps are not about ingest.
They are about synthesis, contracts, and production.

