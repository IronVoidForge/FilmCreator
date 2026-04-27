Status: 5%

# 1.6 SQLite Relational Model

## Goal

Design the local relational database layer that will eventually connect chapters, scenes, clips, characters, environments, prompt packages, runs, reviews, and approvals without replacing the current file-first workflow too early.

## Working Decision

- The database should be `SQLite`, not a client-server database.
- The database should be local-first and per-project.
- The first implementation should be a relational index and orchestration-state layer, not a binary asset store.
- Markdown, JSON, workflow exports, and generated media files remain the canonical content artifacts.
- The database should initially mirror and connect those artifacts.
- The database becomes more authoritative only after the authoring and planning model has stabilized.

## Timing

- Database design is being specified now.
- Database implementation should begin after the following are validated:
  - `lmstudio-check`
  - `write-prompts`
  - scene analysis commands
  - clip planning commands
  - character-to-scene mapping for clips
- The first shipped database phase should be read-mostly and sync-from-files.
- We should not make the database the sole source of truth for prompts or media while the authoring model is still changing quickly.

## Storage Location

- Use one database file per project:
  - `projects/<project_slug>/filmcreator.sqlite3`
- Keep migration scripts in the repo, not inside each project:
  - recommended future location: `orchestrator/database/migrations/`
- Keep ORM models or schema metadata in the repo:
  - recommended future location: `orchestrator/database/models.py`

## What To Download And Set Up

### Required

- No database server download is required.
- Python already includes the `sqlite3` module, so the core engine is available with the existing local runtime.

### Recommended Python Packages

- `SQLAlchemy`
  - for schema definitions, typed queries, and future repository-layer code
- `Alembic`
  - for schema migrations and revision history

### Optional Local Tools

- `sqlite3` command-line tools for Windows
  - useful for direct inspection, dumps, integrity checks, and scripted debugging
- `DB Browser for SQLite`
  - useful for visual inspection of tables, relations, and row-level debugging

## Recommended Future Setup Steps

1. Install Python dependencies into the FilmCreator environment.
2. Add schema models and migration config to the repo.
3. Add commands to initialize and upgrade a project database.
4. Create the database file for a project on demand.
5. Enable required SQLite pragmas on every connection.

## Required SQLite Pragmas

- `PRAGMA foreign_keys = ON`
- `PRAGMA journal_mode = WAL`
- `PRAGMA synchronous = NORMAL`
- `PRAGMA temp_store = MEMORY`

These should be set by the application connection layer, not assumed by the environment.

## Authority Model

### Phase 1

- Files remain canonical:
  - source text
  - chapter excerpts
  - Markdown prompt packages
  - run manifests
  - generated media
- SQLite stores:
  - IDs
  - relationships
  - parsed metadata
  - sync state
  - query-friendly operational state

### Phase 2

- SQLite becomes the canonical home for:
  - run records
  - candidate records
  - review decisions
  - approval links
  - continuity links
  - style-performance summaries
- Files still remain canonical for:
  - prompt bodies
  - raw source text
  - workflow JSON
  - media assets

### Phase 3

- SQLite may become the primary operational planner for:
  - scene queues
  - stage readiness
  - overnight batching
  - dependency resolution
- Even then, prompt packages and media should still live as files.

## Key Modeling Rules

- Every major table should use:
  - an internal integer primary key
  - a stable external human-readable ID where applicable
- External IDs should stay aligned with current filesystem conventions:
  - `project_slug`
  - `CH###`
  - `SC###`
  - `CL###`
  - `beat_id`
  - character/environment `asset_id`
- Store project-relative paths, not machine-specific absolute paths.
- Store JSON-structured flex fields as text columns containing JSON.
- Do not store images or videos as BLOBs.
- Store content hashes for syncable file-backed records.
- Add `created_at` and `updated_at` to operational tables.
- Use foreign keys aggressively so the hierarchy can be traversed safely.
- Keep shared assets as project-owned entities with link tables rather than forcing them into scene/shot parent chains.
- Use a small owner/subject contract for prompt packages rather than adding one nullable foreign key per asset class.
- Capture dialogue as a clip-level or shot-level binding record so it can be queried independently of the timeline blob.

