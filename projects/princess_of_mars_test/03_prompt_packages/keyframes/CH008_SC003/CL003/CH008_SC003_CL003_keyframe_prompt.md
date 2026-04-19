# Title
CH008_SC003 CL003 Keyframe Prompt

# ID
CH008_SC003_CL003_keyframe_prompt

# Purpose
Define the visual intent for the keyframe generation of this clip, focusing on the boarding initiation detail via grappling hook deployment action.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close-up of green-skinned hands gripping and releasing a metal grappling hook, hook swinging through air towards distant gray ship hull, water surface below reflecting light, blurred Martian observers in background, daylight illumination, sharp focus on hook mechanism

# Negative Prompt
blurry, human faces, wrong skin tone, burning fire, dead bodies, close up of prisoner, night scene, indoor setting, out of focus, extra characters

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (hands), Martians (observation)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: open on hook deployment action
- dependency_policy: depends on CL002
- auto_advance_policy: 
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ensure hand anatomy matches previous clips, hook trajectory aligns with ship drift vector, background Martians maintain consistent positioning

# Repair Notes
- If hands look human instead of green-skinned, adjust. If hook is missing, add. If lighting is too dark, brighten.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
