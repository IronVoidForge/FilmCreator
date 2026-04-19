# Title
CH008_SC002 CL007 Keyframe Prompt

# ID
CH008_SC002_CL007_keyframe_prompt

# Purpose
Depict fleet ships executing broadside maneuver in staggered formation, establishing damaged but functional combat capability with coordinated positioning across valley width to maximize firepower and reposition for continued engagement.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide shot of multiple long gray vessels aligned broadside in staggered formation across valley floor with thick smoke rising from hull damage, crew members moving between ship structures adjusting weapons to new firing angles, damaged thrusters visible on vessel prows, banners fluttering in wind, fire glow illuminating scene from battle impacts, ships positioned horizontally across valley width.

# Negative Prompt
visible crew members on deck standing still, extinguished fire or no smoke, daylight without battle illumination, human female figure present, wrong vessel color not gray, chaotic movement inconsistent with broadside maneuver, crowd of civilians, ship rotation mechanism obscured, banners dissolved in flame.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5.0
- required_refs: Fleet ships aligned broadside, Smoke rising from hull damage, Crew members moving to new firing positions, No visible crew standing still on deck
- optional_refs: Window frame edge, Valley floor marked with battle damage
- visible_character_assets: Fleet ships, Crew members moving
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: fire glow dominates ambient daylight
- composition_type: Wide shot
- continuity_mode: staggered formation static hold
- starting_keyframe_strategy: staggered formation static hold
- dependency_policy: sequential to crew realignment medium shot
- auto_advance_policy: insert ship rotation if thruster sway varies
- fallback_strategy: insert ship rotation if thruster sway varies
- consistency_assist_policy: maintain vessel color gray despite fire glow
- consistency_assist_method: verify hull damage visible but not obscuring structure
- anatomy_repair_policy: ensure crew movement consistent with realignment action
- consistency_targets: staggered formation alignment, crew position adjustment
- style_profile: still.scene_build.four_ref.klein.distilled
- batch_role: fleet formation change
- fix_of: CL007
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Fleet ships must be aligned broadside in staggered formation, not random positioning.
- Crew members should be moving between ship structures to new firing positions, not standing still on deck.
- Hull damage visible but vessel color remains gray despite fire glow illumination.
- Smoke rising from impact points and hull fires burning consistently across all ships.
- Banners fluttering in wind without being dissolved in flame.
- Window frame optional if establishing observer POV context.
- Valley floor marked with battle damage from previous impacts.

# Repair Notes
- Ensure fire intensity is high enough for battle effect without obscuring ship structure entirely.
- Fix crew movement consistency to show realignment action rather than static positioning.
- Verify vessel color remains gray despite fire glow illumination on hulls.
- Maintain continuity of staggered formation alignment across all visible ships.
- Check that thruster damage is visible but not causing excessive sway inconsistent with maneuverability.
- Ensure banners are fluttering in wind without being dissolved in flame.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
