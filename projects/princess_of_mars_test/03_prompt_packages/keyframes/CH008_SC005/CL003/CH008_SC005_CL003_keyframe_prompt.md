# Title
CH008_SC005 CL003 Keyframe Prompt

# ID
CH008_SC005_CL003_keyframe_prompt

# Purpose
Establish static medium close-up keyframe capturing urgent female figure with light reddish copper skin and coal black hair, showing emotional intensity and facial expression continuity from previous spatial context where all three parties positioned for gaze exchange.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Medium close-up shot of slender girlish figure with light reddish copper skin tone, large lustrous eyes focused forward, coal black hair waving loosely into strange coiffure, upper body visible, daylight lighting with smoke haze from battle effects, high emotional intensity, static composition, detailed facial features showing finely chiseled expression, expressive eyes conveying appeal signal, cinematic quality, sharp focus on face and eyes.

# Negative Prompt
Motion blur, low resolution, distorted features, wrong character identity, background clutter, low contrast, flat lighting, expressionless face, extreme wide shot, proper nouns, text overlay, watermark, noise, grainy texture, green skin tone, motion artifacts, extreme close-up on eyes only.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: slender girlish figure with light reddish copper skin (face, eyes, upper body)
- look_continuity_policy: Maintain eye line consistency with male observer in adjacent shots
- intended_lighting_change: daylight conditions with smoke haze from battle effects
- composition_type: Medium close-up
- continuity_mode: insert
- starting_keyframe_strategy: Static medium close frame on face showing urgency in expression
- dependency_policy: Depends on CL002 establishing spatial context; no reverse dependency
- auto_advance_policy: None
- fallback_strategy: If facial expression unclear, tighten to extreme close-up on eyes or widen slightly to include more context
- consistency_assist_policy: Apply anatomy repair policy to ensure facial feature integrity
- consistency_assist_method: Use consistency assist method to match previous spatial context
- anatomy_repair_policy: Verify no proper nouns appear in generated text overlays
- consistency_targets: Facial expression urgency without introducing motion artifacts
- style_profile: cinematic_compositional
- batch_role: keyframe
- fix_of: None
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Capture the continuity rules for this stage.
- Maintain eye line consistency with male observer in adjacent shots.
- Ensure lighting matches daylight conditions with smoke haze from battle effects.
- Preserve facial expression urgency without introducing motion artifacts.
- Verify character positioning affects subsequent scene emotional beats.
- Multi-directional gaze exchange between all parties requires clear eyeline tracking for coverage planning.

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- Apply anatomy repair policy to ensure facial feature integrity.
- Use consistency assist method to match previous spatial context.
- Verify no proper nouns appear in generated text overlays.
- Check that skin tone matches light reddish copper rather than green.
- Ensure hair appears coal black and waving loosely into strange coiffure.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
