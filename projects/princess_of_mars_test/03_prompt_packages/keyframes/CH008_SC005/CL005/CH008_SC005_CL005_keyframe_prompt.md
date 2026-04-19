# Title
CH008_SC005 CL005 Keyframe Prompt

# ID
CH008_SC005_CL005_keyframe_prompt

# Purpose
Establish emotional anchor through gaze exchange between human male, companion, and prisoner; show human male reaction to prisoner state while maintaining background movement context. Static frame capturing the tension of connection amidst conflict.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide shot, human male face in foreground center-right, eyes focused on slender female figure in background moving right to left, companion figure present near human male (left side), female figure partially obscured by building entrance threshold, daylight with smoke haze from fire impact, urban structure background with upper floors visible, intense gaze, concern expression, frozen still moment, cinematic lighting, depth of field, exterior corridor threshold, light reddish copper skin tone on female figure, coal black hair.

# Negative Prompt
blurry, distorted face, extra limbs, wrong number of fingers, text, watermark, signature, low resolution, noisy, cartoonish, 3d render, painting, sketch, deformed hands, bad anatomy, missing eyes, closed eyes, bright sunlight, dark shadows, overexposed, underexposed, green skin (unless intended for specific character), uniform lighting.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT003, CH008_SC005/BT003.md Start State
- optional_refs: None
- visible_character_assets: human male face and upper body, slender female figure background partial visibility, companion figure
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight with smoke haze
- composition_type: Wide three-shot, all parties visual connection visible
- continuity_mode: emotional anchor continuity
- starting_keyframe_strategy: Establish all three characters within visual range of each other
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
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- reblock_same_scene mode ensures visual consistency with previous clips in sequence.
- Focus remains on eye contact between foreground observer and background subject.
- Background action (dragging) must remain visible but secondary to facial reaction.
- Lighting must match daylight with smoke haze from fire context.
- Companion figure presence ensures three-shot composition matches clip plan.

# Repair Notes
- If eye contact unclear, tighten to close-up on human male eyes or widen to show more of female figure expression.
- Ensure background movement direction matches scene axis (right to left).
- Verify lighting consistency with daylight and smoke haze from fire context.
- Check skin tone accuracy for female figure (light reddish copper).
- Confirm companion figure visibility if required by wide three-shot composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
