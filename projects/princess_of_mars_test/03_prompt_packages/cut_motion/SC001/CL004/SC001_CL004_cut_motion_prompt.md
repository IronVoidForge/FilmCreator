# Title
SC001 CL004 Cut Motion Prompt

# ID
SC001_CL004_cut_motion_prompt

# Purpose
Generate cut motion video for human male warrior observing approaching alien fleet from window, transitioning from mid-distance to plaza level with rising tension

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot human male warrior standing at dark wood window frame, hands moving from sill to chest position, weight shifting forward toward glass, outside view shows gray airships descending toward plaza street level, green-skinned alien warriors visible in distant fleet formation, midday sunlight reflecting off ship devices, camera slight push-in on warrior reaction, atmosphere tense anticipation, smoke and flame visible in background valley

# Negative Prompt
morphing faces, flickering lights, extra limbs, distorted anatomy, sudden jumps, static image, wrong character count, blurry text, inconsistent lighting, background shifting, glitchy movement, incorrect character identity, interior corridor space, female figure entrance, empty room transition

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: Beat BT004.md, Scene Summary, Chapter Summary daylight conditions
- optional_refs: Medium shot warrior + fleet in frame, POV from warrior looking at approaching ships
- visible_character_assets: human male warrior, green-skinned alien warriors, gray airships
- look_continuity_policy: Midday Light Established - Midday light fully established by end of beat
- intended_lighting_change: soft morning light transitioning to bright midday
- composition_type: medium_shot_to_close_up
- continuity_mode: cutaway
- starting_keyframe_strategy: Fleet at mid-distance, human male warrior maintaining observation posture with neutral expression
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
- Ensure fleet entrance is deliberate not glitchy
- Maintain character consistency with previous clips in scene
- Keep warrior and window positioning stable during motion

# Repair Notes
- If fleet appears too fast, slow motion slightly
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
