# Title
CH008_SC002 CL009 Cut Motion Prompt

# ID
CH008_SC002_CL009_cut_motion_prompt

# Purpose
Depict the engagement and damage to fleet, showing ship rotation mechanics and alignment vector for coordinated volley fire preparation.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
close-up on damaged gray air craft hull rotating on thrusters, crew hands realigning weapons, smoke density increasing, debris scattered around ship base, daylight with fire glow, banners fluttering in wind, mechanical rotation mechanism visible, coordinated volley fire preparation.

# Negative Prompt
static image, no motion blur, wrong skin tone, missing hull damage, floating debris, overexposed, underexposed, distorted rotation mechanism, extra limbs, morphing ship shape.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL009
- duration_seconds: 5
- required_refs: CL008 medium shot, BT003 index
- optional_refs: hull damage visible, smoke density increasing
- visible_character_assets: Ship rotation mechanism, crew hands
- look_continuity_policy: preserve keyframe lighting and grade by default
- intended_lighting_change: none
- composition_type: close-up
- continuity_mode: cutaway
- starting_keyframe_strategy: static on rotation mechanism
- dependency_policy: sequential to crew realignment medium shot
- auto_advance_policy: 
- fallback_strategy: insert debris scattered if rotation heavy
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: action-oriented, awe-inspiring
- batch_role: cut_motion
- fix_of: 

# Continuity Notes
- preserve keyframe lighting and grade by default
- focus on visible motion and camera behavior
- maintain daylight with smoke from fire atmosphere
- ensure mechanical rotation mechanism remains consistent with previous keyframe

# Repair Notes
- insert debris scattered if rotation heavy
- avoid morphing ship shape during thruster movement
- correct any distortion in hull damage visibility

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL009.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
