# Title
CH008_SC002 CL001 Scene Stage Prompt

# ID
CH008_SC002_CL001_scene_stage_prompt

# Purpose
Establish narrator's vantage point and scale of approaching threat through window perspective.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Window frame foreground obstruction, valley floor background, twenty gray airships entering from distance, daylight lighting, deserted city environment.

# Negative Prompt
crew visible on ship hull, significant damage to ships before intended beat, proper nouns, model render artifacts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5.0
- required_refs: Window frame, twenty gray airships, valley floor
- optional_refs: Martians
- visible_character_assets: Narrator
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV/Wide
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ship count must remain twenty until damage sequence.
- No crew visible on ship hull during this beat.
- Daylight lighting consistent with valley setting.

# Repair Notes
- Ensure no significant damage to ships before intended beat.
- Verify window frame obstruction remains intact in foreground.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
