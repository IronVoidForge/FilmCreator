# Title
CH008_SC002 CL001 Fix 01 Prompt

# ID
CH008_SC002_CL001_fix_01_prompt

# Purpose
Fill in the stage intent here.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green-skinned warriors positioned in elevated building window openings, weapons loaded and ready for volley fire, battle zone visible below valley floor, Martian architecture with open valleys and distant hills, smoke rising from impact points on enemy fleet below, static elevated perspective looking down at conflict area, green skin tone consistent, weapons clearly visible and loaded, minimal camera movement, atmospheric lighting appropriate for urban battle setting

# Negative Prompt
blurry details, distorted anatomy, inconsistent skin tones, floating elements, extra limbs, malformed weapons, incorrect perspective, overexposed highlights, underexposed shadows, motion artifacts, watermark text, signature marks, poor composition, wrong color palette, missing background elements, inconsistent lighting direction, warped geometry, low resolution, pixelated edges

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Scene breakdown for building window positioning
- visible_character_assets: Green Warriors (static elevated positions), Weapons (loaded)
- look_continuity_policy: Maintain green skin tone consistency and weapon loading state
- intended_lighting_change: None
- composition_type: Wide shot from building window looking down at valley floor
- continuity_mode: Static elevated perspective with minimal camera movement
- starting_keyframe_strategy: Open on warriors positioned in windows, weapons visible and loaded
- dependency_policy: No hard dependencies; can stand alone as opening beat
- auto_advance_policy: None
- fallback_strategy: Use reframe_same_moment if timing adjustment needed
- consistency_assist_policy: Maintain bullet drop at explosion points consistency
- consistency_assist_method: Progressive damage tracking on banners and impact points
- anatomy_repair_policy: Preserve green skin warrior anatomy clarity
- consistency_targets: Window height, eyeline angle, target area alignment
- style_profile: Urban Martian architecture with elevated battle perspective
- batch_role: Opening conflict establishment shot
- fix_of: CH008_SC002_CL001_fix_01_prompt

# Continuity Notes
- Capture the opening conflict with clear window positioning and firing sequence, maintain static elevated perspective throughout 5-second duration, ensure green skin warriors remain in consistent positions, track smoke progression from impact points below valley floor, preserve weapon loading state across frames, keep minimal camera movement for static shot composition

# Repair Notes
- Fix any distorted weapon geometry or inconsistent skin tones on green-skinned warriors, correct perspective issues where weapons appear floating or malformed, ensure smoke effects progress naturally from impact points without appearing as artifacts, maintain consistent lighting direction across all frames, verify window opening positions remain stable throughout shot duration, address any anatomy distortion on warrior figures positioned in elevated windows

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
