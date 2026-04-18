# Title
SC001 CL003 Scene Stage Prompt

# ID
SC001_CL003_scene_stage_prompt

# Purpose
Establish staging intent for scene SC001 clip CL003, focusing on narrator's window view and emotional transition from interior to exterior observation.

# Workflow Type
authoring.scene_stage

# Positive Prompt
narrator character approaching upper floor window frame, interior room visible behind, POV looking out at empty alien valley and hills, natural sunlight gleaming on exterior landscape, copper-skinned figure with anxious expression, hound nearby but not blocking view, vertical axis from interior floor to exterior view, emotional weight of abandonment conveyed

# Negative Prompt
blurry window frame, extra characters blocking view, wrong lighting direction, crowded valley, text overlays, distorted anatomy, static camera without movement intent, bright interior shadows mismatching exterior light

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md, Scene SC001 breakdown
- optional_refs: Valley/hills landscape details, natural light contrast
- visible_character_assets: Narrator, Hound
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV window view → Close-up on narrator's anxious expression
- continuity_mode: insert
- starting_keyframe_strategy: Approach window position, establish exterior view first
- dependency_policy: Dependent on CL002 for spatial positioning
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
- Maintain narrator's movement path from corridor to window without skipping steps.
- Ensure lighting contrast between interior room and exterior valley remains consistent.
- Keep hound positioned nearby but not obstructing the window view line of sight.
- Preserve emotional tone of abandonment in facial expression during exterior gaze.

# Repair Notes
- Fix any mismatched shadows on narrator's face caused by interior vs exterior light sources.
- Remove accidental characters or objects blocking the window frame visibility.
- Correct distorted anatomy if copper skin texture appears unnatural under sunlight.
- Adjust camera movement to ensure smooth transition from interior approach to POV shot.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
