# Title
CH008_SC004 CL002 Cut Motion Prompt

# ID
CH008_SC004_CL002_cut_motion_prompt

# Purpose
Maintain wide shot composition of green-skinned warriors positioned across three rooftop levels while subtle environmental motion occurs. Ensure continuity with previous keyframe lighting and character placement before transitioning to next clip. Preserve vertical axis from roofs down to valley floor without obstruction.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide angle view, multiple green-skinned warriors standing on urban rooftops, three distinct roof levels visible, missiles held in hands or resting on shoulders, distant valley floor below, smoke rising from ground level, daylight illumination, static camera position, establishing scale and group positioning, vertical axis maintained, unobstructed line of sight.

# Negative Prompt
close-up, portrait, character deformation, extra characters, wrong lighting, night scene, motion blur, incorrect composition, zooming in, warping faces, missing missiles, rooftop collapse, explosion effects on warriors, close proximity to camera, distorted anatomy, inconsistent grade.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Green Warriors distributed across 3 roof levels, partial view of valley floor
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: preserve_keyframe_grade
- composition_type: Wide shot (establishing multiple warriors)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: cutaway_to_next_clip
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: interval_frames
- anatomy_repair_policy: enabled
- consistency_targets: lighting, grade, character_count
- style_profile: action_oriented_awe_inspiring
- batch_role: clip_motion
- fix_of: null

# Continuity Notes
- Maintain vertical axis from roofs down to valley floor without obstruction.
- Ensure warriors hold static positions during launch sequence for stability.
- Preserve daylight illumination and smoke rising from ground level.
- Keep line of sight unobstructed by terrain features.
- Match keyframe lighting and grade by default.

# Repair Notes
- Apply anatomy repair policy for warrior figures if deformation occurs.
- Ensure consistency targets are met for lighting and grade across interval frames.
- Verify character count remains consistent with visible assets (approx 4 per level).
- Correct any motion blur that compromises the static positioning intent.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
