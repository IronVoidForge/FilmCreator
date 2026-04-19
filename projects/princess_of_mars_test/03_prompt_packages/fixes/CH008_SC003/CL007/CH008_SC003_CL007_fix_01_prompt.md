# Title
CH008_SC003 CL007 Fix 01 Prompt

# ID
CH008_SC003_CL007_fix_01_prompt

# Purpose
Correct local issues in the wide shot of the burning ship while preserving composition and look. Ensure fire spread pattern matches ignition point, smoke plume direction aligns with wind vector, and retreating Martians remain off the burning hull to maintain continuity with previous looting state.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot of full burning ship, gray low-profile vessel fully ablaze, fire spreading aft to forward sections, smoke plume rising vertically then dispersing, Martians retreating from immediate danger zone, distant warriors observing from safety, Martian buildings and valley background, southeast drift vector visible, funeral pyre transformation, water surface with ash debris scatter

# Negative Prompt
flickering artifacts, wrong color temperature, missing smoke, anatomy distortion on retreating figures, overexposed highlights, static water surface, extra characters on burning vessel, unburned hull sections, incorrect fire direction, dead sailors reappearing, ship stopping drift

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
- Ensure fire intensity increases over time from aft to forward sections.
- Verify Martians are positioned at safe distance, not on the burning hull.
- Maintain southeast drift vector consistency with previous drifting shots.
- Keep water surface dynamic with ash debris scatter visible.

# Repair Notes
- Correct any static fire spread to match ignition point progression.
- Adjust smoke plume direction to align with wind flow in valley.
- Remove any extra characters appearing on the burning vessel hull.
- Fix overexposed highlights on flames to maintain detail.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
