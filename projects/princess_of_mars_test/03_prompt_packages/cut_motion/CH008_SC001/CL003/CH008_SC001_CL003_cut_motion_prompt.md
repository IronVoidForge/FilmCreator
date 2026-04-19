# Title
CH008_SC001 CL003 Cut Motion Prompt

# ID
CH008_SC001_CL003_cut_motion_prompt

# Purpose
Capture the complete visible action of Green Martian warriors crowding forward on vessel deck. Focus on coordinated movement along horizontal axis and descending air craft background while maintaining keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian warriors crowding forward on vessel deck, coordinated movement along horizontal axis, descending air craft background, daylight with smoke and fire effects, medium shot composition, preserved lighting grade, subtle camera shake indicating urgency, figures distributed across forward sections.

# Negative Prompt
morphing face, extra limbs, flickering signal, wrong color palette, blurry text, distorted background, inconsistent lighting, static image, low resolution, doorway threshold, interior shadows swallowing figures.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md, BT002.md
- optional_refs: CH008_SC001_scene_breakdown, BT003.md
- visible_character_assets: Green Martian figures on forward decks of air craft
- look_continuity_policy: preserve_keyframe_lighting_and_grade_by_default
- intended_lighting_change: none_significant_during_retreat_sequence
- composition_type: medium_shot_vessel_deck
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: depends_on_CL002_establishing_entry_pattern
- auto_advance_policy: none
- fallback_strategy: cut_to_wide_halt_if_crowding_motion_misread
- consistency_assist_policy: ensure_group_consistency_across_vessels
- consistency_assist_method: reference_previous_clip_group_placement
- anatomy_repair_policy: correct_any_figure_drift_during_crowding_motion
- consistency_targets: vessel_deck_axis_and_forward_sections
- style_profile: cinematic_compositional
- batch_role: cut_motion_sequence
- fix_of: CL002_output
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Ensure coordinated movement along deck is active. Vessels descending toward city building facade.

# Repair Notes
- Ensure Green Martian warriors consistency with previous clip group placement. Maintain figure consistency without distortion. Correct any anatomy drift during crowding motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
