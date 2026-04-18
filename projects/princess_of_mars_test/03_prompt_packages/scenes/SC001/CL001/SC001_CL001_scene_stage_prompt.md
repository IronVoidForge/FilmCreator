# Title
SC001 CL001 Scene Stage Prompt

# ID
SC001_CL001_scene_stage_prompt

# Purpose
Define the stage intent for Clip CL001 within Scene SC001, establishing the opening visual context of the deserted city retreat and transitioning from exterior wide to medium tracking.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide establishing view of deserted city streets with ceremonial procession retreating through empty space. Narrator walking forward in center frame, hound following close behind at heel. Distant plaza visible with green warriors in background. Upper floor windows and building roofs framing the scene. Natural daylight gleaming on stone structures. Transition from exterior wide to medium tracking as narrator enters building interior.

# Negative Prompt
Crowds blocking path, vehicles obstructing street, sudden appearance of female character, interior lighting mismatch, chaotic movement, close-up facial expressions, dark shadows obscuring foreground, floating debris, unnatural color grading

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 breakdown
- optional_refs: 
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide establishing → Medium tracking
- continuity_mode: cut
- starting_keyframe_strategy: 
- dependency_policy: 
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain narrator's forward momentum through deserted streets.
- Ensure lighting consistency between exterior wide and interior tracking shots.
- Keep hound positioned close behind narrator without blocking view.
- Preserve distant plaza atmosphere with green warriors visible but not interfering.
- Transition smoothly from exterior context to building entrance depth.

# Repair Notes
- Adjust lighting if interior becomes too dark compared to exterior view.
- Ensure narrator does not stop abruptly during tracking sequence.
- Verify distant warriors do not overlap foreground characters incorrectly.
- Check aspect ratio remains consistent for wide establishing shot.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
