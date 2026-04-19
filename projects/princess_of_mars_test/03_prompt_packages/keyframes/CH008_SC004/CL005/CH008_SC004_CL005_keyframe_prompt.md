# Title
CH008_SC004 CL005 Keyframe Prompt

# ID
CH008_SC004_CL005_keyframe_prompt

# Purpose
Fill the stage intent for a wide shot establishing vessel aftermath, capturing the exact visible state at cut start as a single frozen still of burning vessel drifting away from valley center.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
A wide shot of a long low gray-painted vessel struck by final missile, orange and yellow flames erupting from hull damage, dark gray smoke plume expanding rapidly above the ship, vessel beginning to drift away from valley center, lightened hull visible due to loot removal, roaring fire effects, daylight lighting, open ground plaza background, distant hills beyond.

# Negative Prompt
people close up, clear blue sky, intact hull structure, static composition, green skin characters in foreground, text overlays, blurry details, dark night scene, smokeless environment, calm water surface, vertical camera angle.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Vessel struck by final missile, flames erupting from hull damage, smoke plume expanding rapidly
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight consistent with previous shots
- composition_type: Wide shot (establishing vessel aftermath)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: none
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: four_ref
- anatomy_repair_policy: enabled
- consistency_targets: vessel position, smoke density, flame intensity
- style_profile: still.scene_build.four_ref.klein.distilled
- batch_role: keyframe
- fix_of: null

# Continuity Notes
- Capture the continuity rules for this stage. Horizontal axis following vessel's drift path across valley. Vessel moves from center toward right side of frame. Roaring flames, smoke plume, lightened hull visible. Ensure smoke density matches heat output and flame intensity reflects missile impact severity. Maintain daylight consistency with surrounding environment shots.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If vessel appears too heavy, adjust to reflect loot removal. If smoke is too thin, increase opacity to match fire volume. Ensure flames are concentrated at impact points and spreading outward. Verify drift direction aligns with valley geography context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
