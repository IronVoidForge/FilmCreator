# Title
CH008_SC002 CL006 Fix 01 Prompt

# ID
CH008_SC002_CL006_fix_01_prompt

# Purpose
Correct local artifacts in extreme close-up loot collection sequence while preserving continuity of arms, food, and water items against drifting warship background and fire illumination.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
extreme close-up on ancient weapons being secured by green hands, pile of dried food supplies gathered into baskets, casks of water filled by martian fingers, glowing fire light illuminating storage area, gray painted ship hull in background, detailed texture on metal and wood, solemn atmosphere, high resolution focus on item surfaces.

# Negative Prompt
daylight lighting, distorted anatomy, extra characters, blurry focus, wrong item count, daylight shadows, bright sun, incorrect skin tone, low resolution, morphing hands, overexposed fire glow, missing loot items.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5.0
- required_refs: Arms, food supplies, water containers
- optional_refs: window frame
- visible_character_assets: Martians handling loot items
- look_continuity_policy: match_fire_illumination
- intended_lighting_change: maintain_burning_ship_glow
- composition_type: Extreme Close-up
- continuity_mode: insert
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Match previous loot item styles and lighting conditions from BT005. Ensure fire glow intensity matches burning ship sequence. Maintain consistent green Martian skin tone.

# Repair Notes
- Fix any hand distortion during item handling. Sharpen focus on specific loot textures. Correct color balance to match fire-illuminated environment.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
