# Title
CH008_SC004 CL003 Keyframe Prompt

# ID
CH008_SC004_CL003_keyframe_prompt

# Purpose
Capture the visual state at cut start for warriors dragging action. Freeze frame shows green-skinned figures approaching with intent while pulling slender human figure backward through ship portal. Dim industrial lighting establishes mood before exterior light reveals. Medium shot composition emphasizes movement trajectory from interior toward exit.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Two green-skinned warriors dragging a slender human figure backward through a ship portal. Dim industrial lighting. Oval face visible with coal black hair. Reddish copper skin tone. Gray metallic hull surrounding. Intentful movement trajectory. Medium shot composition.

# Negative Prompt
Modern clothing, bright sunlight, blue sky, white skin, blonde hair, high definition text, watermark, blurry, distorted anatomy, extra limbs, weapons not specified, clean background, indoor lighting mismatch, modern architecture, proper nouns, names, titles.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Medium shot warriors dragging action notes
- visible_character_assets: Green Warriors (2-3 figures), Prisoner figure being dragged backward
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: dim industrial to exterior portal light
- composition_type: medium shot warriors dragging action
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Starting keyframe warriors approaching with intent
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: 
- fallback_strategy: Use close-up prisoner figure if medium unavailable
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain green skin tone consistency across all warrior figures.
- Ensure oval face and coal black hair remain visible in frozen state.
- Preserve dim industrial lighting within ship interior before portal light appears.
- Match movement trajectory from interior toward exit without jumping cuts.
- Keep prisoner vulnerable state consistent with dragging action intent.

# Repair Notes
- Fix distorted grip on prisoner if warriors appear to be holding incorrectly.
- Adjust lighting balance if exterior light overwhelms interior dimness too early.
- Correct anatomy if green skin texture looks unnatural or overly smooth.
- Ensure portal transition is clear without blending into background noise.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
