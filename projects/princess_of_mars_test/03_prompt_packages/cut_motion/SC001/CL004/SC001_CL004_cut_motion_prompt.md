# Title
SC001 CL004 Cut Motion Prompt

# ID
SC001_CL004_cut_motion_prompt

# Purpose
Generate cut motion video for Sola's entrance moment in interior corridor space, transitioning from empty to populated.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot interior corridor space initially empty then female figure enters deliberately from doorway moving toward observer and hound, camera holds steady then slight push to close-up on observer reaction, lighting warm sunlight consistent with previous frame, atmosphere tense quiet

# Negative Prompt
morphing faces, flickering lights, extra limbs, distorted anatomy, sudden jumps, static image, wrong character count, blurry text, inconsistent lighting, background shifting, glitchy movement, incorrect character identity

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot_to_close_up
- continuity_mode: cutaway
- starting_keyframe_strategy: empty_interior_space
- dependency_policy: dependent_on_previous_clip
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
- Match keyframe lighting and grade by default
- Preserve interior shadows and depth cues from opening frame
- Ensure female figure entrance is deliberate not glitchy
- Maintain character consistency with previous clips in scene
- Keep observer and hound positioning stable during motion

# Repair Notes
- If female figure appears too fast, slow motion slightly
- If lighting shifts, revert to base grade from keyframe
- If anatomy distorts on entrance, regenerate with stricter constraints
- If camera push is too abrupt, smooth out transition

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
