# Title
CH008_SC001 CL002 Scene Stage Prompt

# ID
CH008_SC001_CL002_scene_stage_prompt

# Purpose
Establish visual staging for medium group shot from John Carter's upper floor window perspective showing Green Martian ground forces retreating in coordinated formation toward eastern sector of city perimeter. Focus on maintaining consistent spacing between ground forces and tracking their organized withdrawal movement. Frame should show city boundary as visual reference for retreat direction with valley below and hills beyond visible for geographic continuity. The opening keyframe intent is to show Martians positioned at city perimeter ready for engagement, then camera follows retreat path from fixed position during clip duration. This sets stage for coming conflict between Green Martians and Air Fleet while establishing threat level through coordinated troop movement.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium group shot from upper floor window perspective, Green Martian ground forces retreating in coordinated formation toward eastern sector of city perimeter, green skin visible with ornaments worn, spears carried by warriors, consistent spacing between troops maintained throughout movement, organized withdrawal trajectory from city boundary outward, valley below visible in background, hills beyond maintaining geographic continuity, daylight lighting, dust kicked up by retreating troops visible in foreground, anticipation building atmosphere, John Carter observer POV eyeline directed downward toward city perimeter, vertical axis from upper floor to ground level, eastern sector marked as retreat destination.

# Negative Prompt
Close-up facial details, indoor setting only, night time, static pose, wrong faction colors (non-green skin), forward progression into valley terrain, sudden halt or reverse movement within clip duration, blurred background, incorrect character count, missing ornaments on Martians, missing spears carried by warriors, abrupt cuts breaking continuity, Carter position inconsistent in window frame, dust not visible from retreating troops, valley/hills background unstable across shots.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md martian_retreat_beat_documentation, CH008_SC001_scene_breakdown
- optional_refs: CH008_SC001_clip_roster
- visible_character_assets: Green Martians in formation (green skin with ornaments, spears carried), coordinated movement toward eastern sector
- look_continuity_policy: maintain ground force spacing and retreat direction consistency across shots, valley/hills background stable
- intended_lighting_change: daylight consistent with establishing shots
- composition_type: medium_group_shot_from_window_pov
- continuity_mode: cutaway
- starting_keyframe_strategy: static_hold_martians_at_city_perimeter
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: insert_if_movement_disrupted
- consistency_assist_policy: ground force formation and retreat direction tracking
- consistency_assist_method: literal_descriptive_appearance_verification
- anatomy_repair_policy: focus on troop silhouette and movement flow
- consistency_targets: coordinated formation maintained, valley/hills background continuity
- style_profile: cinematic_compositional
- batch_role: martian_retreat_establishment
- fix_of: none

# Continuity Notes
- Maintain tracking shot consistency with coordinated Green Martian retreat movement throughout the 5-second duration.
- Ensure location transition cues (city perimeter to eastern sector) are visible in background/environment without abrupt cuts.
- Keep ground force spacing consistent between troops across shots for formation continuity.
- Position valley below and hills beyond stable across shots for geographic continuity.
- Track dust kicked up by retreating troops visible throughout clip duration.
- Maintain daylight lighting consistency with previous establishing shots.

# Repair Notes
- If troop lacks physical description details, focus on silhouette and movement flow rather than facial features.
- Ensure Green Martians are distinct from any other factions present (Air Fleet separate).
- Verify that the coordinated retreat momentum is maintained until the end of the clip.
- Check for correct lighting consistency with previous establishing shots (daylight).
- If formation appears disrupted, adjust to show consistent spacing between troops during interval beats.
- Ensure dust kicked up by retreating troops is visible in each shot.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
