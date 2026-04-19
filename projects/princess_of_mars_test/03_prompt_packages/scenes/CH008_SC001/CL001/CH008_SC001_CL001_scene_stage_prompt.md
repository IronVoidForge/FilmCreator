# Title
CH008_SC001 CL001 Scene Stage Prompt

# ID
CH008_SC001_CL001_scene_stage_prompt

# Purpose
Establish medium shot of narrator standing at interior window observing cityscape and sky, setting up arrival of enemy airships. Capture calm observation state transitioning to alert posture as visual threat approaches from valley horizon.

# Workflow Type
authoring.scene_stage

# Positive Prompt
medium shot interior, human male narrator standing at window frame, looking out at valley and cityscape below, calm observation posture, subtle body shift to alert, Martian architecture visible through window, daylight lighting, distant hills in background, gray airships entering horizon (distant), clear line of sight from window, interior room details visible

# Negative Prompt
close up shots, static composition, dark lighting, night scene, indoor scenes without window view, blurry movement, distorted anatomy, missing limbs, extra fingers, bad hands, text overlays, watermark, signature, low resolution, poor quality, deformed faces, morphed features, inconsistent colors, wrong era clothing, modern technology, airships visible in frame (too close), disabled ships, burning vessels, captive figure, copper skin character

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: narrator_standing_at_window, interior_window_frame, cityscape_below_view
- look_continuity_policy: reframe_same_moment
- intended_lighting_change: none
- composition_type: medium_shot_interior
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_subtle_body_shift
- dependency_policy: standalone_initial_test_clip
- auto_advance_policy: none
- fallback_strategy: cut_to_wider_room_establishing_if_necessary
- consistency_assist_policy: enabled
- consistency_assist_method: frame_matching
- anatomy_repair_policy: standard
- consistency_targets: character_placement, movement_axis, environmental_context
- style_profile: Barsoom cinematic
- batch_role: observation_setup
- fix_of: none

# Continuity Notes
- Narrator positioned at interior window with clear line of sight to valley
- Martians occupy lower room space before dissolving
- Airships enter frame from horizon moving toward camera/valley center
- Three-minute dissolve timing for martians is critical beat marker
- Eyeline directed horizontally across cityscape then upward to sky
- No cutaways or insert shots within this medium establishing composition

# Repair Notes
- If narrator movement appears static, add subtle forward progression or body shift to maintain continuity with BT001 beat documentation
- Ensure environmental transition from built environment to natural terrain begins at frame boundary as specified in scene breakdown
- Check that no airships or disabled vessels appear in frame during this establishing sequence (they enter later)
- Verify narrator green attire and formation marching style matches Barsoom cinematic style profile (if visible)
- If lighting appears inconsistent with daylight conditions, adjust exposure to maintain clear visibility of city details

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
