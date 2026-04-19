# Title
CH008_SC004 CL006 Cut Motion Prompt

# ID
CH008_SC004_CL006_cut_motion_prompt

# Purpose
Capture wide shot motion of female martians dragging human woman into building portal, transitioning from exterior view to interior light visible.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide shot green-skinned female martians dragging slender human woman forward into building portal. Interior warm light visible through entrance. Dim industrial exterior atmosphere. Camera observes dragging action from threshold. Motion continuous and fluid.

# Negative Prompt
static image, distorted face, extra limbs, wrong skin color, blurry, morphing, missing portal structure, floating elements, low resolution, sudden cuts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT002.md building portal entry beat
- optional_refs: Wide shot showing portal and Martians notes
- visible_character_assets: Female Martians, Prisoner figure, Building portal
- look_continuity_policy: preserve keyframe lighting and grade
- intended_lighting_change: none
- composition_type: wide shot
- continuity_mode: cutaway
- starting_keyframe_strategy: Martians in view
- dependency_policy: independent
- auto_advance_policy: standard
- fallback_strategy: POV dragging into building
- consistency_assist_policy: standard
- consistency_assist_method: 
- anatomy_repair_policy: standard
- consistency_targets: 
- style_profile: A Princess of Mars Chapter VIII
- batch_role: clip_motion
- fix_of: 

# Continuity Notes
- Preserve lighting from approved keyframe to maintain visual grade.
- Maintain green skin tone for Martians and copper/reddish skin for human woman.
- Ensure portal structure remains consistent with BT002.md environmental state.
- Camera movement should follow dragging trajectory without abrupt cuts.

# Repair Notes
- If figure morphs, regenerate with anatomy repair policy enabled.
- If lighting shifts too much, revert to keyframe lighting profile.
- Ensure portal light contrast is maintained throughout motion.
- Check for static elements moving unnaturally and correct if needed.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
