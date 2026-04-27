Status: 95%

# 1.1 Repo Project Scene Clip Hierarchy

## Goal

Define the canonical filesystem layout for FilmCreator so every handoff has one obvious home.

## Decisions

- Repo-level assets live at the root: `spec/`, `workflows/`, `orchestrator/`, and `projects/`.
- Each project lives under `projects/<project_slug>/`.
- Shared approved refs live at the project level under `04_references/`.
- Runtime scene work lives under `05_scenes/SC###/`.
- Runtime shot work lives under `05_scenes/SC###/SH###/`.
- Runtime clip work lives under `05_scenes/SC###/SH###/clips/CL###/`.
- Each shot folder represents one shot-level planning unit inside a story scene.
- Each clip folder represents one render/motion unit inside a shot.
- Clip-local stills live under `stills/` inside the clip folder.
- Interval plans for 3-5 second beats belong to the clip-local analysis, prompt, and state files rather than a separate top-level hierarchy.

## Required Layout

- `01_source/`
- `02_story_analysis/`
- `03_prompt_packages/`
- `04_references/`
- `05_scenes/`
- `06_reviews/selected/`
- `07_finals/`
- `logs/`

## Acceptance

- A new project can be created without inventing new folder names.
- A clip artifact never needs to live in a shared reference folder.
- Shared references can be reused across scenes and clips without duplication becoming the source of truth.
- A story scene can expand into multiple shots and multiple clips without inventing a second parallel filesystem structure.

