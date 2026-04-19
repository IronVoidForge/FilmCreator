# Title
CH008_SC004 CL005 Fix 01 Prompt

# ID
CH008_SC004_CL005_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Uses image_1 as the approved still base and image_2 as a secondary reference when needed. Workflow type is still.scene_insert.two_ref.klein.distilled. Focus on maintaining vessel drift path, flame intensity, and warrior positions consistent with BT002 start state.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot of burning gray vessel drifting across valley floor, roaring orange flames erupting from hull damage, dark gray smoke plume expanding rapidly, green-skinned warriors on building roofs observing, city buildings with upper floors and windows in background, open ground plaza visible, daylight atmosphere with smoke haze, horizontal axis following vessel drift path, lightened hull visible due to loot removal, smoke rising above vessel.

# Negative Prompt
distorted vessel, extra limbs, wrong skin color, text, blurry, low resolution, misplaced flames, incorrect smoke direction, missing warriors, wrong lighting, night scene, explosion debris on ground, floating objects, watermark, signature, darkened hull, static vessel, wrong banner colors.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Vessel struck by final missile, flames erupting from hull damage
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot (establishing vessel aftermath)
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
- Vessel drift path must follow horizontal axis across valley from center toward right side of frame.
- Flame intensity should match BT002 start state with roaring orange/yellow coloration.
- Warrior positions on roofs remain static during observation phase without movement until post-launch.
- Smoke direction must rise above vessel and trail behind it as it drifts.
- Hull lightness is visible due to loot removal, ensuring no heavy debris blocks view.

# Repair Notes
- Ensure hull lightness is visible due to loot removal.
- Correct smoke direction to rise above vessel.
- Fix any local artifacts in flames or smoke texture.
- Maintain daylight atmosphere with smoke haze consistency.
- Verify no extra debris on valley floor from previous impacts.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
