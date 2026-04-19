# Title
CH008_SC003 CL003 Scene Stage Prompt

# ID
CH008_SC003_CL003_scene_stage_prompt

# Purpose
Establish aftermath of battle, vertical transition from building roofs to plain via boarding action completion, set focus for prisoner discovery sequence.

# Workflow Type
authoring.scene_stage

# Positive Prompt
wide shot composition showing green warriors inside drifting craft with movement from roof to craft complete, bodies strewn about in plain below, daylight conditions with smoke from fire visible, city buildings in background, vertical axis established between elevated roofs and ground level.

# Negative Prompt
blurry motion, missing bodies, incorrect lighting, wrong composition angle, lack of smoke or fire aftermath cues, static warriors without movement indication.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC003_BT001.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_inside_drifting_craft, bodies_strewn_about_in_plain
- look_continuity_policy: tracking_shows_building_roofs_to_plain_transition
- intended_lighting_change: daylight_with_smoke_from_fire
- composition_type: wide_shot
- continuity_mode: tracking_shows_building_roofs_to_plain_transition
- starting_keyframe_strategy: show_warriors_successfully_boarding_drifting_craft_with_complete_movement
- dependency_policy: dependent_on_previous_close_up_of_approach_action
- auto_advance_policy: smooth_transition_emphasizing_completion_of_boarding_action_with_focus_shift_to_prisoner
- fallback_strategy: reblock_same_scene_if_tracking_fails_to_show_complete_movement_completion
- consistency_assist_policy: show_warriors_inside_drifting_craft_with_movement_from_roof_to_craft_complete
- consistency_assist_method: 
- anatomy_repair_policy: maintain_vertical_axis_between_roofs_and_plain
- consistency_targets: 
- style_profile: action_oriented_aftermath_of_battle
- batch_role: scene_stage
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage.
- Maintain vertical axis between elevated building roofs and ground plain level.
- Ensure bodies strewn about remain visible as continuity element indicating aftermath.
- Confirm boarding action shows complete movement from roof to craft interior.
- Avoid premature focus shift to prisoner before boarding completion is established.

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- Reblock same scene if tracking fails to show complete movement completion.
- Adjust focus if prisoner signal appears too early relative to boarding action.
- Verify smoke and fire damage cues match previous battle sequence context.
- Ensure green warriors positioning reflects tactical formation during haul operation.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
