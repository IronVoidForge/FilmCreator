# Title
CH008_SC001 CL003 Fix 01 Prompt

# ID
CH008_SC001_CL003_fix_01_prompt

# Purpose
Corrective still-generation that preserves composition and look while fixing local issues for CL003 wide shot exterior valley view from window, maintaining visual continuity with scene requirements regarding airship arrival sequence.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot exterior valley view from interior window perspective, twenty gray low-profile airships sailing toward valley center, banners on stem and stern visible, glowing devices on prow clearly seen, sky environment establishing scale, natural daylight lighting, sharp focus on ship details, subtle camera tracking motion following ships entering frame, green-skinned Martian architecture blurred in background horizon.

# Negative Prompt
motion blur, extra limbs, distorted face, wrong character count, inconsistent anatomy, text overlay, watermark, logo, low resolution, overexposed, underexposed, color shift, facial distortion, unnatural skin texture, background clutter, motion artifacts, depth of field errors, incorrect lighting direction, close-up framing, human face focus, city plaza setting.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md, SC001_scene_breakdown.md
- optional_refs: BT003.md
- visible_character_assets: twenty_gray_airships_sailing_toward_valley, banners_on_ships, glowing_devices_on_ships, sky_environment
- look_continuity_policy: match_previous_clip_lighting_and_color_grade
- intended_lighting_change: none
- composition_type: wide_shot_exterior_valley_view_from_window
- continuity_mode: insert
- starting_keyframe_strategy: static_clear_valley_view_no_ships_visible_yet
- dependency_policy: follows_CL002_directly, final_clip_in_sequence
- auto_advance_policy: false
- fallback_strategy: cut_to_wide_halt_if_reaction_misread
- consistency_assist_policy: enabled
- consistency_assist_method: frame_matching
- anatomy_repair_policy: strict
- consistency_targets: ship_details, background_elements, lighting_direction
- style_profile: cinematic_warfare
- batch_role: still_fix
- fix_of: CL003_airship_arrival_local_issues

# Continuity Notes
- Maintain visual continuity with BT002 martians melting away transition for environmental consistency and timing of airship arrival
- Preserve lighting direction from previous clips in scene to ensure seamless integration with interior window perspective
- Keep background elements consistent with Martian buildings and valley geography, avoiding city plaza references
- Match ship appearance (gray, low profile, banners, glowing devices) as per visual continuity requirements for enemy fleet

# Repair Notes
- Fix any local artifacts or inconsistencies in ship details while preserving emotional context of arrival sequence
- Correct background depth of field errors if visible to ensure focus remains on ships and valley view
- Ensure implied command signal source is properly integrated without being over-exposed (if applicable)
- Repair any anatomy distortions in hands or shoulders if present (though less relevant for wide shot, keep general)
- Match color grading from approved still base image_1

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
