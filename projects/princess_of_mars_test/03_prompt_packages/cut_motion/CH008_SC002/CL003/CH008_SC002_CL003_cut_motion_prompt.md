# Title
CH008_SC002 CL003 Cut Motion Prompt

# ID
CH008_SC002_CL003_cut_motion_prompt

# Purpose
Depict the immediate aftermath of the warrior volley on the Martian fleet through a reaction shot. Camera captures explosion bloom and smoke drift across damaged gray airships, emphasizing hull breaches and fire spurt while maintaining static composition on fleet hulls initially before subtle shudder motion.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
gray airship hulls with banner damage, smoke plumes rising from impact points, fire spurt from missile breaches, daylight illumination mixed with explosion glow, camera static then subtle shudder motion, wide shot of fleet formation, distant green-skinned warriors silhouetted in windows, debris field expanding

# Negative Prompt
blurry, morphing, extra limbs, wrong colors, static image, distorted faces, missing smoke, incorrect lighting, crew on unmanned ship, sudden appearance of people, green skin tone drift, gray paint color shift, sharp focus on foreground debris obscuring fleet

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5.0
- required_refs: Hull breaches visible, smoke rising from damaged ships, one ship remains unmanned
- optional_refs: Window frame
- visible_character_assets: green-skinned warriors (distant)
- look_continuity_policy: Maintain ship damage progression consistency
- intended_lighting_change: Daylight with fire illumination
- composition_type: Wide/Medium
- continuity_mode: insert
- starting_keyframe_strategy: static_on_fleet_hulls
- dependency_policy: linear_sequence
- auto_advance_policy: none
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: preserve_smoke_density
- consistency_assist_method: gradual_drift
- anatomy_repair_policy: maintain_hull_integrity
- consistency_targets: banner_damage_progression
- style_profile: cinematic_action
- batch_role: reaction_shot
- fix_of: BT001

# Continuity Notes
- Maintain ship damage progression consistency
- Preserve daylight with fire illumination
- Keep green-skinned warriors positioned at building windows
- Ensure smoke density increases over interval beats

# Repair Notes
- Ensure green-skinned warriors remain consistent skin tone
- Ships remain gray paint color
- No sudden appearance of crew on drifting vessel
- Prevent hull from melting or disappearing

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
