# Title
CH008_SC002 CL002 Cut Motion Prompt

# ID
CH008_SC002_CL002_cut_motion_prompt

# Purpose
Execute Martian volley fire sequence from building window perspective with camera cuts between shooter POV and target impact on airship hulls.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian warriors at multi-story building windows, rifle muzzle flashes illuminating dark interior, gray projectiles arcing through valley air toward distant airships, smoke rising from damaged ship hulls, narrator observing from window frame, daylight lighting shifting to fire glow on muzzle, medium shot composition, dynamic camera movement following projectile trajectory.

# Negative Prompt
static image, morphing faces, extra limbs, wrong number of ships, missing muzzle flash, distorted projectiles, darkened sky, incorrect lighting grade, blurry text, low resolution, anatomical errors, green skin fading to normal human skin, ship hulls melting, floating debris without cause.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL002
- duration_seconds: 5.0
- required_refs: Muzzle flashes, projectile impacts on ship hulls
- optional_refs: Window frame
- visible_character_assets: Martians at building windows (active), Narrator observing from window
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: 
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: pan_in
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
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain window POV consistency throughout sequence
- Ensure projectile trajectory matches previous frames
- Match muzzle flash timing with sound cues if applicable
- Preserve approved keyframe lighting and grade by default

# Repair Notes
- Fix anatomy if Martians look human
- Ensure ship damage is consistent with BT001/BT002 progression
- Correct lighting grade to match approved keyframe
- Verify projectile count matches visual continuity requirements

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
