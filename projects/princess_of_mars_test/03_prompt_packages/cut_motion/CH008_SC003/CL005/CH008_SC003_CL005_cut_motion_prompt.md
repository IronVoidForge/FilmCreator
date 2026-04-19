# Title
CH008_SC003 CL005 Cut Motion Prompt

# ID
CH008_SC003_CL005_cut_motion_prompt

# Purpose
Smooth action follow removal of valuables from disabled airship interior. Preserve keyframe lighting and grade by default. Focus on visible motion, camera behavior, and environment change. Track food containers and water carboys for continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green-skinned Martian hands removing food containers and water carboys from disabled gray airship interior. Dead sailors stationary in background. Soft ambient lighting consistent with previous frame. Smooth camera follow motion. No sudden cuts.

# Negative Prompt
Distorted anatomy, extra limbs, wrong skin tone, bright flash, dark shadows inconsistent with keyframe, sudden jump cut, floating objects, blurry focus.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (hands), Dead Sailors (stationary)
- look_continuity_policy: preserve keyframe lighting and grade by default
- intended_lighting_change: none
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: open on specific item removal detail
- dependency_policy: depends on CL004
- auto_advance_policy: smooth action follow removal
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: fix hands if distorted
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain lighting grade from approved keyframe. Track item removal sequence strictly. Keep dead sailors static in position. Ensure camera motion follows action smoothly without jitter.

# Repair Notes
- Fix anatomy if hands look wrong or fingers merge. Ensure lighting matches keyframe exactly. Correct any sudden brightness shifts.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
