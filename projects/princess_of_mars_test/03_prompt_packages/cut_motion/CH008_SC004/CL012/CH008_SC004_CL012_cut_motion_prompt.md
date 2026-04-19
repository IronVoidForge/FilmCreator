# Title
CH008_SC004 CL012 Cut Motion Prompt

# ID
CH008_SC004_CL012_cut_motion_prompt

# Purpose
Generate cut motion content for over-the-shoulder observer shot showing warriors returning to plaza after battle conclusion, maintaining keyframe lighting and grade while depicting visible movement of group toward city entrance.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Over-the-shoulder perspective of green-skinned warriors walking toward city plaza entrance, smoke drifting from burning vessel in valley background, daylight illumination consistent with keyframe, camera stationary observing group movement, diminishing flames visible in distance, loot carried on shoulders, atmospheric haze clearing slightly

# Negative Prompt
morphing faces, sudden lighting changes, extra limbs, distorted anatomy, static background when motion expected, incorrect character skin tone, blurry text, watermark, noise, flickering, vessel exploding prematurely, green martian females appearing

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL012
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: john_carter, green_martian_warriors
- look_continuity_policy: preserve_keyframe_lighting
- intended_lighting_change: none
- composition_type: over-the-shoulder
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: false
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: anatomy_and_texture
- anatomy_repair_policy: strict
- consistency_targets: green_skin_tone, smoke_density, vessel_position
- style_profile: cinematic_action
- batch_role: observer_perspective
- fix_of: null

# Continuity Notes
- Maintain keyframe lighting and grade by default for cut motion stage.
- Ensure green skin tone of warriors remains consistent with previous frames.
- Smoke density should decrease gradually without disappearing instantly.
- Carter remains stationary observer throughout beat, partial view of warriors moving toward plaza.
- Vessel lightened by loot removal visible in background context.

# Repair Notes
- If vessel appears too bright, reduce flame intensity to match keyframe grade.
- If warriors stop moving, add subtle weight shift or path continuation.
- If smoke clears too fast, increase atmospheric haze density slightly.
- Ensure no green martian females appear in this observer shot.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL012.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
