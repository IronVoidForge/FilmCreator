# Title
CH008_SC003 CL005 Scene Stage Prompt

# ID
CH008_SC003_CL005_scene_stage_prompt

# Purpose
Fill in the stage intent here. This clip captures the tracking motion following the haul operation, emphasizing the wide context of the plain and building, maintaining continuity with the previous medium shot of the prisoner being dragged.

# Workflow Type
authoring.scene_stage

# Positive Prompt
wide shot green martians dragging prisoner across plain surface drag marks visible building south background daylight smoke aftermath tactical care formation maintained vertical drop emphasized

# Negative Prompt
close up faces static shot night lighting missing building context blurry motion lifeless bodies wrong skin tone no drag marks on ground

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC003_BT002.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: prisoner_being_dragged_across_plain green_warriors_maintaining_formation building_south_of_position_in_background
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_shot
- continuity_mode: tracking_shots_following_haul_operation
- starting_keyframe_strategy: show_tracking_motion_following_haul_operation_with_plain_and_building_context_emphasized
- dependency_policy: dependent_on_previous_medium_shot_of_prisoner_being_dragged
- auto_advance_policy: 
- fallback_strategy: reblock_same_scene_if_tracking_fails_to_show_plain_and_building_context
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- note Tracking motion must remain consistent with previous medium shot of prisoner being dragged
- note Drag marks on plain surface must be visible to show movement axis
- note Building south of position must remain in background for context
- note Lighting must match daylight and smoke from fire aftermath
- note Warrior formation must stay coordinated during haul operation

# Repair Notes
- note If tracking fails to show plain and building context, reblock same scene
- note Ensure vertical drop from craft to ground is emphasized in transition
- note Check prisoner skin tone continuity with previous shots
- note Verify drag marks appear on plain surface indicating movement

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
