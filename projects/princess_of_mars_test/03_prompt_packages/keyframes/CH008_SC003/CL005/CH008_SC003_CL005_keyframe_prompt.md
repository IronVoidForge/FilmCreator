# Title
CH008_SC003 CL005 Keyframe Prompt

# ID
CH008_SC003_CL005_keyframe_prompt

# Purpose
Establish tracking motion of haul operation with plain and building context visible, ensuring continuity with preceding medium shot of prisoner being dragged.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
wide angle tracking shot, green-skinned warriors maintaining tactical formation, slender human female prisoner being hauled across open ground plain surface, gray air craft wreckage in background, daylight illumination, smoke from fire rising, drag marks visible on plain surface, banners on craft prows, ornaments on prisoner body, vertical drop from craft to ground emphasized, building structure south of position in background

# Negative Prompt
distorted anatomy, extra limbs, wrong skin tone, text, watermark, blurry, inconsistent lighting, floating objects, missing drag marks, incorrect formation, faces not matching continuity, proper nouns, names

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
- starting_keyframe_strategy: 
- dependency_policy: 
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain drag marks on plain surface consistent with previous shot.
- Keep warrior formation tight during haul operation.
- Ensure background building position remains static relative to camera movement.
- Match lighting conditions from preceding clip.

# Repair Notes
- If anatomy appears distorted during tracking motion, apply repair policy for limbs and body structure.
- Adjust lighting consistency if shadows shift unexpectedly.
- Verify drag marks are continuous across frame transitions.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
