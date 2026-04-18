# Title
SC001 CL002 Scene Stage Prompt

# ID
SC001_CL002_scene_stage_prompt

# Purpose
Define staging intent for the Martian retreat observation scene, establishing subject placement at the elevated vantage point and environmental context for the opening frame setup. Focus on the transition from interior safety to exterior scale while maintaining continuity with previous window observation sequence. Ensure the visual emphasizes the sudden Martian retreat and narrator's investigation of cause from upper floor window perspective.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Elevated vantage point setup with male warrior observer positioned at window frame, distant procession of green Martians descending over hill crest in background, clear daylight conditions illuminating figures, city rooftops visible below establishing scale, valley vista expanding as Martians approach, vertical axis established between observers and approaching vessels, upper floor observation point context maintained.

# Negative Prompt
interior corridor space, human figure walking forward, bright sunlight glare, crowd of civilians, static camera movement, wide establishing shot only, cartoon style, floating funeral pyre, close-up on faces only, indigenous warriors on balcony ledge, human woman prisoner visible, wrong ship count, incorrect banner designs.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 overview, BT002.md for completion planning
- optional_refs: Window frame for spatial continuity
- visible_character_assets: male warrior observer, gray airships distant figures
- look_continuity_policy: Follows CL001 observation sequence
- intended_lighting_change: Clear daylight conditions
- composition_type: Wide Establishing Shot / Medium Two-shot
- continuity_mode: Fleet Formation Consistent
- starting_keyframe_strategy: First airship visible in distance, fleet beginning to form pattern
- dependency_policy: Follows CL001 observation sequence
- auto_advance_policy: Insert close-up on weapon stations if warriors not visible
- fallback_strategy: Insert close-up on weapon stations if warriors not visible
- consistency_assist_policy: Maintain spatial continuity from previous clip
- consistency_assist_method: Narrator position must align with window axis
- anatomy_repair_policy: Fix anatomy if limbs distort during movement
- consistency_targets: Height of narrator vs city, color of airships vs buildings, number of ships visible
- style_profile: authoring.scene_stage
- batch_role: planning
- fix_of: SC001_CL002_scene_stage_prompt.md
- workflow_type: authoring.scene_stage

# Continuity Notes
- Maintain spatial continuity from previous clip
- Warrior positioning must align with window axis
- Lighting must reflect exterior view consistency
- Fleet formation must match visual continuity notes from chapter summary daylight conditions
- Window frame color and wiper position remain unchanged for continuity
- Ship count (twenty) must be maintained in wide shots
- Banner designs must be identifiable across shots
- Hill crest depth axis reference points consistent

# Repair Notes
- Fix anatomy if limbs distort during movement
- Ensure background portal remains consistent
- Correct lighting balance between entrance and corridor
- Verify ship props match visual continuity notes from chapter summary daylight conditions
- Check eyeline alignment with shoulder height approximately five feet eight inches
- Confirm interior warm lighting contrast to exterior cool lighting

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
