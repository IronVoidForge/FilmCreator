# Title
CH008_SC001 CL001 Fix 01 Prompt

# ID
CH008_SC001_CL001_fix_01_prompt

# Purpose
Refine approved keyframe composition and lighting while correcting local artifacts such as distorted anatomy or inconsistent background colors to maintain continuity with established golden frame style for Narrator at Window Observation scene.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium shot interior, human male narrator standing at window frame, calm observation state, gray airships visible in valley view outside, Martian city architecture below, natural daylight lighting with high stakes atmosphere, sharp focus on character details, correct anatomy for all figures, banners and glowing devices on ships clearly visible.

# Negative Prompt
distorted limbs, extra fingers, blue sky, text artifacts, blurry details, inconsistent lighting, shadow mismatches, deformed faces, missing weapons, incorrect clothing colors, low resolution, noise, grain, green skin on wrong characters, distorted anatomy in narrator, wrong background colors.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: narrator_standing_at_window, interior_window_frame, cityscape_below_view
- look_continuity_policy: preserve_approved_golden_frame_style
- intended_lighting_change: none
- composition_type: medium_shot_interior
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_subtle_body_shift
- dependency_policy: standalone_initial_test_clip
- auto_advance_policy: manual_review_required
- fallback_strategy: cut_to_wider_room_establishing_if_necessary
- consistency_assist_policy: enabled
- consistency_assist_method: frame_interpolation_refinement
- anatomy_repair_policy: strict_correction
- consistency_targets: character_placement, environmental_geometry, lighting_consistency
- style_profile: cinematic_barsoom_warfare
- batch_role: still_fix_primary
- fix_of: approved_keyframe_01

# Continuity Notes
- Maintain narrator position at interior window with clear line of sight to valley.
- Preserve airship movement direction (entering from horizon toward valley center).
- Ensure character positions match approved reference (narrator stationary, subtle body shift).
- Keep environmental transition from built interior to natural exterior view consistent.

# Repair Notes
- Correct any distorted anatomy in human narrator or Martian figures visible outside.
- Fix incorrect background colors (ensure Mars red/orange tones for valley/sky, not blue sky).
- Align lighting with approved golden frame (no sudden shadows or highlights inconsistent with interior daylight).
- Ensure text/wireless apparatus details on ships are clear and consistent if visible.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
