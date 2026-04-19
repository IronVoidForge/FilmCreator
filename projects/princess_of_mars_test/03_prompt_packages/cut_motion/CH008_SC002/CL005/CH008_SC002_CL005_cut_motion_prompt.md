# Title
CH008_SC002 CL005 Cut Motion Prompt

# ID
CH008_SC002_CL005_cut_motion_prompt

# Purpose
Execute tactical boarding sequence with close-ups and medium shots of Martians moving onto ship. Camera follows boarding trajectory from window to ship; cuts between wide boarding shots and close-ups of individual Martians.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian warriors transitioning from building windows to unmanned gray airship deck, boarding equipment deployed, ship hull intact but vulnerable, Martians moving across ship deck, camera following boarding trajectory from window perspective, cuts between wide shot of boarding action and medium shot of Martians on ship, loot items visible in storage areas, valley floor below, daylight lighting preserved.

# Negative Prompt
crew resistance visible, damaged hull inconsistent with previous beats, wrong number of ships, incorrect lighting shift, anatomical errors, extra limbs, morphing faces, crew members on deck, fire illumination before boarding complete, drifting warship without Martians.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: Ship deck accessible, boarding equipment deployed, no crew resistance visible
- optional_refs: Window frame
- visible_character_assets: Martians transitioning from windows to ship deck; Narrator observing boarding action
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: 
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: track_forward
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
- Maintain the unmanned status of the target airship.
- Ensure Martians are shown moving from window positions to ship deck without gaps.
- Preserve daylight lighting and keyframe grade as per stage guidance.
- Do not introduce new damage to the ship hull beyond what was established in BT003/BT004.

# Repair Notes
- If Martians fail to reach the ship, adjust camera trajectory to show successful boarding.
- If lighting shifts significantly from keyframe grade, revert to approved lighting parameters.
- If extra crew members appear on deck, remove them via inpainting or prompt adjustment.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
