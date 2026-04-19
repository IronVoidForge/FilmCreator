# Title
CH008_SC004 CL006 Cut Motion Prompt

# ID
CH008_SC004_CL006_cut_motion_prompt

# Purpose
Generate cut motion video for CL006, maintaining warrior observation stance and vessel drift continuity from opening frame. Bridge the interval beats (maintain positions, weight shift, vessel movement) while preserving keyframe lighting and grade by default. Focus on visible motion of vessel drifting and subtle camera/subject behavior adjustments.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot of green-skinned warriors on building roofs watching a burning gray vessel drift across valley floor. Slight weight shift forward for better view. Smoke plume rising, flames spurt from hull. Daylight setting. Horizontal movement following vessel drift path from center toward right side.

# Negative Prompt
Static image, morphing faces, extra limbs, sudden lighting change, vessel explosion, smoke disappearing, wrong composition close-up, blurry text, distorted anatomy, vertical camera tilt, incorrect color grading.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL006
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium shot (reaction shots)
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
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default.
- Vessel drifts from center to right side of frame over duration.
- Warriors maintain observation positions with slight weight shift at 2.5s interval.
- Horizontal axis follows vessel's drift path across valley.
- Eyelines directed at vessel's position and smoke trail.

# Repair Notes
- Apply anatomy repair policy for warrior figures to ensure consistency.
- Ensure style profile matches Barsoom aesthetic (green skin, gray vessels).
- Check for unintended morphing during vessel drift motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
