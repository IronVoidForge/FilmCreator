# Title
CH008_SC002 CL006 Cut Motion Prompt

# ID
CH008_SC002_CL006_cut_motion_prompt

# Purpose
Fill in stage intent for loot collection via extreme close-ups on arms, food, and water being secured by Martians on the drifting warship.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
extreme close-up on arms and weapons, extreme close-up on food supplies, extreme close-up on water containers, Martians handling loot items, ship storage areas accessible, resource acquisition details, daylight illumination, green Martian warriors

# Negative Prompt
crew activity, resistance, fire flames, blurry focus, distorted hands, morphing items, narration voice, dark shadows, smoke

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5.0
- required_refs: Arms (weapons), food supplies, water containers
- optional_refs: Window frame
- visible_character_assets: Martians handling loot items
- look_continuity_policy: 
- intended_lighting_change: 
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
- Maintain extreme close-up framing on individual loot items throughout the sequence.
- Ensure Martians appear as green warriors consistent with previous shots in scene.
- Preserve lighting continuity from salvage sequence (daylight or storage illumination).
- Avoid showing crew activity or resistance on the ship deck.

# Repair Notes
- Fix any anatomy distortions on hands holding items to ensure natural grip.
- Ensure loot items do not morph into each other during cuts.
- Correct any lighting shifts that deviate from the approved keyframe grade.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
