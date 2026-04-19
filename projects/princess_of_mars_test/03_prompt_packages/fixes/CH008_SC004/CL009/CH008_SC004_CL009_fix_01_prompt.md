# Title
CH008_SC004 CL009 Fix 01 Prompt

# ID
CH008_SC004_CL009_fix_01_prompt

# Purpose
Correct local generation issues while preserving composition and look from approved still base image_1. Ensure warriors match green skin and ornaments, loot is visible on some figures, smoke consistency matches clearing haze, and movement direction aligns with plaza entrance perspective for BT003 beat. Maintain daylight atmosphere and city building background continuity.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
green-skinned warriors, green skin, ornate jewelry, spears, walking from roofs and valley floor toward plaza center, carrying loot containers, small items on shoulders, smoke haze clearing, diminishing flames in distance, daylight, city buildings upper floors, windows, roofs, open ground plaza, distant hills beyond, medium shot movement, camera at plaza entrance looking outward, battle aftermath atmosphere

# Negative Prompt
human female prisoner, John Carter visible face, Air Fleet craft, exploding vessel, modern clothing, extra limbs, distorted faces, dark night, indoor lighting, debris on plaza surface, missile impact flames spurt, unmanned air ship, valley floor explosion

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL009
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium shot (movement)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Warriors must display consistent green skin and ornaments matching previous battle scenes.
- Loot containers should be visible on some warriors but not all, indicating selective carrying.
- Smoke haze must appear clearing but still present in valley air, not fully dissipated.
- Movement paths converge from roofs and valley floor toward plaza center without crossing camera plane abruptly.
- Background city buildings and distant hills remain static to maintain geography continuity.

# Repair Notes
- Fix any anatomy distortions on warrior limbs or faces to match canonical green-skinned design.
- Ensure lighting matches daylight conditions with smoke haze overlay, avoiding dark shadows from previous night scenes.
- Verify vessel drift path is consistent (drifting away in valley) and not reappearing or exploding prematurely.
- Correct any misplaced modern clothing items on warriors to ensure historical/setting accuracy.
- Adjust smoke density if it obscures background geography too heavily for continuity tracking.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL009.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
