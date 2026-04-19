# Title
CH008_SC003 CL005 Cut Motion Prompt

# ID
CH008_SC003_CL005_cut_motion_prompt

# Purpose
Track haul operation with plain and building context visible, emphasize vertical drop from craft to ground, show drag marks on plain surface, maintain warrior formation continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
tracking shot following haul operation with plain and building context visible, green warriors maintaining formation, prisoner being dragged across plain surface, vertical drop from craft to ground emphasized, drag marks on plain surface shown, daylight lighting preserved, smoke from fire visible in background, wide shot composition.

# Negative Prompt
distortion, flickering, wrong composition, extra limbs, morphing faces, inconsistent lighting, sudden cuts, static image, blurry motion, incorrect character count, missing background elements.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC003_BT002.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_shot
- continuity_mode: tracking_shots_following_haul_operation
- starting_keyframe_strategy: show_tracking_motion_following_haul_operation_with_plain_and_building_context_emphasized
- dependency_policy: dependent_on_previous_medium_shot_of_prisoner_being_dragged
- auto_advance_policy: 
- fallback_strategy: reblock_same_scene_if_tracking_fails_to_show_plain_and_building_context
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Lighting must match previous keyframe daylight with smoke from fire context.
- Character placement must show green warriors maintaining formation during haul.
- Environment state must include plain surface showing drag marks and building south of position in background.
- Motion should emphasize vertical drop from craft to ground smoothly.

# Repair Notes
- If tracking fails to show plain and building context, reblock same scene immediately.
- Ensure no sudden cuts or static image artifacts during motion transition.
- Verify drag marks are visible on plain surface for continuity with previous beat.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
