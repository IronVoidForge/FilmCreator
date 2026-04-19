# Title
CH008_SC004 CL006 Fix 01 Prompt

# ID
CH008_SC004_CL006_fix_01_prompt

# Purpose
Corrective still generation to fix local artifacts while preserving composition and look of warriors on roofs observing drifting vessel.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium shot of green-skinned warriors standing on urban building roofs, observing a long low gray air craft drifting in the valley floor below. Warriors maintain observation positions with slight forward lean. Vessel shows burning hull with orange flames and dark smoke plume rising. City buildings surround upper floors and windows. Daylight atmosphere with fire smoke.

# Negative Prompt
distorted anatomy, extra limbs, missing hands, inconsistent lighting, blurry details, modern technology, text artifacts, wrong sky color, floating objects, distorted faces, extra weapons, incorrect vessel shape, excessive debris on roofs, low resolution, noise

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL006
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: none
- composition_type: Medium shot (reaction shots)
- continuity_mode: insert
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: none
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: none
- consistency_assist_method: 
- anatomy_repair_policy: fix_local_issues
- consistency_targets: 
- style_profile: Barsoom cinematic
- batch_role: still_fix
- fix_of: CL006

# Continuity Notes
- Maintain horizontal axis following vessel drift path. Warrior eyelines directed at vessel position and smoke trail. Consistent daylight with fire smoke effects.

# Repair Notes
- Ensure vessel flames match previous impact severity. Keep warrior positions static during observation phase. Preserve roof surface integrity without debris.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
