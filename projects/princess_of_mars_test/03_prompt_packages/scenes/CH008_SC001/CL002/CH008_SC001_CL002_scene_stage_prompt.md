# Title
CH008_SC001 CL002 Scene Stage Prompt

# ID
CH008_SC001_CL002_scene_stage_prompt

# Purpose
Establish the visual staging for the medium shot of the tactical retreat order into buildings. Focus on Green Martian warriors pausing at building entrances before entering in groups. Capture the sudden urgency and synchronized entry motion as they melt into doorways. The frame should convey the transition from open plaza to covered interiors without showing the subsequent vanishing action yet (that is a subsequent beat).

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium shot, group clusters of Green Martian warriors at building entrances, sudden urgency atmosphere, synchronized entry motion inward, deserted city architecture framing sides, daylight lighting, high stakes atmosphere, anticipation building, forward progression movement logic into interiors, over-the-shoulder from doorway perspective.

# Negative Prompt
Static pose, close-up facial details, chaotic movement, wrong faction colors (non-green attire), indoor setting only, night time, sudden halt or reverse movement within this clip duration, blurred background, incorrect character count, forward progression into valley terrain.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md building_entry_beat_documentation, CH008_SC001_scene_breakdown
- optional_refs: CH008_SC001_clip_roster
- visible_character_assets: Green Martian warriors group clusters (2-3 per doorway), building interiors dark
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot_building_entry
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: building_entrance_axis_eyelines_inward
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: 
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain tracking shot consistency with synchronized steps throughout the 5-second duration.
- Ensure location transition cues (plaza to building entrances) are visible in background/environment without abrupt cuts.
- Keep Green Martian attire consistent (green color, specific weaponry).
- Position Martians clearly at building entrances relative to camera angle.

# Repair Notes
- If character lacks physical description details, focus on silhouette and movement flow rather than facial features.
- Ensure Green Martians are distinct from any other factions present.
- Verify that the entry momentum is maintained until the end of the clip (retreat order happens in subsequent beats).
- Check for correct lighting consistency with previous establishing shots (daylight).

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
