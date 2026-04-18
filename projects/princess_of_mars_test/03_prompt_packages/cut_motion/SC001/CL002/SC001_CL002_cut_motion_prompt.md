# Title
SC001 CL002 Cut Motion Prompt

# ID
SC001_CL002_cut_motion_prompt

# Purpose
Execute cut motion transition from building entrance to interior corridor while maintaining spatial continuity and increasing framing tension.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium tracking shot moving forward from doorway into interior corridor space. Narrator figure walks through entrance with hound following close behind at heel. Camera slowly pushes in towards narrator's face as movement slows down. Corridor walls visible with dim lighting. Portal depth visible at far end of hallway.

# Negative Prompt
static image, sudden jump cut, distorted anatomy, extra limbs, flickering lights, wrong color grade, exterior sunlight bleeding into interior, blurry motion, morphing characters, static background, incorrect camera angle

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: 
- continuity_mode: 
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
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve the keyframe lighting and grade by default.
- Focus on visible motion, camera behavior, and environment change.
- Start from building entrance doorway frame.
- Maintain spatial continuity from previous clip.
- Movement slows as tension increases.

# Repair Notes
- Fix any anatomy distortions if movement is too fast.
- Ensure lighting remains consistent with interior corridor baseline.
- Correct color grade drift towards exterior sunlight.
- Smooth out camera push-in speed inconsistencies.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
