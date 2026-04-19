# Title
CH008_SC002 CL008 Keyframe Prompt

# ID
CH008_SC002_CL008_keyframe_prompt

# Purpose
Establish the visual intent for the damage detail close-up keyframe, focusing on the retreat of the enemy fleet with visible destruction indicators and progressive flame damage on banners.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Gray low-profile vessels drifting away from valley floor, banners dissolving in flame, smoke trails rising from damaged craft, glowing devices on prow, fire glow reflecting off hulls, medium close-up composition, open aerial space background, multiple ships showing damage indicators, limping retreat motion implied by angle.

# Negative Prompt
Blurry, distorted geometry, extra limbs, blue sky, text, logos, human faces, green skin, bright daylight without fire contrast, static ship position, clean hulls, intact banners, wrong color palette, low resolution, noise artifacts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5
- required_refs: BT004.md
- optional_refs: Damage detail close-ups coverage families
- visible_character_assets: Enemy Fleet, Banners with flame damage
- look_continuity_policy: Progressive tracking showing damage visible on multiple vessels
- intended_lighting_change: Fire glow intensifies on damaged areas
- composition_type: Medium close-up of vessels showing damage indicators
- continuity_mode: Close-up progressive tracking of damage indicators
- starting_keyframe_strategy: Open on multiple vessels with visible damage indicators
- dependency_policy: Soft dependency on CL007; can follow retreat sequence
- auto_advance_policy: N/A
- fallback_strategy: Use insert if need to emphasize damage progression timing
- consistency_assist_policy: N/A
- consistency_assist_method: 
- anatomy_repair_policy: N/A
- consistency_targets: Damage indicators, banner flame state
- style_profile: Klein distilled still scene build
- batch_role: Damage detail close-ups coverage
- fix_of: None

# Continuity Notes
- Capture the continuity rules for this stage. Ensure damage progression is consistent with previous shots in the retreat sequence. Verify banner flame state matches BT004.md beat bundle. Smoke trails must align with retreat path direction. Ship count must match fleet retreat sequence.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If flame damage appears static, adjust to show progressive burning. Ensure ship geometry remains consistent across the clip roster. Correct any color shifts that deviate from fire glow reflection on hulls.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
