# Title
SC001 CL005 Fix 01 Prompt

# ID
SC001_CL005_fix_01_prompt

# Purpose
Correct local generation artifacts while preserving the established visual style of the Martian city retreat scene

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
A deserted city street with upper floors and windows, gray painted airships hovering low over hills, green warriors in spears and chariots, narrator figure observing from a window or roof, copper skin tones, black hair, crimson lighting accents, sunlight gleaming on devices, stone vessels, silks, furs, jewels, open valleys, outlying hills

# Negative Prompt
blurry, distorted anatomy, fused fingers, wrong color palette, bright blue sky, modern clothing, text, watermark, low resolution, excessive smoke obscuring faces, floating debris, incorrect ship banners

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: 
- continuity_mode: 
- starting_keyframe_strategy: 
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
- workflow_type: still.scene_insert.two_ref.klein.distilled
- image_1_reference: approved_still_base
- image_2_reference: secondary_style_reference

# Continuity Notes
- Match lighting consistency from previous clips (sunlight vs fire)
- Maintain character appearance consistency (narrator position, green warrior armor style)
- Preserve city architecture details and color palette
- Ensure hound positioning follows close at heel if present
- Keep emotional tone of high-stakes military engagement

# Repair Notes
- Fix any local artifacts like floating debris or incorrect ship banners
- Ensure narrator expression matches tension level of retreat
- Verify copper skin tones are not too red or too pale
- Check that gray airships maintain low altitude and painted finish
- Correct any anatomy distortions in warrior gear or hands

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
