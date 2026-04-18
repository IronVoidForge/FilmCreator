# Title
SC001 CL002 Fix 01 Prompt

# ID
SC001_CL002_fix_01_prompt

# Purpose
corrective still generation preserving composition and look while fixing local issues

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
medium tracking shot through dim corridor interior, narrator moving forward into space, hound following close at heel, stone walls visible, portal depth visible at far end, tension increasing, sunlight gleaming on devices, fire from burning ship creates floating funeral pyre effect in background, high stakes military engagement atmosphere, cinematic lighting, detailed textures

# Negative Prompt
blurry, distorted anatomy, extra limbs, wrong colors, low resolution, artifacts, noise, bad hands, missing fingers, morphing faces, inconsistent lighting, watermark, text, signature

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: image_1, image_2
- optional_refs: corridor wall details, portal visibility at far end
- visible_character_assets: narrator, hound
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: dimmer than exterior
- composition_type: medium tracking -> close-up
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: begin at building entrance
- dependency_policy: dependent on CL001 completion for spatial continuity
- auto_advance_policy: standard
- fallback_strategy: static medium shot if tracking unavailable
- consistency_assist_policy: 
- consistency_assist_method: anatomy repair
- anatomy_repair_policy: fix local issues
- consistency_targets: 
- style_profile: princess_of_mars_test
- batch_role: still_fix
- fix_of: CL002

# Continuity Notes
- match lighting consistency between interior and exterior views
- maintain narrator position and movement through building
- keep corridor depth perception consistent with previous shots
- ensure portal visibility at far end remains clear
- preserve spatial continuity while increasing tension through closer framing

# Repair Notes
- fix local anatomy issues on hound and narrator
- correct lighting contrast between interior and exterior references
- remove artifacts or noise from image_1 base
- ensure portal visibility is not obscured by shadows
- maintain high stakes military engagement atmosphere without distortion

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
