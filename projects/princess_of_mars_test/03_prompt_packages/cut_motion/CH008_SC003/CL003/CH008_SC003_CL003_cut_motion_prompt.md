# Title
CH008_SC003 CL003 Cut Motion Prompt

# ID
CH008_SC003_CL003_cut_motion_prompt

# Purpose
Complete boarding action transition from roof to craft, shift focus to interior and prisoner context while maintaining battle aftermath lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green warriors inside drifting craft, movement from roof to craft complete, building roofs to plain transition, smoke and flame effects, camera tracking smooth motion, daylight lighting, aftermath battle environment, focus shift interior, bodies strewn about in plain, wide shot composition.

# Negative Prompt
morphing faces, flickering frames, extra limbs, wrong colors, static images, text artifacts, blurry details, inconsistent lighting, sudden cuts, distorted geometry, missing characters, floating objects.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC003_BT001.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_inside_drifting_craft, bodies_strewn_about_in_plain
- look_continuity_policy: preserve_keyframe_lighting_and_grade_by_default
- intended_lighting_change: none
- composition_type: wide_shot
- continuity_mode: tracking_shows_building_roofs_to_plain_transition
- starting_keyframe_strategy: show_warriors_successfully_boarding_drifting_craft_with_complete_movement
- dependency_policy: dependent_on_previous_close_up_of_approach_action
- auto_advance_policy: 
- fallback_strategy: reblock_same_scene_if_tracking_fails_to_show_complete_movement_completion
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain daylight lighting and smoke/flame effects from approved keyframe.
- Ensure smooth camera tracking transition from building roofs to plain level.
- Preserve bodies strewn about in plain for continuity with previous clips.
- Focus shift from boarding action to interior must be gradual within motion interval.
- Avoid sudden jumps in warrior positioning or craft drift direction.

# Repair Notes
- If tracking fails to show complete movement, reblock same scene if necessary.
- Check focus shift timing; adjust if prisoner is not visible at 5s mark.
- Verify lighting consistency with previous clip (CL002) before generation.
- Ensure craft damage and banners remain consistent with battle aftermath state.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