## Core Schema

### Projects And Source Text

- `projects`
  - `id`
  - `project_slug` unique
  - `display_name`
  - `root_path`
  - `status`
  - `created_at`
  - `updated_at`

- `source_documents`
  - `id`
  - `project_id` fk -> `projects.id`
  - `document_type`
    - `chapter`
    - `excerpt`
    - `notes`
    - later optional `script`
  - `document_code`
    - recommended for chapters: `CH###`
  - `title`
  - `relative_path`
  - `text_hash`
  - `word_count`
  - `ingest_status`
  - `created_at`
  - `updated_at`

- `chapters`
  - `id`
  - `project_id` fk -> `projects.id`
  - `chapter_code` unique within project
  - `source_document_id` fk -> `source_documents.id`
  - `ordinal`
  - `title`
  - `summary`
  - `status`
  - `created_at`
  - `updated_at`

### Scene And Beat Breakdown

- `scenes`
  - `id`
  - `project_id` fk -> `projects.id`
  - `chapter_id` fk -> `chapters.id`, nullable
  - `scene_code` unique within project
  - `ordinal_within_project`
  - `ordinal_within_chapter`
  - `title`
  - `purpose`
  - `summary`
  - `source_start_offset`, nullable
  - `source_end_offset`, nullable
  - `status`
  - `created_at`
  - `updated_at`

- `beats`
  - `id`
  - `scene_id` fk -> `scenes.id`
  - `beat_code` unique within scene
  - `ordinal`
  - `purpose`
  - `summary`
  - `axis_rules`
  - `continuity_rules_json`
  - `created_at`
  - `updated_at`

### Clips And Motion Segments

### Shots

- `shots`
  - `id`
  - `project_id` fk -> `projects.id`
  - `scene_id` fk -> `scenes.id`
  - `beat_id` fk -> `beats.id`, nullable
  - `shot_code` unique within scene
  - `ordinal_within_scene`
  - `title`
  - `purpose`
  - `shot_type`
  - `camera_description`
  - `composition`
  - `prompt_seed`
  - `status`
  - `created_at`
  - `updated_at`

- `clips`
  - `id`
  - `project_id` fk -> `projects.id`
  - `scene_id` fk -> `scenes.id`
  - `shot_id` fk -> `shots.id`
  - `clip_code` unique within shot
  - `ordinal`
  - `title`
  - `purpose`
  - `duration_seconds`
  - `start_mode`
  - `composition_type`
  - `continuity_mode`
  - `starting_keyframe_strategy`
  - `dependency_policy`
  - `auto_advance_policy`
  - `fallback_strategy`
  - `look_continuity_policy`
  - `consistency_assist_policy`
  - `consistency_assist_method`
  - `anatomy_repair_policy`
  - `status`
  - `created_at`
  - `updated_at`

- `clip_motion_segments`
  - `id`
  - `clip_id` fk -> `clips.id`
  - `segment_index`
  - `duration_seconds`
  - `camera_motion`
  - `subject_motion`
  - `environment_motion`
  - `input_frame_policy`
  - `notes`
  - `created_at`
  - `updated_at`

This table is where approximately 10-second clips can be represented as two planned short motion segments without hiding that logic inside one oversized prompt.

### Characters And Environments

- `characters`
  - `id`
  - `project_id` fk -> `projects.id`
  - `asset_id` unique within project
  - `display_name`
  - `description`
  - `continuity_traits_json`
  - `status`
  - `created_at`
  - `updated_at`

- `environments`
  - `id`
  - `project_id` fk -> `projects.id`
  - `asset_id` unique within project
  - `display_name`
  - `description`
  - `continuity_traits_json`
  - `status`
  - `created_at`
  - `updated_at`

