# Title
CH008_SC004 CL002 Fix 01 Prompt

# ID
CH008_SC004_CL002_fix_01_prompt

# Purpose
Corrective pass for CL002 wide shot, maintaining Green Warrior composition on roofs while fixing local artifacts and ensuring vessel drift continuity from approved base image.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green Martian warriors on building roofs, wide shot, multiple levels, green skin, ornaments, missiles in hands, valley floor background, burning vessel drifting, smoke rising, daylight haze, cinematic lighting, vertical axis from roofs to valley, unobstructed line of sight, static composition during launch phase.

# Negative Prompt
human skin tones, distorted faces, extra limbs, modern clothing, clear sky, text, logos, blurry, floating objects, debris on roof surfaces, missing weapons, inconsistent smoke density, modern architecture elements.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot (establishing multiple warriors)
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
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Vertical axis from building roofs down to valley floor must remain consistent.
- Line of sight unobstructed by terrain features or debris.
- Warriors distributed across 3 roof levels (approximately 4 per level).
- Vessel drifting southeast/southwesterly with visible smoke trail.
- Missiles visible in hands or on shoulders, no movement during launch phase.

# Repair Notes
- Ensure smoke plume density matches beat plan (rising steadily from valley floor).
- Correct any skin tone shifts to maintain green Martian appearance.
- Verify flame coloration is orange/yellow with spurt of flame from missile impact.
- Maintain static composition for warriors during launch sequence.
- Remove any modern clothing or architectural elements not present in Barsoom setting.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
