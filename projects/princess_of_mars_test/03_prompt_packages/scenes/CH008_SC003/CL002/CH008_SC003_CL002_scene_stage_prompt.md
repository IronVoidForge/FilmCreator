# Title
CH008_SC003 CL002 Scene Stage Prompt

# ID
CH008_SC003_CL002_scene_stage_prompt

# Purpose
Define visual staging intent for boarding action sequence focusing on aftermath context and warrior coordination during approach to damaged vessel. Establish vertical axis from building roofs to plain surface while maintaining continuity with previous wide establishment shots of drifting craft position. Focus on movement dynamics and tactical formation without premature reveal of prisoner interior state.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green warriors in tactical formation moving from elevated building roofs down to plain surface, approaching long low gray painted air craft with strange banners, daylight atmosphere with smoke from fire, medium shot composition emphasizing movement and coordination, bodies strewn about indicating aftermath, no sign of life inside craft yet, vertical drop from roof to ground visible, damaged vessel drifting southeast.

# Negative Prompt
human female prisoner visible before haul operation, green skin warriors static or not moving, night lighting conditions, excessive background detail obscuring craft position, signs of life inside craft interior, wrong species features on warriors, destroyed craft instead of damaged drifting vessel, John Carter observing from window, air fleet crew members present.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC003_BT001.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_in_tactical_formation, drifting_craft_interior_visible
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: close_ups_on_boarding_action
- starting_keyframe_strategy: focus_on_warriors_coordination_during_approach_with_craft_in_background
- dependency_policy: dependent_on_previous_wide_establishment_of_drifting_craft_position
- auto_advance_policy: 
- fallback_strategy: insert_close_up_if_tracking_shows_too_much_environmental_context
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage.
- Maintain aftermath visual state with bodies strewn about and no sign of life inside craft.
- Ensure vertical axis from building roofs to plain is consistent with previous wide shots.
- Warriors must maintain tactical formation during approach without breaking cohesion.
- Lighting must reflect daylight conditions with smoke cues from battle fire.
- Craft damage must match battle aftermath context without appearing fully destroyed.

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- Verify anatomy repair for warrior hands and arms during movement to prevent distortion.
- Ensure craft interior visibility does not reveal prisoner before haul operation beat.
- Check consistency of smoke density against daylight lighting conditions.
- Confirm vertical drop from roof to ground is visually clear in composition.
- Adjust environmental context if tracking shots show too much background detail.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
