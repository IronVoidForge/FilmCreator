# Title
CH008_SC003 CL004 Fix 01 Prompt

# ID
CH008_SC003_CL004_fix_01_prompt

# Purpose
Fill in the stage intent here. This prompt corrects local generation issues for CL004 while preserving the over-the-shoulder composition and Martian looting action continuity within the disabled ship interior scene.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green-skinned Martians inside gray ship interior over-the-shoulder view looting removing arms swords collecting silks jewels dead sailors stationary background banners visible hull intact lighting consistent with urban Martian architecture systematic search and removal of valuables from vessel compartments

# Negative Prompt
human faces wrong skin tones fire unless burning phase cluttered backgrounds incorrect anatomy bright daylight indoor shadows inconsistent floating debris without context wrong weapon types

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (looting), Dead Sailors (stationary)
- look_continuity_policy: 
- intended_lighting_change: 
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
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Maintain green skin tone consistency for all Martian figures in this shot
- Ensure dead sailors remain stationary and do not interact with looting actions
- Track specific items removed (arms, silks, jewels) for visual continuity across clips
- Preserve ship interior layout including banners on stem/stern and glowing devices on prow

# Repair Notes
- Fix any anatomy errors in Martian hands or shoulders visible in over-the-shoulder frame
- Correct lighting to match indoor ship environment rather than outdoor daylight
- Ensure no human artifacts appear where Martians should be present during looting phase
- Adjust composition to keep focus on systematic search and removal actions

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
