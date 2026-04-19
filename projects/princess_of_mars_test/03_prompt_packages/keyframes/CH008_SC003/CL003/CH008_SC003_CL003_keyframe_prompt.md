# Title
CH008_SC003 CL003 Keyframe Prompt

# ID
CH008_SC003_CL003_keyframe_prompt

# Purpose
Capture the completion of boarding action within a damaged vessel, emphasizing vertical transition from elevated structures to plain below under daylight with smoke and fire effects indicating recent conflict.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
group of green-skinned warriors positioned within damaged gray painted vessel, bodies strewn about on plain surface, building roofs visible above, daylight illumination, smoke rising from missile impact flames, damaged vessel prows, tactical formation, aftermath of battle, wide angle composition, vertical axis transition, ornate ornaments, spears, crimson cheeks, coal black hair

# Negative Prompt
blurry, distorted anatomy, extra limbs, wrong skin tone, bright blue sky, modern technology, clean surfaces, no smoke, no fire, static pose without context, low resolution, text, watermark, signature, human observer visible, aerial craft crews operating

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC003_BT001.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: green_warriors_inside_drifting_craft, bodies_strewn_about_in_plain
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_shot
- continuity_mode: tracking_shows_building_roofs_to_plain_transition
- starting_keyframe_strategy: show_warriors_successfully_boarding_drifting_craft_with_complete_movement
- dependency_policy: dependent_on_previous_close_up_of_approach_action
- auto_advance_policy: 
- fallback_strategy: reblock_same_scene_if_tracking_fails_to_show_complete_movement_completion
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain green skin tone consistency across all warriors
- Ensure craft damage matches previous shots in scene
- Preserve daylight lighting conditions without shadows from artificial sources
- Keep bodies strewn about for aftermath context
- Avoid showing human observer or companion figures
- Integrate smoke and fire effects naturally with environment

# Repair Notes
- Fix any anatomy distortions on warriors limbs or torsos
- Ensure smoke/fire effects are integrated naturally without clipping
- Correct color balance if craft appears too dark or light compared to environment
- Verify vertical axis transition is clear between roofs and plain
- Check for accidental inclusion of modern technology elements

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
