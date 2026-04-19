# Title
CH008_SC001 CL002 Cut Motion Prompt

# ID
CH008_SC001_CL002_cut_motion_prompt

# Purpose
Establish the stage intent here. Show the dissolution of Martian presence and transition to enemy arrival focus. Preserve keyframe lighting and grade from approved opening frame. Ensure visible motion matches dissolve progression logic.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot of room showing dissolution, POV from window tracking dissolve. Martians occupy floor level before dissolving upward/outward into mist. No physical movement, only state change. Mist/moisture effect critical for continuity; three-minute timing marker. Narrator at interior window with clear line of sight to valley. Airships enter frame from horizon moving toward camera/valley center. Banners and glowing devices on ships are key visual identifiers.

# Negative Prompt
Static shot. Wrong composition. Lighting shift. Grade change. Anatomy error. Clothing distortion. Background blur. Motion stall. Reverse movement. Panic expression. Inconsistent character proportions. Degraded features. Overexposed or underexposed. Wrong color palette.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5s
- required_refs: BT002.md martians_melting_away_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: martians_visible_in_lower_room_space, mist_moisture_dissolve_effect, narrator_at_window_periphery
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: wide_shot_interior_to_exterior_blend
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_showing_martian_presence_beginning_dissolve
- dependency_policy: follows_CL001_directly, leads_to_CL003
- auto_advance_policy: advance_if_motion_stalls
- fallback_strategy: cut_to_close_up_on_mist_effect_if_continuity_issue
- consistency_assist_policy: apply_consistency_targets
- consistency_assist_method: anatomy_and_style_alignment
- anatomy_repair_policy: repair_degraded_features
- consistency_targets: character_proportions, clothing_details, lighting_consistency
- style_profile: cinematic_warfare_barsoom
- batch_role: cut_motion_clip
- fix_of: CL001

# Continuity Notes
- Maintain dissolve progression logic (state change from presence to absence).
- Preserve keyframe lighting and grade from approved opening frame.
- Ensure transition from martian presence to empty room is visible but smooth.
- Keep character proportions consistent with previous clips in sequence.
- Avoid sudden camera jerks or focus pulls during motion.

# Repair Notes
- If motion stalls, advance dissolve progression slightly.
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
