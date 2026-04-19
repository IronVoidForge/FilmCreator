# Title
CH008_SC001 CL002 Cut Motion Prompt

# ID
CH008_SC001_CL002_cut_motion_prompt

# Purpose
Establish medium group shot showing Green Martians retreating from city perimeter toward eastern sector. Start from approved opening frame where Martians are positioned at city boundary. Ensure visible motion matches retreat trajectory (diagonal movement away from center). Preserve keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium group shot showing coordinated Green Martians in formation retreating from city perimeter toward eastern sector. Warriors maintain consistent spacing with green skin and ornaments visible. Dust kicked up by retreating troops visible in foreground. City boundary serves as visual reference for movement direction. Valley below and hills beyond maintain continuity. Green Martians move in unison maintaining formation.

# Negative Prompt
Static shot. Wrong composition. Lighting shift. Grade change. Anatomy error. Clothing distortion. Background blur. Motion stall. Reverse movement (ascending). Panic expression. Inconsistent character proportions. Degraded features. Overexposed or underexposed. Wrong color palette. Air craft visible.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5s
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Green Martians in formation
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: medium_group
- continuity_mode: cutaway
- starting_keyframe_strategy: eastern_sector_marked_as_retreat_destination
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: advance_if_motion_stalls
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: apply_consistency_targets
- consistency_assist_method: anatomy_and_style_alignment
- anatomy_repair_policy: repair_degraded_features
- consistency_targets: character_proportions, clothing_details, lighting_consistency
- style_profile: cinematic_warfare_barsoom
- batch_role: cut_motion_clip
- fix_of: CL001

# Continuity Notes
- Maintain Green Martian appearance consistency (green skin, ornaments, spears).
- Preserve keyframe lighting and grade from approved opening frame.
- Ensure transition from city perimeter to eastern sector is visible but smooth.
- Keep background valley/hills continuity stable throughout motion.
- Avoid sudden camera jerks or focus pulls during retreat.

# Repair Notes
- If motion stalls, advance camera position slightly.
- If anatomy degrades, apply consistency targets for character proportions and clothing details.
- If lighting shifts, revert to keyframe lighting profile.
- If composition drifts, re-align with starting_keyframe_strategy.
- If style inconsistency appears, reinforce cinematic_warfare_barsoom style_profile.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
