# Title
CH008_SC001 CL002 Cut Motion Prompt

# ID
CH008_SC001_CL002_cut_motion_prompt

# Purpose
Establish wide establishing shot showing air craft fleet descending from upper sky toward city building. Start from approved opening frame where first craft is visible in distance. Ensure visible motion matches descent trajectory (downward diagonal). Preserve keyframe lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide establishing shot showing twenty large gray air craft descending from upper sky toward city building facade. Long low vessels with strange banners visible on prows. Valley below and hills beyond maintain continuity. Figures crowd forward decks of air craft. Downward diagonal movement from upper sky to lower city level. Gray-painted vessels drift southeast/southwesterly.

# Negative Prompt
Static shot. Wrong composition. Lighting shift. Grade change. Anatomy error. Clothing distortion. Background blur. Motion stall. Reverse movement (ascending). Panic expression. Inconsistent character proportions. Degraded features. Overexposed or underexposed. Wrong color palette.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5s
- required_refs: BT002.md air_craft_descending_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Air Craft fleet (20 vessels), Green Martians on forward decks
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: wide_establishing
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_hold_first_craft_visible_in_distance
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
- Maintain air craft appearance consistency (long, low, gray-painted vessels with strange banners).
- Preserve keyframe lighting and grade from approved opening frame.
- Ensure transition from upper sky to city level is visible but smooth.
- Keep background valley/hills continuity stable throughout motion.
- Avoid sudden camera jerks or focus pulls during descent.

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
