# Title
CH008_SC001 CL004 Scene Stage Prompt

# ID
CH008_SC001_CL004_scene_stage_prompt

# Purpose
Establish John Carter's observational perspective from upper floor window as he witnesses twenty large gray air craft descending toward city building. Focus on emotional progression from initial curiosity to growing concern and anticipation as vessels appear in valley view below. Window frame visible on left edge of composition serves as visual boundary. Shot functions as character reaction close-up that will cutaway to aircraft fleet for scene transition. Opening keyframe establishes Carter's stationary observation stance with city view through glass, maintaining continuity across frames while expression shifts subtly reflect emotional response to unfolding events.

# Workflow Type
authoring.scene_stage

# Positive Prompt
John Carter upper torso and face positioned at window frame edge, body angled downward toward city view, expression shifting from curiosity to concern with subtle eyebrow movement and slight mouth tension, partial window frame visible on left side of composition, background valley floor stable with distant hills beyond, minimal posture movement reflecting emotional change, daylight illumination consistent with Mars environment, no motion blur artifacts, clear facial features showing growing anticipation.

# Negative Prompt
deformed facial features, extra fingers, static expression without concern shift, blurry text, low resolution, blue sky, green sky, inconsistent character count, wrong emotional expressions, motion blur artifacts, distorted architecture, missing window frame edge, incorrect color palette for Mars environment, valley floor with debris, hills beyond not visible, group formations of Martians in plaza, calm expression without growing concern.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT001.md, BT002.md, BT003.md
- optional_refs: CH008_SC001_scene_breakdown, CH008_SC001_clip_roster
- visible_character_assets: John Carter upper torso face, window frame partial
- look_continuity_policy: close_up_face_with_window_frame_edge_focus
- intended_lighting_change: daylight_consistent_with_mars_environment
- composition_type: character_reaction_close_up
- continuity_mode: dependent_on_aircraft_arrival_context
- starting_keyframe_strategy: static_hold_with_expression_shift
- dependency_policy: none
- auto_advance_policy: advance_to_cutaway_aircraft_fleet_after_4_seconds
- fallback_strategy: insert_if_continuity_breaks
- consistency_assist_policy: maintain_window_frame_position_across_frames
- consistency_assist_method: facial_expression_tracking_for_concern_progression
- anatomy_repair_policy: prevent_deformation_during_subtle_posture_shift
- consistency_targets: window_frame_edge, valley_background_stability, expression_progression_marker
- style_profile: character_reaction_establishing_shot
- batch_role: character_perspective_clip
- fix_of: CL003_reaction_close_up_continuity

# Continuity Notes
- John Carter's position at window frame must remain consistent across all frames with partial frame visible on left edge. Background valley floor and distant hills beyond must stay stable for continuity tracking. Expression progression from curiosity to concern should be subtle but visible through eyebrow movement, slight mouth tension, and posture shifts reflecting emotional change. Window frame edge position must not shift between frames. Valley/hills background continuity is critical - no debris or changes in terrain appearance. Minimal movement overall - only subtle shifts in posture reflecting emotional progression.

# Repair Notes
- Address potential issues like facial expression consistency during concern progression, ensuring window frame edge remains visible and stable across frames, verifying that valley background does not shift or introduce debris artifacts. Ensure daylight illumination remains consistent with Mars environment without shifting to generic tones. Check that subtle posture shifts do not create motion blur artifacts. Verify John Carter's upper torso positioning at window frame edge maintains consistency throughout clip duration. Confirm expression progression marker is visible by 4-second mark for scene transition preparation.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
