# Title
CH008_SC002 CL006 Fix 01 Prompt

# ID
CH008_SC002_CL006_fix_01_prompt

# Purpose
Correct local artifacts in wide shot of fire arcs sequence while preserving continuity of fleet ships, return fire vectors, and debris field against valley background and burning ship illumination.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
wide shot showing multiple gray painted vessels firing across valley floor, bright orange fire arcs rising from muzzle points toward ridge, smoke trails visible in air, debris falling from impact zones, green Martian crew members huddled behind damaged ship structures, weapons elevated and firing, hull fires burning along sides, daylight illumination with fire glow overlay, high resolution focus on fleet formation, cinematic composition with valley-to-ridge eyeline.

# Negative Prompt
daylight lighting without fire glow, distorted anatomy, extra characters, blurry focus, wrong item count, bright sun, incorrect skin tone, low resolution, morphing hands, overexposed fire glow, missing fleet ships, daylight shadows, wrong debris field, incorrect ship colors.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5.0
- required_refs: Fleet ships, return fire vectors, debris field
- optional_refs: valley background, burning ship glow
- visible_character_assets: Green Martian crew members
- look_continuity_policy: match_fire_illumination
- intended_lighting_change: maintain_burning_ship_glow
- composition_type: Wide shot
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
- Match previous fleet ship styles and lighting conditions from BT002. Ensure fire glow intensity matches burning ship sequence. Maintain consistent green Martian skin tone. Preserve valley background geography and debris field continuity.

# Repair Notes
- Fix any hand distortion during weapon handling. Sharpen focus on specific fleet textures and fire arcs. Correct color balance to match fire-illuminated environment. Ensure ship hull damage is visible and consistent with previous shots.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
