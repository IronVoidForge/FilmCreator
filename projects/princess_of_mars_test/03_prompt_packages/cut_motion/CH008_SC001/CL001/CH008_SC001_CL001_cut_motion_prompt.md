# Title
CH008_SC001 CL001 Cut Motion Prompt

# ID
CH008_SC001_CL001_cut_motion_prompt

# Purpose
Establish John Carter's perspective and emotional state as he watches air craft descend from upper floor window. Start State: Static hold showing curiosity, End State: Slight posture shift indicating engagement with scene. Capture smooth progression of observation while maintaining established lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
close-up shot of John Carter standing at upper floor window frame edge, face displaying initial curiosity and concern, background valley and hills stable in daylight, slight camera movement or subtle subject motion visible, natural lighting preserved, atmospheric depth maintained, static opening frame transitioning to gentle observation motion

# Negative Prompt
morphing faces, flickering lights, static camera when motion expected, distorted limbs, inconsistent color grading, sudden zooms, blurry text, extra characters, wrong background, low resolution, noise, anatomy errors, lighting shifts, jerky movement, inconsistent character placement, warping environment, incorrect horizon line

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: John Carter (upper torso, face), window frame partial
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: close-up_face_with_window_frame_edge
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
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
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain John Carter's position at window frame edge
- Preserve established lighting and color grade from approved keyframe
- Ensure background valley/hills remain stable for continuity
- Monitor subtle posture shifts reflecting emotional change
- Keep character count consistent (John Carter only)

# Repair Notes
- If face morphs, revert to stable anatomy matching keyframe
- If lighting shifts occur, match keyframe grade exactly
- If camera movement is jerky, smooth interpolation
- If background warps, correct to valley/hills continuity

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
