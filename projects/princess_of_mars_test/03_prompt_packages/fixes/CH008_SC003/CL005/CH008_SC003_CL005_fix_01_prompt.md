# Title
CH008_SC003 CL005 Fix 01 Prompt

# ID
CH008_SC003_CL005_fix_01_prompt

# Purpose
Corrective still generation for CL005 tracking shot following haul operation. Preserves wide shot composition and lighting while ensuring drag marks on plain surface and prisoner visibility align with approved base. Maintains visual continuity of green warriors in formation and building background context.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot tracking motion following haul operation, plain surface with visible drag marks, building south of position in background, green warriors maintaining formation, human female prisoner being dragged across ground, light reddish copper skin, coal black hair waving, highly wrought ornaments, daylight smoke from fire, missile impact flames context.

# Negative Prompt
distorted anatomy, missing drag marks, night lighting, extra characters, blurry motion, wrong background valley instead of building, prisoner face obscured, warriors not in formation, low resolution, incorrect skin tone, missing ornaments.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC003_BT002.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: prisoner_being_dragged_across_plain, green_warriors_maintaining_formation, building_south_of_position_in_background
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_shot
- continuity_mode: tracking_shots_following_haul_operation
- starting_keyframe_strategy: show_tracking_motion_following_haul_operation_with_plain_and_building_context_emphasized
- dependency_policy: dependent_on_previous_medium_shot_of_prisoner_being_dragged
- auto_advance_policy: smooth_transition_emphasizing_vertical_drop_from_craft_to_ground_with_plain_surface_shows_drag_marks
- fallback_strategy: reblock_same_scene_if_tracking_fails_to_show_plain_and_building_context
- consistency_assist_policy: maintain_drag_marks_on_plain_surface
- consistency_assist_method: preserve_base_composition
- anatomy_repair_policy: fix_prisoner_visibility_and_warrior_formation
- consistency_targets: prisoner_skin_tone, warrior_green_skin, background_building
- style_profile: action_oriented_awe_inspiring
- batch_role: still_fix
- fix_of: CL005_tracking_shot_following_haul_operation

# Continuity Notes
- Maintain drag marks on plain surface to indicate haul operation.
- Ensure prisoner skin tone matches light reddish copper description.
- Keep warrior green skin and ornaments consistent throughout shot.
- Background must show building south of position, not just valley or hills.
- Lighting should reflect daylight with smoke from fire context.

# Repair Notes
- Fix any missing drag marks on plain surface in generated still.
- Clarify prisoner's face if obscured by motion blur or angle.
- Ensure warriors are in tactical formation during haul operation.
- Correct background to prioritize building structure over distant hills.
- Verify ornament details on prisoner are highly wrought and visible.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
