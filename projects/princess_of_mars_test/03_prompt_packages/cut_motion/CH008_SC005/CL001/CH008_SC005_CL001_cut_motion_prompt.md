# Title
CH008_SC005 CL001 Cut Motion Prompt

# ID
CH008_SC005_CL001_cut_motion_prompt

# Purpose
Establish wide shot exterior corridor motion where humanoid figure enters left edge moving right towards stationary observer center-right, increasing speed as distance decreases, daylight with smoke haze, building entrance threshold, urgent approach trajectory, static camera hold for 5 seconds before cut.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot exterior corridor, humanoid figure entering left edge moving right towards stationary observer center-right, speed increasing as distance decreases, daylight with smoke haze, building entrance threshold, urgent approach trajectory, static camera hold, visible motion blur on approaching figure, ambient fire smoke drifting slowly.

# Negative Prompt
static image, morphing faces, wrong character count, sudden camera zoom, dark lighting, fire explosion, blurry background, incorrect speed trajectory, extra limbs, distorted anatomy, low resolution, flickering.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md Start State
- optional_refs: None
- visible_character_assets: Sola (full body), Carter (center-right, partial profile)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: preserve_keyframe_grade
- composition_type: Wide shot, exterior corridor threshold
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Static wide frame, Sola entering from left edge of frame
- dependency_policy: No dependencies; standalone establishing shot
- auto_advance_policy: None
- fallback_strategy: If Sola entry is unclear, tighten to medium wide and emphasize movement path
- consistency_assist_policy: Preserve character identity and spatial axis
- consistency_assist_method: Frame alignment with keyframe reference
- anatomy_repair_policy: Enable for motion continuity
- consistency_targets: Sola trajectory, Carter position, lighting grade
- style_profile: Barsoom cinematic daylight
- batch_role: establishing_motion
- fix_of: None

# Continuity Notes
- Capture the continuity rules for this stage. Maintain humanoid figure diagonal path from left to center-right throughout clip duration. Keep stationary observer in center-right profile view without significant movement until approaching figure arrives. Preserve daylight lighting conditions and smoke haze density from keyframe reference. Ensure camera remains static wide shot, no zoom or pan during motion sequence. Match fire smoke drift direction and intensity to established environment state.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If approaching figure speed appears too slow, increase motion blur intensity in prompt. If character identity shifts, reinforce descriptive noun phrases for humanoid figure and observer. If lighting darkens unexpectedly, add daylight and smoke haze descriptors back to positive prompt. If camera moves unexpectedly, enforce static camera hold instruction in negative prompt.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
