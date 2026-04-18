# Title
SC001 CL004 Fix 01 Prompt

# ID
SC001_CL004_fix_01_prompt

# Purpose
Corrective still generation preserving composition and look while fixing local issues based on approved base image

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium shot interior corridor space, slender female figure entering from doorway, dark hair loosely caught, oval face, large lustrous eyes, finely chiseled features, destitute of clothes except ornaments, copper skin tone, male observer reacting in foreground, hound reacting to presence, dim interior lighting, stone walls visible, portal depth background, cinematic composition, high stakes military engagement atmosphere

# Negative Prompt
distorted anatomy, extra limbs, missing fingers, bad hands, blurry, low quality, text, watermark, signature, deformed face, ugly, mutation, morphed, disfigured, inconsistent lighting, floating elements, artifacts, crowd in immediate foreground, wrong skin tone, poor resolution

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: image_1, image_2
- optional_refs: portal visibility in background, lighting consistency
- visible_character_assets: narrator, hound, female figure
- look_continuity_policy: preserve interior lighting consistency with previous beats
- intended_lighting_change: none
- composition_type: medium shot capturing entrance
- continuity_mode: cutaway
- starting_keyframe_strategy: show interior space empty, then introduce female figure presence
- dependency_policy: dependent on CL003 for emotional progression
- auto_advance_policy: static medium if movement unavailable
- fallback_strategy: use static medium if movement unavailable
- consistency_assist_policy: maintain character positioning relative to corridor depth
- consistency_assist_method: align character scale with medium shot framing
- anatomy_repair_policy: fix any hand distortion on entering figure
- consistency_targets: copper skin tone, black hair, dim interior lighting
- style_profile: still.scene_insert.two_ref.klein.distilled
- batch_role: fix_stage
- fix_of: local issues in approved still base

# Continuity Notes
- preserve interior lighting consistency with previous beats
- maintain character positioning relative to corridor depth
- ensure copper skin tone matches visual baseline
- keep observer reaction expression consistent with emotional arc
- avoid introducing new crowd elements in immediate foreground

# Repair Notes
- fix any hand distortion on entering figure
- correct lighting mismatch between doorway and interior wall
- ensure hound anatomy is anatomically correct
- remove any floating artifacts near portal depth
- align character scale with medium shot framing

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
