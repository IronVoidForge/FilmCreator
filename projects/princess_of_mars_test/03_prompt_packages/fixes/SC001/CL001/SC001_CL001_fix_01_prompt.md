# Title
SC001 CL001 Fix 01 Prompt

# ID
SC001_CL001_fix_01_prompt

# Purpose
corrective still generation preserving composition and look while fixing local issues on approved base

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
faithful reproduction of approved still base composition, human male observer standing at upper floor window frame, hands resting on stone sill, profile view facing outward, deserted city skyline background, gray airships visible in daylight sky, distant green warriors on lower balconies, polished stone floor tiles visible inside, soft morning sunlight filtering through glass, dark wood window frame with metal accents, medium profile shot composition, cinematic lighting consistency

# Negative Prompt
distorted anatomy, extra limbs, wrong skin tone, inconsistent lighting, blurry details, text, watermark, floating objects, mismatched colors, crowded foreground, sudden movement artifacts, new crowd elements, incorrect character positioning, wrong number of ships, incorrect ship color, distorted window frame, misplaced horizon line

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: image_1
- optional_refs: image_2
- visible_character_assets: observer character, hound companion
- look_continuity_policy: preserve window frame geometry and exterior lighting
- intended_lighting_change: none - maintain soft morning daylight
- composition_type: medium profile shot at window
- continuity_mode: window frame consistent
- starting_keyframe_strategy: establish vertical axis with narrator elevated above city
- dependency_policy: standalone observation clip
- auto_advance_policy: none
- fallback_strategy: maintain sill position for first three seconds
- consistency_assist_policy: match gray airship color to background sky
- consistency_assist_method: color palette alignment
- anatomy_repair_policy: fix foreground character distortions
- consistency_targets: window frame, ship count, lighting
- style_profile: cinematic_compositional
- batch_role: still_fix
- fix_of: local artifacts on approved base

# Continuity Notes
- maintain deserted city atmosphere
- preserve lighting consistency with exterior view
- keep observer position forward
- ensure hound follows close
- avoid introducing new crowd elements
- match gray airship color to background sky
- ensure green warriors match balcony elevation

# Repair Notes
- correct local artifacts on approved base
- smooth edges of distant figures
- match color palette to alien setting
- fix any anatomical distortions in foreground characters
- align window frame geometry with perspective
- ensure ship count matches continuity requirements

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
