# Title
CH008_SC001 CL001 Scene Stage Prompt

# ID
CH008_SC001_CL001_scene_stage_prompt

# Purpose
Establish John Carter's perspective from an upper floor window as he observes the arrival of twenty large gray air craft descending toward the city. Capture his initial curiosity and growing anticipation regarding the procession retreat to a city building due to immediate orders. Frame the shot with the window edge visible to ground the viewer in location, showing the valley/hills background for continuity.

# Workflow Type
authoring.scene_stage

# Positive Prompt
close-up face, John Carter upper torso, standing at window frame edge, looking downward toward valley, initial curiosity visible on expression, daylight conditions, city building interior background, partial view of air craft descending outside window, window frame left edge, valley hills beyond stable background, Barsoom cinematic style, observer perspective

# Negative Prompt
wide establishing shot, medium shots, static composition, single character focus without window context, dark lighting, night scene, indoor scenes without window view, blurry movement, distorted anatomy, missing limbs, extra fingers, bad hands, text overlays, watermark, signature, low resolution, poor quality, deformed faces, morphed features, inconsistent colors, wrong era clothing, modern technology, disabled ships, burning vessels, captive figure, copper skin character, air fleet combat sequences

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: John Carter (upper torso, face), window frame partial
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: none
- composition_type: close_up_face_with_window_frame_edge
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: insert
- consistency_assist_policy: enabled
- consistency_assist_method: frame_matching
- anatomy_repair_policy: standard
- consistency_targets: character_placement, movement_axis, environmental_context
- style_profile: Barsoom cinematic
- batch_role: establishing_sequence
- fix_of: none

# Continuity Notes
- Establish Carter's perspective from upper floor window with window frame edge visible to ground viewer in location
- Show initial curiosity on face as he observes arrival of twenty large gray air craft descending toward city
- Maintain valley/hills background stability for continuity across shots
- Ensure daylight conditions remain consistent showing clear visibility of air craft details
- Keep Carter's position at window frame without shifting to central or leading position
- Avoid wide establishing shots or medium shots that contradict close-up face composition intent
- Verify no disabled ships, burning vessels, or captive figures appear in this initial observation sequence

# Repair Notes
- If Carter's expression appears static, add subtle shifts reflecting growing concern/anticipation as more craft appear
- Ensure window frame edge remains visible on left side to maintain location context
- Check that valley/hills background is stable and consistent with previous shots for continuity
- If air craft details are unclear, adjust exposure to maintain clear visibility of descending vessels
- Verify no modern technology or wrong era clothing appears in scene
- If lighting appears inconsistent with daylight conditions, adjust exposure to maintain clear visibility of air craft details

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
