# Title
CH008_SC002 CL003 Cut Motion Prompt

# ID
CH008_SC002_CL003_cut_motion_prompt

# Purpose
Show consequence of battle through visible damage to airships in wide coverage shots, camera pans across damaged ships, focus shifts to single undamaged ship becoming focal point.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Camera pans across damaged gray airships, smoke rising from hull breaches, Green Martian warriors observing from building windows, daylight with fire glow, focus shifts to single undamaged ship, visible motion of camera movement.

# Negative Prompt
blurry, morphing, extra limbs, wrong colors, static image, distorted faces, missing smoke, incorrect lighting, crew on unmanned ship, sudden appearance of people, green skin tone drift, gray paint color shift.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5.0
- required_refs: Hull breaches visible, smoke rising from damaged ships, one ship remains unmanned
- optional_refs: Window frame
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/Medium
- continuity_mode: insert
- starting_keyframe_strategy: pan_across
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain ship damage progression consistency
- Preserve daylight with fire illumination
- Keep Martians positioned at building windows

# Repair Notes
- Ensure Martians remain green skin tone
- Ships remain gray paint
- No sudden appearance of crew on drifting vessel

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
