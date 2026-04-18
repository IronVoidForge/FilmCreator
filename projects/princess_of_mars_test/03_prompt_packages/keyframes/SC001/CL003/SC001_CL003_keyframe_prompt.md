# Title
SC001 CL003 Keyframe Prompt

# ID
SC001_CL003_keyframe_prompt

# Purpose
Establish upper floor window observation perspective showing exterior landscape and interior lighting contrast while maintaining spatial continuity with previous shot, capturing a frozen still of the observer at the window frame looking out at distant gray airships approaching under bright sunlight.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
A frozen still of a green-skinned figure standing at an upper floor window frame looking out at distant gray airships approaching under bright sunlight. The interior room shows polished stone tiles and wooden furniture with dim lighting contrasting the exterior glow. Outside, the landscape is barren with multiple ships visible in formation. Hand rests on window sill. Over-the-shoulder composition showing shoulder profile. Small hound companion visible in periphery without obstructing view. Natural light gleams on devices inside while the view remains clear and open.

# Negative Prompt
crowded streets, moving camera, dark shadows, night time, vehicles in valley, other characters blocking view, blurry details, text overlays, interior clutter, excessive motion, female companion present, specific character titles, names visible, proper nouns, human observer, John Carter, Sola, Woola.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md, Scene SC001 breakdown
- optional_refs: Valley/hills landscape details, natural light contrast
- visible_character_assets: green-skinned figure (at window), hound companion (nearby)
- look_continuity_policy: insert
- intended_lighting_change: brightening daylight
- composition_type: Over-the-Shoulder Observation
- continuity_mode: Window Frame Shadows Deepening
- starting_keyframe_strategy: Approach window position, establish exterior view first
- dependency_policy: Dependent on CL002 for spatial positioning
- auto_advance_policy: none
- fallback_strategy: Maintain sill position for first 2 seconds
- consistency_assist_policy: facial expression consistency
- consistency_assist_method: reference alignment
- anatomy_repair_policy: standard
- consistency_targets: window frame, lighting contrast
- style_profile: cinematic_compositional
- batch_role: keyframe
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain spatial positioning relative to previous clip
- Ensure lighting consistency between interior and exterior views
- Keep hound companion nearby but not obstructing the window view
- Window frame shadows deepen slightly as light changes
- Ship positions relative to hill crests must remain consistent

# Repair Notes
- Fix any facial expression inconsistencies
- Ensure window frame is clearly defined
- Correct lighting contrast if too flat
- Verify hound companion does not block main eyeline
- Check ship formation alignment with previous wide shot

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
