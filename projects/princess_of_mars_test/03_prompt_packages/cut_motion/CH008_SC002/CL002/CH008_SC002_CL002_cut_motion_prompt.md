# Title
CH008_SC002 CL002 Cut Motion Prompt

# ID
CH008_SC002_CL002_cut_motion_prompt

# Purpose
Execute cut motion for weapon discharge close-up. Maintain static camera with slight zoom on discharge moment. Focus on hands/weapon mechanics and smoke effects.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green warrior hands holding firearm, medium close-up, tension build in grip, muzzle flash discharge, smoke explosion initiation, impact points below, banners dissolving in flame, green skin texture visible, downward line of sight to valley floor, static elevated perspective, cinematic lighting, high detail on weapon mechanics.

# Negative Prompt
human face visible, wrong lighting grade, blurry motion, incorrect bullet trajectory, missing smoke effects, distorted anatomy, low resolution, color shift, banner damage inconsistency.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Close-up weapon discharge coverage families
- visible_character_assets: Green Warriors, Smoke effects
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: 
- composition_type: Medium close-up
- continuity_mode: Close-up detail work
- starting_keyframe_strategy: Open on weapon already positioned
- dependency_policy: Soft dependency on CL001
- auto_advance_policy: N/A
- fallback_strategy: Use insert if need to emphasize discharge timing
- consistency_assist_policy: Preserve keyframe lighting and grade by default
- consistency_assist_method: 
- anatomy_repair_policy: Maintain green skin texture consistency
- consistency_targets: 
- style_profile: A Princess of Mars Chapter VIII
- batch_role: Action detail work
- fix_of: 

# Continuity Notes
- Bullet drops at explosion points (timing and placement consistency)
- Banners dissolving in flame (progressive damage tracking)

# Repair Notes
- Maintain green skin texture consistency
- Preserve keyframe lighting and grade by default

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
