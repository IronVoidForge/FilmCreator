# Title
CH008_SC002 CL004 Keyframe Prompt

# ID
CH008_SC002_CL004_keyframe_prompt

# Purpose
Establish the unmanned target vessel and tactical observation point for boarding preparation within the aerial conflict sequence.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide angle view of valley floor with multiple gray airships, one hull intact among damaged ones, smoke rising from breached vessels, green warriors positioned at building windows observing unmanned craft, window frame visible in foreground, daylight lighting with haze.

# Negative Prompt
crew on deck, burning ship yet, loot collected, nighttime, wrong number of ships, close-up on face only, human female captive visible.

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
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain count of twenty airships total with nineteen damaged and one undamaged.
- Ensure ship hull remains intact but vulnerable without visible crew activity on deck.
- Keep green warriors positioned at building windows observing the unmanned craft.
- Preserve daylight lighting conditions consistent with valley floor visibility.

# Repair Notes
- Apply anatomy repair policy to ensure green warrior figures are consistent across shots.
- Use consistency assist method to maintain ship hull integrity and damage state.
- Verify window frame obstruction remains visible in foreground for continuity.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
