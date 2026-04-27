Status: 60%

# 4.4 Automated Testing and CI Strategy

## Goal

Make automated testing part of the product contract so the orchestrator can evolve without breaking pathing, state, manifests, or workflow resolution.

## Testing Principles

- Automated tests are required for deterministic behavior.
- Manual review stays responsible for image quality and creative approval.
- Fast tests should run locally and in CI on every code change.
- Live ComfyUI smoke tests should be isolated from the fast deterministic suite.
- Local-first authoring and rendering contracts should be testable without hosted services.
- LM Studio authoring checks and ComfyUI rendering checks should be runnable independently on VRAM-constrained machines.

## Required Automated Test Layers

### Unit Tests

- ID validation for `SC###` and `CL###`
- path and naming helpers
- workflow registry loading and lookup
- state file read and write helpers
- token replacement and template expansion
- continuity-source resolution helpers

### Contract Tests

- prompt package schema validation against required Markdown headings
- clip-plan interval structure validation
- workflow registry shape validation
- workflow patch-point validation against the canonical workflow JSON files
- state file schema validation for project, scene, and clip state

### Integration Tests

- `init-project`, `init-scene`, and `init-clip` create the correct hierarchy
- `plan-run` writes manifests into the correct project, scene, or clip scope
- `promote-asset` copies selected files into the canonical destinations
- golden-frame promotion updates `clip_state.json`
- continuation jobs resolve the latest approved continuity source from `clip_state.json`
- shared character and environment promotion updates `project_state.json`
- output routing never writes clip assets into shared reference folders by mistake

### Live Smoke Tests

- optional LM Studio connectivity test for local authoring integration
- optional ComfyUI connectivity test
- optional workflow submission smoke test using a fixture prompt and fixture refs
- optional continuation workflow smoke test that hands the last approved frame into the next run
- optional output fetch verification

## CI Rules

- CI must run unit, contract, and filesystem-only integration tests.
- CI must not require a live ComfyUI or LM Studio instance for the default pipeline.
- Live smoke tests should run only when explicitly enabled by environment flag or separate job.
- A pull request that changes runner logic, registry logic, state contracts, continuity resolution, or path routing should fail if automated coverage breaks.

## Test Layout

- `tests/unit/`
- `tests/contracts/`
- `tests/integration/`
- `tests/fixtures/`
- `tests/live/`

## Acceptance

- Core orchestrator behavior can be validated without manual clicking.
- A regression in path routing, state updates, continuity resolution, or workflow lookup is caught automatically.
- Manual review remains focused on creative judgment instead of structural debugging.

