# Title
CH008_SC004 CL005 Cut Motion Prompt

# ID
CH008_SC004_CL005_cut_motion_prompt

# Purpose
Fill in the stage intent for cut motion. Focus on dragging action into portal, camera observation perspective, lighting consistency, and environment transition from ship exterior to building entrance while maintaining keyframe grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green-skinned Martian warriors dragging slender human woman prisoner from gray ship exterior into building portal, oval face visible, copper skin, interior light glowing through entrance, dragging motion forward, camera positioned for narrator observation, urban Martian architecture background, visible motion blur, environmental change.

# Negative Prompt
Static image, no motion blur, distorted face, extra limbs, wrong skin tone, bright daylight, dark shadows, morphing features, low resolution, watermark, text overlay, flickering, inconsistent lighting, wrong anatomy.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: Close-up of prisoner face notes
- visible_character_assets: Prisoner figure, Female Martians
- look_continuity_policy: preserve keyframe lighting and grade by default
- intended_lighting_change: 
- composition_type: Close-up of prisoner face
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: oval face visible
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
- ending_keyframe_strategy: entering portal with interior light
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve keyframe lighting and grade by default
- Maintain character appearance stability (oval face, copper skin)
- Ensure environment transition from ship exterior to building entrance is clear
- Camera positioned for narrator observation of dragging action
- Avoid static frames during motion sequence

# Repair Notes
- Fix anatomy if dragging looks unnatural or limbs distort
- Ensure interior light is visible at end frame through portal
- Maintain grade consistency across motion frames
- Correct any flickering in lighting transitions
- Verify prisoner face remains oval and distinct throughout clip

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
