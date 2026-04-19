# Title
CH008_SC002 CL006 Scene Stage Prompt

# ID
CH008_SC002_CL006_scene_stage_prompt

# Purpose
Describe the staging intent for this scene stage to capture resource acquisition details through extreme close-ups on the drifting warship during the salvage sequence, establishing the value of salvaged goods while maintaining continuity with the battle context.

# Workflow Type
authoring.scene_stage

# Positive Prompt
extreme close-up green skin hands securing metallic weapons and ammunition casks, organic food supplies being gathered into woven baskets, water containers filled from ship storage areas, dim interior lighting reflecting off polished hull surfaces, static hold framing on individual loot items, linear sequence of resource collection actions.

# Negative Prompt
blurry focus, wide angle shots, human faces, extra limbs, bright daylight, fire flames directly on face, distorted anatomy, low resolution, text overlays, motion blur during static hold, incorrect scale of weapons.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5.0
- required_refs: Arms (weapons), food supplies, water containers visible and being collected; ship storage areas accessible.
- optional_refs: Window frame.
- visible_character_assets: Martians handling loot items; Narrator observing collection process.
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: extreme_close_up
- continuity_mode: insert
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage regarding BT006 Loot Collection beat, ensuring static hold start strategy is maintained.
- Track specific item types (arms, food, water) to ensure linear sequence dependency policy is followed without skipping visual beats.
- Verify that extreme close-up framing remains consistent across cuts to avoid scale shifts during resource acquisition shots.

# Repair Notes
- Ensure extreme close-up framing is maintained throughout the clip to match intended composition type.
- Check for correct item identification in storage areas to align with required refs list.
- Verify continuity with previous loot shots if this stage is inserted into a larger sequence.
- Correct any motion blur that violates the static hold starting keyframe strategy.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