### Key Items

- `key_items`
  - `id`
  - `project_id` fk -> `projects.id`
  - `asset_id` unique within project
  - `display_name`
  - `description`
  - `item_kind`
  - `continuity_traits_json`
  - `status`
  - `created_at`
  - `updated_at`

### Character And Environment Mapping

- `scene_characters`
  - `scene_id` fk -> `scenes.id`
  - `character_id` fk -> `characters.id`
  - `role`
  - `importance`
  - `notes`
  - composite pk: `scene_id`, `character_id`

- `scene_environments`
  - `scene_id` fk -> `scenes.id`
  - `environment_id` fk -> `environments.id`
  - `role`
  - `notes`
  - composite pk: `scene_id`, `environment_id`

- `clip_characters`
  - `clip_id` fk -> `clips.id`
  - `character_id` fk -> `characters.id`
  - `visibility`
  - `framing_role`
  - `is_primary`
  - `consistency_target`
  - `notes`
  - composite pk: `clip_id`, `character_id`

- `clip_environments`
  - `clip_id` fk -> `clips.id`
  - `environment_id` fk -> `environments.id`
  - `is_primary`
  - `notes`
  - composite pk: `clip_id`, `environment_id`

- `chapter_key_items`
  - `chapter_id` fk -> `chapters.id`
  - `key_item_id` fk -> `key_items.id`
  - `role`
  - `notes`
  - composite pk: `chapter_id`, `key_item_id`

- `scene_key_items`
  - `scene_id` fk -> `scenes.id`
  - `key_item_id` fk -> `key_items.id`
  - `role`
  - `notes`
  - composite pk: `scene_id`, `key_item_id`

- `clip_key_items`
  - `clip_id` fk -> `clips.id`
  - `key_item_id` fk -> `key_items.id`
  - `visibility`
  - `framing_role`
  - `is_primary`
  - `notes`
  - composite pk: `clip_id`, `key_item_id`

### Ref Binding Layer

- `clip_ref_bindings`
  - `id`
  - `clip_id` fk -> `clips.id`
  - `stage_family`
    - `keyframe`
    - `still_fix`
    - `cut_motion`
  - `slot_name`
    - examples:
      - `image_1`
      - `image_2`
      - `image_3`
      - `image_4`
      - `source_frame`
  - `binding_type`
    - `character_reference`
    - `environment_reference`
    - `approved_keyframe`
    - `approved_still_fix`
    - `approved_video_last_frame`
    - `manual_path`
  - `character_id` nullable fk -> `characters.id`
  - `environment_id` nullable fk -> `environments.id`
  - `required_flag`
  - `sort_order`
  - `notes`

This table is the key bridge between authoring and rendering. It should eventually answer:

- which approved character refs belong in a clip
- which environment ref belongs in the clip
- which workflow slot each ref should fill
- which continuity image should be used for motion or correction

### Prompt Packages

- `prompt_packages`
  - `id`
  - `project_id` fk -> `projects.id`
  - `scene_id` nullable fk -> `scenes.id`
  - `shot_id` nullable fk -> `shots.id`
  - `clip_id` nullable fk -> `clips.id`
  - `character_id` nullable fk -> `characters.id`
  - `environment_id` nullable fk -> `environments.id`
  - `key_item_id` nullable fk -> `key_items.id`
  - `stage`
  - `workflow_type`
  - `relative_path`
  - `source_hash`
  - `purpose`
  - `positive_prompt`
  - `negative_prompt`
  - `inputs_json`
  - `continuity_notes`
  - `repair_notes`
  - `generated_by`
  - `generated_model`
  - `created_at`
  - `updated_at`

These direct nullable foreign keys are transitional compatibility fields.
The long-term ownership model should prefer `prompt_owners` plus `prompt_subject_links` so prompt lineage stays normalized as new asset kinds arrive.

