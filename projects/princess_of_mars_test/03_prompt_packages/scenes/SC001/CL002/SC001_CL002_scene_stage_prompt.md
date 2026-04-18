# Title
SC001 CL002 Scene Stage Prompt

# ID
SC001_CL002_scene_stage_prompt

# Purpose
Define staging intent for the balcony combat preparation scene, establishing subject placement on the ledge and environmental context for the opening frame setup.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium shot of green-skinned warriors positioned on stone balcony ledge, weapons held ready at stations, spears and banners visible, distant gray airships in sky above valley vista, clear daylight conditions, urban city buildings in background, combat tension atmosphere, vertical axis established between elevated warriors and distant fleet

# Negative Prompt
interior corridor space, human figure walking forward, bright sunlight glare, crowd of civilians, static camera movement, wide establishing shot, cartoon style, floating funeral pyre, close-up on faces only

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 overview
- optional_refs: Window frame for spatial continuity
- visible_character_assets: Green Martian Warriors (collective on balcony/ledge), Airships (distant in sky)
- look_continuity_policy: Follows CL001 observation sequence
- intended_lighting_change: Clear daylight conditions
- composition_type: Medium shot of warriors on balcony
- continuity_mode: Cut to combat preparation
- starting_keyframe_strategy: Warriors positioned, weapons ready for engagement
- dependency_policy: Follows CL001 observation sequence
- auto_advance_policy: Insert close-up on weapon stations if warriors not visible
- fallback_strategy: Insert close-up on weapon stations if warriors not visible
- consistency_assist_policy: Maintain spatial continuity from previous clip
- consistency_assist_method: Narrator position must align with corridor axis
- anatomy_repair_policy: Fix anatomy if limbs distort during movement
- consistency_targets: Height of narrator vs city, color of airships vs buildings, number of ships visible
- style_profile: authoring.scene_stage
- batch_role: planning
- fix_of: SC001_CL002_scene_stage_prompt.md
- workflow_type: authoring.scene_stage

# Continuity Notes
- Maintain spatial continuity from previous clip
- Warrior positioning must align with balcony axis
- Lighting must reflect exterior view consistency
- Woola remains trailing narrator throughout movement

# Repair Notes
- Fix anatomy if limbs distort during movement
- Ensure background portal remains consistent
- Correct lighting balance between entrance and corridor

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
