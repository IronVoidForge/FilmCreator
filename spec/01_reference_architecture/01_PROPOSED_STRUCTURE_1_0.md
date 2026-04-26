# Proposed Structure 1.0

## Purpose

This document sketches the first SQLite-backed relational layer for FilmCreator without replacing the file-first artifact model.

The goal is to make stable entities, relationships, lifecycle state, and quality metadata queryable while keeping evolving prompt payloads and evidence blobs flexible.

## Design Principles

- file artifacts remain canonical
- SQLite mirrors stable relationships, not every prose field
- version every row family
- keep prompt payloads and evidence in JSON until they stabilize further
- preserve file paths and provenance pointers so the database can always point back to the source artifact
 
## Schema Draft

All timestamps use ISO-8601 text. All JSON payloads are stored as `TEXT` containing serialized JSON.

### `projects`

Purpose:

- one row per FilmCreator project

Fields:

- `project_id INTEGER PRIMARY KEY`
- `slug TEXT NOT NULL UNIQUE`
- `title TEXT NOT NULL`
- `status TEXT NOT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- none

### `pipeline_runs`

Purpose:

- track resumable orchestration runs and their phase state

Fields:

- `run_id TEXT PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `run_type TEXT NOT NULL`
- `status TEXT NOT NULL`
- `current_phase TEXT NULL`
- `started_at TEXT NOT NULL`
- `finished_at TEXT NULL`
- `input_signature TEXT NOT NULL`
- `notes_json TEXT NULL`

Foreign keys:

- `project_id -> projects.project_id`

### `artifacts`

Purpose:

- registry of file-backed canonical artifacts

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `artifact_type TEXT NOT NULL`
- `canonical_id TEXT NOT NULL`
- `display_name TEXT NOT NULL`
- `chapter_id TEXT NULL`
- `scene_id TEXT NULL`
- `shot_id TEXT NULL`
- `file_path TEXT NOT NULL`
- `markdown_path TEXT NULL`
- `json_path TEXT NULL`
- `status TEXT NOT NULL`
- `version_tag TEXT NOT NULL`
- `fingerprint TEXT NOT NULL`
- `source_signature TEXT NULL`
- `provenance_json TEXT NULL`
- `payload_json TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `project_id -> projects.project_id`

Recommended meaning:

- one row per canonical artifact snapshot
- `payload_json` may mirror the current file contents

### `artifact_versions`

Purpose:

- retain version history for artifacts

Fields:

- `artifact_version_id INTEGER PRIMARY KEY`
- `artifact_id INTEGER NOT NULL`
- `version_tag TEXT NOT NULL`
- `fingerprint TEXT NOT NULL`
- `payload_json TEXT NOT NULL`
- `created_at TEXT NOT NULL`
- `created_by_run_id TEXT NULL`
- `locked INTEGER NOT NULL DEFAULT 0`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `created_by_run_id -> pipeline_runs.run_id`

### `dependencies`

Purpose:

- directed dependency edges for staleness and selective rebuilds

Fields:

- `dependency_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `parent_artifact_id INTEGER NOT NULL`
- `child_artifact_id INTEGER NOT NULL`
- `dependency_type TEXT NOT NULL`
- `staleness_rule TEXT NOT NULL`
- `required INTEGER NOT NULL DEFAULT 1`
- `created_at TEXT NOT NULL`

Foreign keys:

- `project_id -> projects.project_id`
- `parent_artifact_id -> artifacts.artifact_id`
- `child_artifact_id -> artifacts.artifact_id`

### `review_queue`

Purpose:

- queue low-confidence or incomplete artifacts for human review or patch repair

Fields:

