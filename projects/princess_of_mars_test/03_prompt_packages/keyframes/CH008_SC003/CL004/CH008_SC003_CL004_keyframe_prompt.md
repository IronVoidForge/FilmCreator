# Title
CH008_SC003 CL004 Keyframe Prompt

# ID
CH008_SC003_CL004_keyframe_prompt

# Purpose
Establish systematic looting action within ship interior from over-the-shoulder perspective. Show green-skinned figures moving through compartments to remove valuables while maintaining continuity with previous boarding shots. Focus on texture and lighting consistency for still scene build workflow.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Over-the-shoulder view inside dim gray vessel hull. Green-skinned figures moving systematically through compartments. Hands removing metallic weapons and fabric bundles from surfaces. Stationary pale human bodies lying in corners. Dust motes floating in shafts of light. Detailed textures on ship interior walls. Soft ambient lighting highlighting removal actions. High fidelity still image quality.

# Negative Prompt
blurry, distorted faces, extra limbs, bright sunlight, modern clothing, clean surfaces, smiling, motion blur, low resolution, text, watermark, out of focus, noisy, deformed anatomy, wrong color palette, floating debris, excessive smoke, modern technology.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: green-skinned figures, stationary human bodies
- look_continuity_policy: strict
- intended_lighting_change: none
- composition_type: over-the-shoulder shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on Martians entering main deck
- dependency_policy: none
- auto_advance_policy: disabled
- fallback_strategy: 
- consistency_assist_policy: active
- consistency_assist_method: 
- anatomy_repair_policy: enabled
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Capture the continuity rules for this stage. Maintain consistent removal of specific items (arms, silks) across interval frames. Ensure green-skinned figures match previous boarding shots in scale and lighting. Keep stationary human bodies in same positions relative to ship interior landmarks.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If anatomy of green-skinned figures appears distorted, apply consistency assist method. If lighting is too bright, adjust to match dim vessel interior profile. Ensure no modern objects appear in background.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
