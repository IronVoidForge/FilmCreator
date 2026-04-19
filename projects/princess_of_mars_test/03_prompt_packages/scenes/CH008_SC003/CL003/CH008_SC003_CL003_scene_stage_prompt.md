# Title
CH008_SC003 CL003 Scene Stage Prompt

# ID
CH008_SC003_CL003_scene_stage_prompt

# Purpose
Define visual setup for CL003 within SC003, focusing on boarding initiation detail via grappling hook deployment. Establish close-up composition on mechanical action and Green Warrior hands interacting with ship hull. Ensure continuity of ship drift vector southeast and connection to previous clip approach sequence.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green warrior hands deploying grappling hook, gray ship hull drifting southeast, water surface reflection, distant Martian observation from elevated position, banners visible on stem, daylight with smoke haze, close-up composition on mechanical action, green skin texture, ship hull damage marks, rope tension visible.

# Negative Prompt
Human faces, night scene, static background, excessive smoke obscuring subject, wrong skin tone, floating debris without physics, blurry focus on hands, civilian clothing, bright sun glare, water surface distortion inconsistent with wind direction.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (hands), Martians (observation)
- look_continuity_policy: insert
- intended_lighting_change: consistent with battle aftermath
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: open on hook deployment action
- dependency_policy: depends on CL002
- auto_advance_policy: none
- fallback_strategy: cutaway if needed
- consistency_assist_policy: enabled
- consistency_assist_method: anatomy check
- anatomy_repair_policy: strict
- consistency_targets: ship position, hand anatomy
- style_profile: authoring.scene_stage
- batch_role: scene_stage
- fix_of: CL002 approach sequence

# Continuity Notes
- Ship drift vector must remain southeast throughout clip.
- Hook release timing aligns with boarding initiation beat.
- Green Warrior hands match previous clip skin tone and anatomy.
- Distant Martians maintain elevated observation position relative to ship.
- Water surface reflection consistent with wind direction from battle smoke.

# Repair Notes
- Ensure Martian hand anatomy differs from human hand if visible in background.
- Verify ship hull damage marks match previous clips for continuity.
- Check that hook deployment does not obscure distant observation figures.
- Repair any lighting inconsistencies caused by smoke haze effects.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
