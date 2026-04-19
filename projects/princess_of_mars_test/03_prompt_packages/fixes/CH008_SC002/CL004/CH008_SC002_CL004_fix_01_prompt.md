# Title
CH008_SC002 CL004 Fix 01 Prompt

# ID
CH008_SC002_CL004_fix_01_prompt

# Purpose
Correct local inconsistencies in the approved still base while maintaining the established window POV composition and lighting continuity for the unmanned ship discovery beat.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green Martian warriors positioned at building windows overlooking valley floor, single undamaged gray airship floating in sky among damaged vessels, smoke rising from burning ships, daylight illumination, boarding equipment visible near ship hull, no crew on deck, window frame foreground obstruction, wide medium shot composition

# Negative Prompt
distorted anatomy, extra limbs, wrong colors, text, watermark, blurry, low resolution, inconsistent lighting, floating debris, crew members on deck, damaged hull where intact, missing smoke, overexposed, underexposed

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL004
- duration_seconds: 5.0
- required_refs: Ship hull intact but vulnerable, no crew visible on deck, boarding equipment being prepared
- optional_refs: Window frame
- visible_character_assets: Martians at windows observing unmanned ship, Narrator noting opportunity
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/Medium
- continuity_mode: cutaway
- starting_keyframe_strategy: zoom_in
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain window POV obstruction
- Ensure single undamaged ship among damaged ones
- Preserve daylight lighting with smoke glow

# Repair Notes
- Fix Martian anatomy at windows
- Correct ship damage consistency
- Adjust color grading to match previous beats

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
