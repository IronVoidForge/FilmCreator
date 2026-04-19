# Title
CH008_SC002 CL009 Fix 01 Prompt

# ID
CH008_SC002_CL009_fix_01_prompt

# Purpose
Generate corrected still for CL009 close-up on ship rotation mechanism within BT003 sequence. Maintain continuity with approved base frame while ensuring mechanical clarity and environmental consistency regarding smoke density and debris field.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Close-up of damaged gray air craft hull rotation mechanism, crew hands adjusting alignment vector, smoke density increasing, debris scattered, Martian city buildings upper floors windows background, daylight with fire glow illumination, ship banners fluttering, missile impact flames visible, low angle view, cinematic lighting, high detail, mechanical precision.

# Negative Prompt
distorted mechanics, missing crew members, earth green skin, low resolution, excessive motion blur, glitched hands, wrong color palette, blurry background, artifacts, watermark, text, overexposed fire, underexposed hull.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL009
- duration_seconds: 5
- required_refs: BT003 index, CL008 medium shot
- optional_refs: hull damage visible, smoke density increasing
- visible_character_assets: Ship rotation mechanism, crew hands
- look_continuity_policy: preserve established Martian city palette and lighting
- intended_lighting_change: maintain daylight with fire glow consistency
- composition_type: close-up
- continuity_mode: cutaway
- starting_keyframe_strategy: static on rotation mechanism
- dependency_policy: sequential to crew realignment medium shot
- auto_advance_policy: 
- fallback_strategy: insert debris scattered if rotation heavy
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: cinematic action, high contrast smoke
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain alignment vector across valley width consistent with previous shots.
- Preserve smoke trails visible from impact points in background.
- Ensure ship color matches established gray-painted vessel palette.
- Keep debris field consistent with BT003 beat progression.
- Match crew hand positioning to realignment medium shot reference.

# Repair Notes
- Fix any mechanical distortion in the rotation mechanism visible on hull.
- Ensure crew hands are visible and not glitched or missing fingers.
- Correct lighting consistency with fire glow from missile impacts.
- Remove unwanted artifacts around the ship banners.
- Adjust smoke density to match increasing trajectory from previous frames.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL009.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
