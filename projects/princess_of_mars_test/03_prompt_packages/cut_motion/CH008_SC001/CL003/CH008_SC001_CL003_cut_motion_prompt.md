# Title
CH008_SC001 CL003 Cut Motion Prompt

# ID
CH008_SC001_CL003_cut_motion_prompt

# Purpose
Establish airship fleet arrival and introduce visual threat elements.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Multiple gray-painted airships descend into frame from northern horizon, strange banners on prow, odd devices on prow, daylight with smoke and fire effects, extreme long sky composition, preserved lighting grade, static camera position to capture full approach, vessels maintain consistent descent angle.

# Negative Prompt
morphing face, extra limbs, flickering signal, wrong color palette, blurry text, distorted background, inconsistent lighting, static image, low resolution, interior shadows swallowing figures.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md, color grading notes
- optional_refs: prop placement for banners and devices on prow
- visible_character_assets: multiple gray-painted airships
- look_continuity_policy: preserve_keyframe_lighting_and_grade_by_default
- intended_lighting_change: none_significant_during_retreat_sequence
- composition_type: extreme_long_sky
- continuity_mode: insert
- starting_keyframe_strategy: northern_sky_clear_with_no_visible_aircraft
- dependency_policy: none_required
- auto_advance_policy: none
- fallback_strategy: static_wide_angle_showing_full_fleet_formation_if_descent_fails
- consistency_assist_policy: ensure_group_consistency_across_vessels
- consistency_assist_method: reference_previous_clip_group_placement
- anatomy_repair_policy: correct_any_figure_drift_during_crowding_motion
- consistency_targets: vessel_deck_axis_and_forward_sections
- style_profile: cinematic_compositional
- batch_role: cut_motion_sequence
- fix_of: CL002_output
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Ensure airship descent angle is consistent. Vessels descending toward city building facade.

# Repair Notes
- Ensure airship consistency with previous clip group placement. Maintain vessel consistency without distortion. Correct any vessel drift during descent motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
