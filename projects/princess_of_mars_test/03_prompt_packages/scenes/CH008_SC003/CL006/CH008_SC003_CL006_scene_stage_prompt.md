# Title
CH008_SC003 CL006 Scene Stage Prompt

# ID
CH008_SC003_CL006_scene_stage_prompt

# Purpose
Establish aftermath and emotional shift from curiosity to discovery. Medium shots showing Green Warriors gathering around the stationary prisoner on the plain with a building south of position visible in background. Focus on tactical positioning and environmental context of battle aftermath including smoke and daylight.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green warriors gathering around prisoner on plain, building south of position visible in background, daylight smoke from fire aftermath, medium shot composition, human female prisoner stationary discovered state, green skin ornaments spears, light reddish copper skin coal black hair, open ground plaza valley hills beyond.

# Negative Prompt
Close-up shots, Air Fleet crew members, living bodies strewn about, wrong background geography, bright sunlight without smoke, close facial expressions only, wide angle tracking shot, unmanned air craft visible.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL006
- duration_seconds: 5
- required_refs: CH008_SC003_BT003.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_gathering_around_prisoner, prisoner_stationary_discovered_state, building_south_of_position_in_background
- look_continuity_policy: match_previous_lighting_and_smoke_density
- intended_lighting_change: maintain_daylight_with_fire_afterglow
- composition_type: medium_shot
- continuity_mode: medium_shows_prisoner_discovery
- starting_keyframe_strategy: focus_on_warriors_gathering_around_prisoner_with_building_south_of_position_in_background
- dependency_policy: dependent_on_previous_tracking_shot_following_haul_operation_completion
- auto_advance_policy: wait_for_emotional_shift_confirmation
- fallback_strategy: insert_close_up_if_medium_shots_fails_to_show_emotional_shift
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Green Warriors must remain in tactical formation while gathering around prisoner.
- Prisoner remains stationary in discovered state without movement during this clip.
- Background building south of position must be consistent with previous shots showing haul operation.
- Smoke density from fire should match aftermath beat documentation.
- No new bodies strewn about should appear beyond continuity element established in BT001.

# Repair Notes
- If emotional shift from curiosity to concern is not visible, adjust warrior positioning to show more concern.
- If background building is incorrect, correct to south of position reference point.
- If prisoner appears moving, freeze animation or adjust prompt to stationary discovered state.
- If lighting lacks fire aftermath glow, add smoke and ember particles to scene.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
