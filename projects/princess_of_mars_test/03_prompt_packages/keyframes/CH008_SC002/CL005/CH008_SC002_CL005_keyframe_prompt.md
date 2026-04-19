# Title
CH008_SC002 CL005 Keyframe Prompt

# ID
CH008_SC002_CL005_keyframe_prompt

# Purpose
Depict close-up of weapon muzzle flash from fleet crew perspective showing counter-battery discharge against ridge buildings with daylight illumination and damaged ship hull background context.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close-up of weapon barrel, hands gripping trigger mechanism, bright muzzle flash burst, smoke trails rising, green-skinned crew members huddled behind armored structures, gray painted hull visible, valley city background, daylight illuminating scene, loose black hair on figures, ornate jewelry visible, damaged ship plating showing scorch marks.

# Negative Prompt
blurry, distorted anatomy, extra limbs, text, watermark, human faces close up (unless crew hands), bright sun glare overpowering flash, dark shadows inconsistent with daylight, floating debris not part of ship, wrong color skin tone, missing weapon parts, boarding equipment visible, fire consuming hull prematurely.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: Weapon barrel accessible, muzzle flash timing aligned, damaged ship hull visible
- optional_refs: Valley city background
- visible_character_assets: Crew hands, weapon barrel, muzzle flash
- look_continuity_policy: reframe_same_moment
- intended_lighting_change: daylight with fire glow accents
- composition_type: Close-up
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static on weapon muzzle
- dependency_policy: parallel to medium shot for coverage
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
- Maintain green skin consistency across all crew figures in sequence
- Ensure gray hull color remains consistent with previous airship shots
- Valley city background must match deserted buildings established in BT001-BT004
- Weapon barrel state must align with firing shown in BT002
- No visible boarding equipment to maintain firing continuity

# Repair Notes
- Fix anatomy during firing motion to ensure natural weight distribution
- Ensure lighting matches fire glow if present from distant burning ships
- Check for extra crew members on open deck and remove if detected
- Verify weapon barrel connects correctly between hands and flash
- Adjust skin tone saturation to match established green warrior profile

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
