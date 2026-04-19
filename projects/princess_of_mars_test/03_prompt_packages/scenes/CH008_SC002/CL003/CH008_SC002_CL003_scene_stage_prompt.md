# Title
CH008_SC002 CL003 Scene Stage Prompt

# ID
CH008_SC002_CL003_scene_stage_prompt

# Purpose
Describe the stage intent for CL003 in CH008_SC002. This clip captures the enemy fleet's response to the Martian volley, specifically focusing on the lead vessel swinging broadside and firing while completing a circular arc. The staging must emphasize dynamic aerial tracking, clear weapon positioning, and smoke trails to indicate active engagement. Subject placement centers on the gray ship in the battle zone, with crew visible on deck operating weapons. Environmental context includes the open valley floor below and distant green warriors in building windows providing perspective depth. The intended visible opening frame setup begins with the ship in initial position with weapons charging, transitioning through the swing arc to full circle completion verified by smoke trails.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Gray low-profile vessel with banners on stem and stern, glowing devices on prow, deck crew operating weapons, smoke trails from firing points, aerial tracking perspective, broadside positioning, valley floor below, green warriors in building windows visible in distance, wide shot composition, dynamic movement, horizontal rotation around central pivot point, battle zone atmosphere.

# Negative Prompt
Static camera angle, wrong ship color, missing crew members, no smoke effects, incomplete swing arc, close-up only, ground level perspective, calm water, peaceful environment, single vessel focus without context, obscured banners, dim lighting.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: Scene breakdown for ship swing arc completion verification
- visible_character_assets: Enemy Fleet (lead vessel), Crew on deck, Smoke trails
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide aerial shot tracking lead vessel's 360-degree swing
- continuity_mode: Dynamic aerial tracking shot following ship movement
- starting_keyframe_strategy: Open on ship in initial position, weapons charging
- dependency_policy: Hard dependency on BT002 beat; must show full circle completion
- auto_advance_policy: Use reblock_same_scene if swing arc timing needs adjustment
- fallback_strategy: Use reblock_same_scene if swing arc timing needs adjustment
- consistency_assist_policy: Verify full circle completion and smoke trail progression
- consistency_assist_method: 
- anatomy_repair_policy: Ensure crew positions match firing operations context
- consistency_targets: 
- style_profile: Action-oriented aerial battle sequence
- batch_role: Lead vessel response coverage
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage. Full circle completion must be verified by smoke trails and visible rotation. Bullet drops at explosion points require timing consistency with BT002 beat. Banners dissolving in flame must show progressive damage tracking from contact points. Ship swing arc timing is critical; if adjustment is needed, use fallback strategy to reblock same scene.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If swing arc timing needs adjustment, apply fallback strategy using reblock_same_scene. Ensure crew positions match firing operations context during the swing. Verify smoke trail progression aligns with weapon discharge points. Check that banners show flame damage consistent with contact points from previous beats.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
