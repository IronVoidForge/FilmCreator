# Title
CH008_SC001 CL002 Cut Motion Prompt

# ID
CH008_SC001_CL002_cut_motion_prompt

# Purpose
Establish medium tracking shot showing Green Martian warriors retreating into building entrances. Start from approved opening frame where retreat command is given. Ensure visible motion matches tactical retreat logic (entering doorways). Preserve keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium tracking shot following Green Martian warriors entering building doorways. Group clusters of 2-3 Martians per entrance. Synchronized entry motion into dark interiors. Building exteriors frame left and right. Environmental transition from plaza to occupied buildings begins. Tactical retreat urgency visible. Gray-painted airships distant on hill crest. Deserted city architecture frames scene.

# Negative Prompt
Static shot. Wrong composition. Lighting shift. Grade change. Anatomy error. Clothing distortion. Background blur. Motion stall. Reverse movement (marching forward). Panic expression. Inconsistent character proportions. Degraded features. Overexposed or underexposed. Wrong color palette.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5s
- required_refs: BT002.md building_entry_pattern_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Green Martian warriors (group clusters 2-3 Martians per doorway), building interiors dark
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: medium_tracking
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: building_entrance_axis_eyelines_inward_toward_interior_spaces
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
- Maintain tactical retreat logic (entering doorways).
- Preserve keyframe lighting and grade from approved opening frame.
- Ensure transition from city plaza to occupied buildings is visible but smooth.
- Keep character proportions consistent with previous clips in sequence.
- Avoid sudden camera jerks or focus pulls during motion.

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
