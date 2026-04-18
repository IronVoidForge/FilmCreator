# Title
SC001 CL001 Scene Stage Prompt

# ID
SC001_CL001_scene_stage_prompt

# Purpose
Define the stage intent for Clip CL001 within Scene SC001, establishing the opening visual context of threat observation from an elevated position and transitioning from exterior wide to medium tracking.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Over-the-shoulder view of Narrator standing at upper floor window frame looking outward. Distant gray-painted airships visible in sky approaching valley/hills vista. Green Martian warriors positioned on balcony ledge below narrator observing fleet. Deserted city buildings surrounding observation point. Clear natural daylight illuminating stone structures and sky.

# Negative Prompt
Crowds blocking path, vehicles obstructing street, sudden appearance of female character, interior lighting mismatch, chaotic movement, close-up facial expressions, dark shadows obscuring foreground, floating debris, unnatural color grading, wrong number of ships visible, airships appearing too close or too far

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 overview
- optional_refs: 
- visible_character_assets: Narrator (stationary at window frame), Green Martian Warriors (positioned on balcony below)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Over-the-shoulder at narrator looking out
- continuity_mode: Long shot of fleet in distance
- starting_keyframe_strategy: Establish vertical axis with narrator elevated above city
- dependency_policy: None - standalone observation clip
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
- Maintain Narrator's stationary position at window frame.
- Ensure gray airships are distant and not overlapping foreground characters.
- Keep Green Martian Warriors below Narrator on balcony, not blocking view of fleet.
- Preserve vertical axis (Narrator elevated above city).
- Verify natural daylight consistency across stone structures and sky.

# Repair Notes
- Adjust lighting if interior window frame becomes too dark compared to exterior view.
- Ensure Narrator does not move or stop abruptly during observation sequence.
- Verify distant warriors do not overlap foreground characters incorrectly.
- Check aspect ratio remains consistent for long shot of fleet.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
