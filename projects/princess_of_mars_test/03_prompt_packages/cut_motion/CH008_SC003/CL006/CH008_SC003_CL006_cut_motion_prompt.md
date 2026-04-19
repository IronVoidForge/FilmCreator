# Title
CH008_SC003 CL006 Cut Motion Prompt

# ID
CH008_SC003_CL006_cut_motion_prompt

# Purpose
Fill in the stage intent for CL006 cut motion. Show simultaneous looting operations on main deck with smooth movement across ship interior.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
green-skinned warriors moving through ship cargo holds, removing objects like arms and silks, lifeless bodies in background, gray hull interior, smooth movement across deck, multiple figures working simultaneously, items being carried away, carboy dumping visible

# Negative Prompt
distorted anatomy, extra limbs, wrong skin tone, static image, flickering, blurry motion, incorrect lighting, sudden cuts, missing objects, floating elements

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (multiple), Dead Sailors (clusters)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on main deck with multiple Martians
- dependency_policy: none
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
- Maintain lighting and grade from approved keyframe. Ensure green skin tone consistency. Keep ship structure static except for minor drift. Match interval beats for aft to forward sections and carboy dumping point.

# Repair Notes
- If anatomy is unclear, apply style profile. If motion is jerky, smooth trajectory. Correct any color bleeding on green skin. Ensure dead sailors remain stationary.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
