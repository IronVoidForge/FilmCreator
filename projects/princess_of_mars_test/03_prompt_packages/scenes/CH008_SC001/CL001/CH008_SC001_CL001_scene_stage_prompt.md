# Title
CH008_SC001 CL001 Scene Stage Prompt

# ID
CH008_SC001_CL001_scene_stage_prompt

# Purpose
Establish John Carter's observation position from upper floor window with city perimeter visible in background, showing approaching ground forces and horizon anchor line. Frame composition as wide exterior angle to capture procession approach while maintaining valley/hills continuity reference. Ground viewer in location through partial window frame edge visible on left side, showing initial curiosity expression without shifting to close-up face that contradicts wide exterior staging intent.

# Workflow Type
authoring.scene_stage

# Positive Prompt
wide exterior shot, John Carter upper torso standing at window frame edge left side, looking downward toward approaching ground forces and horizon line, initial curiosity visible on facial expression, daylight conditions, city building interior background with partial view of valley hills beyond stable reference, Barsoom cinematic style, observer perspective from upper floor, wide angle showing city boundary as visual anchor, horizon line marked for eyeline reference, procession figures entering frame from distance, no close-up face composition, window frame edge visible maintaining location context

# Negative Prompt
close-up face shot, medium shots, static composition, single character focus without window context, dark lighting, night scene, indoor scenes without exterior view, blurry movement, distorted anatomy, missing limbs, extra fingers, bad hands, text overlays, watermark, signature, low resolution, poor quality, deformed faces, morphed features, inconsistent colors, wrong era clothing, modern technology, disabled ships, burning vessels, captive figure, copper skin character, air fleet combat sequences, Carter in central leading position, valley background unstable or missing

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: John Carter (upper torso, face), window frame partial left edge
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: none
- composition_type: wide_exterior_with_window_frame_edge
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: horizon_anchor_with_city_perimeter_line
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: static_wide_if_tracking_fails
- consistency_assist_policy: enabled
- consistency_assist_method: frame_matching
- anatomy_repair_policy: standard
- consistency_targets: character_placement, movement_axis, environmental_context
- style_profile: Barsoom cinematic
- batch_role: establishing_sequence
- fix_of: none

# Continuity Notes
- Establish Carter's perspective from upper floor window with window frame edge visible on left side to ground viewer in location
- Show initial curiosity on face as he observes arrival of approaching ground forces and horizon anchor line
- Maintain valley/hills background stability for continuity across shots
- Ensure daylight conditions remain consistent showing clear visibility of procession figures entering frame
- Keep Carter's position at window frame without shifting to central or leading position
- Avoid close-up face compositions that contradict wide exterior staging intent from BT001 beat bundle
- Verify no disabled ships, burning vessels, or captive figures appear in this initial observation sequence

# Repair Notes
- If Carter's expression appears static, add subtle shifts reflecting growing concern/anticipation as more procession figures appear
- Ensure window frame edge remains visible on left side to maintain location context and prevent composition drift
- Check that valley/hills background is stable and consistent with previous shots for continuity tracking
- If procession figures are unclear or not entering frame properly, adjust exposure to maintain clear visibility of approaching elements
- Verify no modern technology or wrong era clothing appears in scene
- If lighting appears inconsistent with daylight conditions, adjust exposure to maintain clear visibility of horizon anchor line

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
