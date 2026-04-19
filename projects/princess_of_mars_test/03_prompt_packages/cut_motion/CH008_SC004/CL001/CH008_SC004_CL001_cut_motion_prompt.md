# Title
CH008_SC004 CL001 Cut Motion Prompt

# ID
CH008_SC004_CL001_cut_motion_prompt

# Purpose
Fill in the stage intent here. Establish smooth motion trajectory for prisoner extraction from ship interior to exterior while maintaining keyframe lighting and character consistency. Ensure camera follows dragging action without introducing unwanted cuts or morphing artifacts during the transition.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Close-up of slender girlish figure being dragged by green-skinned warriors from gray airship interior to exterior hull. Camera follows movement trajectory through open portal. Dim industrial lighting persists. Oval face visible with copper skin and ornaments. Warriors maintain grip on prisoner. Ship banners dissolve in background flame or remain static depending on beat.

# Negative Prompt
Bright daylight, distorted anatomy, morphing faces, extra characters, flickering, blurry motion, wrong skin tones, narrator POV, blue sky, green grass, sudden lighting shifts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Scene lighting dim, industrial atmosphere
- visible_character_assets: Prisoner figure (slender girlish form), Green Warriors (2-3 figures approaching)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: None (preserve keyframe grade)
- composition_type: Close-up of prisoner figure
- continuity_mode: cut_motion
- starting_keyframe_strategy: Starting keyframe shows prisoner inside ship, ending keyframe at ship exterior
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: Standard
- fallback_strategy: Use medium shot warriors dragging if close-up unavailable
- consistency_assist_policy: Maintain character appearance (green skin, copper skin)
- consistency_assist_method: 
- anatomy_repair_policy: Fix morphing limbs or face distortion
- consistency_targets: 
- style_profile: Dim industrial atmosphere
- batch_role: CL001
- fix_of: 

# Continuity Notes
- Preserve keyframe lighting and grade by default. Maintain character consistency (green skin for Martians, copper skin for prisoner). Ensure smooth transition from interior to exterior without jumping cuts.

# Repair Notes
- Adjust motion strength if dragging looks stiff. Fix anatomy if limbs morph during movement. Correct skin tone shifts if lighting changes unexpectedly.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
