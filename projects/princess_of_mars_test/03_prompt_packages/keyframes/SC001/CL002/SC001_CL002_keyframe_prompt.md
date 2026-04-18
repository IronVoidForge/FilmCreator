# Title
SC001 CL002 Keyframe Prompt

# ID
SC001_CL002_keyframe_prompt

# Purpose
Establish full scale of green-skinned Martian Incubators positioned at base of first hill crest, showing mist-like retreat formation from elevated observation point with warm interior lighting contrast to cool exterior sky

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
elevated stone window frame on upper floor, two human figures in profile view observing distant horizon, green-skinned Martian Incubators forming pattern across multiple hill crests, deserted urban rooftop network below, valley vista stretching southward, morning sunlight illuminating sky, mechanical devices gleaming on Incubator prows, strange banners visible on vessel fronts, open ground where procession ended

# Negative Prompt
interior corridor, close-up facial features, crowd of civilians, fire, smoke, burning vessel, prisoner figure, distorted anatomy, blurry focus, text, watermark, low resolution, extra limbs, missing weapons, chariots, mounted warriors, stone vessels, food items, jewels, silks, furs, ammunition, arms

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: SC001 beat bundle BT001.md and BT002.md, Incubator positions relative to hill crests continuity notes, banner visibility markers across shots
- optional_refs: Hill crest depth axis reference points, movement timing consistency notes, interior lighting level contrast warm versus cool
- visible_character_assets: human male observer, female companion, Martian Incubators
- look_continuity_policy: motion_opening
- intended_lighting_change: golden hour sunlight
- composition_type: wide exterior establishing shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Incubators positioned at base of first hill crest
- dependency_policy: dependent_on_CL001
- auto_advance_policy: none
- fallback_strategy: cutaway_to_individual_Incubator_detail
- consistency_assist_policy: maintain Incubator count and positioning
- consistency_assist_method: reference previous exterior shots
- anatomy_repair_policy: fix observer figure distortions
- consistency_targets: twenty Incubators, window framing elements, banner designs, device shapes
- style_profile: sci-fi adventure aesthetic
- batch_role: establishing shot
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled
- video_prompt_package: projects/princess_of_mars_test/03_prompt_packages/cut_motion/SC001/CL002/SC001_CL002_cut_motion_prompt.md

# Continuity Notes
- Maintain vertical axis with elevated observation point from upper floor window
- Ensure distant Incubators visible but not dominating frame composition
- Match lighting conditions with previous exterior shots for consistency
- Keep rooftop network consistent for scale reference across shots
- Incubator count of twenty must remain constant in wide exterior compositions
- Banner designs must be identifiable across multiple viewing angles
- Window framing elements must stay consistent with interior observation point

# Repair Notes
- Fix any anatomy distortions on observer figure profile view
- Correct lighting mismatch if window frame appears too dark compared to exterior
- Ensure distant Incubators are clearly defined against horizon line
- Verify window frame details match continuity from previous shots
- Check that hill crest positioning matches established depth axis reference points

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
