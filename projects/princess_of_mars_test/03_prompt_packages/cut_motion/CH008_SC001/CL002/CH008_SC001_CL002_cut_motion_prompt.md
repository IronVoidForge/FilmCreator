# Title
CH008_SC001 CL002 Cut Motion Prompt

# ID
CH008_SC001_CL002_cut_motion_prompt

# Purpose
Fill in the stage intent here. Establish a medium tracking shot following Carter from the rear of the procession, moving forward with synchronized steps and anticipation building as they approach the boundary between city plaza and open ground. Preserve keyframe lighting and grade from approved opening frame. Ensure visible motion matches procession movement logic.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium tracking shot following Carter from rear position. Procession moves forward with synchronized steps. Warriors in central column visible. City architecture frames left and right. Environmental transition from built environment to natural terrain begins. Anticipation building among onlookers. Forward progression with coordinated movement. Gray-painted airships distant on hill crest. Green Martians marching in formation.

# Negative Prompt
Static shot. Wrong composition. Lighting shift. Grade change. Anatomy error. Clothing distortion. Background blur. Motion stall. Reverse movement. Panic expression. Inconsistent character proportions. Degraded features. Overexposed or underexposed. Wrong color palette.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5s
- required_refs: BT001.md processions_return_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter rear_position, Warriors central_column visible
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: medium_tracking
- continuity_mode: insert
- starting_keyframe_strategy: follow_carter_position_from_rear_of_procession
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
- Maintain procession movement logic (forward progression with synchronized steps).
- Preserve keyframe lighting and grade from approved opening frame.
- Ensure transition from city plaza to open ground boundary is visible but smooth.
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
