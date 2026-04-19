# Title
CH008_SC002 CL001 Cut Motion Prompt

# ID
CH008_SC002_CL001_cut_motion_prompt

# Purpose
Establish narrator's vantage point and scale of approaching threat through window POV shots. Camera maintains window POV throughout; airships move closer across valley floor.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Window frame foreground obstruction, narrator eye extreme close-up, twenty gray airships approaching across valley floor, distant hills beyond, daylight illumination, slow camera pan following ship approach path, atmospheric tension building, deserted city buildings below

# Negative Prompt
crew visible on ships, damage to hulls, fire, burning, loot items, boarding equipment, Martian warriors firing, close-up on narrator face, static camera, night lighting, smoke rising from ships

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5.0
- required_refs: window frame, twenty gray airships, valley floor
- optional_refs: deserted city buildings
- visible_character_assets: narrator (window observer)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV/Wide
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
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
- Maintain window frame obstruction in foreground throughout motion.
- Keep number of airships at twenty without variation.
- Preserve daylight lighting grade and avoid fire or smoke introduction.
- Camera movement follows ship approach path across valley floor.
- Do not show Martians firing or boarding in this beat.

# Repair Notes
- If camera drifts from window POV, re-anchor to frame obstruction.
- If ship count changes, revert to twenty ships.
- If lighting shifts to night or fire, restore daylight illumination.
- If Martians appear prematurely, remove them from frame.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
