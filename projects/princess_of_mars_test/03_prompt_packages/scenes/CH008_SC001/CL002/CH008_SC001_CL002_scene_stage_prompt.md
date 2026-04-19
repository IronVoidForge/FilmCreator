# Title
CH008_SC001 CL002 Scene Stage Prompt

# ID
CH008_SC001_CL002_scene_stage_prompt

# Purpose
Establish visual staging for the medium tracking shot where Martians dissolve into mist within the city building interior, transitioning focus to the narrator at the window observing the valley. Capture the synchronized state change of Green Martians fading upward and outward while maintaining the three-minute timing marker. The frame should convey the transition from built environment presence to absence without showing the sudden retreat order yet (that is a subsequent beat). Focus on the blend of interior room space and exterior valley view opening up as airships enter.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium tracking shot, lower room space visible, Green Martians dissolving upward into mist/moisture effect, Narrator silhouette at window periphery, window frame visible, exterior valley view opening up, gray airships entering horizon, banners and glowing devices on ships clearly visible, daylight lighting, high stakes atmosphere, anticipation building, forward progression movement logic, three-minute timing marker.

# Negative Prompt
Static pose, close-up facial details, chaotic movement, wrong faction colors (non-green attire), indoor setting only, night time, sudden halt or reverse movement within this clip duration, blurred background, incorrect character count, Carter visible, physical props involved in dissolution, abrupt cuts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md processions_return_beat_documentation, BT002.md martians_melting_away_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Narrator window_periphery, Martians lower_room_space_dissolving
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight_consistent
- composition_type: wide_shot_interior_to_exterior_blend
- continuity_mode: insert
- starting_keyframe_strategy: static_showing_martian_presence_beginning_dissolve
- dependency_policy: follows_CL001_directly, leads_to_CL003
- auto_advance_policy: follow_dissolution_progression
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: track_state_change_from_presence_to_absence
- consistency_assist_method: dissolve_tracking
- anatomy_repair_policy: focus_on_silhouette_and_mist_effect
- consistency_targets: mist_timing, narrator_visibility
- style_profile: cinematic_compositional
- batch_role: transition_clip
- fix_of: CL001_wide_establishing_first

# Continuity Notes
- Maintain tracking shot consistency with synchronized steps throughout the 5-second duration.
- Ensure location transition cues (plaza to valley) are visible in background/environment without abrupt cuts.
- Keep Green Martian attire consistent (green color, specific weaponry).
- Position Narrator clearly at window periphery relative to the camera angle.
- Track dissolution progression from lower room space upward/outward into mist.
- Ensure airships enter frame from horizon moving toward valley center.
- Verify that the three-minute dissolve timing marker is respected in visual pacing.

# Repair Notes
- If Martians lack physical description details, focus on silhouette and movement flow rather than facial features.
- Ensure Green Martians are distinct from any other factions present.
- Verify that the forward momentum of dissolution is maintained until the end of the clip (retreat order happens in subsequent beats).
- Check for correct lighting consistency with previous establishing shots (daylight).
- If Narrator visibility is unclear, emphasize window frame and silhouette placement.
- Ensure mist/moisture effect is critical for continuity without obscuring key visual identifiers.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
