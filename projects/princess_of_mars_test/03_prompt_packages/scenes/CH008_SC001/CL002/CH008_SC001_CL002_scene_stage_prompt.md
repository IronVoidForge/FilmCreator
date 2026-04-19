# Title
CH008_SC001 CL002 Scene Stage Prompt

# ID
CH008_SC001_CL002_scene_stage_prompt

# Purpose
Establish the visual staging for the medium tracking shot of the procession returning from the incubation ceremony. Focus on Carter positioned at the rear of the formation, moving forward through the city plaza towards the open ground boundary. Capture the synchronized movement of Green Martians in the central column and the anticipation building as they approach the valley entrance. The frame should convey forward momentum and the transition from built environment to natural terrain without showing the sudden retreat order yet (that is a subsequent beat).

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium tracking shot, Carter visible at rear of procession, Green Martians in central column marching forward, city plaza architecture framing left and right sides, open ground valley horizon ahead, synchronized steps, daylight lighting, high stakes atmosphere, anticipation building, forward progression movement logic.

# Negative Prompt
Static pose, close-up facial details, chaotic movement, wrong faction colors (non-green attire), indoor setting only, night time, sudden halt or reverse movement within this clip duration, blurred background, incorrect character count.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md processions_return_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter rear_position, Warriors central_column visible
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_tracking
- continuity_mode: insert
- starting_keyframe_strategy: follow_carter_position_from_rear_of_procession
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
- Ensure location transition cues (plaza to valley) are visible in background/environment without abrupt cuts.
- Keep Green Martian attire consistent (green color, specific weaponry).
- Position Carter clearly at the rear of the formation relative to the camera angle.

# Repair Notes
- If Carter lacks physical description details, focus on silhouette and movement flow rather than facial features.
- Ensure Green Martians are distinct from any other factions present.
- Verify that the forward momentum is maintained until the end of the clip (retreat order happens in subsequent beats).
- Check for correct lighting consistency with previous establishing shots (daylight).

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
