# Title
CH008_SC003 CL004 Cut Motion Prompt

# ID
CH008_SC003_CL004_cut_motion_prompt

# Purpose
Generate motion video for the over-the-shoulder looting sequence based on the approved keyframe. Ensure smooth camera tracking through ship compartments while maintaining established lighting and grade. Focus on visible actions of green-skinned figures removing items from cargo holds without altering the static background elements like dead sailors.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Over-the-shoulder view of green-skinned warriors entering main deck compartments of gray ship interior. Hands systematically removing swords and shields from storage racks. Collecting silk fabrics and jewels from cargo areas. Dead sailors remain stationary in background. Smooth camera tracking movement through ship interior. Dim industrial lighting preserved.

# Negative Prompt
distorted anatomy, flickering motion, extra limbs, wrong colors, bright sunlight, modern technology, text overlays, blurry details, inconsistent lighting, morphing faces, floating objects, sudden jumps, noise artifacts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: 
- visible_character_assets: Martians (looting), Dead Sailors (stationary)
- look_continuity_policy: preserve keyframe lighting and grade
- intended_lighting_change: none
- composition_type: over-the-shoulder shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on Martians entering main deck
- dependency_policy: none
- auto_advance_policy: 
- fallback_strategy: insert if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain specific item types (swords, silks, jewels) consistent with previous frames.
- Keep ship interior layout and background dead sailors static throughout motion.
- Ensure green skin tone matches established character profile without shifting to human tones.
- Preserve dim industrial lighting conditions from keyframe.
- Camera movement must follow the looting action smoothly without abrupt cuts.

# Repair Notes
- Fix any hand anatomy errors during item removal actions.
- Correct motion flickering if background elements appear unstable.
- Adjust color grading if green skin appears too bright or desaturated compared to keyframe.
- Ensure no sudden lighting shifts occur during the tracking shot.
- Repair any morphing artifacts on the gray ship hull.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
