# Title
CH008_SC002 CL003 Cut Motion Prompt

# ID
CH008_SC002_CL003_cut_motion_prompt

# Purpose
Execute dynamic aerial tracking shot following lead vessel's 360-degree swing arc, maintaining continuity from approved keyframe and preserving lighting grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
gray low-profile vessel swinging horizontally around central pivot point, smoke trails expanding from firing points, crew on deck operating weapons, banners fluttering in flame damage, aerial camera tracking rotation, valley floor visible below, consistent lighting and grade preserved, urban architecture background.

# Negative Prompt
static image, morphing ship structure, extra vessels appearing, distorted crew anatomy, lighting shift, wrong color palette, sudden jump cuts, banner dissolving too fast, smoke disappearing, green skin on vessel, human face on enemy crew.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: 
- visible_character_assets: Enemy Fleet, Crew on deck, Smoke trails
- look_continuity_policy: Hard dependency on BT002 beat
- intended_lighting_change: Preserve keyframe lighting and grade by default
- composition_type: Wide aerial shot tracking lead vessel's 360-degree swing
- continuity_mode: Dynamic aerial tracking shot following ship movement
- starting_keyframe_strategy: Open on ship in initial position, weapons charging
- dependency_policy: Hard dependency on BT002 beat; must show full circle completion
- auto_advance_policy: 
- fallback_strategy: Use reblock_same_scene if swing arc timing needs adjustment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Capture the continuity rules for this stage.
- Ensure swing arc completes full circle within duration.
- Maintain bullet drop timing at explosion points relative to ship rotation.
- Track banner flame damage progression from contact points without over-dissolving.
- Keep valley floor perspective consistent during aerial tracking.

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- Adjust motion speed if swing feels rushed or sluggish.
- Fix anatomy if crew distorts during rotation.
- Reblock same scene if timing adjustment is required.
- Verify smoke trails persist throughout the arc without vanishing prematurely.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
