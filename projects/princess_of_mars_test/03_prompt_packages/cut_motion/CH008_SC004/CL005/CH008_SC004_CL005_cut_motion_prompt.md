# Title
CH008_SC004 CL005 Cut Motion Prompt

# ID
CH008_SC004_CL005_cut_motion_prompt

# Purpose
Animate the burning vessel drifting horizontally across the valley floor, maintaining continuity of fire intensity and smoke expansion from the approved keyframe. Focus on visible motion of the air craft and environment change without altering lighting grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot of burning air craft drifting horizontally across valley floor, roaring orange flames erupting from damaged hull, thick gray smoke plume expanding rapidly upward, lightened wooden structure visible through fire damage, camera panning slightly to follow vessel movement toward right side of frame, daylight illumination with smoke haze.

# Negative Prompt
static image, morphing vessel shape, sudden lighting change, dark shadows, green skin visible, human figures in foreground, explosion debris floating, blurry motion, distorted flames, wrong color palette, static background elements.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Vessel struck by final missile, flames erupting from hull damage, smoke plume expanding rapidly
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve vessel drift path across valley floor without stopping.
- Maintain fire intensity consistent with keyframe lighting and grade.
- Ensure smoke plume expands naturally without morphing into other shapes.
- Keep camera motion subtle to follow horizontal axis of vessel movement.

# Repair Notes
- If vessel stops moving, add subtle horizontal drift motion to maintain continuity.
- If flames die out too fast, intensify glow on hull edges to sustain visual interest.
- Check for static background elements that should remain consistent with previous clip.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
