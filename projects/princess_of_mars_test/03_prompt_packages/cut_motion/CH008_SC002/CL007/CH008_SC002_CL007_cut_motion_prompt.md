# Title
CH008_SC002 CL007 Cut Motion Prompt

# ID
CH008_SC002_CL007_cut_motion_prompt

# Purpose
Execute broadside maneuver for fleet ships during combat engagement. Camera captures wide shot of formation change and crew realignment on damaged vessels within the valley environment.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian fleet ships swinging broadside in valley, damaged hulls visible with scorched plating, crew members moving to new firing positions, smoke rising from previous impacts, daylight illumination, ship thrusters swaying, debris field expanding, banners fluttering in wind.

# Negative Prompt
Ships stationary, burning funeral pyre, cold daylight without fire illumination, distorted Martian anatomy, sudden lighting changes unrelated to combat smoke, missing limbs, wrong character count, blurry ship rotation effects, green skin turning brown.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5.0
- required_refs: Fleet ships swinging broadside, damaged hulls visible, crew moving to new positions, smoke rising from impacts
- optional_refs: Banners fluttering, debris field expanding
- visible_character_assets: Green Martian fleet crews on damaged ships
- look_continuity_policy: reframe_same_moment
- intended_lighting_change: Daylight dominant with smoke haze
- composition_type: Wide shot of formation change
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: staggered formation static hold
- dependency_policy: sequential to crew realignment medium shot
- auto_advance_policy: 
- fallback_strategy: insert ship rotation if thruster sway varies
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain ship formation change and rotation motion throughout the sequence.
- Ensure crew members are actively moving to new firing positions to match beat plan.
- Preserve smoke density from previous impacts without introducing unrelated fire sources.
- Keep damaged hull state consistent (scorched plating, thruster sway) across frames.

# Repair Notes
- If ships appear stationary, increase rotation motion and thruster sway in prompt.
- If burning funeral pyre appears, reduce fire intensity to match daylight combat scene.
- If crew members are missing from deck, add them moving to new positions.
- Ensure green skin tone remains consistent under daylight without washing out.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
