# Title
CH008_SC003 CL006 Cut Motion Prompt

# ID
CH008_SC003_CL006_cut_motion_prompt

# Purpose
Fill in the stage intent here. Establish emotional shift from curiosity to concern and discovery during medium shot of prisoner gathering, maintaining continuity with previous haul operation completion and keyframe lighting.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot of green warriors gathering around discovered human female prisoner on open plain, building south of position visible in background, daylight with smoke from fire, subtle camera movement emphasizing concern and discovery, prisoner remains stationary, tactical formation surrounding figure, atmospheric tension, wide horizon valley beyond.

# Negative Prompt
distorted anatomy, extra limbs, wrong lighting, dark shadows, night scene, blurry faces, excessive motion blur, floating objects, inconsistent skin tone, missing background elements, sudden camera shake, low resolution, morphing characters.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL006
- duration_seconds: 5
- required_refs: CH008_SC003_BT003.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_gathering_around_prisoner, prisoner_stationary_discovered_state, building_south_of_position_in_background
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: medium_shot
- continuity_mode: medium_shows_prisoner_discovery
- starting_keyframe_strategy: focus_on_warriors_gathering_around_prisoner_with_building_south_of_position_in_background
- dependency_policy: dependent_on_previous_tracking_shot_following_haul_operation_completion
- auto_advance_policy: smooth_transition_emphasizing_emotional_shift_from_curiosity_to_concern_and_discovery
- fallback_strategy: insert_close_up_if_medium_shots_fails_to_show_emotional_shift_from_curiosity_to_concern
- consistency_assist_policy: maintain_character_consistency_across_frames
- consistency_assist_method: 
- anatomy_repair_policy: fix_distorted_warrior_hands_and_prisoner_features
- consistency_targets: 
- style_profile: barsoom_action_daylight
- batch_role: cut_motion
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage. Maintain warrior green skin tone consistency. Ensure prisoner remains stationary during gathering. Keep background building stable. Preserve smoke/fire lighting effects from previous shots.

# Repair Notes
- Capture any repair or corrective guidance for this stage. Fix any morphing in prisoner's face if visible. Ensure warriors don't overlap incorrectly. Check for continuity errors with haul operation completion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
