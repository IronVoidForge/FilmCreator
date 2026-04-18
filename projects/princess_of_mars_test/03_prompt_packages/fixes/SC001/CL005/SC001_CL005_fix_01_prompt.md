# Title
SC001 CL005 Fix 01 Prompt

# ID
SC001_CL005_fix_01_prompt

# Purpose
Correct local generation artifacts for CL005 Beat 003 detail insert while preserving midday daylight continuity and rising tension composition from approved still base

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
human male protagonist standing at upper floor window, dark wood frame with metal accents, polished stone tiles visible, gray painted airships hovering low over plaza street level, midday sunlight reflecting off ship devices, concern expression on face, hands near window sill, distant green-skinned warriors in fleet formation, open valley background, outlying hills

# Negative Prompt
blurry, distorted anatomy, fused fingers, wrong color palette, bright blue sky, modern clothing, text, watermark, low resolution, excessive smoke obscuring faces, floating debris, incorrect ship banners, red lighting accents, copper skin tones too pale

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: approved_still_base
- optional_refs: secondary_style_reference
- visible_character_assets: human male protagonist, green-skinned warriors
- look_continuity_policy: midday daylight consistency
- intended_lighting_change: none
- composition_type: detail insert
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_device_detail_focus
- dependency_policy: dependent_on_banner_visibility_and_device_shapes
- auto_advance_policy: standard
- fallback_strategy: cutaway_to_ship_prow_detail
- consistency_assist_policy: enabled
- consistency_assist_method: lighting_match
- anatomy_repair_policy: strict
- consistency_targets: ship count twenty, window frame position, banner designs, device shapes
- style_profile: sci-fi adventure
- batch_role: fix_01
- fix_of: CL005_Beat003_detail_insert
- workflow_type: still.scene_insert.two_ref.klein.distilled
- image_1_reference: approved_still_base
- image_2_reference: secondary_style_reference

# Continuity Notes
- Match midday lighting shift from soft morning to bright daylight
- Maintain window frame position and wiper location consistency
- Preserve fleet formation angle approaching plaza at fifteen degree tilt
- Keep human male protagonist distance from window sill constant
- Ensure stone vessel props match visual continuity notes

# Repair Notes
- Fix any local artifacts like floating debris or incorrect ship banners
- Ensure narrator expression matches tension level of approach
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
