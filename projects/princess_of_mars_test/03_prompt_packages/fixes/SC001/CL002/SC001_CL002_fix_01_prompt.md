# Title
SC001 CL002 Fix 01 Prompt

# ID
SC001_CL002_fix_01_prompt

# Purpose
corrective still generation preserving composition and look while fixing local issues

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
human male warrior standing at window frame observing gray painted airships in sky distance, desert city buildings environment, valley hills vista background, daylight lighting conditions, cinematic exterior match, high tension atmosphere, detailed textures, upper floor observation point, military engagement preparation

# Negative Prompt
blurry, distorted anatomy, extra limbs, wrong colors, low resolution, artifacts, noise, bad hands, missing fingers, morphing faces, inconsistent lighting, watermark, text, signature, dark shadows obscuring details

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: image_1, image_2
- optional_refs: balcony ledge details, airship visibility in sky
- visible_character_assets: green Martian warriors collective
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: cinematic exterior match
- composition_type: medium shot balcony
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: warriors positioned weapons ready
- dependency_policy: dependent on CL001 completion for spatial continuity
- auto_advance_policy: standard
- fallback_strategy: static medium shot if tracking unavailable
- consistency_assist_policy: anatomy repair
- consistency_assist_method: fix local issues
- anatomy_repair_policy: preserve warrior features
- consistency_targets: 
- style_profile: princess_of_mars_test
- batch_role: still_fix
- fix_of: CL002

# Continuity Notes
- match lighting consistency between balcony and sky views
- maintain warrior position and movement through building
- keep corridor depth perception consistent with previous shots
- ensure airship visibility at far end remains clear
- preserve spatial continuity while increasing tension through closer framing

# Repair Notes
- fix local anatomy issues on warriors and weapons
- correct lighting contrast between interior balcony and exterior sky references
- remove artifacts or noise from image_1 base
- ensure airship visibility is not obscured by shadows
- maintain high stakes military engagement atmosphere without distortion

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
