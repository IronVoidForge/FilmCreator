# Title
CH008_SC002 CL005 Keyframe Prompt

# ID
CH008_SC002_CL005_keyframe_prompt

# Purpose
Depict tactical boarding sequence from window perspective showing green-skinned warriors moving onto gray vessel deck, capturing transition from building to ship with daylight illumination and valley city background context.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Green-skinned warriors climbing onto floating gray hull, wooden planks connecting building to ship, daylight illuminating valley city background, loose black hair on figures, ornate jewelry visible, smoke rising from distant damaged ships, wide angle capturing boarding trajectory, medium detail on warrior movement, no crew resistance on deck, boarding equipment deployed, ship storage areas accessible.

# Negative Prompt
blurry, distorted anatomy, extra limbs, text, watermark, human faces close up, bright sun glare, dark shadows inconsistent with daylight, floating debris not part of ship, wrong color skin tone, missing boarding equipment, crew members on deck, fire consuming hull prematurely.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: Ship deck accessible, boarding equipment deployed, no crew resistance visible
- optional_refs: Window frame
- visible_character_assets: Martians transitioning from windows to ship deck; Narrator observing boarding action
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/Medium
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: track_forward
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
- Maintain green skin consistency across all warrior figures in sequence
- Ensure gray hull color remains consistent with previous airship shots
- Valley city background must match deserted buildings established in BT001-BT004
- Boarding equipment state must align with deployment shown in BT004
- No visible crew members on deck to maintain unmanned ship continuity

# Repair Notes
- Fix anatomy during climbing motion to ensure natural weight distribution
- Ensure lighting matches fire glow if present from distant burning ships
- Check for extra crew members on deck and remove if detected
- Verify boarding planks connect correctly between building and hull
- Adjust skin tone saturation to match established green warrior profile

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
