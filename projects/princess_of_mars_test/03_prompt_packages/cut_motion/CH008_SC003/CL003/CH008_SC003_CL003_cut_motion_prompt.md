# Title
CH008_SC003 CL003 Cut Motion Prompt

# ID
CH008_SC003_CL003_cut_motion_prompt

# Purpose
Fill in the stage intent here.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Close-up view of green warrior hands releasing grappling hook mechanism, smooth deployment action following previous boarding sequence, ship drifting southeast in background, urban Martian architecture visible through window, natural daylight lighting preserved, cinematic color grade maintained, water surface reflecting hull movement, smoke beginning to rise from disabled vessel, atmospheric depth consistent with scene.

# Negative Prompt
static image, no motion blur, hook stuck, ship stationary, wrong lighting, distorted anatomy, extra characters, sudden cuts, flickering, low resolution, inconsistent color grade, floating objects, unnatural shadows.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (hands), Martians (observation)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: open on hook deployment action
- dependency_policy: depends on CL002
- auto_advance_policy: 
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain ship drift vector southeast throughout motion sequence.
- Ensure hook release matches previous deployment action from CL002.
- Keep lighting consistent with scene daylight and urban environment.
- Preserve urban Martian architecture background visibility.
- Match atmospheric smoke density to disabled vessel state.

# Repair Notes
- If motion is too slow, increase action intensity in prompt.
- If anatomy looks distorted on hands, apply repair policy for limbs.
- Ensure no sudden jump cuts between frames during deployment.
- Check consistency of ship drift direction against previous clip.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
