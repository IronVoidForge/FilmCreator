# Title
CH008_SC002 CL001 Keyframe Prompt

# ID
CH008_SC002_CL001_keyframe_prompt

# Purpose
Establish opening conflict with clear window positioning and firing sequence for static elevated perspective shot.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Green-skinned warriors positioned in elevated building windows, weapons loaded and ready, downward line of sight to valley floor, gray low-profile vessels visible below, urban Martian architecture, open sky, smoke beginning to rise from impact points, static elevated perspective, wide shot composition.

# Negative Prompt
blurry, distorted anatomy, modern technology, close-up facial features, moving camera, bright sunlight, indoor lighting only, wrong color palette, text, logos, watermarks, human faces, green skin on humans, mechanical limbs.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Scene breakdown for building window positioning
- visible_character_assets: Green Warriors (static elevated positions), Weapons (loaded)
- look_continuity_policy: Static hold for 5 seconds, minimal movement focus on firing mechanics
- intended_lighting_change: None
- composition_type: Wide shot from building window looking down at valley floor
- continuity_mode: Static elevated perspective with minimal camera movement
- starting_keyframe_strategy: Open on warriors positioned in windows, weapons visible and loaded
- dependency_policy: No hard dependencies; can stand alone as opening beat
- auto_advance_policy: None
- fallback_strategy: Use reframe_same_moment if timing adjustment needed
- consistency_assist_policy: Bullet drops at explosion points (timing and placement consistency)
- consistency_assist_method: Progressive damage tracking
- anatomy_repair_policy: Green skin on warriors, no human faces
- consistency_targets: Window height, Eyeline angle, Target area
- style_profile: still.scene_build.four_ref.klein.distilled
- batch_role: Initial Test Clips
- fix_of: None

# Continuity Notes
- Capture the continuity rules for this stage.
- Maintain static elevated perspective throughout the 5-second hold.
- Ensure weapons remain loaded and visible in initial state.
- Match urban Martian architecture and valley floor environment exactly.
- Track smoke progression from impact points below without camera movement.

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- Verify green skin texture on warriors matches established style profile.
- Check window positioning aligns with building interior portal geometry.
- Ensure no human facial features appear in the frame during this shot.
- Confirm weapon loading state is consistent with BT001 start state.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
