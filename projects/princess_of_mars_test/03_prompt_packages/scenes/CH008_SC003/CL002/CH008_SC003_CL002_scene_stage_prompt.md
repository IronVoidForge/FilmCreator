# Title
CH008_SC003 CL002 Scene Stage Prompt

# ID
CH008_SC003_CL002_scene_stage_prompt

# Purpose
Define the visual staging intent for the medium shot capturing green warriors approaching the disabled gray airship within the Martian valley environment, ensuring continuity with the drifting ship trajectory and elevated observer positions.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium shot, green-skinned martian warriors approaching disabled gray low-profile airship, drifting southeast vector, banners on stem stern, glowing devices on prow, martian buildings in background, open valley, daylight, smoke haze, warrior eyeline tracking ship movement, elevated martians observing from windows.

# Negative Prompt
human woman prisoner, blue sky, green warriors melting into mist prematurely, wrong anatomy, extra limbs, distorted faces, burning ship yet, close-up of looting items, dead sailors visible in foreground, static camera, low resolution, text, watermark.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (approaching), Martians (elevated)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium shot
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: open on warrior eyeline tracking ship
- dependency_policy: depends on CL001
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
- Maintain ship drift vector southeast consistency with CL001.
- Ensure green warriors approach from north/south positions without melting prematurely.
- Keep elevated martian observation points static relative to building windows.
- Avoid showing human woman prisoner in this clip sequence.

# Repair Notes
- Correct Martian anatomy if skin tone appears too human or vice versa.
- Ensure ship hull remains intact (no fire damage yet).
- Verify lighting matches previous clips (daytime, smoke haze).

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
