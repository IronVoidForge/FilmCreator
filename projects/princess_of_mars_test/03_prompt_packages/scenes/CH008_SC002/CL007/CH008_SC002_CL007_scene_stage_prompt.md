# Title
CH008_SC002 CL007 Scene Stage Prompt

# ID
CH008_SC002_CL007_scene_stage_prompt

# Purpose
Depict the engagement and damage to fleet through wide shots establishing staggered formation transitioning to broadside alignment. Camera captures entire fleet movement across valley floor with hills beyond. Focus on visual continuity of damaged hulls maneuvering, smoke rising from impact points, and crew members realigning positions for coordinated volley fire. Authoring intent is to resolve aerial conflict sequence through resourcefulness in salvaging supplies and honoring fallen vessel. Staging includes wide coverage of valley floor with hills beyond, medium coverage of figures near pyre, and POV coverage from building window.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Gray-painted vessels with strange banners and odd devices on prows, thick smoke rising into valley sky, crew members moving on forward decks, debris field expanding across ground, hills beyond visible in distance, damaged thrusters swaying on hulls, coordinated volley fire arcs toward ridge, figures crowd forward decks, fire causes spurt of flame from missile impact, banners fluttering in wind.

# Negative Prompt
Intact hulls without damage, modern technology, text, logo, bright daylight without smoke/fire context, floating debris unrelated to battle, window frame missing, ship intact without flames, visible enemy fleet, crew resistance, modern uniforms.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5.0
- required_refs: Fleet formation change, staggered to broadside alignment, damaged hulls visible, smoke density increasing
- optional_refs: Ship banners fluttering, debris scattered
- visible_character_assets: Fleet ships, crew members moving
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: pan_across
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
- Fleet in staggered formation changing to broadside
- Damaged hulls visible with smoke rising from impact points
- Valley floor geography establishing scale
- Hills beyond providing directional context
- Crew members realigning positions for coordinated volley fire
- Debris field expanding after previous impacts

# Repair Notes
- Ensure ship rotation is smooth but shows damage
- Verify fire intensity matches battle context
- Check consistency of ship banners and devices
- Confirm smoke direction aligns with valley wind flow
- Validate debris field matches salvage sequence (arms, food, water)

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
