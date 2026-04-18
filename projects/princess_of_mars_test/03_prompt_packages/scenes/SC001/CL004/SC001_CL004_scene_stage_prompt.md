# Title
SC001 CL004 Scene Stage Prompt

# ID
SC001_CL004_scene_stage_prompt

# Purpose
Define staging intent and subject placement for Scene SC001 Clip CL004, focusing on the human male narrator observing the approaching fleet from the upper floor window while maintaining visual continuity with previous beats regarding lighting and composition.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Upper floor window frame visible in foreground. Human male narrator standing at sill observing distant horizon. Gray airships fleet approaching plaza level below. Midday sunlight reflecting off ship devices. Rooftops and hills visible in background valley. Atmosphere tense and action-oriented. Camera positioned outside looking through window OR inside with shallow depth of field.

# Negative Prompt
Interior building corridor space, female character entering from doorway, distant warrior figures close up, floating characters, incorrect lighting, motion blur on static elements, crowded plaza visible through windows without ships, exterior landscape only without narrator.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: beat BT004.md, scene summary, chapter summary daylight conditions
- optional_refs: medium shot narrator plus fleet in frame, POV from narrator looking at approaching ships
- visible_character_assets: human male narrator, distant warrior figures, airship crews
- look_continuity_policy: Match interior daylight from previous clips
- intended_lighting_change: Consistent with BT003 window view beat
- composition_type: medium two-shot
- continuity_mode: midday light established
- starting_keyframe_strategy: Interior space empty then introduce presence
- dependency_policy: Dependent on CL003 for emotional progression
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: authoring.scene_stage
- beat_index: BT004
- environment_context: upper floor window, rooftops, plaza street level
- lighting_condition: midday sunlight reflecting off ship devices
- camera_position: outside looking through window OR inside with shallow depth of field

# Continuity Notes
- Match lighting from previous beats to ensure interior consistency with midday transition.
- Maintain narrator position established in previous clips without sudden movement.
- Ensure fleet approaches from consistent angle toward plaza level as per visual continuity notes.
- Keep window wiper position unchanged for continuity throughout the beat.
- Preserve the abandoned atmosphere until fleet presence is fully visible at street level.

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
