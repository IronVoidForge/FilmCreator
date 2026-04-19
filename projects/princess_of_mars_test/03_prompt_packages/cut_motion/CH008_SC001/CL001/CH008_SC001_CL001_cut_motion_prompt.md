# Title
CH008_SC001 CL001 Cut Motion Prompt

# ID
CH008_SC001_CL001_cut_motion_prompt

# Purpose
Capture smooth forward progression of observation from interior window to sky view while maintaining established lighting and grade, ensuring visible motion aligns with approved keyframe continuity (static hold to subtle tension).

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
medium shot interior narrator standing at window frame, static opening frame transitioning to subtle body shift alert posture, cityscape below view visible through glass, valley terrain emerging ahead, natural lighting preserved, anticipation building in atmosphere, sky movement detected, calm observation state shifting to alertness, synchronized breathing visible, dust motes dancing in light, static camera maintaining medium shot

# Negative Prompt
morphing faces, flickering lights, static camera when motion expected, distorted limbs, inconsistent color grading, sudden zooms, blurry text, extra characters, wrong background, low resolution, noise, anatomy errors, lighting shifts, jerky movement, inconsistent character placement, marching warriors, airships appearing prematurely

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: narrator_standing_at_window, interior_window_frame, cityscape_below_view
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: medium_shot_interior
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_subtle_body_shift
- dependency_policy: standalone_initial_test_clip
- auto_advance_policy: smooth_forward_progression
- fallback_strategy: cut_to_wider_room_establishing_if_necessary
- consistency_assist_policy: enabled
- consistency_assist_method: motion_flow_matching
- anatomy_repair_policy: standard
- consistency_targets: character_placement_and_motion_smoothness
- style_profile: cinematic_warfare
- batch_role: clip_01
- fix_of: null

# Continuity Notes
- Maintain narrator position at interior window frame
- Preserve established lighting and color grade from approved keyframe
- Ensure camera holds medium shot without abrupt cuts or zooms
- Keep character placement consistent (narrator central, window framing view)

# Repair Notes
- If motion appears jerky, adjust interpolation for smoothness
- If lighting shifts occur, revert to keyframe grade
- If anatomy distorts during body shift, apply standard repair targets

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
