# Title
CH008_SC001 CL003 Keyframe Prompt

# ID
CH008_SC001_CL003_keyframe_prompt

# Purpose
Establish the wide exterior view from the window, capturing the open valley landscape before the gray airships fully enter the frame. Freeze the moment of initial observation with clear sky and horizon visible.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide angle view from interior window looking out over a dusty open valley under natural daylight. Gray low-profile airships with banners on stem and glowing devices on prow entering from horizon moving toward valley center. Clear sky environment. Cinematic composition. Static hold framing.

# Negative Prompt
Close-up portrait, distorted face, modern clothing, crowded background, wrong lighting, blurry text, extra limbs, cartoonish, oversaturated, city architecture instead of valley, ships missing or static, interior walls obscuring view.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: twenty_gray_airships_sailing_toward_valley, banners_on_ships, glowing_devices_on_ships, sky_environment
- look_continuity_policy: match_previous_clip_lighting
- intended_lighting_change: none
- composition_type: wide_shot_exterior_valley_view_from_window
- continuity_mode: insert
- starting_keyframe_strategy: static_clear_valley_view_no_ships_visible_yet
- dependency_policy: follows_CL002_directly, final_clip_in_sequence
- auto_advance_policy: manual_review_required
- fallback_strategy: cut_to_pov_tracking_ships_if_scale_issue
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: vehicle_positioning, sky_environment
- style_profile: cinematic_realism
- batch_role: keyframe_generation
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Ensure lighting matches previous interior observation sequences.
- Maintain static hold on valley view before tracking ships enter frame.
- Keep horizon line clear to show airship entry direction.

# Repair Notes
- If airships appear stationary, adjust motion to show entry from horizon.
- If composition is too close, widen to show valley scale.
- Ensure banners and glowing devices are visible on airships.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
