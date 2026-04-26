# Artifact Lifecycle and Reuse

## Purpose

Define how FilmCreator artifacts are created, reviewed, reused, marked stale, approved, superseded, and locked.

This spec is intentionally cross-cutting.
It applies to:

- story analysis artifacts
- world registries
- character bibles
- environment bibles
- scene contracts
- shot packages
- dialogue timelines
- prompt packages
- generated media assets

Without this layer, reruns become destructive and the pipeline becomes difficult to trust.

---

## Design Principles

### Non-destructive by default

The pipeline should prefer:

- review existing
- reuse current
- update stale
- regenerate only when necessary

It should not blindly overwrite valid work.

### Explicit state is better than implicit replacement

A changed upstream dependency should mark an artifact stale rather than silently replacing it.

### User-approved work must survive reruns

If the user has reviewed, approved, or locked an artifact, the default rerun path must preserve that decision unless explicitly forced.

### Characters and environments are evolving artifacts

Character and environment bibles are special:

- later chapters may add new evidence
- reruns may need synthesis updates
- user-locked fields must survive those updates

---

## Artifact Status Model

Every major artifact should support a status field.

Recommended statuses:

- `missing`
- `generated`
- `reviewed`
- `approved`
- `stale`
- `superseded`
- `locked`

### Meanings

#### `missing`
Artifact does not exist yet.

#### `generated`
Artifact exists and was machine-generated but has not been human-reviewed.

#### `reviewed`
Artifact exists and was inspected by a user or operator but is not necessarily the final approved form.

#### `approved`
Artifact is the preferred current artifact for downstream use.

#### `stale`
Artifact still exists and may be viewable, but one or more upstream dependencies changed and it should not be trusted as current.

#### `superseded`
Artifact has been replaced by a newer version and should no longer be treated as current.

#### `locked`
Artifact or fields within it should not be modified by default reruns.

---

## Artifact Metadata Contract

Every major JSON contract should support lifecycle metadata.

Recommended shape:

```json
{
  "artifact_id": "CHAR_john_carter",
  "artifact_type": "character_bible",
  "status": "approved",
  "created_at_utc": "2026-04-20T00:00:00Z",
  "updated_at_utc": "2026-04-20T01:00:00Z",
  "upstream_dependencies": [
    {
      "dependency_type": "character_registry_entry",
      "dependency_id": "john_carter",
      "version": "sha-or-fingerprint"
    }
  ],
  "source_fingerprint": "sha-or-fingerprint",
  "locked_fields": {
    "stable_visual_summary": true
  },
  "manual_overrides": {
    "stable_visual_summary": "Approved final visual canon..."
  },
  "supersedes_artifact_id": null,
  "revision_history": []
}
```

---

## Reuse Rules

### Rule 1 — reuse current artifacts when upstream is unchanged

If:

- artifact exists
- artifact is not stale
- upstream dependencies match

Then the default behavior should be to reuse the artifact.

### Rule 2 — stale, don’t silently replace

If upstream changes, the artifact should be marked `stale` first.

It may then be:

- left for review
- regenerated
- regenerated only if the caller requested `only_stale=True`

### Rule 3 — approved and locked artifacts are protected

If an artifact is:

- `approved`
- `locked`

Then default reruns must not overwrite it.

### Rule 4 — allow targeted force regeneration

A caller may explicitly request a force path for:

- one artifact
- one phase
- one chapter
- one scene

Force should be explicit and auditable.

---

## Locked Fields vs Locked Artifacts

### Locked artifact

The whole artifact should not be replaced automatically.

### Locked field

The artifact may be updated, but the locked field must preserve:

- manual value
- approval state

This is especially important for:

- character bible visual descriptions
- environment bible visual descriptions
- approved prompt phrasing
- approved timeline timing entries

---

## Suggested Commands / Modes

The pipeline should eventually support modes such as:

- `generate-missing-only`
- `rebuild-stale-only`
- `review-existing-only`
- `retry-failed-only`
- `force-regenerate-target`

These modes should use lifecycle state rather than ad hoc file existence checks.

---

## Field-Level Merge Policy

For evolving artifacts like bibles:

### Machine-synthesized fields

May be updated when new evidence arrives, unless locked.

### Manual override fields

Should win over machine synthesis unless explicitly cleared.

### Evidence lists and revision history

Should be append-only where practical.

---

## Recommended Implementation Files

Add focused implementation modules rather than folding this into existing large authoring files.

Suggested files:

```text
orchestrator/artifact_lifecycle.py
orchestrator/staleness.py
orchestrator/review_queue.py
```

Potential touched files:

```text
orchestrator/common.py
orchestrator/cli.py
orchestrator/state.py
orchestrator/book_authoring.py
```

---

## Example Python Model

```python
from dataclasses import dataclass, field
from typing import Any

@dataclass
class ArtifactMetadata:
    artifact_id: str
    artifact_type: str
    status: str
    created_at_utc: str
    updated_at_utc: str
    upstream_dependencies: list[dict[str, Any]] = field(default_factory=list)
    source_fingerprint: str | None = None
    locked_fields: dict[str, bool] = field(default_factory=dict)
    manual_overrides: dict[str, Any] = field(default_factory=dict)
    supersedes_artifact_id: str | None = None
    revision_history: list[dict[str, Any]] = field(default_factory=list)
```

---

## Acceptance Criteria

This spec is considered validated when:

1. At least one major synthesis artifact can detect unchanged upstream dependencies and skip regeneration.
2. At least one artifact can be marked stale rather than silently overwritten.
3. Approved or locked artifacts survive a normal rerun.
4. Manual override fields survive synthesis updates.
