# Title
SC001 CL006 Scene Stage Prompt

# ID
SC001_CL006_scene_stage_prompt

# Purpose
Describe staging intent for scene stage clip within heavy damage observation sequence showing Martian fleet retreat from hill crests with continuity markers maintained across banner designs and device shapes on ship prows, focusing on visible damage progression indicators like smoke trails and hull breaches as observed from the upper floor window.

# Workflow Type
authoring.scene_stage

# Positive Prompt
human male protagonist standing at upper floor window observing distant formation of twenty gray airships positioned over hill crests, daylight conditions bright midday, polished stone floor visible inside, dark wood window frame with metal accents, profile view facing outward, strange banners on ship prows visible in distance, odd devices mounted on vessel prows identifiable, smoke trails rising from hulls, minor damage indicators visible, ships drifting slightly southeast, valley floor visible below, hills beyond framing the action.

# Negative Prompt
night scene, indoor artificial lighting, different character attire, crowded street level inside window, modern technology props, incorrect fleet formation, dark wood frame missing metal accents, close up facial expressions only, single ship instead of twenty ships, banners dissolving in flame, green figures dropping at bullet explosions, no smoke trails, no hull breaches, wrong banner designs, missing device shapes.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL006
- duration_seconds: 5
- required_refs: SC001 beat bundle BT003.md, banner designs continuity markers across all shots, device shapes continuity markers across all shots, ship prow details visible in frame
- optional_refs: Hill crests depth context for close-ups, lighting consistency notes, interior lighting level warm contrast from CL001
- visible_character_assets: human male protagonist narrator observer
- look_continuity_policy: window frame consistent
- intended_lighting_change: morning to midday
- composition_type: cutaway detail shots maintaining continuity markers
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_continuity_marker_detail
- dependency_policy: dependent_on_all_previous_clip_continuity_elements
- auto_advance_policy: none
- fallback_strategy: cutaway_to_hill_crest_context
- consistency_assist_policy: enabled
- consistency_assist_method: banner design and device shape matching
- anatomy_repair_policy: minimal
- consistency_targets: ship count twenty, window framing elements, interior lighting level, banner designs, device shapes
- style_profile: action oriented
- batch_role: continuity detail shot
- fix_of: SC001_CL005_scene_stage_prompt

# Continuity Notes
- narrator maintains consistent distance from window frame throughout clip sequence
- window wiper position remains unchanged for continuity across all shots
- fleet positioned over hill crests in wide formation with angle toward plaza maintained
- lighting shifts from soft morning to brighter midday conditions visible in exterior shots
- floor material remains consistent polished stone tiles inside observation point
- ship count of twenty must be maintained in wide establishing shots
- banner designs on ship prows must be identifiable across all detail shots
- device shapes mounted on vessel prows must match visual notes from previous clips
- interior lighting level warm contrast must align with CL001 established conditions
- damage progression (smoke trails, hull breaches) must track logically across shots

# Repair Notes
- ensure narrator hand placement on window sill varies by emotional beat while maintaining continuity
- verify fleet formation consistency across shots with hill crest positioning maintained
- match daylight continuity conditions accurately between exterior and interior lighting levels
- check for any visible props or devices on ships matching visual notes from banner design continuity markers
- confirm ship prow details are visible in frame during cutaway detail shots
- validate that twenty ships remain visible in wide formation shots without counting errors
- ensure window frame elements including metal accents appear consistent across all angles
- fix smoke trail density to reflect heavy damage sustained phase of BT003

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
