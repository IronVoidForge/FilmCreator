# Title
CH008_SC003 CL003 Fix 01 Prompt

# ID
CH008_SC003_CL003_fix_01_prompt

# Purpose
Fix CL003 still generation to ensure complete boarding movement is visible within wide shot composition, correcting any local continuity errors regarding craft positioning or scattered bodies while maintaining established lighting and style.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
green warriors inside drifting craft with movement from roof to craft complete, bodies strewn about in plain, daylight, smoke from fire, missile impact flames, city buildings upper floors windows roofs background, wide shot composition, action oriented, awe inspiring, high fidelity details

# Negative Prompt
blurry motion, distorted faces, extra limbs, wrong lighting, dark shadows, incomplete movement, floating objects, low resolution, inconsistent anatomy, missing craft damage, incorrect character count

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
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Preserve wide shot composition and established lighting. Ensure boarding action shows complete movement from roof to craft. Maintain consistency with scattered bodies in plain. Do not introduce new characters or alter craft damage state.

# Repair Notes
- Correct any local issues where craft appears stationary or warriors are missing. Verify background buildings match scene geography. Ensure fire effects (smoke/flames) align with battle aftermath context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
