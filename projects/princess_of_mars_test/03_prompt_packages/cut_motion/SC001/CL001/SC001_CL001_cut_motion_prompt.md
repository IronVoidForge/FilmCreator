# Title
SC001 CL001 Cut Motion Prompt

# ID
SC001_CL001_cut_motion_prompt

# Purpose
Generate cut motion starting from approved opening frame, preserving keyframe lighting and grade, focusing on visible motion, camera behavior, and environment change for window observation establishing shot.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Human male warrior stands at dark wood window sill inside upper floor room. Medium profile shot three-quarter angle facing outward. Hands resting on polished stone window ledge. Slight head tilt right toward distant horizon where gray airships form fleet in valley. Subtle forward weight shift onto legs as interest grows. Daylight sunlight reflects off ship devices outside. Dust motes visible in beam inside room. Cinematic grade preserved.

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
- composition_type: medium_profile_shot
- continuity_mode: window_frame_consistent
- starting_keyframe_strategy: establish_vertical_axis_elevated_observer
- dependency_policy: none_standalone_opening_shot
- auto_advance_policy: standard
- fallback_strategy: use_static_wide_if_zoom_unavailable
- consistency_assist_policy: enabled
- consistency_assist_method: interval_frames
- anatomy_repair_policy: enabled
- consistency_targets: narrator_position, green_warriors_fleet_position
- style_profile: epic_narrative
- batch_role: opening_sequence
- fix_of: none
- workflow_type: video.cut_motion.wan.i2v
- beat_index: BT001

# Continuity Notes
- Preserve keyframe lighting and grade by default.
- Focus on visible motion, camera behavior, and environment change.
- Ensure fleet approaches smoothly without jumping.
- Maintain window frame consistency (dark wood with metal accents).
- Keep window wiper position unchanged (upper right).
- Preserve floor material (polished stone tiles).
- Ensure narrator maintains 2-3 feet from window frame.

# Repair Notes
- Fix any morphing artifacts during zoom/pan transition.
- Ensure lighting consistency between exterior view and window frame interior.
- Correct anatomy if human observer or green warriors distort during movement.
- Maintain environment state (upper floor observation point) without introducing new crowds prematurely.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
