# Title
CH008_SC004 CL001 Fix 01 Prompt

# ID
CH008_SC004_CL001_fix_01_prompt

# Purpose
Corrective fix for Clip CL001, maintaining medium shot composition of green-skinned warrior preparing missile on roof, ensuring continuity with scene lighting and style while resolving local generation issues.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green-skinned warrior standing on building roof level, holding missile device ready in hands, daylight illumination, smoke haze in air, vertical axis from roofs down to valley floor, eyelines directed downward at vessel position, static weight shift for stability, green skin tone consistent with established characters, ornamental jewelry visible, medium shot close-up on warrior, action-oriented aesthetic, high detail texture.

# Negative Prompt
blurry, distorted anatomy, extra fingers, wrong skin tone, dark shadows, text artifacts, debris on roof surface, incorrect lighting, overexposed, underexposed, low resolution, morphing hands, floating objects, background clutter, inconsistent color grading.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium shot (close-up on warrior)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: action_oriented_awe_inspiring_tense_combat_sequences
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain vertical axis from roofs down to valley floor.
- Ensure eyelines directed downward at vessel position.
- Preserve Green Warrior skin tone and ornamentation style.
- Keep missile visible in hands or on shoulders.
- Match daylight illumination with smoke haze consistency.

# Repair Notes
- Fix any anatomical distortions on the warrior's hands holding the missile.
- Adjust lighting to match daylight with smoke haze consistency.
- Ensure background roof surface matches established texture without debris.
- Correct skin tone variations to align with canonical character index.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
