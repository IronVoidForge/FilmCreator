# Title
CH008_SC002 CL006 Scene Stage Prompt

# ID
CH008_SC002_CL006_scene_stage_prompt

# Purpose
Stage the impact reaction points following the targeting sequence, ensuring visual consistency with the preceding targeting close-up and maintaining the correct environmental context of the Martian city. Focus on medium shots of specific target points with impact reactions, adhering to the continuity mode of point-specific reaction shots showing impact effects.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian warriors positioned in elevated building windows firing downward, gray low-profile airships below with banners on stem and stern, smoke at specific target points, sighting apparatus active, gunners and officers hit sequentially, flames dissolving banners, open valley background, distant hills visible.

# Negative Prompt
Human faces in targeting shots, green painted vessels, missing banners, blurry impact effects, wrong ship color, cluttered window interiors, bright daylight without smoke, incorrect banner placement, floating debris unrelated to battle.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: Impact reaction shots coverage families
- visible_character_assets: Martians (targeting team), Impact smoke at target points
- look_continuity_policy: Hard dependency on CL005; must follow targeting sequence
- intended_lighting_change: Smoke trails from firing points, progressive damage tracking
- composition_type: Medium shot of specific target points with impact reactions
- continuity_mode: Point-specific reaction shots showing impact effects
- starting_keyframe_strategy: Open on sighting apparatus, then cut to impact points
- dependency_policy: Hard dependency on CL005; must follow targeting sequence
- auto_advance_policy: Use insert if need to emphasize impact timing
- fallback_strategy: Use insert if need to emphasize impact timing
- consistency_assist_policy: Strengthen smoke if weak
- consistency_assist_method: Correct ship color to gray
- anatomy_repair_policy: Ensure Martian anatomy is consistent with established green warriors
- consistency_targets: Impact timing, banner damage progression, ship swing arc completion
- style_profile: Action/Impact tracking
- batch_role: Clip 6 of Scene Stage Batch
- fix_of: CL005 targeting close-up

# Continuity Notes
- Capture the continuity rules for this stage. Hard dependency on CL005; must follow targeting sequence. Impact timing consistency is critical. Bullet drops at explosion points require placement consistency. Banners dissolving in flame require progressive damage tracking. Ship swing arc completion requires full circle verification.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If impacts look weak, strengthen smoke effects. If ship color is wrong, correct to gray. If banner damage is missing, add flame contact points. Ensure no human faces appear in targeting shots. Verify sighting apparatus is active and tracking.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
