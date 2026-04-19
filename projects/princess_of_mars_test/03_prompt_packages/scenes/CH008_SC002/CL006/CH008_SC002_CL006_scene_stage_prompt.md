# Title
CH008_SC002 CL006 Scene Stage Prompt

# ID
CH008_SC002_CL006_scene_stage_prompt

# Purpose
Depict the engagement and damage to fleet through wide shot of fire arcs toward ridge, establishing return fire impact on warrior positions while maintaining continuity with battle context and debris field expansion.

# Workflow Type
authoring.scene_stage

# Positive Prompt
wide shot fire arcs from damaged ships swinging broadside toward ridge, explosions erupting on warrior positions, debris falling from missile impact points, smoke density increasing across valley floor, hull fires burning on ship structures, banners partially dissolved in flame, static hold framing on return fire vectors, linear sequence of fleet repositioning actions.

# Negative Prompt
blurry focus, extreme close-up shots, human faces, extra limbs, bright daylight without smoke, fire flames directly on face, distorted anatomy, low resolution, text overlays, motion blur during static hold, incorrect scale of ships, missing debris field, banners fully intact.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5.0
- required_refs: Fire arcs, explosions on ridge, debris falling visible; ship storage areas accessible.
- optional_refs: Window frame, smoke trails visible.
- visible_character_assets: Fleet ships, return fire vectors, Green Martians firing from buildings.
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_shot
- continuity_mode: cut
- starting_keyframe_strategy: static_on_valley_floor
- dependency_policy: sequential_to_broadside_formation_change
- auto_advance_policy: insert_debris_falling_if_fire_arcs_heavy
- fallback_strategy: 
- consistency_assist_policy: smoke_density_increase_tracking
- consistency_assist_method: 
- anatomy_repair_policy: ship_scale_verification
- consistency_targets: 
- style_profile: action_oriented_awe_inspiring
- batch_role: fleet_damage_sequence
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage regarding BT002 Fleet Returns Fire beat, ensuring static hold start strategy is maintained.
- Track specific fire arc vectors and explosion points to ensure sequential dependency policy is followed without skipping visual beats.
- Verify that wide shot framing remains consistent across cuts to avoid scale shifts during fleet movement shots.
- Monitor smoke density increase across interval beats 0-2s, 2-4s, 4-5s for proper progression tracking.

# Repair Notes
- Ensure wide shot framing is maintained throughout the clip to match intended composition type.
- Check for correct fire arc identification in valley-to-ridge return vector to align with required refs list.
- Verify continuity with previous fleet shots if this stage is inserted into a larger sequence.
- Correct any motion blur that violates the static hold starting keyframe strategy.
- Ensure debris field expansion matches interval beat progression from 0-2s to 4-5s.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
