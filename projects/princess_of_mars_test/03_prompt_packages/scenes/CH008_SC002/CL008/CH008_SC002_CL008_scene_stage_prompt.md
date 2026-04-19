# Title
CH008_SC002 CL008 Scene Stage Prompt

# ID
CH008_SC002_CL008_scene_stage_prompt

# Purpose
Describe the stage intent for CL008 within CH008_SC002. The purpose is to visually track damage progression on enemy vessels during the fleet retreat phase. Focus on close-up framing of hull details and banners showing flame damage, establishing the conclusion of the aerial conflict without showing full fleet wide shots. This clip serves as a damage detail close-up progressive tracking shot within the Battle Initiation & Victory scene sequence.

# Workflow Type
authoring.scene_stage

# Positive Prompt
gray low-profile vessels with banners on stem and stern, smoke trails from damaged craft, banners with flame damage visible, Martian city architecture background blurred, close-up framing of hull details, progressive tracking motion, soot marks on ship surfaces, glowing devices on prow showing dim light, aerial battle zone atmosphere.

# Negative Prompt
full fleet wide shots, green skin warriors in foreground, clean hulls without soot, bright daylight without smoke atmosphere, human faces visible, sharp focus on distant hills, pristine banners without flame damage, static ship positioning without swing arc, overexposed sky.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5
- required_refs: BT004.md
- optional_refs: Damage detail close-ups coverage families
- visible_character_assets: Enemy Fleet (multiple vessels), Banners with flame damage
- look_continuity_policy: Progressive tracking showing damage visible on multiple vessels
- intended_lighting_change: Dimming light indicating retreat and smoke density
- composition_type: Medium close-up of vessels showing damage indicators
- continuity_mode: Close-up progressive tracking of damage indicators
- starting_keyframe_strategy: Open on multiple vessels with visible damage indicators
- dependency_policy: Soft dependency on CL007; can follow retreat sequence
- auto_advance_policy: Standard interval advance based on damage progression
- fallback_strategy: Use insert if need to emphasize damage progression timing
- consistency_assist_policy: Maintain damage state consistency across frames
- consistency_assist_method: Visual tracking of flame and soot accumulation
- anatomy_repair_policy: Ensure ship structures match established design
- consistency_targets: Hull damage level, banner flame state, smoke trail density
- style_profile: Action-oriented aerial battle aesthetic
- batch_role: Damage detail close-up coverage family
- fix_of: None

# Continuity Notes
- Maintain damage progression timing consistent with BT004 beat bundle.
- Ensure banner flame states show progressive burning from contact points.
- Verify ship swing arc completion matches full circle verification requirement.
- Keep smoke trails density aligned with battle conclusion atmosphere.
- Avoid introducing new vessel types or clean hulls that contradict retreat state.
- Ensure background architecture remains consistent with Martian city structures.

# Repair Notes
- If hulls appear too clean, add soot marks to surfaces to match damage indicators.
- If banners lack flame damage, apply progressive burning effects at contact points.
- If ships are positioned statically, introduce slight swing motion to indicate retreat.
- If smoke trails are missing, add atmospheric haze consistent with battle aftermath.
- If vessel count is inconsistent with fleet size, adjust framing to show multiple damaged craft.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
