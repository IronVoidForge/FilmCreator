# Title
CH008_SC001 CL003 Cut Motion Prompt

# ID
CH008_SC001_CL003_cut_motion_prompt

# Purpose
Capture the complete vanishing action of Green Martian warriors at doorway threshold. Focus on retreat timing constraint and interior shadows swallowing figures while maintaining keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian warriors at doorway threshold, melting inward motion, interior shadows swallowing figures, close-up on doorway frame axis, eyelines from exterior looking into darkness, deserted city buildings background, preserved lighting grade, subtle camera shake indicating urgency.

# Negative Prompt
morphing face, extra limbs, flickering signal, wrong color palette, blurry text, distorted background, inconsistent lighting, static image, low resolution.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown, BT003.md
- visible_character_assets: Green Martian warriors (individual or small group at doorway edge), interior shadows swallowing figures
- look_continuity_policy: preserve_keyframe_lighting_and_grade_by_default
- intended_lighting_change: none_significant_during_retreat_sequence
- composition_type: close_up_on_doorway_threshold
- continuity_mode: insert
- starting_keyframe_strategy: doorway_frame_axis_with_martians_at_edge
- dependency_policy: depends_on_CL002_establishing_entry_pattern
- auto_advance_policy: none
- fallback_strategy: cut_to_wide_halt_if_vanishing_action_misread
- consistency_assist_policy: ensure_group_consistency_across_doorways
- consistency_assist_method: reference_previous_clip_group_placement
- anatomy_repair_policy: correct_any_figure_drift_during_melting_motion
- consistency_targets: doorway_frame_axis_and_interior_shadows
- style_profile: cinematic_compositional
- batch_role: cut_motion_sequence
- fix_of: CL002_output
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Ensure retreat timing marker (3 minutes) is active. Doorways empty at end state.

# Repair Notes
- Ensure Green Martian warriors consistency with previous clip group placement. Maintain interior shadow swallowing figures without distortion. Correct any anatomy drift during melting motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
