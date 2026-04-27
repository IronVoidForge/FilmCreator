Status: 20%

# Dependency Graph and Staleness

## Purpose

Define how FilmCreator tracks upstream dependencies and determines when artifacts are stale.

This enables:

- selective regeneration
- safe reuse
- non-destructive reruns
- debugging of downstream inconsistencies

---

## Core Concept

Every artifact depends on upstream artifacts.

If any upstream dependency changes, the artifact becomes **stale**.

This is preferred over silent overwrite.

---

## Dependency Model

Each artifact should track:

- dependency type
- dependency id
- dependency version (hash / fingerprint)

Example:

```json
{
  "dependency_type": "character_bible",
  "dependency_id": "CHAR_john_carter",
  "version": "abc123"
}
```

---

## Dependency Types

Common types:

- chapter source
- chapter summary
- character registry entry
- environment registry entry
- key item registry entry
- character bible
- environment bible
- scene contract
- shot
- shot package
- dialogue binding
- dialogue timeline

---

## Staleness Detection

An artifact is stale if:

- any dependency version differs from stored version
- any dependency is missing

---

## Propagation

Staleness should propagate downstream.

Example:

- character bible changes â†’ scene contracts stale
- scene contract changes â†’ shot packages stale
- shot packages change â†’ dialogue timeline stale

---

## Fingerprinting Strategy

Use:

- file hash
- or deterministic content hash

Avoid timestamps as the sole signal.

---

## Rebuild Modes

The system should support:

- rebuild stale only
- rebuild all
- rebuild specific artifact

---

## Suggested Implementation Files

```text
orchestrator/dependency_graph.py
orchestrator/staleness.py
```

---

## Acceptance Criteria

- Changing one upstream artifact marks downstream artifacts stale
- Rebuild-stale mode regenerates only affected artifacts


