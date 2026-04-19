# Title
CH008_SC003 CL007 Scene Stage Prompt

# ID
CH008_SC003_CL007_scene_stage_prompt

# Purpose
Describe the stage intent for CL007, which is a wide shot of the burning ship acting as a funeral pyre. The scene shows the aftermath of looting where the Martians have set the vessel ablaze with a missile. The ship drifts southeast while smoke rises. Martians are retreating from the immediate danger zone to maintain safety.

# Workflow Type
authoring.scene_stage

# Positive Prompt
A wide shot of a gray low-profile ship fully ablaze, drifting southeast as a funeral pyre, smoke plume rising vertically then dispersing against sky backdrop, banners dissolving in flame on stem and stern, glowing devices on prow flickering in firelight, green-skinned Martians retreating from immediate danger zone to distant safety positions, buildings in background providing scale reference for burning vessel, ash and debris scattering on water surface.

# Negative Prompt
Close-up of human faces, detailed facial expressions of Martians, intact crew members on ship, specific item removal actions, missile deployment action, interior shots of ship compartments, bright daylight without fire glow, static camera without drift motion, characters remaining on burning vessel.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL007
- duration_seconds: 5
- required_refs: BT003.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (retreating), Warriors (distant safety)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on missile ignition point
- dependency_policy: none
- auto_advance_policy: 
- fallback_strategy: insert if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ship drift vector continues southeast throughout clip.
- Fire spread pattern moves from aft to forward sections.
- Martians retreat from immediate danger zone while ship burns.
- Warriors maintain distance for safety, no characters remain on burning vessel.
- Smoke plume rises vertically then disperses with wind direction.

# Repair Notes
- Ensure fire intensity increases over time as per beat progression.
- Verify character visibility in wide shot does not contradict retreating action.
- Check that ship hull shows progressive damage consistent with burning state.
- Maintain consistency of drift path against background buildings.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
