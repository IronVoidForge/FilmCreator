# Title
CH008_SC005 CL005 Cut Motion Prompt

# ID
CH008_SC005_CL005_cut_motion_prompt

# Purpose
Establish emotional anchor through eye contact; show observer's reaction to captive's state. Cut from background action to this reaction shot.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot of observer face and upper body, eyes focused on captive figure in background right, micro-expression shift showing concern, daylight lighting with smoke haze, city building exterior corridor, static camera slight breathing movement, cinematic Barsoom style.

# Negative Prompt
distorted faces, extra limbs, wrong character identities, sudden camera zooms, flickering lighting, blurry details, text, watermarks, green screen, cartoonish.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT003, CH008_SC005/BT003.md Start State
- optional_refs: None
- visible_character_assets: observer face and upper body, captive figure background partial visibility
- look_continuity_policy: match keyframe lighting and grade by default
- intended_lighting_change: none
- composition_type: medium shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static frame showing observer's face locked on captive's background movement
- dependency_policy: depends on CL004 establishing conflict context; no reverse dependency
- auto_advance_policy: prepare scene transition at 3s
- fallback_strategy: tighten to close-up on observer's eyes or widen to show more of captive's expression
- consistency_assist_policy: maintain eye contact direction
- consistency_assist_method: gaze vector preservation
- anatomy_repair_policy: preserve facial features during motion
- consistency_targets: observer face, captive figure silhouette
- style_profile: cinematic action drama
- batch_role: final clip emotional anchor
- fix_of: None

# Continuity Notes
- Capture the continuity rules for this stage. Match keyframe lighting and grade by default. Preserve eye contact direction between observer and captive figure. Maintain medium shot composition without sudden zooms. Ensure smoke haze remains consistent with background fire effects.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If motion is too fast, reduce scale of micro-expressions. If faces blur during breathing movement, increase focus strength on observer's eyes. If lighting shifts, revert to keyframe daylight settings.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
