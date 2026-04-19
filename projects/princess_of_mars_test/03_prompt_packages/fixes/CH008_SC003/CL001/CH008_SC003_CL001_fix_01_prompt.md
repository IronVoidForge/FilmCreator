# Title
CH008_SC003 CL001 Fix 01 Prompt

# ID
CH008_SC003_CL001_fix_01_prompt

# Purpose
Correct local generation artifacts while preserving the established composition and visual style for the Earthling captive introduction sequence. Ensure continuity of copper skin tone, green warrior features, and plaza environment without introducing new distortions or lighting inconsistencies.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
medium shot, deserted city plaza with copper flooring, 45-degree camera angle, group of green-skinned warriors dragging a slender female figure with copper skin and black hair towards building entrance, highly wrought ornaments on figure, daylight lighting, shadows deepening at threshold, V-shape formation visible, static opening composition, two reference style integration

# Negative Prompt
distorted hands, extra limbs, blurry face, wrong skin tone, green skin on human, naked clothes, text, watermark, low resolution, motion blur, inconsistent lighting, floating elements, distorted anatomy, poor detail, overexposed, underexposed

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, CH008_SC003/BEAT_INDEX.md
- optional_refs: plaza_environment_assets.md
- visible_character_assets: Earthling Woman, Green Martian Females, Narrator (edge)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_opening
- dependency_policy: independent
- auto_advance_policy: 
- fallback_strategy: insert_alternate_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: CH008_SC003_CL001_fix_01_prompt
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Maintain copper skin color consistency across frames to match reference images.
- Ensure green warrior skin contrasts distinctly with human figure without blending.
- Preserve plaza copper flooring reflections and ambient light direction.
- Keep camera angle at 45 degrees to group approach path for spatial continuity.
- Match ornament style and placement on the female figure to approved assets.

# Repair Notes
- Fix any hand distortion during dragging action to ensure natural anatomy.
- Correct lighting shifts between plaza daylight and building shadowed interior.
- Ensure ornaments are visible but do not clutter the face or obscure features.
- Verify that the V-shape formation of warriors is clear and consistent with previous frames.
- Adjust skin tone saturation if reference images show slight variations in copper hue.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
