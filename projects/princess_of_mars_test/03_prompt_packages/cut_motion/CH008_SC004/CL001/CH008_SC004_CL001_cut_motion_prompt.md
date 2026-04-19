# Title
CH008_SC004 CL001 Cut Motion Prompt

# ID
CH008_SC004_CL001_cut_motion_prompt

# Purpose
Establish visible motion of Green-skinned warrior preparing missile on roof level, maintaining continuity with scene lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green-skinned warrior front-facing holding missile ready, roof surface partial view, daylight smoke rising, slight weight shift for stability, camera stable medium shot, green skin ornaments visible, daylight atmosphere

# Negative Prompt
morphing anatomy, extra limbs, sudden camera movement, blurry motion, wrong lighting, dark shadows, incorrect skin tone, floating objects, morphing weapons

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Green Warrior (front-facing, holding missile)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain Green-skinned warrior skin tone and ornament consistency.
- Preserve roof surface texture and smoke density.
- Ensure weight shift is subtle and stable.

# Repair Notes
- If anatomy drifts, correct to standard Green-skinned warrior structure.
- If lighting shifts, revert to keyframe grade.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
