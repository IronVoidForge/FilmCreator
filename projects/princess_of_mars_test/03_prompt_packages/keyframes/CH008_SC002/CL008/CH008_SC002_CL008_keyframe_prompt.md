# Title
CH008_SC002 CL008 Keyframe Prompt

# ID
CH008_SC002_CL008_keyframe_prompt

# Purpose
Resolve scene through wide shot showing ship being towed away with finality, establishing aftermath of salvage ritual and funeral pyre completion.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide shot of valley city with hills beyond, large gray airship fully ablaze floating above ground, fire consuming hull structure, towing cables deployed connecting ship to unseen anchor point, green-skinned warriors operating mechanical equipment near vessel base, smoke billowing upward, daylight mixed with orange fire illumination, deserted buildings in background, window frame visible in foreground edge.

# Negative Prompt
crew members on deck, intact ship hull, dark night sky, close-up shots, indoor lighting only, human faces without green skin, modern technology, text overlays, blurry details, distorted anatomy, missing towing equipment, unburned cargo, floating debris unrelated to ship.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Ship fully consumed by fire, towing equipment deployed, ship moving away from building
- optional_refs: Window frame
- visible_character_assets: Martians operating towing equipment; Narrator watching resolution
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/POV
- continuity_mode: cutaway
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
- Maintain wide shot perspective showing ship departure path.
- Ensure fire intensity matches funeral pyre state (fully ablaze).
- Keep towing equipment visible and functional.
- Preserve valley city geography with hills beyond.

# Repair Notes
- If ship looks intact, increase fire coverage.
- If towing cables missing, add mechanical rigging details.
- Ensure green skin tone consistency on warriors.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
