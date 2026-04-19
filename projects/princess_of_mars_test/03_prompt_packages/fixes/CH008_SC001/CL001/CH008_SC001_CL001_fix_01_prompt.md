# Title
CH008_SC001 CL001 Fix 01 Prompt

# ID
CH008_SC001_CL001_fix_01_prompt

# Purpose
Refine approved keyframe composition and lighting while correcting local artifacts such as distorted anatomy or inconsistent background colors to maintain continuity with established golden frame style.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide establishing shot of procession returning through city plaza, green warriors in central column marching forward, rear figure positioned at back, anticipation building among onlookers, city architecture framing left and right sides, environmental transition from built environment to natural valley terrain visible in background, natural daylight lighting with high stakes atmosphere, sharp focus on character details, correct anatomy for all figures.

# Negative Prompt
distorted limbs, extra fingers, wrong background colors, blue sky, text artifacts, blurry details, inconsistent lighting, shadow mismatches, deformed faces, missing weapons, incorrect clothing colors, low resolution, noise, grain.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: rear_position, central_column_warriors, implied_commanders_ahead
- look_continuity_policy: preserve_approved_golden_frame_style
- intended_lighting_change: none
- composition_type: wide_establishing
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_opening_with_procession_movement_visible
- dependency_policy: independent_no_prerequisites
- auto_advance_policy: manual_review_required
- fallback_strategy: cut_to_alternate_wide_angle_if_needed
- consistency_assist_policy: enabled
- consistency_assist_method: frame_interpolation_refinement
- anatomy_repair_policy: strict_correction
- consistency_targets: character_placement, environmental_geometry, lighting_consistency
- style_profile: cinematic_barsoom_warfare
- batch_role: still_fix_primary
- fix_of: approved_keyframe_01

# Continuity Notes
- Maintain procession movement direction (forward through plaza).
- Preserve city architecture framing on left/right.
- Ensure character positions match approved reference (rear figure, Warriors center).
- Keep environmental transition from built to natural terrain consistent.

# Repair Notes
- Correct any distorted anatomy in green warriors or rear figure.
- Fix incorrect background colors (ensure Mars red/orange tones, not blue sky).
- Align lighting with approved golden frame (no sudden shadows or highlights).
- Ensure text/wireless apparatus details are clear and consistent.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
