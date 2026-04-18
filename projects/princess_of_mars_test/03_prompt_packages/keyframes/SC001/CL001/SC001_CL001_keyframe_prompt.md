# Title
SC001 CL001 Keyframe Prompt

# ID
SC001_CL001_keyframe_prompt

# Purpose
Establish frozen keyframe for opening observation beat, showing distant fleet descending from hills and valley floor

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Twenty gray airships visible in formation descending from hills, banners fully unfurled on hulls, valley floor empty below establishing scale, daylight illumination reflecting off dark painted vessels, hill crests creating depth reference points, distant green Martians occupying upper windows of deserted buildings firing volleys, wide establishing composition

# Negative Prompt
blurry, distorted faces, extra limbs, missing hands, text, watermark, low resolution, dark shadows, night time, crowded streets, modern clothing, fire, smoke, collapsing buildings, indoor artificial light, close-up of prisoner, specific names, observer figure at window foreground

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 breakdown
- optional_refs: Valley floor geography map
- visible_character_assets: Fleet crew inside ships (silhouettes), Green Martians in distant windows
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide establishing
- continuity_mode: valley level consistent
- starting_keyframe_strategy: establish vertical axis with fleet descending from hills
- dependency_policy: Standalone
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
- Ensure ship count (20) is maintained in wide shots
- Keep distant plaza warriors visible but not obstructing foreground action
- Verify banners are fully unfurled on each hull
- Preserve deserted city buildings state throughout keyframe
- Hill crests must create depth reference points

# Repair Notes
- Apply anatomy repair policy for fleet crew silhouettes if visible
- Ensure style profile consistency with Martian architectural textures
- Correct any facial distortion on distant green Martians in windows
- Verify no modern clothing elements appear in environment assets
- Fix lighting contrast between daylight exterior and interior window frames

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
