# Title
CH008_SC001 CL001 Cut Motion Prompt

# ID
CH008_SC001_CL001_cut_motion_prompt

# Purpose
Capture smooth forward progression of procession from city plaza to open ground threshold while maintaining established lighting and grade, ensuring visible motion aligns with approved keyframe continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
wide establishing shot of green martian warriors marching in formation through city plaza towards open ground horizon, procession moving forward smoothly along axis, camera tracks alongside group maintaining wide angle, built structures receding left right, valley terrain emerging ahead, natural lighting preserved, anticipation building in atmosphere, synchronized steps visible, dust rising from boots, static opening frame transitioning to motion

# Negative Prompt
morphing faces, flickering lights, static camera when motion expected, distorted limbs, inconsistent color grading, sudden zooms, blurry text, extra characters, wrong background, low resolution, noise, anatomy errors, lighting shifts, jerky movement, inconsistent character placement

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter rear_position, Warriors central_column
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: wide_establishing
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_opening_with_procession_movement_visible
- dependency_policy: independent_no_prerequisites
- auto_advance_policy: smooth_forward_progression
- fallback_strategy: cut_to_alternate_wide_angle_if_needed
- consistency_assist_policy: enabled
- consistency_assist_method: motion_flow_matching
- anatomy_repair_policy: standard
- consistency_targets: character_placement_and_motion_smoothness
- style_profile: cinematic_warfare
- batch_role: clip_01
- fix_of: null

# Continuity Notes
- Maintain procession movement direction from city plaza to open ground
- Preserve established lighting and color grade from approved keyframe
- Ensure camera tracks smoothly without abrupt cuts or zooms
- Keep character placement consistent (Carter rear, Warriors center)

# Repair Notes
- If motion appears jerky, adjust interpolation for smoothness
- If lighting shifts occur, revert to keyframe grade
- If anatomy distorts during march, apply standard repair targets

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
