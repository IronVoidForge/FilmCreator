# Title
SC001 CL001 Keyframe Prompt

# ID
SC001_CL001_keyframe_prompt

# Purpose
Generate frozen keyframe for opening observation beat, establishing exterior city context and threat presence before narrator movement

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
over-the-shoulder view of human observer standing at upper floor window frame, distant sky containing gray-painted airships approaching valley, green-skinned warriors positioned on balcony ledge below, clear daylight illumination, vertical axis established with elevated position, deserted city buildings visible in background, calm atmosphere before combat

# Negative Prompt
blurry, distorted faces, extra limbs, missing hands, text, watermark, low resolution, dark shadows, night time, crowded streets, modern clothing, fire, smoke, collapsing buildings, indoor artificial light, close-up of prisoner

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 breakdown
- optional_refs: Procession garment details, plaza distance markers
- visible_character_assets: human observer, green-skinned warriors
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: over-the-shoulder at narrator looking out
- continuity_mode: cut
- starting_keyframe_strategy: establish vertical axis with narrator elevated above city
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
- Maintain exterior daylight lighting consistency with valley view
- Ensure narrator remains stationary at window frame during keyframe
- Keep distant plaza warriors visible but not obstructing foreground action
- Verify hound follows close behind without blocking narrator path if present
- Preserve deserted city street environment state throughout keyframe

# Repair Notes
- Apply anatomy repair policy for hands and feet during walking motion
- Ensure style profile consistency with ceremonial garment textures
- Correct any facial distortion on narrator or distant warriors
- Verify no modern clothing elements appear in environment assets

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
