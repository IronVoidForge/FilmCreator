# Title
CH008_SC003 CL001 Scene Stage Prompt

# ID
CH008_SC003_CL001_scene_stage_prompt

# Purpose
Establish ship trajectory and unmanned state within wide tracking composition.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide angle view of gray low-profile vessel drifting southeast, banners on stem stern, glowing devices on prow, Martian buildings in background, distant green warriors, elevated observation points, valley lighting.

# Negative Prompt
Close-up faces, manned crew visible, cluttered foreground, wrong color palette, static camera, night scene, human female prisoner.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors distant, Martians elevated observation
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide tracking shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on ship drift vector from distance
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
- Ship drift vector southeast must match previous and next shots.
- Warrior positions relative to ship must remain consistent.
- Lighting matches valley scene context.

# Repair Notes
- If ship appears manned, remove crew immediately.
- If warriors too close, increase distance to maintain wide shot scale.
- Ensure banners and glowing devices are visible on vessel.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
