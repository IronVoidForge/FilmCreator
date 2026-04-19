# Title
CH008_SC002 CL005 Cut Motion Prompt

# ID
CH008_SC002_CL005_cut_motion_prompt

# Purpose
Depict close-up of weapon muzzle flash from Martian Fleet ship firing counter-battery volley. Camera captures intensity of discharge and recoil. Cut motion matches return vector to previous angle.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian fleet automated weapon systems on damaged gray airship hull, muzzle flash burst visible, smoke trails rising, valley floor below, daylight lighting preserved, camera following weapon discharge trajectory, close-up shot composition.

# Negative Prompt
boarding sequence visible, crew resistance, wrong number of ships, incorrect lighting shift, anatomical errors, extra limbs, morphing faces, fire illumination before discharge complete, drifting warship without weapon discharge.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: Unmanned airship hull, weapon barrel visible, smoke trails rising
- optional_refs: Window frame
- visible_character_assets: Weapon barrel, muzzle flash, smoke
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static on weapon muzzle
- dependency_policy: parallel to medium shot for coverage
- auto_advance_policy: 
- fallback_strategy: cutaway to fire arcs if flash timing varies
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain the unmanned status of the target airship.
- Ensure weapon discharge is consistent with unmanned status.
- Preserve daylight lighting and keyframe grade as per stage guidance.
- Do not introduce new damage to the ship hull beyond what was established in previous beats.

# Repair Notes
- If weapon discharge fails to appear, adjust camera trajectory to show muzzle flash clearly.
- If lighting shifts significantly from keyframe grade, revert to approved lighting parameters.
- If extra crew members appear on deck, remove them via inpainting or prompt adjustment.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
