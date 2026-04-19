# Title
CH008_SC001 CL003 Scene Stage Prompt

# ID
CH008_SC001_CL003_scene_stage_prompt

# Purpose
Establish immediate tactical response to enemy airships approaching. Capture sudden retreat order given as enemy vessels visible on horizon. Show Green Martian warriors at doorway threshold beginning to melt into interior spaces, establishing three-minute timing constraint for complete vanishing action. Maintain continuity with procession movement while transitioning from open valley floor to building entry pattern.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian warrior figures at doorway threshold, close-up on doorway frame axis, melting motion inward toward interior darkness, doorway edges visible, interior shadows swallowing figures, three-minute timing marker active, deserted city buildings in valley with hills beyond, daylight lighting, cinematic composition, tactical retreat urgency implied, group entity without individual physical descriptions, vanishing point reference, atmospheric depth, clear focus on doorway threshold action.

# Negative Prompt
blurry doorway frame, distorted anatomy, wrong skin tone, static image, missing timing marker, protagonist wearing green attire, dark lighting, crowded city buildings in foreground, calm expression, low resolution, extra limbs, incorrect eye direction, foggy atmosphere, text overlay, visible faces on Martians, individual warrior descriptions, bright interior spaces, empty doorways.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: CH008_SC001_scene_breakdown, CH008_SC001_clip_roster
- visible_character_assets: Green Martian warriors group at doorway edge, interior shadows swallowing figures
- look_continuity_policy: match_previous_procession_movement
- intended_lighting_change: maintain_daylight_deserted_city
- composition_type: close_up_doorway_threshold
- continuity_mode: insert
- starting_keyframe_strategy: doorway_frame_axis_with_martians_at_threshold_beginning_to_melt
- dependency_policy: depends_on_CL002_establishing_entry_pattern
- auto_advance_policy: standard_cut_on_vanishing_completion
- fallback_strategy: cut_to_wide_if_close_unavailable
- consistency_assist_policy: enable_character_consistency_check
- consistency_assist_method: match_doorway_threshold_placement
- anatomy_repair_policy: prioritize_group_entity_consistency
- consistency_targets: doorway_frame_axis, interior_shadows, three_minute_timing_marker
- style_profile: cinematic_barsoom_warfare
- batch_role: scene_stage_authoring
- fix_of: 

# Continuity Notes
- Ensure Green Martian warrior group position matches previous building entry pattern from CL002.
- Maintain deserted city buildings in valley with hills beyond environment consistent with BT003.md retreat order beat.
- Doorway threshold must show melting motion inward to justify vanishing action sequence.
- Interior shadows should be visible swallowing figures without showing individual warrior faces.
- Lighting must remain daylight to match preceding clips CL001 and CL002.
- Three-minute timing marker must be active throughout clip duration.

# Repair Notes
- If doorway threshold appears empty, add Green Martian warriors at edge beginning to melt inward.
- If interior shadows are missing or too bright, adjust lighting to show dark interior spaces swallowing figures.
- If background shows open valley instead of deserted buildings, adjust environment to match BT003.md geography.
- If movement looks static despite retreat order implication, introduce subtle melting motion toward interior darkness.
- If timing marker is not visible, add three-minute constraint indicator in doorway frame axis.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
