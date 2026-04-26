# 5.1 Story Analysis Outputs

## Goal

Define the analysis outputs that FilmCreator produces before canonical synthesis, scene contracts, shot planning, and downstream generation.

This spec now describes the **upstream analysis layer**.
It is no longer intended to be the final production-facing layer.

The purpose of this phase is to produce:

- structured, reviewable story analysis
- durable evidence for later canonical synthesis
- continuity-carrying scene decomposition
- stable inputs for phases 7–11

---

## Design Principles

- Analysis is upstream evidence, not the final production contract.
- Analysis remains file-first and reviewable.
- Analysis should preserve uncertainty instead of hallucinating details.
- Analysis should separate:
  - what the text says directly
  - what is inferred structurally
  - what remains unresolved
- Analysis artifacts should be reusable by later synthesis phases and should not need to be regenerated if unchanged.
- Analysis must remain modular: chapter summary, extraction, decomposition, continuity, and later planning should stay separable rather than collapsing into one monolithic LLM response.

---

## Local Runtime Contract

- Authoring talks to a local LM Studio instance through its OpenAI-compatible API.
- Rendering does not depend on LM Studio remaining open after authoring completes.
- Analysis output is file-first. Downstream phases later consume files, not live LLM responses.
- Every LM Studio invocation should perform one bounded authoring task only.
- Higher-level authoring commands may orchestrate multiple LM Studio calls, but should not collapse chapter analysis, scene planning, bible synthesis, shot planning, and prompt writing into one response.
- Chapter-analysis and scene-planning tasks should prefer tagged Markdown packets plus parser-side validation over strict nested JSON.

---

## Analysis Outputs Required Before Later Phases

### Project-level

- project story summary
- recurring character index input
- recurring environment index input

### Chapter-level

- chapter summary
- character extraction outputs
- environment extraction outputs
- scene decomposition outputs
- chapter continuity state and continuity summary
- chapter world snapshot

### Registry-level

- chapter-local character registry
- chapter-local environment registry
- global character registry updates
- global environment registry updates

### Review/logging

- per-task raw LM Studio logs
- resilient book-run metadata
- failed chapter run metadata when applicable

---

## Planned Files

### Analysis layer

- `02_story_analysis/story_summary/project_summary.md`
- `02_story_analysis/chapter_analysis/CH###_summary.md`
- `02_story_analysis/scene_breakdowns/indices/CH###_SCENE_INDEX.md`
- `02_story_analysis/character_breakdowns/indices/CH###_CHARACTER_INDEX.md`
- `02_story_analysis/environment_breakdowns/indices/CH###_ENVIRONMENT_INDEX.md`

### World state layer

- `02_story_analysis/world/local/CH###_CHARACTER_REGISTRY.json`
- `02_story_analysis/world/local/CH###_ENVIRONMENT_REGISTRY.json`
- `02_story_analysis/world/global/CHARACTER_REGISTRY_GLOBAL.json`
- `02_story_analysis/world/global/ENVIRONMENT_REGISTRY_GLOBAL.json`
- `02_story_analysis/world/snapshots/CH###_WORLD_SNAPSHOT.json`
- `02_story_analysis/world/continuity/CH###_STATE.json`
- `02_story_analysis/world/continuity/CH###_CONTINUITY_SUMMARY.md`

### Run/logging layer

- `02_story_analysis/logs/...`
- `02_story_analysis/runs/BOOK_RUN_latest.json`
- `02_story_analysis/runs/BOOK_RUN_<timestamp>.json`
- `02_story_analysis/runs/failed_chapters.json`
- `02_story_analysis/runs/FAILED_CHAPTERS_REPORT.md`

---

## Required Analysis Content

### `project_summary.md`

- overall premise
- major recurring characters
- major recurring environments
- continuity-sensitive visual or narrative rules
- high-level retrieval surface for later librarian use

### `chapter_analysis/CH###_summary.md`

- concise chapter summary
- chapter-local visual motifs
- chapter-local recurring entities
- continuity-sensitive facts that later scene packages must preserve
- chapter-level unresolved ambiguities if present

### chapter-scoped character outputs

These should capture:

- identity candidates
- aliases and references
- extracted visual clues
- continuity-critical character facts
- whether evidence is strong or underdescribed

These outputs are evidence for later **character bible synthesis**, not the final character contract.

### chapter-scoped environment outputs

These should capture:

- location candidates
- environmental and layout clues
- lighting and atmosphere notes
- recurring landmarks and props
- underdescribed environment warnings

These outputs are evidence for later **environment bible synthesis**, not the final environment contract.

### scene decomposition outputs

These should capture:

- scene purpose
- emotional and dramatic function
- ordered beats
- scene-local continuity implications
- likely required characters and environments
- useful future shot opportunities when identifiable

These outputs are evidence for later **scene production contract synthesis**, not the final scene contract.

### continuity outputs

These should capture:

- known characters through the chapter
- known environments through the chapter
- unresolved ids through the chapter
- snapshot path
- chapter-bounded continuity notes

These outputs are the continuity substrate for later phases 7–11.

---

## Rules

- Analysis files live under `02_story_analysis/`.
- Analysis remains file-first.
- Analysis should identify facts, inferred structure, and unresolved ambiguity separately.
- Analysis should not hallucinate missing character or environment detail.
- Underdescribed inputs should be flagged for later synthesis review or manual supplementation.
- Analysis should not mention ComfyUI node details, workflow JSON details, or render patch points.
- Analysis should not assume that legacy clip planning is the final planning abstraction.
- Analysis may still emit useful scene/beat/clip-oriented information, but that information is now upstream input to later **scene contracts** and **shot packages**.

---

## Relationship To Later Phases

### Analysis → Phase 7 character bible synthesis

Character extraction and registry artifacts provide evidence for canonical character definitions.

### Analysis → Phase 8 environment bible synthesis

Environment extraction and registry artifacts provide evidence for canonical environment definitions.

### Analysis → Phase 9 scene production contracts

Scene decomposition plus continuity state provide the baseline narrative structure for scene contract generation.

### Analysis → Phase 10 shot planning

Legacy beat or clip-oriented planning hints may still be useful, but future shot planning should be driven by scene contracts and canonical bibles rather than raw analysis alone.

---

## Planned Commands

- `python -m orchestrator lmstudio-check`
  - verifies LM Studio connectivity and local model availability
- `python -m orchestrator analyze-chapter <project_slug> --chapter <chapter_file>`
  - writes analysis outputs for one chapter
- `python -m orchestrator analyze-book <project_slug>`
  - runs resilient multi-chapter analysis and writes run metadata

Later phases should add separate commands rather than further overloading analysis commands.

---

## Suggested Future Implementation Files

This spec is largely implemented, but future cleanup should prefer new modules over continued growth in existing monoliths.

Relevant files today include:

```text
orchestrator/story_authoring.py
orchestrator/book_authoring.py
orchestrator/world_global.py
orchestrator/book_librarian.py
```

Future synthesis and planning stages should live in new focused modules rather than further expanding this phase’s files.

---

## Acceptance

This phase is considered complete enough to build on when:

- prompt and synthesis stages can trace their work back to stable analysis files
- one full multi-chapter run can complete successfully and produce coherent chapter analysis outputs
- world snapshots and continuity summaries are usable as upstream evidence for later phases
- analysis outputs are stable enough that later synthesis phases can decide whether to reuse or rebuild without brute-force regeneration
