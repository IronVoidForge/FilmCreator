# Title
CH008_SC005 CL005 Fix 01 Prompt

# ID
CH008_SC005_CL005_fix_01_prompt

# Purpose
Corrective pass for CL005 (Eye Contact & Reaction) to ensure emotional connection between observer and captive is clear, fixing local artifacts while maintaining established Barsoom aesthetic. Preserve composition and look while fixing local issues. Assume image_1 is the approved still base and image_2 is a secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium shot, human male observer face locked on background captive movement, exterior corridor daylight, smoke from fire, Martian city buildings upper floors, open ground plaza, valley hills beyond, action-oriented tone, awe-inspiring atmosphere, tense during combat sequences, light reddish copper skin features, coal black hair waving, highly wrought ornaments, crimson cheeks, ruby lips, observer face and upper body visible, captive background partial visibility

# Negative Prompt
blurry, distorted face, extra fingers, missing eyes, text, watermark, signature, low resolution, bad anatomy, morphed hands, inconsistent lighting, wrong skin tone, extra limbs, facial distortion, low quality, jpeg artifacts, noise, grain, overexposed, underexposed

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL005
- duration_seconds: 5s
- required_refs: CH008_SC005/BEAT_INDEX.md BT003, CH008_SC005/BT003.md Start State
- optional_refs: None
- visible_character_assets: Carter (face and upper body), Prisoner (background, partial visibility)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight smoke from fire
- composition_type: Medium shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Static frame showing Carter's face locked on prisoner's background movement
- dependency_policy: Depends on CL004 establishing conflict context; no reverse dependency
- auto_advance_policy: None
- fallback_strategy: If eye contact unclear, tighten to close-up on Carter's eyes or widen to show more of prisoner's expression
- consistency_assist_policy: Preserve composition and look while fixing local issues
- consistency_assist_method: still_fix
- anatomy_repair_policy: Fix local artifacts only
- consistency_targets: Eye contact clarity
- style_profile: Barsoom aesthetic
- batch_role: clip_prompt
- fix_of: CL005
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Preserve composition and look while fixing local issues. Assume image_1 is the approved still base and image_2 is a secondary reference when needed. Use descriptive noun phrases and avoid proper nouns in prompt text. Keep duration and workflow metadata in inputs_markdown, not in the prompt body.

# Repair Notes
- Ensure eye contact clarity between observer and captive. Fix any local artifacts like blur or distortion. Maintain Barsoom aesthetic (Martian city environment). Focus on emotional anchor through eye contact; show observer's reaction to captive's state.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
