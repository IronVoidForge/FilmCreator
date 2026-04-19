# Title
CH008_SC004 CL010 Cut Motion Prompt

# ID
CH008_SC004_CL010_cut_motion_prompt

# Purpose
Establishing wide shot of green warriors converging at plaza entrance after battle conclusion. Capture motion of group gathering, smoke clearing from environment, and camera behavior maintaining keyframe lighting grade for transition to next scene.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot of green warriors moving from multiple points toward plaza center, converging paths from roofs and valley floor, loot consolidated or being carried in hands, smoke clearing significantly from battle aftermath, daylight horizon with distant hills, diminished fire glow on building surfaces, vertical axis from upper floors down to open ground, camera positioned at plaza entrance looking outward, clean plaza surface without debris.

# Negative Prompt
distorted anatomy, extra limbs, missing weapons, wrong skin tone, dark shadows, night time, explosion, debris on clean plaza, blurry motion, morphing faces, text, watermark, sudden lighting shift, teleportation of characters.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL010
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: preserve_keyframe_lighting
- composition_type: Wide shot (establishing)
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
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain daylight consistency with smoke clearing gradually.
- Ensure warriors converge smoothly without teleportation or abrupt movement.
- Preserve keyframe lighting grade to match approved opening frame.
- Keep plaza surface clean of debris from battle impacts.
- Focus on visible motion and environment change for cut_motion stage.

# Repair Notes
- If motion is too jerky, smooth camera behavior during convergence.
- If lighting shifts to night or dark shadows, revert to daylight horizon.
- Ensure loot items are visible but not overwhelming the main action.
- Fix any morphing faces or distorted anatomy immediately.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL010.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
