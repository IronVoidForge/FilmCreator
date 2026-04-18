# Title
SC001 CL003 Keyframe Prompt

# ID
SC001_CL003_keyframe_prompt

# Purpose
Establish window view moment and emotional weight of abandonment through exterior landscape

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
A frozen still of a figure standing at an upper floor window frame looking out at an empty valley and distant hills under bright sunlight. The interior room shows wooden furniture and stone walls with dim lighting contrasting the exterior glow. Outside, the landscape is barren with no ships or vehicles visible. Natural light gleams on devices inside while the view remains clear and open.

# Negative Prompt
crowded streets, moving camera, dark shadows, night time, vehicles in valley, other characters blocking view, blurry details, female companion present, narrator name visible, proper names, text overlays

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md, Scene SC001 breakdown
- optional_refs: Valley/hills landscape details, natural light contrast
- visible_character_assets: Narrator (at window), Woola (nearby but not blocking view)
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
- Maintain spatial positioning relative to previous clip
- Ensure lighting consistency between interior and exterior views
- Keep Woola nearby but not obstructing the window view

# Repair Notes
- Fix any facial expression inconsistencies
- Ensure window frame is clearly defined
- Correct lighting contrast if too flat

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