- `prompt_owners`
  - `id`
  - `prompt_package_id` fk -> `prompt_packages.id`
  - `owner_kind`
    - `character`
    - `environment`
    - `key_item`
    - `scene`
    - `shot`
    - `clip`
  - `owner_id`
  - `primary_subject_kind`
  - `primary_subject_id`
  - `variant_role`
  - `created_at`
  - `updated_at`

- `prompt_subject_links`
  - `id`
  - `prompt_package_id` fk -> `prompt_packages.id`
  - `subject_kind`
    - `character`
    - `environment`
    - `key_item`
    - `scene`
    - `shot`
    - `clip`
  - `subject_id`
  - `relationship_role`
  - `dependency_type`
  - `notes`
  - `created_at`
  - `updated_at`

- `prompt_sources`
  - `id`
  - `prompt_package_id` fk -> `prompt_packages.id`
  - `source_kind`
    - `source_document`
    - `chapter`
    - `scene`
    - `beat`
    - `clip`
    - `character`
    - `environment`
    - `key_item`
    - `file_path`
  - `source_id` nullable
  - `relative_path` nullable
  - `notes`

- `asset_mentions`
  - `id`
  - `project_id` fk -> `projects.id`
  - `asset_kind`
    - `character`
    - `environment`
    - `key_item`
  - `asset_id`
  - `source_kind`
    - `chapter`
    - `scene`
    - `clip`
    - `prompt_package`
    - `media_asset`
  - `source_id`
  - `role`
  - `source_span`
  - `confidence`
  - `notes`
  - `created_at`
  - `updated_at`

- `dialogue_bindings`
  - `id`
  - `project_id` fk -> `projects.id`
  - `clip_id` fk -> `clips.id`
  - `shot_id` nullable fk -> `shots.id`
  - `speaker_character_id` nullable fk -> `characters.id`
  - `speaker_label`
  - `dialogue_text`
  - `source_span`
  - `timing_estimate_seconds` nullable
  - `delivery_notes`
  - `created_at`
  - `updated_at`

### Media Assets

- `media_assets`
  - `id`
  - `project_id` fk -> `projects.id`
  - `scene_id` nullable fk -> `scenes.id`
  - `clip_id` nullable fk -> `clips.id`
  - `character_id` nullable fk -> `characters.id`
  - `environment_id` nullable fk -> `environments.id`
  - `asset_family`
    - `character_reference`
    - `environment_reference`
    - `keyframe_candidate`
    - `approved_keyframe`
    - `still_fix_candidate`
    - `approved_still_fix`
    - `cut_motion_candidate`
    - `approved_video`
    - `approved_video_last_frame`
    - `anchor_frame`
    - `interval_frame`
  - `relative_path`
  - `file_ext`
  - `file_hash`
  - `width` nullable
  - `height` nullable
  - `duration_seconds` nullable
  - `status`
  - `created_at`
  - `updated_at`

### Workflow Runs And Candidates

- `workflow_runs`
  - `id`
  - `project_id` fk -> `projects.id`
  - `scene_id` nullable fk -> `scenes.id`
  - `clip_id` nullable fk -> `clips.id`
  - `prompt_package_id` nullable fk -> `prompt_packages.id`
  - `run_code`
    - example: `RUN_0040`
  - `workflow_id`
  - `stage`
  - `stage_family`
  - `status`
  - `manifest_relative_path`
  - `patched_workflow_relative_path`
  - `seed`
  - `error_text`
  - `created_at`
  - `completed_at`

- `run_candidates`
  - `id`
  - `workflow_run_id` fk -> `workflow_runs.id`
  - `candidate_rank`
  - `style_profile`
  - `candidate_prompt_package_id` nullable fk -> `prompt_packages.id`
  - `output_asset_id` nullable fk -> `media_assets.id`
  - `status`
  - `review_status`
  - `seed`
  - `notes`

### Review And Approval

