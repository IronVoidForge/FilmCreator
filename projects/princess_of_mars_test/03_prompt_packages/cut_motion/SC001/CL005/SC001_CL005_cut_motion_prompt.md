# Title
SC001 CL005 Cut Motion Prompt

# ID
SC001_CL005_cut_motion_prompt

# Purpose
Generate cut motion for clip CL005 in scene SC001, continuing from approved opening frame with preserved lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Motion continues from previous frame. Camera pans slightly right following narrator gaze towards window view. Green-skinned warriors visible in distance valley. Smoke rises gently. Lighting preserved with sunlight and fire glow.

# Negative Prompt
morphing faces, flickering lights, wrong color grade, extra limbs, distorted anatomy, sudden lighting changes, blurry textures

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: 
- continuity_mode: 
- starting_keyframe_strategy: 
- dependency_policy: 
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
- Maintain keyframe lighting and grade by default
- Preserve narrator position relative to window
- Keep green-skinned warriors consistent in distance
- Ensure smoke movement is natural and not glitchy

# Repair Notes
- Fix any lighting leaks from exterior view
- Correct anatomy if characters morph during motion
- Ensure camera movement matches approved frame trajectory

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
