# Title
CH008_SC001 CL004 Scene Stage Prompt

# ID
CH008_SC001_CL004_scene_stage_prompt

# Purpose
Establish immediate tactical response to enemy airships approaching valley city. Martians halt procession and execute coordinated retreat into deserted buildings within three-minute window. Wide-angle framing captures full group movement from plaza floor toward building entrances, emphasizing urgency shift from calm procession to sudden scurrying for cover. Shot serves as establishing context for subsequent close-ups of doorway vanishing action.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian warriors in formation marching through deserted city plaza into open valley with hills beyond, gray-painted enemy airships visible on horizon crest, sudden halt motion followed by synchronized reverse movement toward multi-story building entrances, wide angle composition, high stakes warfare atmosphere, red copper sky lighting, detailed green armor and weaponry, deserted buildings intact with clear doorways, urgent tactical retreat sequence, procession reversing direction upon command signal.

# Negative Prompt
deformed limbs, extra fingers, static shot, blurry text, low resolution, blue sky, green sky, inconsistent character count, wrong facial expressions, motion blur artifacts, distorted architecture, missing command signal source, incorrect color palette for Mars environment, open ground without buildings, city plaza with debris, calm procession without urgency, single warrior instead of group formation.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT001.md, BT002.md, BT003.md
- optional_refs: CH008_SC001_scene_breakdown, CH008_SC001_clip_roster
- visible_character_assets: Green Martian Warriors group_formation, implied_command_signal_source
- look_continuity_policy: wide_halt_reverse_with_building_entry_focus
- intended_lighting_change: daylight_to_dramatic_fire_illumination_transition
- composition_type: wide_establishing_tactical_response
- continuity_mode: dependent_on_airship_threat_context
- starting_keyframe_strategy: static_opening_with_full_procession_visible_before_movement_change
- dependency_policy: dependent_on_CL003_reaction_clip_first
- auto_advance_policy: advance_to_doorway_entry_sequence_after_halt_completion
- fallback_strategy: cut_to_high_angle_command_source_if_continuity_breaks
- consistency_assist_policy: maintain_character_count_across_wide_frame
- consistency_assist_method: group_formation_tracking_through_building_entrances
- anatomy_repair_policy: prevent_deformation_during_rapid_pivot_motion
- consistency_targets: doorway_entry_pattern, retreat_timing_marker_three_minutes
- style_profile: tactical_warfare_establishing_shot
- batch_role: establishing_context_clip
- fix_of: CL003_reaction_close_up_continuity

# Continuity Notes
- Procession movement must transition smoothly from city plaza to open valley terrain with hills beyond. Character placement consistency is critical (Green Martian Warriors group formation maintaining cohesion). The halt and reverse motion must be synchronized across the wide frame. Environmental context shifts from built architecture to natural valley floor before building entry sequence. Enemy airships visible on horizon crest establish threat scale without dominating composition. Doorway entrances must remain clear and accessible throughout retreat sequence. Three-minute timing marker active for vanishing action completion.

# Repair Notes
- Address potential issues like motion blur consistency during rapid pivot from forward movement to reverse direction, ensuring character deformation does not occur during the retreat motion, verifying that the valley floor environment is distinct from city plaza in terms of lighting and texture. Ensure the command signal source is visible or correctly implied for continuity with airship threat context. Verify doorway entry pattern maintains consistent group clusters (2-3 Martians per entrance). Confirm red copper sky lighting remains consistent throughout Mars environment without shifting to generic tones. Check that deserted buildings show no debris or damage from previous combat sequences.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
