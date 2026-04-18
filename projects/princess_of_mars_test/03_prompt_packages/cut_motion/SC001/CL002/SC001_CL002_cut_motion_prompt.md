# Title
SC001 CL002 Cut Motion Prompt

# ID
SC001_CL002_cut_motion_prompt

# Purpose
Execute cut motion transition from observation point to combat preparation while maintaining spatial continuity and increasing framing tension.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot tracking forward from upper floor window frame towards balcony ledge space. Green Martian warriors positioned on ledge with weapons ready for engagement. Camera slowly pushes in towards warriors' faces as movement slows down. Distant airships visible in sky above valley vista. Dim lighting consistent with interior observation point. Portal depth visible at far end of balcony.

# Negative Prompt
static image, sudden jump cut, distorted anatomy, extra limbs, flickering lights, wrong color grade, exterior sunlight bleeding into interior, blurry motion, morphing characters, static background, incorrect camera angle, narrator figure walking through entrance, interior corridor space, doorway frame, building entrance, interior corridor

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: 
- optional_refs: 
- visible_character_assets: Green Martian Warriors, Airships
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Medium shot of warriors on balcony
- continuity_mode: Cut to combat preparation
- starting_keyframe_strategy: Warriors positioned, weapons ready for engagement
- dependency_policy: Follows CL001 observation sequence
- auto_advance_policy: 
- fallback_strategy: Insert close-up on weapon stations if warriors not visible
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- - Preserve the keyframe lighting and grade by default.
- - Focus on visible motion, camera behavior, and environment change.
- - Start from upper floor window frame.
- - Maintain spatial continuity from previous clip.
- - Movement slows as tension increases.

# Repair Notes
- - Fix any anatomy distortions if movement is too fast.
- - Ensure lighting remains consistent with interior observation point baseline.
- - Correct color grade drift towards exterior sunlight.
- - Smooth out camera push-in speed inconsistencies.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
