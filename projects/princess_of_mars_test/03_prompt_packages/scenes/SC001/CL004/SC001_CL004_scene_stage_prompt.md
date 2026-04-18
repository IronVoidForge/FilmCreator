# Title
SC001 CL004 Scene Stage Prompt

# ID
SC001_CL004_scene_stage_prompt

# Purpose
Define staging intent and subject placement for Scene SC001 Clip CL004, focusing on close-up banner designs on ship prows while maintaining visual continuity with previous beats regarding lighting and composition. The narrator's eyeline shift from wide formation to detail focus is central to the beat.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Upper floor window frame visible in foreground or implied through perspective. Human male narrator standing at sill observing distant horizon, eyeline focused on specific ships. Gray airships fleet approaching plaza level below, twenty vessels over hill crests. Midday sunlight reflecting off ship devices and banners. Rooftops and hills visible in background valley. Atmosphere tense and action-oriented. Camera positioned to capture detail of banner designs while maintaining continuity with previous shots.

# Negative Prompt
Interior building corridor space, female character entering from doorway, distant warrior figures close up, floating characters, incorrect lighting, motion blur on static elements, crowded plaza visible through windows without ships, exterior landscape only without narrator context, wrong ship count, missing banner designs, dark shadows obscuring details.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: beat BT003.md, scene summary, chapter summary daylight conditions
- optional_refs: medium shot narrator plus fleet in frame, POV from narrator looking at approaching ships
- visible_character_assets: human male narrator, distant warrior figures on ships, airship crews
- look_continuity_policy: Match interior daylight from previous clips
- intended_lighting_change: Consistent with BT003 window view beat
- composition_type: close-up detail shot
- continuity_mode: midday light established
- starting_keyframe_strategy: insert_banner_detail_focus
- dependency_policy: dependent_on_fleet_position_and_banner_visibility
- auto_advance_policy: 
- fallback_strategy: cutaway_to_device_shape_detail
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: authoring.scene_stage
- beat_index: BT003
- environment_context: upper floor window, rooftops, plaza street level
- lighting_condition: midday sunlight reflecting off ship devices
- camera_position: outside looking through window OR inside with shallow depth of field

# Continuity Notes
- Match lighting from previous beats to ensure interior consistency with midday transition.
- Maintain narrator position established in previous clips without sudden movement.
- Ensure fleet approaches from consistent angle toward plaza level as per visual continuity notes.
- Keep window wiper position unchanged for continuity throughout the beat.
- Preserve the abandoned atmosphere until fleet presence is fully visible at street level.
- Focus on banner designs and device shapes for continuity markers across shots.

# Repair Notes
- If lighting is too dark, brighten to match interior daylight from previous beats.
- If narrator appears distorted during observation, stabilize pose and remove motion blur artifacts.
- Correct any floating elements by grounding characters to the floor plane.
- Ensure no distant warrior figures appear in immediate foreground or doorway.
- Verify ship props match visual continuity notes from chapter summary daylight conditions.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
