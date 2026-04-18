# Title
SC001 CL001 Keyframe Prompt

# ID
SC001_CL001_keyframe_prompt

# Purpose
Establish frozen keyframe for opening observation beat, showing observer at window and distant fleet over hills

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Observer figure standing at upper floor window frame, hands resting on polished stone sill, observing distant horizon with neutral expression, daylight illumination reflecting off dark wood window frame with metal accents, twenty gray airships visible in formation across valley sky, hill crests creating depth reference points, interior warm lighting contrasting exterior cool tones

# Negative Prompt
blurry, distorted faces, extra limbs, missing hands, text, watermark, low resolution, dark shadows, night time, crowded streets, modern clothing, fire, smoke, collapsing buildings, indoor artificial light, close-up of prisoner, green-skinned warriors in foreground, specific names

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 breakdown
- optional_refs: Procession garment details, plaza distance markers
- visible_character_assets: observer figure, distant fleet figures
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium profile at window looking out
- continuity_mode: window frame consistent
- starting_keyframe_strategy: establish vertical axis with observer elevated above city
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
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain exterior daylight lighting consistency with valley view
- Ensure observer remains stationary at window frame during keyframe
- Keep distant plaza warriors visible but not obstructing foreground action
- Verify hound follows close behind without blocking observer path if present
- Preserve deserted city street environment state throughout keyframe
- Ship count (20) must be maintained in wide shots
- Window framing and interior elements must stay consistent

# Repair Notes
- Apply anatomy repair policy for hands and feet during walking motion
- Ensure style profile consistency with ceremonial garment textures
- Correct any facial distortion on observer or distant warriors
- Verify no modern clothing elements appear in environment assets
- Fix lighting contrast between interior warm and exterior cool tones

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
