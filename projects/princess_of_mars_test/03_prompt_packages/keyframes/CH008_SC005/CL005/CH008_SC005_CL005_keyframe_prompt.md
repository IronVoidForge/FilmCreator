# Title
CH008_SC005 CL005 Keyframe Prompt

# ID
CH008_SC005_CL005_keyframe_prompt

# Purpose
Establish emotional anchor through eye contact; show human male reaction to prisoner state. Static frame showing human male face locked on slender female figure background movement.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Medium shot, human male face in foreground, eyes focused on slender female figure in background, female figure moving right to left, being dragged into building entrance, daylight, smoke haze, urban structure background, intense gaze, concern expression, frozen still moment, cinematic lighting, depth of field, exterior corridor threshold.

# Negative Prompt
blurry, distorted face, extra limbs, wrong number of fingers, text, watermark, signature, low resolution, noisy, cartoonish, 3d render, painting, sketch, deformed hands, bad anatomy, missing eyes, closed eyes, bright sunlight, dark shadows, overexposed, underexposed.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT003, CH008_SC005/BT003.md Start State
- optional_refs: None
- visible_character_assets: human male face and upper body, slender female figure background partial visibility
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium shot, both human male and female figure in frame for eye contact
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Static frame showing human male face locked on female figure background movement
- dependency_policy: Depends on CL004 establishing conflict context; no reverse dependency
- auto_advance_policy: 
- fallback_strategy: If eye contact unclear, tighten to close-up on human male eyes or widen to show more of female figure expression
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage.
- reblock_same_scene mode ensures visual consistency with previous clips in sequence.
- Focus remains on eye contact between foreground observer and background subject.
- Background action (dragging) must remain visible but secondary to facial reaction.

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- If eye contact unclear, tighten to close-up on human male eyes or widen to show more of female figure expression.
- Ensure background movement direction matches scene axis (right to left).
- Verify lighting consistency with daylight and smoke haze from fire context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