- `review_batches`
  - `id`
  - `project_id` fk -> `projects.id`
  - `scene_id` fk -> `scenes.id`
  - `clip_id` fk -> `clips.id`
  - `workflow_run_id` fk -> `workflow_runs.id`
  - `stage`
  - `stage_family`
  - `review_decision`
  - `created_at`

- `review_batch_candidates`
  - `review_batch_id` fk -> `review_batches.id`
  - `run_candidate_id` fk -> `run_candidates.id`
  - `is_top_two`
  - `is_primary`
  - composite pk: `review_batch_id`, `run_candidate_id`

- `approvals`
  - `id`
  - `project_id` fk -> `projects.id`
  - `scene_id` nullable fk -> `scenes.id`
  - `clip_id` nullable fk -> `clips.id`
  - `approval_type`
    - `approved_keyframe`
    - `approved_still_fix`
    - `approved_video`
    - `approved_video_last_frame`
    - `character_reference`
    - `environment_reference`
  - `media_asset_id` fk -> `media_assets.id`
  - `source_run_id` nullable fk -> `workflow_runs.id`
  - `source_candidate_id` nullable fk -> `run_candidates.id`
  - `approved_at`

### Continuity And Learning

- `continuity_links`
  - `id`
  - `clip_id` fk -> `clips.id`
  - `source_approval_id` fk -> `approvals.id`
  - `continuity_role`
    - `current_continuity_source`
    - `approved_keyframe_base`
    - `approved_still_fix_base`
    - `previous_video_last_frame_fallback`
  - `is_active`
  - `notes`

- `style_profile_stats`
  - `id`
  - `clip_id` fk -> `clips.id`
  - `stage_family`
  - `style_profile`
  - `appearances`
  - `top_two_count`
  - `win_count`
  - unique: `clip_id`, `stage_family`, `style_profile`

## Indexing Requirements

- Unique indexes
  - `projects.project_slug`
  - `chapters(project_id, chapter_code)`
  - `scenes(project_id, scene_code)`
  - `shots(scene_id, shot_code)`
  - `clips(scene_id, clip_code)`
  - `characters(project_id, asset_id)`
  - `environments(project_id, asset_id)`
  - `key_items(project_id, asset_id)`
  - `workflow_runs(project_id, run_code)`

- Query indexes
  - `shots(scene_id, ordinal_within_scene)`
  - `clips(scene_id, ordinal)`
  - `beats(scene_id, ordinal)`
  - `clip_motion_segments(clip_id, segment_index)`
  - `prompt_packages(clip_id, stage)`
  - `prompt_owners(prompt_package_id, owner_kind, owner_id)`
  - `media_assets(clip_id, asset_family)`
  - `workflow_runs(clip_id, stage, status)`
  - `run_candidates(workflow_run_id, candidate_rank)`
  - `approvals(clip_id, approval_type)`
  - `clip_ref_bindings(clip_id, stage_family, slot_name)`
  - `asset_mentions(asset_kind, asset_id)`
  - `dialogue_bindings(clip_id, shot_id)`

## Migration Sequence

The database rollout should be incremental and file-first. Each migration step should be independently useful and should not force a full rewrite of the runtime hierarchy.

### Step 1 - Foundation Tables

Create the structural tables first:

- `projects`
- `source_documents`
- `chapters`
- `scenes`
- `beats`
- `shots`
- `clips`
- `clip_motion_segments`

This step gives the database the canonical hierarchy:

- project -> chapter -> scene -> shot -> clip

This hierarchy is intentional and transitional:

- scenes remain the planning parent
- shots become the first-class planning unit beneath scenes
- clips remain the render/motion execution unit beneath shots
- older clip-centric runtime code may still exist during migration, but it should not dictate the target schema

### Step 2 - Shared Asset Tables

Add the project-owned shared assets:

- `characters`
- `environments`
- `key_items`

Then add the link tables:

- `scene_characters`
- `scene_environments`
- `scene_key_items`
- `clip_characters`
- `clip_environments`
- `clip_key_items`
- `chapter_key_items`
- `asset_mentions`

