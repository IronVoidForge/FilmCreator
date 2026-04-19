# Title
CH008_SC004 CL009 Cut Motion Prompt

# ID
CH008_SC004_CL009_cut_motion_prompt

# Purpose
Bridge the battle conclusion with the return to plaza, maintaining visual continuity of warriors moving from scattered positions to the gathering point while preserving the post-battle atmosphere.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green warriors walking across rooftops and valley floor, smoke drifting in daylight haze, loot visible on shoulders, converging paths toward plaza entrance, fading flames in distance, medium shot movement, daylight lighting preserved.

# Negative Prompt
morphing faces, flickering fire artifacts, disappearing limbs, wrong character count, style drift to dark or light, background instability, extra smoke plumes, incorrect skin tone.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL009
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Warriors scattered across roofs and valley floor, some warriors carrying loot from vessel
- look_continuity_policy: 
- intended_lighting_change: preserve_keyframe_lighting_and_grade
- composition_type: Medium shot (movement)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain daylight lighting with smoke haze consistency across frames.
- Ensure Green warrior skin tone and ornament details remain stable during motion.
- Track environment state changes: smoke clearing from immediate area, flames diminishing in distance.
- Preserve converging motion paths from roofs and valley floor toward plaza center.

# Repair Notes
- Apply anatomy repair policy for limbs moving across rooftops to prevent distortion.
- Enforce style consistency targets to maintain Barsoom aesthetic during cut motion.
- Use artifact removal guidance for flickering smoke or fire effects that do not match keyframe lighting.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL009.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
