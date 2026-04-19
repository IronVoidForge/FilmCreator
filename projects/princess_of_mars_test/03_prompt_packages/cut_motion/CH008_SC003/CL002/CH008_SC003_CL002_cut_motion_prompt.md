# Title
CH008_SC003 CL002 Cut Motion Prompt

# ID
CH008_SC003_CL002_cut_motion_prompt

# Purpose
Fill in the stage intent here. Focus on smooth transition emphasizing coordination between warriors during approach to the drifting craft. Maintain continuity of lighting and grade from previous keyframe.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green warriors in tactical formation moving from building roofs down to plain with low gray drifting craft as target, medium shot tracking coordination between warriors during approach, daylight lighting with smoke and fire sparks in background, damaged craft interior visible, smooth transition emphasizing coordination

# Negative Prompt
static pose, wrong character count, lighting shift, morphing anatomy, extra limbs, blurry motion, inconsistent grade, sudden jump cut, floating objects, distorted faces

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC003_BT001.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_in_tactical_formation, drifting_craft_interior_visible
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: close_ups_on_boarding_action
- starting_keyframe_strategy: focus_on_warriors_coordination_during_approach_with_craft_in_background
- dependency_policy: dependent_on_previous_wide_establishment_of_drifting_craft_position
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Lighting and grade must match previous keyframe exactly to preserve visual continuity.
- Character count of green warriors must remain consistent throughout the motion sequence.
- Environment transition from building roofs to plain should be smooth without abrupt cuts.
- Craft damage and banners must remain visible and consistent with established state.

# Repair Notes
- If motion appears jerky, adjust interpolation policy for smoother warrior coordination.
- Check anatomy consistency on warriors during movement to prevent morphing artifacts.
- Ensure lighting intensity does not fluctuate unexpectedly during the approach sequence.
- Verify craft interior visibility remains clear and matches reference documentation.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