### Step 3 - Prompt Ownership And Lineage

Add prompt tracking as its own lineage layer:

- `prompt_packages`
- `prompt_owners`
- `prompt_subject_links`
- `prompt_sources`

At this stage, prompt packages should still have transitional nullable foreign keys for compatibility, but the long-term ownership contract should come from `prompt_owners` and `prompt_subject_links` style linkage.

The prompt lineage contract should stay small and explicit:

- one owner
- one primary subject
- a bounded set of dependency links
- variant roles for alternate-angle, reference-sheet, repair, and motion-generation use cases

### Step 4 - Dialogue And Review Bindings

Add the records needed for timeline and review work:

- `dialogue_bindings`
- `workflow_runs`
- `run_candidates`
- `review_batches`
- `review_batch_candidates`
- `approvals`

This is the step where dialogue becomes a first-class clip/shot binding instead of only a narrative note.

Dialogue bindings should be able to point at either:

- a clip as the primary execution unit
- a shot when the dialogue must be tied to the shot plan directly

### Step 5 - Media And Runtime Sync

Add the media and runtime tables:

- `media_assets`
- `clip_ref_bindings`
- any run manifest or approval support rows needed for sync

Then implement the file-to-database sync commands:

- `db-init`
- `db-upgrade`
- `db-sync-from-files`
- `db-validate`

### Step 6 - Staleness And Write-Through

Only after the tables above are stable:

- enable dependency propagation
- enable stale marking across downstream artifacts
- add limited write-through from runner/review flows
- keep file artifacts canonical

### Special Attention

- Do not collapse scene, shot, and clip into one table just because older runtime code still uses `clip_id` heavily.
- Do not treat shots as an alias for clips; shots are the planning layer and clips are the execution layer.
- Do not model characters, environments, or key items as children of scene or shot rows.
- Do not hide key items inside character or environment rows; they need their own registry and link tables.
- Do not let prompt packages become a wide nullable table with one column per asset class.
- Do not add new asset kinds by widening `prompt_packages`; add subject links instead.
- Do not treat dialogue as timeline-only data; it needs its own binding record.
- Do not require dialogue to be clip-only; keep shot binding available where the plan needs it.
- Do not make SQLite authoritative until the file-first contracts have stabilized.
- Do not let the migration sequence skip the file-first review artifacts; files remain the canonical source until the sync layer is proven.

## Sync Strategy

### First Sync Direction

- Files -> database

### Planned Sync Commands

- `python -m orchestrator db-init <project_slug>`
  - create the SQLite file if missing
- `python -m orchestrator db-upgrade <project_slug>`
  - apply migrations
- `python -m orchestrator db-sync-from-files <project_slug>`
  - parse project files and refresh relational records
- `python -m orchestrator db-validate <project_slug>`
  - verify file paths, foreign-key integrity, hashes, and required state links

### Write-Through Later

- runner and review flows should later update both:
  - files
  - SQLite rows

## Important Non-Goals For First Implementation

- Do not store prompt packages only in the database.
- Do not store image or video binary data inside the database.
- Do not require the database to exist for basic file inspection.
- Do not force a server or remote service.
- Do not make SQLite the only planner until the authoring and mapping model has stabilized.

## Acceptance

- A project database can represent:
  - chapters
  - scenes
  - beats
  - shots
  - clips
  - motion segments
  - characters
  - environments
  - key items
  - prompt packages
  - prompt ownership and lineage
  - dialogue bindings
  - runs
  - candidates
  - reviews
  - approvals
  - continuity links
- The database can answer:
  - which shots belong to a scene
  - which characters appear in a clip
  - which environment belongs to a clip
  - which key items are linked to a scene or clip
  - which refs should populate workflow slots
  - which prompt package belongs to a stage
  - which entity owns a prompt package
  - which dialogue belongs to a clip
  - which candidate won a review
  - which asset is currently approved for motion continuity
- The database supports later overnight batching and dependency resolution without replacing the file hierarchy.

