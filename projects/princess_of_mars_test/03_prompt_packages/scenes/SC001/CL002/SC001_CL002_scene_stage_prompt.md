# Title
SC001 CL002 Scene Stage Prompt

# ID
SC001_CL002_scene_stage_prompt

# Purpose
Define the staging intent for the interior corridor transition, establishing subject placement within the building depth and environmental context for the opening frame setup.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium tracking shot through dim interior corridor, narrator moving forward into depth, hound following close behind, stone walls visible, portal depth in background, lighting consistent with exterior view but darker, tense atmosphere, transition from entrance to corridor space

# Negative Prompt
exterior valley view, bright sunlight, crowd of martians, Sola present, static camera, wide establishing shot, cartoon style, floating funeral pyre

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium tracking through corridors
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: begin at building entrance
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
- workflow_type: authoring.scene_stage

# Continuity Notes
- Maintain spatial continuity from previous clip
- Narrator position must align with corridor axis
- Lighting must reflect interior depth shift
- Woola remains trailing narrator throughout movement

# Repair Notes
- Fix anatomy if limbs distort during movement
- Ensure background portal remains consistent
- Correct lighting balance between entrance and corridor

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
