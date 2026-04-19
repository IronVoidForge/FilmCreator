# Title
CH008_SC001 CL003 Fix 01 Prompt

# ID
CH008_SC001_CL003_fix_01_prompt

# Purpose
Corrective still-generation that preserves composition and look while fixing local issues for CL003 close-up doorway vanishing action shot, maintaining visual continuity with scene requirements showing Green Martian warriors at doorway threshold beginning to melt into interior spaces.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Close-up on doorway threshold showing Green Martian warriors at edge of frame beginning to melt into interior darkness, deserted city buildings in valley with hills beyond visible through opening, natural daylight transitioning to interior shadow illumination, sharp focus on doorway frame edges, subtle melting motion inward toward dark interior spaces, group entity without individual physical descriptions, interior shadows swallowing figures, timing marker active for three minute retreat window.

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
- composition_type: close_up_doorway_threshold
- continuity_mode: insert
- starting_keyframe_strategy: doorway_frame_axis_with_martians_at_threshold
- dependency_policy: depends_on_CL002_establishing_entry_pattern
- auto_advance_policy: false
- fallback_strategy: cut_to_wide_halt_if_vanishing_action_unavailable
- consistency_assist_policy: enabled
- consistency_assist_method: frame_matching
- anatomy_repair_policy: strict
- consistency_targets: doorway_frame, interior_shadows, lighting_direction
- style_profile: cinematic_warfare
- batch_role: still_fix
- fix_of: CL003_doorway_vanishing_local_issues
- approved_still_base: image_1
- secondary_reference: image_2

# Continuity Notes
- Maintain visual continuity with BT002 building entry pattern shots for character placement and environmental consistency
- Preserve lighting direction from previous clips in scene to ensure seamless integration
- Keep background elements consistent with deserted city buildings and valley geography
- Match doorway frame visibility and interior shadow swallowing motion within same shot sequence
- Ensure three minute timing marker remains active throughout vanishing action

# Repair Notes
- Fix any local artifacts or inconsistencies in doorway frame edges while preserving melting motion
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
