# Title
CH008_SC005 CL002 Cut Motion Prompt

# ID
CH008_SC005_CL002_cut_motion_prompt

# Purpose
Fill in the stage intent here. Transition from wide establishing shot to tighter medium two-shot as approaching companion reaches proximity, maintaining spatial context and lighting continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium two shot, over the shoulder view, stationary observer shoulder profile foreground left, approaching companion full face upper body moving diagonally from background right, daylight illumination, building exterior corridor entrance threshold, smoke haze distant hills visible horizon, intimate perspective, cinematic lighting grade consistent with previous clip.

# Negative Prompt
static image, single shot, wide angle, distorted faces, extra limbs, morphing characters, inconsistent lighting, blurry motion, low resolution, dark shadows, indoor artificial light, green screen background.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: Carter (shoulder/back profile), Sola (full face and upper body)
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Medium two shot, over-the-shoulder from Carter's perspective
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: Shoulder of Carter in foreground left, Sola approaching from background right
- dependency_policy: Depends on CL001 establishing spatial context; no reverse dependency
- auto_advance_policy: None
- fallback_strategy: If shoulder framing is unclear, shift to medium shot with both characters fully visible
- consistency_assist_policy: None
- consistency_assist_method: None
- anatomy_repair_policy: None
- consistency_targets: None
- style_profile: Action-oriented, awe-inspiring, daylight haze
- batch_role: cut_motion
- fix_of: None

# Continuity Notes
- Lighting must match previous clip keyframe exactly to maintain visual continuity.
- Character count and identity must remain consistent with established assets.
- Motion flow should reflect approaching trajectory without sudden jumps in position.
- Background environment (corridor/plaza threshold) must stay stable during motion.

# Repair Notes
- If anatomy appears distorted, apply repair to match canonical character structure.
- If lighting shifts unexpectedly, revert to base keyframe illumination values.
- Ensure no morphing occurs between the stationary observer and approaching figure.
- Check for any artifacts from the cut transition and smooth them out if visible.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
