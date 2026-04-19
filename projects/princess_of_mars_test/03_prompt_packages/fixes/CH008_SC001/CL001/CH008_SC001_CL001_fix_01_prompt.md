# Title
CH008_SC001 CL001 Fix 01 Prompt

# ID
CH008_SC001_CL001_fix_01_prompt

# Purpose
Refine approved keyframe composition showing John Carter at upper floor window observing air craft arrival, correcting local artifacts such as distorted anatomy or inconsistent background colors to maintain continuity with established golden frame style. Preserve close-up face framing with window frame edge visible on left side.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Close-up shot of John Carter standing at upper floor window frame edge visible on left side, initial curiosity visible on face, body angled toward city view below, background valley and hills stable for continuity, natural daylight lighting with smoke from fire visible in distance, sharp focus on character details, correct anatomy for all figures, Mars red orange tones in environment.

# Negative Prompt
distorted limbs, extra fingers, blue sky, text artifacts, blurry details, inconsistent lighting, shadow mismatches, deformed faces, missing window frame, incorrect clothing colors, low resolution, noise, grain, green skin on Carter, wrong background geometry, sudden shadows or highlights.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: john_carter_upper_torso_face, window_frame_partial
- look_continuity_policy: preserve_approved_golden_frame_style
- intended_lighting_change: none
- composition_type: close_up_face_with_window_frame_edge
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: independent_no_prerequisites
- auto_advance_policy: manual_review_required
- fallback_strategy: insert
- consistency_assist_policy: enabled
- consistency_assist_method: frame_interpolation_refinement
- anatomy_repair_policy: strict_correction
- consistency_targets: character_placement, environmental_geometry, lighting_consistency
- style_profile: cinematic_barsoom_warfare
- batch_role: still_fix_primary
- fix_of: approved_keyframe_01

# Continuity Notes
- Maintain John Carter position at upper floor window.
- Preserve window frame visible on left edge of composition.
- Ensure background valley and hills stable for continuity across shots.
- Keep lighting consistent with approved golden frame (no sudden shadows or highlights).
- Maintain Mars red orange tones in environment, not blue sky.

# Repair Notes
- Correct any distorted anatomy on John Carter face or upper torso.
- Fix incorrect background colors (ensure Mars red/orange tones, not blue sky).
- Align lighting with approved golden frame (no sudden shadows or highlights).
- Ensure window frame edge is visible and properly positioned on left side.
- Verify valley/hills background continuity matches established reference.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
