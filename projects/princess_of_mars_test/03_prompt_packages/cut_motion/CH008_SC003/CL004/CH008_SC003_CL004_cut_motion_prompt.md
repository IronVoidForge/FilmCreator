# Title
CH008_SC003 CL004 Cut Motion Prompt

# ID
CH008_SC003_CL004_cut_motion_prompt

# Purpose
Define smooth tracking motion following haul operation emphasizing tactical care for prisoner while maintaining medium shot composition and daylight smoke lighting consistency.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
medium shot of slender prisoner with light reddish copper skin being dragged across plain surface by green warriors maintaining formation, daylight smoke atmosphere, smooth tracking motion following haul operation

# Negative Prompt
morphing faces, inconsistent lighting, static frames, close-up composition, wide angle, extra limbs, background flickering, wrong character count

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL004
- duration_seconds: 5
- required_refs: CH008_SC003_BT002.md
- optional_refs: CH008_SC003_scene_breakdown.md
- visible_character_assets: prisoner_human_woman, green_warriors_maintaining_formation_during_haul
- look_continuity_policy: preserve_keyframe_lighting_and_grade_by_default
- intended_lighting_change: none
- composition_type: medium_shot
- continuity_mode: medium_shot_of_prisoner_being_dragged
- starting_keyframe_strategy: focus_on_prisoner_being_dragged_across_plain_surface_with_warriors_surrounding
- dependency_policy: dependent_on_previous_boarding_action_completion_inside_craft
- auto_advance_policy: 
- fallback_strategy: insert_close_up_if_medium_shot_fails_to_show_tactical_care_for_prisoner
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- note maintain daylight lighting with smoke from battle aftermath visible in background
- note ensure prisoner skin tone remains light reddish copper and hair stays coal black throughout motion
- note keep green warriors in formation during haul operation to show tactical care
- note preserve plain surface texture without flickering or morphing
- note reference haul to ground beat documentation for movement accuracy

# Repair Notes
- note if prisoner appears injured incorrectly, adjust to reflect aftermath state without excessive damage
- note if warriors break formation during drag, correct to maintain tactical coordination
- note ensure smooth tracking motion avoids jerky transitions between keyframes
- note verify background building south of position remains consistent in scale and position

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
