# Title
CH008_SC001 CL003 Scene Stage Prompt

# ID
CH008_SC001_CL003_scene_stage_prompt

# Purpose
Establish the visual entry of the airship fleet from the northern horizon into the frame, observed from John Carter's upper floor window perspective. Define the composition as Extreme Long Sky to capture the scale of arrival and maintain continuity with the procession movement context.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Northern sky clear with visible horizon line, multiple long low gray-painted airships descending into frame from northern direction, strange banners on prows, odd devices on prow, daylight lighting, cinematic composition, static camera position holding full approach, atmospheric depth, tactical arrival urgency implied, group entity without individual physical descriptions.

# Negative Prompt
blurry vessel form, distorted anatomy, wrong skin tone, static image, missing timing marker, dark lighting, crowded city buildings in foreground, calm expression, low resolution, extra limbs, incorrect eye direction, foggy atmosphere, text overlay, visible faces on Martians, bright interior spaces, empty vessel decks, vertical descent path missing.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: CH008_SC001_scene_breakdown, CH008_SC001_clip_roster
- visible_character_assets: multiple gray-painted airships, horizon line reference
- look_continuity_policy: match_previous_procession_movement
- intended_lighting_change: maintain_daylight_deserted_city
- composition_type: extreme_long_sky_fleet_arrival
- continuity_mode: insert
- starting_keyframe_strategy: northern_sky_clear_with_horizon_line_visible
- dependency_policy: none
- auto_advance_policy: standard_cut_on_arrival_completion
- fallback_strategy: cut_to_wide_if_close_unavailable
- consistency_assist_policy: enable_character_consistency_check
- consistency_assist_method: match_forward_vessel_deck_placement
- anatomy_repair_policy: prioritize_group_entity_consistency
- consistency_targets: vessel_deck_axis, forward_movement_trajectory, daylight_lighting
- style_profile: cinematic_barsoom_warfare
- batch_role: scene_stage_authoring
- fix_of: 

# Continuity Notes
- Ensure Green Martian warrior group position matches previous building entry pattern from CL002.
- Maintain deserted city buildings in valley with hills beyond environment consistent with BT003.md retreat order beat.
- Vessel deck must show forward crowding motion toward front edge to justify arrival sequence.
- Air craft form should be visible as long low gray-painted vessels with strange banners on prows.
- Lighting must remain daylight to match preceding clips CL001 and CL002.
- Horizontal axis along vessel deck must be maintained throughout clip duration.

# Repair Notes
- If vessel deck appears empty, add Green Martian warriors at forward edge beginning to crowd toward front.
- If air craft form is missing or incorrect, adjust environment to show long low gray-painted vessels with strange banners.
- If background shows open valley instead of deserted buildings with hills, adjust environment to match BT003.md geography.
- If movement looks static despite arrival implication, introduce subtle forward crowding motion along vessel length.
- If lighting is not daylight, adjust to maintain daylight consistent with preceding clips.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
