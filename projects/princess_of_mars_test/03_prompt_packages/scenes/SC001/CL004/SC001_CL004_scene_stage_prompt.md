# Title
SC001 CL004 Scene Stage Prompt

# ID
SC001_CL004_scene_stage_prompt

# Purpose
Define staging intent and subject placement for Scene SC001 Clip CL004, focusing on the entrance of Sola within the building interior context while maintaining continuity with previous beats.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Interior building corridor space. Narrator standing in foreground reacting. Hound positioned nearby. Female character enters from background doorway. Lighting consistent with upper floor window view. Atmosphere tense and quiet before entrance spike.

# Negative Prompt
Exterior landscape, wide establishing shot, green martians close up, floating characters, incorrect lighting, motion blur on static elements, crowded plaza visible through windows

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: Narrator, Woola, Sola
- look_continuity_policy: Match interior daylight from previous clips
- intended_lighting_change: Consistent with BT003 window view beat
- composition_type: Medium shot capturing entrance
- continuity_mode: cutaway
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

# Continuity Notes
- Match lighting from BT003 window view beat to ensure interior consistency.
- Maintain narrator position established in previous clips without sudden movement.
- Ensure Sola enters from corridor depth not exterior plaza or open valley.
- Keep Woola positioned close to heel but not blocking the entrance path.
- Preserve the abandoned atmosphere until Sola's presence is fully visible.

# Repair Notes
- If lighting is too dark, brighten to match interior daylight from previous beats.
- If Sola appears distorted during entrance, stabilize pose and remove motion blur artifacts.
- Correct any floating elements by grounding characters to the floor plane.
- Ensure no Green Martian warriors appear in immediate foreground or doorway.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
