# Title
CH008_SC002 CL006 Keyframe Prompt

# ID
CH008_SC002_CL006_keyframe_prompt

# Purpose
Depict return fire impact vectors and debris field expansion across valley floor, showing fire arcs striking ridge positions while smoke density increases from missile impacts, establishing the defensive aggression to desperation emotional shift during fleet limping sequence.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide shot of multiple fire arcs traveling through air toward ridge positions, explosions erupting at impact points on warrior formations, debris falling from blast zones, smoke trails visible in daylight, damaged ship hulls in valley floor with scorched surfaces, banners partially dissolved in heat haze, crew members huddled behind ship structures firing elevated weapons, valley-to-ridge return vector showing vertical firing angle from lower elevation.

# Negative Prompt
Blurry image, distorted anatomy, extra fingers, human facial features, modern clothing, plastic materials, bright sunlight shadows inconsistent with interior, text overlays, low resolution, deformed weapons, floating objects, fire flames on loot items yet, close-up framing instead of wide shot, static composition without motion intent, clean ridge positions without explosions.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5.0
- required_refs: Fire arcs visible traveling through air, explosions at ridge impact points, debris falling from blast zones, smoke trails and density increase, damaged ship hulls in valley floor, crew firing elevated weapons.
- optional_refs: Window frame, banners partially dissolved.
- visible_character_assets: Fleet ships, return fire vectors, crew members behind structures.
- look_continuity_policy: Maintain interior lighting consistency with previous boarding sequence.
- intended_lighting_change: Smoke density increases from 0-2s to 4-5s interval beats.
- composition_type: Wide shot
- continuity_mode: cut
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: sequential_to_broadside_formation_change
- fallback_strategy: insert_debris_falling_if_fire_arcs_heavy
- consistency_assist_policy: smoke_trails_visible
- consistency_assist_method: banners_partially_dissolved
- anatomy_repair_policy: crew_members_huddled_behind_structures
- consistency_targets: valley_to_ridge_return_vector
- style_profile: action_oriented_awe_inspiring
- batch_role: fleet_returns_fire
- fix_of: BT002
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Ensure fire arcs appear as multiple traveling vectors through air toward ridge positions; explosions must erupt at impact points on warrior formations; debris falling from blast zones must be visible; smoke trails and density increase from 0-2s to 4-5s interval beats; damaged ship hulls in valley floor with scorched surfaces; banners partially dissolved in heat haze; crew members huddled behind ship structures firing elevated weapons; maintain interior lighting consistency with previous boarding sequence; no fire flames on loot items yet as burning occurs in next beat.

# Repair Notes
- If fire arcs appear weak or single, regenerate with multiple traveling vectors through air toward ridge positions; if explosions look small, increase blast zone impact at warrior formations; ensure debris falling from blast zones is visible and matches interval beats; verify smoke trails and density increase from 0-2s to 4-5s; check damaged ship hulls in valley floor show scorched surfaces; confirm banners partially dissolved in heat haze; if crew members appear exposed, regenerate with huddled behind ship structures firing elevated weapons.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
