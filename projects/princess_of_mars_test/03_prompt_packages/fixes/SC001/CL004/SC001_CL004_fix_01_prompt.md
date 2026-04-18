# Title
SC001 CL004 Fix 01 Prompt

# ID
SC001_CL004_fix_01_prompt

# Purpose
Corrective still generation preserving composition and look while fixing local issues based on approved base image

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Medium shot interior window space, male human warrior observing exterior view, gray airships fleet approaching plaza, daylight reflecting off ship devices, stone floor tiles visible, dark wood window frame foreground, polished stone walls, midday light fully established, cinematic composition, high stakes military engagement atmosphere

# Negative Prompt
distorted anatomy, extra limbs, missing fingers, bad hands, blurry, low quality, text, watermark, signature, deformed face, ugly, mutation, morphed, disfigured, inconsistent lighting, floating elements, artifacts, crowd in immediate foreground, wrong skin tone, poor resolution, female figure, interior corridor space

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: image_1, image_2
- optional_refs: fleet formation consistency, daylight continuity
- visible_character_assets: male human warrior, gray airships fleet
- look_continuity_policy: preserve midday lighting consistency with previous beats
- intended_lighting_change: none
- composition_type: medium shot capturing observation posture
- continuity_mode: cutaway
- starting_keyframe_strategy: show observer at window, fleet at mid-distance
- dependency_policy: dependent on CL003 for emotional progression
- auto_advance_policy: static medium if movement unavailable
- fallback_strategy: use static medium if movement unavailable
- consistency_assist_policy: maintain character positioning relative to window frame
- consistency_assist_method: align character scale with medium shot framing
- anatomy_repair_policy: fix any hand distortion on observer
- consistency_targets: male skin tone, dark hair, bright daylight
- style_profile: still.scene_insert.two_ref.klein.distilled
- batch_role: fix_stage
- fix_of: local issues in approved still base

# Continuity Notes
- preserve midday lighting consistency with previous beats
- maintain character positioning relative to window frame
- ensure fleet formation matches visual baseline
- keep observer reaction expression consistent with emotional arc
- avoid introducing new crowd elements in immediate foreground

# Repair Notes
- fix any hand distortion on observer
- correct lighting mismatch between interior and exterior view
- ensure fleet anatomy is anatomically correct
- remove any floating artifacts near window frame
- align character scale with medium shot framing

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
