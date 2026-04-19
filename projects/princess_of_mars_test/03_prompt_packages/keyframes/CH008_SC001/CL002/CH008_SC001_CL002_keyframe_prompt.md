# Title
CH008_SC001 CL002 Keyframe Prompt

# ID
CH008_SC001_CL002_keyframe_prompt

# Purpose
Establish the visual state of the Martian presence beginning to dissolve into mist within the interior room space, transitioning from a populated lower area to an empty one observed by the narrator at the window.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Interior room view from window perspective, lower floor space occupied by green-skinned figures fading into translucent mist, narrator visible in upper periphery standing at window frame, atmospheric haze rising from below, static dissolve progression tracking state change, cinematic lighting, high fidelity still, alien architecture interior, mist texture blending with figures.

# Negative Prompt
blur, distortion, extra limbs, marching, plaza, procession, forward movement, solid opaque figures, dark shadows, overexposed, low resolution, cartoonish, 3d render, plastic skin, bad anatomy, mismatched lighting, static pose (referring to the dissolve action), crowded composition, out of focus.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md, SC001_scene_breakdown.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: martians_visible_in_lower_room_space, mist/moisture_dissolve_effect, narrator_at_window_periphery
- look_continuity_policy: dependent_on_CL001_wide_establishing_first
- intended_lighting_change: none
- composition_type: medium_static_interior_view
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_showing_martian_presence_beginning_dissolve
- dependency_policy: follows_CL001_directly, leads_to_CL003
- auto_advance_policy: none
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: reference_alignment
- anatomy_repair_policy: strict
- consistency_targets: character_count, limb_placement, formation_geometry (dissolving state)
- style_profile: cinematic_warfare_era
- batch_role: interval_frame
- fix_of: CL001_wide_establishing_first

# Continuity Notes
- Maintain dissolve progression logic with three-minute timing marker.
- Ensure location transition from built environment to natural terrain begins subtly (via window view).
- Keep green-skinned figures visible in lower space while fading into mist.
- Capture anticipation building among onlookers and procession members (referring to Martians melting away).
- Avoid showing command signals or retreat order in this keyframe.

# Repair Notes
- Correct any motion blur that obscures character details during dissolve.
- Ensure formation geometry matches previous wide establishing shot.
- Fix lighting mismatches from preceding clip to maintain continuity.
- Verify character count remains consistent with dissolution scale.
- Adjust anatomy if limbs appear distorted during tracking movement.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
