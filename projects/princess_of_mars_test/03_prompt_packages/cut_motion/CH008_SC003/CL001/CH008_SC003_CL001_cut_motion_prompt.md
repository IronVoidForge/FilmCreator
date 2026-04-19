# Title
CH008_SC003 CL001 Cut Motion Prompt

# ID
CH008_SC003_CL001_cut_motion_prompt

# Purpose
Bridge static opening frame with lateral group movement and dragging action into shadowed interior while maintaining lighting consistency.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian females moving laterally from left edge toward center plaza, dragging slender figure with copper skin and black hair into shadowed archway, camera tracking group movement maintaining forty-five degree angle, copper flooring reflecting ambient light, building entrance deepening shadows, narrator observing from right edge static.

# Negative Prompt
morphing faces, extra limbs, blue skin, green hair, static camera, flickering textures, disappearing characters, wrong lighting, distorted anatomy, sudden cuts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, CH008_SC003/BEAT_INDEX.md
- optional_refs: plaza_environment_assets.md
- visible_character_assets: Green Martian females, copper-skinned figure, narrator edge
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_opening
- dependency_policy: independent
- auto_advance_policy: 
- fallback_strategy: insert_alternate_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain keyframe lighting grade throughout motion sequence.
- Preserve copper skin texture against green Martian skin for visual distinction.
- Keep 45-degree camera angle stable relative to group approach path.
- Ensure building interior remains shadowed relative to plaza daylight.

# Repair Notes
- If skin color shifts to blue or purple, re-render with correct palette.
- If camera shakes excessively, apply stabilization filter.
- If characters merge visually, separate bounding boxes in next pass.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