- `review_item_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `artifact_id INTEGER NOT NULL`
- `queue_type TEXT NOT NULL`
- `priority INTEGER NOT NULL`
- `status TEXT NOT NULL`
- `focus_fields_json TEXT NULL`
- `reason_json TEXT NULL`
- `created_at TEXT NOT NULL`
- `resolved_at TEXT NULL`

Foreign keys:

- `project_id -> projects.project_id`
- `artifact_id -> artifacts.artifact_id`

### `quality_grades`

Purpose:

- capture grading snapshots for artifacts and rerun decisions

Fields:

- `grade_id INTEGER PRIMARY KEY`
- `artifact_id INTEGER NOT NULL`
- `project_id INTEGER NOT NULL`
- `completeness REAL NOT NULL`
- `evidence_support REAL NOT NULL`
- `consistency REAL NOT NULL`
- `prompt_readiness REAL NOT NULL`
- `inference_load REAL NOT NULL`
- `continuity_risk REAL NULL`
- `review_density REAL NULL`
- `dependency_impact REAL NULL`
- `grade_band TEXT NOT NULL`
- `grade_json TEXT NULL`
- `created_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`

### `approvals`

Purpose:

- record explicit human approvals and locks

Fields:

- `approval_id INTEGER PRIMARY KEY`
- `artifact_id INTEGER NOT NULL`
- `project_id INTEGER NOT NULL`
- `approval_type TEXT NOT NULL`
- `status TEXT NOT NULL`
- `approved_by TEXT NULL`
- `approved_at TEXT NULL`
- `notes TEXT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`

### `character_bibles`

Purpose:

- canonical character detail row, keyed by artifact

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `canonical_id TEXT NOT NULL`
- `source_artifact_id INTEGER NULL`
- `age_range TEXT NULL`
- `sex TEXT NULL`
- `height TEXT NULL`
- `build TEXT NULL`
- `skin_tone TEXT NULL`
- `hair_color TEXT NULL`
- `hair_style TEXT NULL`
- `eye_color TEXT NULL`
- `face_shape TEXT NULL`
- `facial_hair TEXT NULL`
- `distinctive_features TEXT NULL`
- `age_variants_json TEXT NULL`
- `portrait_variant_ids_json TEXT NULL`
- `locked_fields_json TEXT NULL`
- `evidence_refs_json TEXT NULL`
- `prompt_ready_descriptors_json TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`
- `source_artifact_id -> artifacts.artifact_id`

### `environment_bibles`

Purpose:

- canonical environment detail row, keyed by artifact

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `canonical_id TEXT NOT NULL`
- `source_artifact_id INTEGER NULL`
- `environment_type TEXT NULL`
- `hierarchy_path_json TEXT NULL`
- `subzones_json TEXT NULL`
- `lighting_modes_json TEXT NULL`
- `surface_materials_json TEXT NULL`
- `camera_friendly_landmarks_json TEXT NULL`
- `locked_fields_json TEXT NULL`
- `evidence_refs_json TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`
- `source_artifact_id -> artifacts.artifact_id`

### `scene_contracts`

Purpose:

- canonical scene contract row, keyed by artifact

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `canonical_id TEXT NOT NULL`
- `chapter_id TEXT NOT NULL`
- `scene_number TEXT NULL`
- `source_artifact_id INTEGER NULL`
- `scene_short_description TEXT NULL`
- `scene_primary_scale_story_point TEXT NULL`
- `summary TEXT NULL`
- `emotional_arc TEXT NULL`
- `characters_required_json TEXT NULL`
- `environments_required_json TEXT NULL`
- `scene_required_anchor_catalog_json TEXT NULL`
- `planned_shots_json TEXT NULL`
- `beat_list_json TEXT NULL`
- `scene_binding_json TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`
- `source_artifact_id -> artifacts.artifact_id`

### `scene_bindings`

Purpose:

- beat-level environment and cast binding for a scene

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `scene_artifact_id INTEGER NOT NULL`
- `canonical_id TEXT NOT NULL`
- `chapter_id TEXT NOT NULL`
- `scene_id TEXT NOT NULL`
- `dominant_environment_id TEXT NULL`
- `beat_environment_overrides_json TEXT NULL`
- `visible_subjects_json TEXT NULL`
- `offscreen_pressure_json TEXT NULL`
- `binding_notes_json TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`
- `scene_artifact_id -> scene_contracts.artifact_id`
- `dominant_environment_id -> artifacts.canonical_id` (resolved against the environment family)

### `shot_packages`

Purpose:

- canonical generation-facing shot plan row, keyed by artifact

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `scene_artifact_id INTEGER NOT NULL`
- `scene_binding_artifact_id INTEGER NOT NULL`
- `canonical_id TEXT NOT NULL`
- `chapter_id TEXT NOT NULL`
- `scene_id TEXT NOT NULL`
- `shot_id TEXT NOT NULL`
- `shot_number INTEGER NOT NULL`
- `shot_size TEXT NOT NULL`
- `shot_type TEXT NOT NULL`
- `camera_angle TEXT NULL`
- `lens_family TEXT NULL`
- `camera_motion TEXT NULL`
- `zoom_behavior TEXT NULL`
- `lighting_style TEXT NULL`
- `subject_visibility TEXT NULL`
- `primary_subject_id TEXT NULL`
- `visible_primary_subject_id TEXT NULL`
- `visible_secondary_subject_ids_json TEXT NULL`
- `characters_in_frame_json TEXT NULL`
- `primary_subject_frame_position TEXT NULL`
- `primary_subject_scale_relation TEXT NULL`
- `primary_subject_facing_direction TEXT NULL`
- `primary_subject_pose_description TEXT NULL`
- `subject_relation_summary TEXT NULL`
- `required_environment_anchor_1 TEXT NULL`
- `required_subject_anchor_1 TEXT NULL`
- `required_celestial_anchor_1 TEXT NULL`
- `required_scale_proof_detail TEXT NULL`
- `environment_id TEXT NULL`
- `environment_subzone TEXT NULL`
- `camera_package_description TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`
- `scene_artifact_id -> scene_contracts.artifact_id`
- `scene_binding_artifact_id -> scene_bindings.artifact_id`

### `shot_descriptors`

Purpose:

- descriptor enrichment output for a shot, kept close to prompt-facing fields

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `shot_artifact_id INTEGER NOT NULL`
- `canonical_id TEXT NOT NULL`
- `chapter_id TEXT NOT NULL`
- `scene_id TEXT NOT NULL`
- `shot_id TEXT NOT NULL`
- `environment_id TEXT NULL`
- `subject_positions TEXT NULL`
- `pose_notes TEXT NULL`
- `background_layers TEXT NULL`
- `foreground_elements TEXT NULL`
- `midground_elements TEXT NULL`
- `depth_cues TEXT NULL`
- `start_state TEXT NULL`
- `end_state TEXT NULL`
- `movement_notes TEXT NULL`
- `gaze_direction TEXT NULL`
- `review_flags_json TEXT NULL`
- `field_origin_json TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`
- `shot_artifact_id -> shot_packages.artifact_id`

### `prompt_packages`

Purpose:

- final assembled prompt bundles for reference sheets and generation workflows

Fields:

- `artifact_id INTEGER PRIMARY KEY`
- `project_id INTEGER NOT NULL`
- `source_artifact_id INTEGER NOT NULL`
- `prompt_type TEXT NOT NULL`
- `workflow_type TEXT NOT NULL`
- `canonical_id TEXT NOT NULL`
- `chapter_id TEXT NULL`
- `scene_id TEXT NULL`
- `shot_id TEXT NULL`
- `positive_prompt TEXT NOT NULL`
- `negative_prompt TEXT NULL`
- `template_name TEXT NOT NULL`
- `template_version TEXT NOT NULL`
- `input_map_json TEXT NOT NULL`
- `validation_json TEXT NULL`
- `review_queue_status TEXT NULL`
- `created_at TEXT NOT NULL`
- `updated_at TEXT NOT NULL`

Foreign keys:

- `artifact_id -> artifacts.artifact_id`
- `project_id -> projects.project_id`
- `source_artifact_id -> artifacts.artifact_id`

## Relationships

Recommended high-level linkage:

- `projects` owns everything
- `pipeline_runs` points to a `project`
- `artifacts` is the registry spine
- `artifact_versions` hangs off `artifacts`
- `dependencies` links artifact-to-artifact relationships
- `quality_grades`, `review_queue`, and `approvals` all point back to `artifacts`
- `character_bibles` and `environment_bibles` are artifact-specialized rows keyed by `artifact_id`
- `scene_contracts` feeds `scene_bindings`
- `scene_bindings` feeds `shot_packages`
- `shot_packages` feeds `shot_descriptors`
- `shot_descriptors` feeds `prompt_packages`

## Recommended Indexes

- `artifacts(project_id, artifact_type, canonical_id)`
- `artifacts(project_id, chapter_id, scene_id)`
- `artifacts(project_id, status)`
- `artifact_versions(artifact_id, version_tag)`
- `dependencies(parent_artifact_id)`
- `dependencies(child_artifact_id)`
- `quality_grades(artifact_id, grade_band)`
- `review_queue(project_id, status, priority)`
- `approvals(artifact_id, status)`
- `scene_bindings(project_id, chapter_id, scene_id)`
- `shot_packages(project_id, chapter_id, scene_id, shot_id)`
- `prompt_packages(project_id, prompt_type, canonical_id)`

## Upgrade Strategy

The first SQLite release should:

- mirror existing file artifacts rather than replace them
- ingest the current JSON and Markdown outputs as-is
- add foreign keys and indexes without changing the file layout
- allow prompt fields to evolve through JSON payloads
- support later normalization only after the prompt variable set stops changing frequently

## Suggested First Release Scope

- project registry
- pipeline runs
- artifact registry
- artifact versions
- dependencies
- quality grades
- review queue
- approvals

## Not In First Release

- full replacement of file artifacts
- aggressive normalization of every prompt field
- hard migration of all evidence text into 3NF
- generated asset binaries
