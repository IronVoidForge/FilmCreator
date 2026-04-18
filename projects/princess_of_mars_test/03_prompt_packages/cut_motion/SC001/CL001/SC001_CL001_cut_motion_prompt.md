# Title
SC001 CL001 Cut Motion Prompt

# ID
SC001_CL001_cut_motion_prompt

# Purpose
Generate cut motion starting from approved opening frame, preserving keyframe lighting and grade, focusing on visible motion, camera behavior, and environment change.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Over-the-shoulder view of human observer looking out window frame. Fleet of gray vessels approaches in distance valley. Slight zoom or pan tracks fleet movement. Deserted city buildings and open plaza visible. Daylight lighting consistent with keyframe. Cinematic grade.

# Negative Prompt
morphing artifacts, flickering lighting, wrong anatomy, extra characters, sudden crowd appearance, incorrect camera angle, distorted background, inconsistent grade, blurry motion, static frame, low resolution

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 breakdown
- optional_refs: Procession garment details, plaza distance markers
- visible_character_assets: human observer at window frame, green warriors on balcony below
- look_continuity_policy: preserve_keyframe_lighting
- intended_lighting_change: none
- composition_type: over_the_shoulder_observation_to_zoom_track_fleet
- continuity_mode: cut
- starting_keyframe_strategy: establish_vertical_axis_elevated_observer
- dependency_policy: none_standalone_opening_shot
- auto_advance_policy: standard
- fallback_strategy: use_static_wide_if_zoom_unavailable
- consistency_assist_policy: enabled
- consistency_assist_method: interval_frames
- anatomy_repair_policy: enabled
- consistency_targets: narrator_position, woola_position
- style_profile: epic_narrative
- batch_role: opening_sequence
- fix_of: none

# Continuity Notes
- Preserve keyframe lighting and grade by default.
- Focus on visible motion, camera behavior, and environment change.
- Ensure fleet approaches smoothly without jumping.
- Maintain vertical axis of observer above city.
- Keep green warriors stationary or firing in place below.

# Repair Notes
- Fix any morphing artifacts during zoom/pan transition.
- Ensure lighting consistency between exterior view and window frame interior.
- Correct anatomy if human observer or green warriors distort during movement.
- Maintain environment state (deserted streets) without introducing new crowds prematurely.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
