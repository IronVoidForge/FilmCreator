# Title
SC001 CL002 Keyframe Prompt

# ID
SC001_CL002_keyframe_prompt

# Purpose
Establish fleet formation and scale relative to city landscape from elevated observation point

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
elevated stone observation platform, two human observers in profile view, distant gray-painted airships forming pattern across horizon, deserted urban rooftop network below, valley vista stretching southward, morning sunlight illuminating sky, fleet halfway over hill crest, mechanical devices gleaming on prows

# Negative Prompt
interior corridor, close-up facial features, crowd of civilians, fire, smoke, burning vessel, prisoner figure, distorted anatomy, blurry focus, text, watermark, low resolution, extra limbs, missing weapons, green Martian warriors, chariots

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: human male observer, female companion
- look_continuity_policy: motion_opening
- intended_lighting_change: golden hour sunlight
- composition_type: medium tracking through corridors
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: fleet halfway over hill crest
- dependency_policy: dependent_on_CL001
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled
- video_prompt_package: 

# Continuity Notes
- Maintain vertical axis with elevated observation point
- Ensure distant airships visible but not dominating frame
- Match lighting conditions with previous exterior shots
- Keep rooftop network consistent for scale reference

# Repair Notes
- Fix any anatomy distortions on observer figure
- Correct lighting mismatch if balcony looks too dark
- Ensure distant ships are clearly defined against horizon
- Verify window frame details match continuity

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
