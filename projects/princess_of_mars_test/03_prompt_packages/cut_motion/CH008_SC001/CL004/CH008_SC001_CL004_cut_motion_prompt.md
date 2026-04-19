# Title
CH008_SC001 CL004 Cut Motion Prompt

# ID
CH008_SC001_CL004_cut_motion_prompt

# Purpose
Describe the cut beat, framing, and continuity intent for this clip. Establish John Carter's growing concern/anticipation as he watches air craft descend from upper floor window. Focus on subtle emotional shifts in facial expression and minimal posture movement reflecting anticipation.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Close-up face of human male protagonist showing growing concern and anticipation. Window frame visible on left edge of composition. Background valley and distant hills stable for continuity. Minimal camera movement - subtle shifts in facial expression and slight posture adjustment reflecting emotional change. Daylight high contrast lighting consistent with previous keyframe. No sudden motion or dramatic gestures.

# Negative Prompt
morphing faces extra limbs sudden zoom darkening or brightening exposure floating objects incorrect marching direction blurry text distorted anatomy static image low resolution color bleeding glitchy transitions facial distortion expression snapping camera shake lighting shift background blur.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: john_carter upper_torso_face, window_frame partial_left_edge
- look_continuity_policy: preserve_lighting_grade
- intended_lighting_change: none
- composition_type: close_up_face_window_frame
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: none
- auto_advance_policy: insert
- fallback_strategy: insert
- consistency_assist_policy: preserve_character_count
- consistency_assist_method: literal_descriptive
- anatomy_repair_policy: apply_if_distortion_detected
- consistency_targets: facial_expression_progression, window_frame_position, background_continuity
- style_profile: cinematic_compositional
- batch_role: cut_motion
- fix_of: CL003
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Ensure subtle emotional progression in facial expression without snapping. Maintain window frame position consistent with previous shot. Keep background valley/hills stable for continuity tracking. Character count remains at one protagonist.

# Repair Notes
- If facial expression shift is too abrupt, reduce intensity of concern markers. If lighting shifts, force continuity with previous frame. If window frame position drifts, apply spatial correction. If background blurs or moves unexpectedly, stabilize environment elements. If anatomy distorts during subtle posture adjustment, apply repair policy to maintain natural proportions.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
