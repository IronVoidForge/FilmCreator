# Title
SC001 CL002 Fix 01 Prompt

# ID
SC001_CL002_fix_01_prompt

# Purpose
corrective still generation preserving composition and look while fixing local issues, specifically ensuring fleet continuity and ship count accuracy over hill crests

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
twenty gray painted airships descending over hill crest background, fortified city buildings environment, valley hills vista background, daylight lighting conditions, cinematic exterior match, high tension atmosphere, detailed textures, upper floor observation point, military engagement preparation, golden hour sunlight highlights on prows devices, strange banners on prows, odd devices visible

# Negative Prompt
blurry, distorted anatomy, extra limbs, wrong colors, low resolution, artifacts, noise, bad hands, missing fingers, morphing faces, inconsistent lighting, watermark, text, signature, dark shadows obscuring details, motion blur, overexposed highlights, underexposed shadows, missing airships, incorrect banner designs, wrong ship count, distorted hill crests

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: image_1, image_2
- optional_refs: hill crest depth axis reference points, banner visibility markers across shots
- visible_character_assets: green-skinned warrior collective
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: cinematic exterior match
- composition_type: wide exterior establishing shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: fleet positioned at base of first hill crest
- dependency_policy: dependent on CL001 completion for spatial continuity
- auto_advance_policy: standard
- fallback_strategy: static wide shot if tracking unavailable
- consistency_assist_policy: anatomy repair
- consistency_assist_method: fix local issues
- anatomy_repair_policy: preserve ship and banner features
- consistency_targets: ship count, hill crest alignment, banner visibility
- style_profile: princess_of_mars_test
- batch_role: still_fix
- fix_of: CL002
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- match lighting consistency between upper floor window and sky views
- maintain ship position relative to hill crests across frames
- keep banner visibility clear on individual vessels
- ensure airship count remains consistent at twenty ships
- preserve spatial continuity while increasing tension through closer framing

# Repair Notes
- fix local distortions in ship hulls and prows
- correct lighting contrast between interior observation point and exterior sky references
- remove artifacts or noise from image_1 base that obscure fleet details
- ensure airship visibility is not obscured by shadows or foreground elements
- maintain high stakes military engagement atmosphere without distortion of fleet formation

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
