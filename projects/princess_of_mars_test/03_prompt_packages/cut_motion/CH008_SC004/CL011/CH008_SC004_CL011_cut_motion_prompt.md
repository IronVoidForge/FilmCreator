# Title
CH008_SC004 CL011 Cut Motion Prompt

# ID
CH008_SC004_CL011_cut_motion_prompt

# Purpose
Generate cut motion video for CL011 within BT003, transitioning from keyframe to interval beats while maintaining lighting and grade. Focus on warrior movement carrying loot, smoke clearing in valley air, and flames diminishing to background elements over 5 seconds. Ensure camera behavior supports close-up detail focus without breaking continuity with previous clips.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian warrior carrying small loot items walking forward close-up detail daylight smoke drifting in air valley floor visible distant hills flames reduced to background elements warrior skin green ornaments visible arms moving slightly loot containers shifting weight walking towards plaza entrance smoke clearing significantly battle aftermath acknowledged group

# Negative Prompt
static image blurry low resolution morphing faces extra limbs wrong skin tone exploding vessel unexpected debris static camera motion glitch high contrast shadows incorrect lighting grade face distortion anatomy error background noise overexposed underexposed

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL011
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Warriors: Some carrying weapons, others with empty hands, Loot: Visible on some warriors (small items, containers)
- look_continuity_policy: strict
- intended_lighting_change: preserve_keyframe_grade
- composition_type: Close-up (detail)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: none
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: action_oriented_awe_inspiring
- batch_role: test_clip_3
- fix_of: 

# Continuity Notes
- Preserve keyframe lighting and grade by default throughout motion generation.
- Ensure smoke clearing progresses from 2.5s mark to 5s mark without disappearing instantly.
- Maintain warrior skin tone as green with ornaments visible on shoulders or chest.
- Keep loot visibility consistent (small items, containers) on warriors carrying them.
- Environment geography must remain valley floor with distant hills beyond city buildings.
- Camera behavior should support close-up detail focus without drifting to wide shots unexpectedly.

# Repair Notes
- If motion is too jerky, smooth out warrior walking animation for natural flow.
- Adjust smoke density if it clears too fast at 2.5s mark; slow down clearing rate.
- Ensure flames do not reappear or intensify beyond background element status by 5s.
- Check for morphing between warrior and other characters (e.g., Green Martian females) in background.
- Verify lighting consistency with previous clips in BT003 sequence to avoid grade shifts.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL011.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
