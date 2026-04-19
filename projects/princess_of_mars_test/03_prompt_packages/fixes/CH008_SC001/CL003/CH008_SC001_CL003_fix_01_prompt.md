# Title
CH008_SC001 CL003 Fix 01 Prompt

# ID
CH008_SC001_CL003_fix_01_prompt

# Purpose
Corrective still-generation that preserves composition and look while fixing local issues for CL003 medium close-up reaction shot of Carter's face during retreat order beat, maintaining visual continuity with scene requirements.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium close-up reaction on Carter face showing emotional shift from anticipation to urgency, implied command signal visible above frame, city plaza background with open ground horizon, natural daylight lighting, sharp focus on facial expression, subtle head movement indicating sudden realization, green Martian warriors blurred in distance.

# Negative Prompt
motion blur, extra limbs, distorted face, wrong character count, inconsistent anatomy, text overlay, watermark, logo, low resolution, overexposed, underexposed, color shift, facial distortion, unnatural skin texture, background clutter, motion artifacts, depth of field errors, incorrect lighting direction.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md retreat_order_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter face_reaction, implied_command_signal_source
- look_continuity_policy: match_previous_clip_lighting_and_color_grade
- intended_lighting_change: none
- composition_type: medium_close_up_reaction
- continuity_mode: cutaway
- starting_keyframe_strategy: static_on_carter_face_with_command_signal_visible_above
- dependency_policy: independent_can_follow_any_previous_clip
- auto_advance_policy: false
- fallback_strategy: cut_to_wide_halt_if_reaction_misread
- consistency_assist_policy: enabled
- consistency_assist_method: frame_matching
- anatomy_repair_policy: strict
- consistency_targets: facial_expression, background_elements, lighting_direction
- style_profile: cinematic_warfare
- batch_role: still_fix
- fix_of: CL003_reaction_shot_local_issues

# Continuity Notes
- Maintain visual continuity with BT001 procession return shots for character placement and environmental consistency
- Preserve lighting direction from previous clips in scene to ensure seamless integration
- Keep background elements consistent with city plaza and open ground valley geography
- Match facial expression progression from anticipation beat to urgency beat within same shot sequence

# Repair Notes
- Fix any local artifacts or inconsistencies in facial features while preserving emotional expression
- Correct background depth of field errors if visible
- Ensure command signal source is properly implied without being over-exposed
- Repair any anatomy distortions in hands or shoulders if present
- Match color grading from approved still base image_1

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
