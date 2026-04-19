# Title
CH008_SC003 CL004 Scene Stage Prompt

# ID
CH008_SC003_CL004_scene_stage_prompt

# Purpose
Define staging for over-the-shoulder looting sequence, emphasizing systematic item removal and Martian movement within ship interior.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green-skinned Martians moving through gray ship interior compartments, picking up arms silks jewels food containers water carboys, dead sailors stationary in background, over-the-shoulder perspective, dim interior lighting.

# Negative Prompt
Human faces, modern clothing, bright sunlight, clutter obscuring action, burning fire effects (save for later beat), floating debris.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (looting), Dead Sailors (stationary)
- look_continuity_policy: track item removal and movement logic
- intended_lighting_change: maintain interior dimness consistent with ship hull
- composition_type: over-the-shoulder shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on Martians entering main deck
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
- Track specific items removed for continuity (arms, silks, jewels, food/water).
- Ensure movement follows aft to forward sections within ship compartments.
- Maintain consistency with previous boarding shot (CL003) regarding Martian appearance and ship interior state.
- Dead sailors must remain stationary throughout the sequence.

# Repair Notes
- Address potential anatomy inconsistencies in Martian hands and arms during item handling.
- Ensure lighting does not shift to exterior brightness or fire glow prematurely (burning occurs in BT003).
- Verify ship interior texture matches previous clips to avoid environmental drift.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
