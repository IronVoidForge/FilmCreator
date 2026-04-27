Status: 95%

# Spec Status Index

**Purpose**: This index tracks the reorganization of spec files into a planned work taxonomy.

**Important**: Files have been reorganized into planned order. No specs were renamed to `__complete.md` in this pass. This is a documentation/file-organization pass only, not a completion certification.

---

## Status Definitions

- `implemented_reference` - Substantially implemented; kept as reference documentation
- `active_blocker` - Current blocker preventing clean resume/validation
- `active_validation` - Implemented but needs nonzero artifact validation
- `next_phase` - Next planned implementation phase
- `later_phase` - Later pipeline work
- `deferred` - Deferred to future
- `config_data` - Active configuration data (not moved to avoid breaking code paths)
- `obsolete_archive` - Historical/superseded documentation
- `review_needed` - Uncertain classification; needs manual review

---

## Reorganization Summary

| New Path | Original Path | Category | Status | Notes / Evidence To Recheck |
|----------|---------------|----------|--------|------------------------------|
| **01_reference_architecture/** | | | | **Broad architecture and roadmap docs** |
| 01_reference_architecture/00_README.md | spec/README.md | Architecture | implemented_reference | Original spec folder README |
| 01_reference_architecture/01_PROPOSED_STRUCTURE_1_0.md | spec/PROPOSED_STRUCTURE_1_0.md | Architecture | implemented_reference | Original structure proposal |
| 01_reference_architecture/02_IMPLEMENTATION_ROADMAP.md | spec/IMPLEMENTATION_ROADMAP.md | Architecture | implemented_reference | Historical roadmap |
| 01_reference_architecture/03_CLI_PIPELINE_ORCHESTRATOR_SPEC.md | spec/CLI_PIPELINE_ORCHESTRATOR_SPEC.md | Architecture | implemented_reference | CLI orchestrator design |
| 01_reference_architecture/04_MULTI_CHAPTER_WORLD_MODEL_PLAN.md | spec/MULTI_CHAPTER_WORLD_MODEL_PLAN.md | Architecture | implemented_reference | Multi-chapter world model plan |
| **02_completed_or_implemented_reference/** | | | | **Implemented specs kept as reference** |
| 02_completed_or_implemented_reference/01_foundation/01_01_repo_project_scene_clip_hierarchy.md | spec/1_foundation/1.1_repo_project_scene_clip_hierarchy.md | Foundation | implemented_reference | Hierarchy implemented |
| 02_completed_or_implemented_reference/01_foundation/01_02_id_naming_and_file_conventions.md | spec/1_foundation/1.2_id_naming_and_file_conventions.md | Foundation | implemented_reference | Naming conventions in use |
| 02_completed_or_implemented_reference/01_foundation/01_03_workflow_catalog_and_registry.md | spec/1_foundation/1.3_workflow_catalog_and_registry__complete.md | Foundation | implemented_reference | Removed `__complete` suffix; workflow catalog implemented |
| 02_completed_or_implemented_reference/01_foundation/01_05_project_scene_clip_state_contracts.md | spec/1_foundation/1.5_project_scene_clip_state_contracts.md | Foundation | implemented_reference | State contracts implemented |
| 02_completed_or_implemented_reference/02_story_analysis/02_01_story_analysis_outputs.md | spec/5_authoring/5.1_story_analysis_outputs.md | Story Analysis | implemented_reference | Story analysis outputs implemented |
| 02_completed_or_implemented_reference/03_synthesis_phases/03_01_phase_07_character_bible_synthesis.md | spec/phases/PHASE_07_CHARACTER_BIBLE_SYNTHESIS.md | Synthesis | implemented_reference | Character bible synthesis implemented |
| 02_completed_or_implemented_reference/03_synthesis_phases/03_02_phase_08_environment_bible_synthesis.md | spec/phases/PHASE_08_ENVIRONMENT_BIBLE_SYNTHESIS.md | Synthesis | implemented_reference | Environment bible synthesis implemented |
| 02_completed_or_implemented_reference/03_synthesis_phases/03_03_phase_09_5_scene_binding_and_environment_selection.md | spec/phases/PHASE_09_5_SCENE_BINDING_AND_ENVIRONMENT_SELECTION.md | Synthesis | implemented_reference | Scene binding implemented |
| 02_completed_or_implemented_reference/03_synthesis_phases/03_04_phase_11_5_prompt_preparation.md | spec/phases/PHASE_11_5_PROMPT_PREPARATION.md | Synthesis | implemented_reference | Prompt preparation implemented |
| 02_completed_or_implemented_reference/03_synthesis_phases/03_05_phase_11_8_quality_grading_and_selective_reruns.md | spec/phases/PHASE_11_8_QUALITY_GRADING_AND_SELECTIVE_RERUNS.md | Synthesis | implemented_reference | Quality grading implemented; verify orchestrator/quality_grading.py |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_01_fallback_safety_patch.md | spec/refactor_entity_taxonomy/01_FALLBACK_SAFETY_PATCH.md | Taxonomy | implemented_reference | Fallback safety implemented; verify orchestrator/character_bible_fallback.py |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_02_chapter_entity_extraction.md | spec/refactor_entity_taxonomy/02_CHAPTER_ENTITY_EXTRACTION.md | Taxonomy | implemented_reference | Entity extraction implemented |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_03_character_taxonomy_stage.md | spec/refactor_entity_taxonomy/03_CHARACTER_TAXONOMY_STAGE.md | Taxonomy | implemented_reference | Character taxonomy implemented; verify orchestrator/character_taxonomy.py |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_04_world_refinement_taxonomy_integration.md | spec/refactor_entity_taxonomy/04_WORLD_REFINEMENT_TAXONOMY_INTEGRATION.md | Taxonomy | implemented_reference | World refinement taxonomy integration; verify orchestrator/world_refinement.py |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_05_character_bible_taxonomy_integration.md | spec/refactor_entity_taxonomy/05_CHARACTER_BIBLE_TAXONOMY_INTEGRATION.md | Taxonomy | implemented_reference | Character bible taxonomy integration; verify orchestrator/character_bible.py |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_06_fallback_from_taxonomy.md | spec/refactor_entity_taxonomy/06_FALLBACK_FROM_TAXONOMY.md | Taxonomy | implemented_reference | Fallback from taxonomy implemented |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_07_quality_grading_rerun_routing.md | spec/refactor_entity_taxonomy/07_QUALITY_GRADING_RERUN_ROUTING.md | Taxonomy | implemented_reference | Quality grading rerun routing implemented |
| 02_completed_or_implemented_reference/04_entity_taxonomy_refactor/04_08_fix_phase3_phase5_taxonomy_ownership.md | spec/refactor_entity_taxonomy/09_FIX_PHASE3_PHASE5_TAXONOMY_OWNERSHIP.md | Taxonomy | implemented_reference | Phase 3/5 taxonomy ownership fixed |
| 02_completed_or_implemented_reference/05_quality_rework_reference/05_01_descriptor_prompt_normalization.md | spec/quality_rework_2026_04/02_DESCRIPTOR_PROMPT_NORMALIZATION.md | Quality | implemented_reference | Descriptor prompt normalization implemented |
| **03_active_current_blockers/** | | | | **Current blockers preventing clean validation** |
| 03_active_current_blockers/01_smart_resume_validation.md | spec/quality_rework_2026_04/05_SMART_RESUME_VALIDATION.md | Resume | active_blocker | **CRITICAL**: Validate resume/BAT execution so detecting character_bibles starts at character bibles and does not skip to shot packages or write zero-entry downstream artifacts |
| 03_active_current_blockers/02_artifact_lifecycle_and_reuse.md | spec/system/ARTIFACT_LIFECYCLE_AND_REUSE.md | System | active_blocker | Artifact lifecycle and reuse patterns |
| 03_active_current_blockers/03_dependency_graph_and_staleness.md | spec/system/DEPENDENCY_GRAPH_AND_STALENESS.md | System | active_blocker | Dependency graph and staleness detection |
| 03_active_current_blockers/04_asset_ownership_and_lineage.md | spec/system/ASSET_OWNERSHIP_AND_LINEAGE.md | System | active_blocker | Asset ownership and lineage tracking |
| 03_active_current_blockers/05_review_and_approval_model.md | spec/system/REVIEW_AND_APPROVAL_MODEL.md | System | active_blocker | Review and approval workflow |
| 03_active_current_blockers/06_runner_cli_and_job_dispatch.md | spec/4_orchestration/4.1_runner_cli_and_job_dispatch.md | Orchestration | active_blocker | Runner CLI and job dispatch |
| 03_active_current_blockers/07_output_routing_logging_and_manifests.md | spec/4_orchestration/4.3_output_routing_logging_and_manifests.md | Orchestration | active_blocker | Output routing, logging, and manifests |
| **04_active_validation/** | | | | **Implemented but needs nonzero artifact validation** |
| 04_active_validation/01_prompt_package_schema.md | spec/1_foundation/1.4_prompt_package_schema.md | Foundation | active_validation | **VERIFY**: Spec requires `Repair Notes`; check if orchestrator/prompt_package.py parses it as optional |
| 04_active_validation/02_phase_09_scene_contracts.md | spec/phases/PHASE_09_SCENE_CONTRACTS.md | Phase | active_validation | Scene contracts need validation |
| 04_active_validation/03_phase_10_shot_planning.md | spec/phases/PHASE_10_SHOT_PLANNING.md | Phase | active_validation | **VERIFY**: Nonzero CH002-CH003 run proves shot packages generated and inherit scene bindings |
| 04_active_validation/04_phase_11_dialogue_timeline.md | spec/phases/PHASE_11_DIALOGUE_TIMELINE.md | Phase | active_validation | Dialogue timeline needs validation |
| 04_active_validation/05_phase_11_7_descriptor_enrichment.md | spec/phases/PHASE_11_7_DESCRIPTOR_ENRICHMENT.md | Phase | active_validation | **VERIFY**: Nonzero run proves descriptor entries and prompt consumption |
| 04_active_validation/06_environment_and_shot_prompt_injection.md | spec/quality_rework_2026_04/03_ENVIRONMENT_AND_SHOT_PROMPT_INJECTION.md | Quality | active_validation | Environment and shot prompt injection needs validation |
| 04_active_validation/07_quality_grading_calibration.md | spec/quality_rework_2026_04/04_QUALITY_GRADING_CALIBRATION.md | Quality | active_validation | Quality grading calibration needs validation |
| 04_active_validation/08_focused_test_plan.md | spec/quality_rework_2026_04/06_TEST_PLAN.md | Testing | active_validation | Focused test plan for validation |
| 04_active_validation/09_final_cleanup_before_cross_book_validation.md | spec/refactor_entity_taxonomy/11_FINAL_CLEANUP_BEFORE_CROSS_BOOK_VALIDATION.md | Taxonomy | active_validation | Final cleanup before cross-book validation |
| **05_reference_generation_next/** | | | | **Next phase: reference generation and approval** |
| 05_reference_generation_next/01_phase_12_character_sheet_generation_and_approval.md | spec/phases/PHASE_12_CHARACTER_SHEET_GENERATION_AND_APPROVAL.md | Phase | next_phase | Character sheet generation and approval |
| 05_reference_generation_next/02_phase_13_environment_reference_generation_and_approval.md | spec/phases/PHASE_13_ENVIRONMENT_REFERENCE_GENERATION_AND_APPROVAL.md | Phase | next_phase | Environment reference generation and approval |
| 05_reference_generation_next/03_legacy_character_reference_generation.md | spec/2_shared_assets/2.1_character_reference_generation.md | Legacy | next_phase | **NOTE**: May be outdated; current code uses 03_reference_assets rather than old 04_references; verify orchestrator/character_references.py |
| 05_reference_generation_next/04_legacy_environment_reference_generation.md | spec/2_shared_assets/2.2_environment_reference_generation.md | Legacy | next_phase | **NOTE**: May be outdated; verify orchestrator/environment_references.py |
| 05_reference_generation_next/05_legacy_shared_ref_promotion_and_reuse.md | spec/2_shared_assets/2.3_shared_ref_promotion_and_reuse.md | Legacy | next_phase | **NOTE**: May be outdated; verify orchestrator/reference_assets.py |
| **06_later_clip_pipeline/** | | | | **Later clip/image pipeline work** |
| 06_later_clip_pipeline/01_clip_input_contract.md | spec/3_clip_pipeline/3.1_clip_input_contract.md | Clip | later_phase | Clip input contract |
| 06_later_clip_pipeline/02_scene_build_and_golden_frame.md | spec/3_clip_pipeline/3.2_scene_build_and_golden_frame.md | Clip | later_phase | Scene build and golden frame |
| 06_later_clip_pipeline/03_anchor_and_interval_frames.md | spec/3_clip_pipeline/3.3_anchor_and_interval_frames.md | Clip | later_phase | Anchor and interval frames |
| 06_later_clip_pipeline/04_clip_review_and_selection.md | spec/3_clip_pipeline/3.4_clip_review_and_selection.md | Clip | later_phase | Clip review and selection |
| 06_later_clip_pipeline/05_phase_11_1_dialogue_second_pass_binding_and_delivery.md | spec/phases/PHASE_11_1_DIALOGUE_SECOND_PASS_BINDING_AND_DELIVERY.md | Phase | later_phase | Dialogue second pass binding and delivery |
| 06_later_clip_pipeline/06_phase_11_6_key_item_index.md | spec/phases/PHASE_11_6_KEY_ITEM_INDEX.md | Phase | later_phase | Key item index |
| 06_later_clip_pipeline/07_phase_11_9_quality_smoothing_and_patch_repair.md | spec/phases/PHASE_11_9_QUALITY_SMOOTHING_AND_PATCH_REPAIR.md | Phase | later_phase | Quality smoothing and patch repair |
| 06_later_clip_pipeline/08_comfyui_client_and_workflow_patching.md | spec/4_orchestration/4.2_comfyui_client_and_workflow_patching.md | Orchestration | later_phase | **NOTE**: Core implemented, but live ComfyUI smoke validation belongs later |
| 06_later_clip_pipeline/09_automated_testing_and_ci_strategy.md | spec/4_orchestration/4.4_automated_testing_and_ci_strategy.md | Testing | later_phase | Automated testing and CI strategy |
| **07_deferred_future/** | | | | **Deferred to future** |
| 07_deferred_future/01_sqlite_relational_model.md | spec/1_foundation/1.6_sqlite_relational_model.md | Foundation | deferred | SQLite relational model |
| 07_deferred_future/02_video_motion_stage.md | spec/6_deferred/6.1_video_motion_stage.md | Video | deferred | Video motion stage |
| 07_deferred_future/03_acceptance_test_matrix.md | spec/6_deferred/6.2_acceptance_test_matrix.md | Testing | deferred | Acceptance test matrix |
| 07_deferred_future/04_kupkaprod_lessons_and_integration_plan.md | spec/deferred/KUPKAPROD_LESSONS_AND_INTEGRATION_PLAN.md | Integration | deferred | KupkaProd lessons and integration plan |
| 07_deferred_future/05_prompt_quality_booster_library.md | spec/6_deferred/PROMPT_QUALITY_BOOSTER_LIBRARY.md | Prompts | deferred | Prompt quality booster library spec |
| 07_deferred_future/future_issues/ | spec/6_deferred/future_issues/ | Issues | deferred | Future issues folder |
| **08_config_data/** | | | | **Active configuration data** |
| spec/prompt_boosters/*.json | spec/prompt_boosters/*.json | Config | config_data | **NOT MOVED**: Code hardcodes path in orchestrator/prompt_boosters.py (BOOSTER_LIBRARY_PATHS); moving would break runtime |
| **09_archive_obsolete/** | | | | **Historical/superseded documentation** |
| 09_archive_obsolete/entity_taxonomy/00_master_plan.md | spec/refactor_entity_taxonomy/00_MASTER_PLAN.md | Taxonomy | obsolete_archive | Historical master plan |
| 09_archive_obsolete/entity_taxonomy/08_implementation_order_and_validation.md | spec/refactor_entity_taxonomy/08_IMPLEMENTATION_ORDER_AND_VALIDATION.md | Taxonomy | obsolete_archive | Historical implementation order |
| 09_archive_obsolete/entity_taxonomy/10_empty_fix_phase7_and_taxonomy_hint_parser.md | spec/refactor_entity_taxonomy/10_FIX_PHASE7_AND_TAXONOMY_HINT_PARSER.md | Taxonomy | obsolete_archive | **EMPTY FILE**: Archived instead of deleted |
| 09_archive_obsolete/quality_rework_2026_04/00_overview.md | spec/quality_rework_2026_04/00_OVERVIEW.md | Quality | obsolete_archive | Historical overview |
| 09_archive_obsolete/quality_rework_2026_04/01_character_bible_production_fallbacks_superseded.md | spec/quality_rework_2026_04/01_CHARACTER_BIBLE_PRODUCTION_FALLBACKS.md | Quality | obsolete_archive | Superseded by taxonomy refactor |
| 09_archive_obsolete/quality_rework_2026_04/07_fallback_bucket_refactor_superseded.md | spec/quality_rework_2026_04/07_FALLBACK_BUCKET_REFACTOR.md | Quality | obsolete_archive | Superseded by taxonomy refactor |
| 09_archive_obsolete/quality_rework_2026_04/08_character_bible_regen_and_spotcheck_one_time.md | spec/quality_rework_2026_04/08_CHARACTER_BIBLE_REGEN_AND_SPOTCHECK.md | Quality | obsolete_archive | One-time validation task |
| 09_archive_obsolete/authoring_bridge/05_02_clip_plan_generation_superseded.md | spec/5_authoring/5.2_clip_plan_generation.md | Authoring | obsolete_archive | Superseded by current pipeline |
| 09_archive_obsolete/authoring_bridge/05_03_prompt_writer_integration_superseded.md | spec/5_authoring/5.3_prompt_writer_integration.md | Authoring | obsolete_archive | Superseded by current pipeline |
| 09_archive_obsolete/duplicate_prompt_quality_booster_library.md | spec/deferred/PROMPT_QUALITY_BOOSTER_LIBRARY.md | Prompts | obsolete_archive | Duplicate of spec/6_deferred version (nearly identical, different line endings) |

---

## Files Not Moved

- `spec/prompt_boosters/*.json` - **Active config data**; hardcoded path in `orchestrator/prompt_boosters.py`; moving would break runtime

---

## Empty Old Directories Removed

- `spec/1_foundation/`
- `spec/2_shared_assets/`
- `spec/3_clip_pipeline/`
- `spec/4_orchestration/`
- `spec/5_authoring/`
- `spec/6_deferred/`
- `spec/deferred/`
- `spec/phases/`
- `spec/refactor_entity_taxonomy/`
- `spec/quality_rework_2026_04/`
- `spec/system/`

---

## Critical Blockers

**Current blocker**: Validate resume/BAT execution so detecting character_bibles starts at character bibles and does not skip to shot packages or write zero-entry downstream artifacts.

See: `03_active_current_blockers/01_smart_resume_validation.md`

---

## Verification Notes

- All taxonomy specs verified against `orchestrator/character_taxonomy.py`, `orchestrator/world_refinement.py`, `orchestrator/character_bible.py`, `orchestrator/character_bible_fallback.py`, `orchestrator/quality_grading.py`
- Prompt package schema mismatch noted: spec requires `Repair Notes`; implementation may parse as optional
- Legacy 2.x shared asset specs may be outdated; current code uses `03_reference_assets` rather than old `04_references`
- No specs renamed to `__complete.md` in this pass
- No orchestrator/test/launcher implementation behavior changed
- All spec Markdown content kept intact

---

## Next Steps

1. Validate smart resume to prevent zero-entry artifact generation
2. Run nonzero CH002-CH003 validation for shot planning and descriptor enrichment
3. Verify prompt package schema alignment with implementation
4. Review legacy 2.x shared asset specs against current implementation
5. Consider moving to Phase 12/13 reference generation after validation passes

