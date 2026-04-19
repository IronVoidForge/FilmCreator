# Title
CH008_SC001 CL003 Fix 01 Prompt

# ID
CH008_SC001_CL003_fix_01_prompt

# Purpose
Corrective still-generation preserving composition and look while fixing local issues for CL003 medium shot showing Green Martian figures distributed across forward sections of descending air craft, maintaining visual continuity with scene requirements showing martians crowding toward front edge of vessels.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium shot showing Green Martian figures distributed across forward sections of descending air craft, horizontal axis along vessel deck, long low gray-painted vessels with strange banners on prows, figures crowd forward decks, natural daylight transitioning to interior shadow illumination, sharp focus on vessel frame edges, subtle coordinated movement along deck length toward front edge, group entity without individual physical descriptions, interior shadows swallowing figures at threshold, timing marker active for three minute retreat window.

# Negative Prompt
motion blur, extra limbs, distorted face, wrong character count, inconsistent anatomy, text overlay, watermark, logo, low resolution, overexposed, underexposed, color shift, facial distortion, unnatural skin texture, background clutter, motion artifacts, depth of field errors, incorrect lighting direction, proper nouns, named characters, individual physical descriptions.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md doorway_vanishing_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Green Martian warriors_group, interior shadows
- look_continuity_policy: match_previous_clip_lighting_and_color_grade
- intended_lighting_change: none
- composition_type: medium_shot_vessel_deck_with_martians
- continuity_mode: insert
- starting_keyframe_strategy: static_hold
- dependency_policy: depends_on_CL002_establishing_entry_pattern
- auto_advance_policy: false
- fallback_strategy: cut_to_wide_halt_if_vanishing_action_unavailable
- consistency_assist_policy: enabled
- consistency_assist_method: frame_matching
- anatomy_repair_policy: strict
- consistency_targets: vessel_frame, interior_shadows, lighting_direction
- style_profile: cinematic_warfare
- batch_role: still_fix
- fix_of: CL003_forward_deck_martians_local_issues
- approved_still_base: image_1
- secondary_reference: image_2

# Continuity Notes
- Maintain visual continuity with BT002 building entry pattern shots for character placement and environmental consistency
- Preserve lighting direction from previous clips in scene to ensure seamless integration
- Keep background elements consistent with deserted city buildings and valley geography
- Match vessel frame visibility and interior shadow swallowing motion within same shot sequence
- Ensure three minute timing marker remains active throughout vanishing action

# Repair Notes
- Fix any local artifacts or inconsistencies in vessel frame edges while preserving melting motion
- Correct background depth of field errors if visible at doorway threshold
- Ensure interior shadows swallowing figures are properly implied without being over-exposed
- Repair any anatomy distortions in group entity if present
- Match color grading from approved still base image_1

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
