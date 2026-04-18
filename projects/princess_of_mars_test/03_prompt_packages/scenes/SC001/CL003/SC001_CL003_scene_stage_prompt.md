# Title
SC001 CL003 Scene Stage Prompt

# ID
SC001_CL003_scene_stage_prompt

# Purpose
Establish staging intent for scene SC001 clip CL003, focusing on narrator's over-the-shoulder observation from upper floor window frame while twenty gray air ships retreat across hill crests in coordinated formation, conveying curiosity about sudden Martian fleet withdrawal and maintaining spatial continuity with preceding wide exterior shot

# Workflow Type
authoring.scene_stage

# Positive Prompt
narrator character standing at upper floor window frame interior room visible behind subject over-the-shoulder composition looking out at twenty gray air ships distributed across multiple hill crests in formation each carrying strange banners on prows and odd devices visible, natural sunlight gleaming on exterior landscape copper-skinned figure with anxious expression hand placement transitioning from sill to chest vertical axis from interior warm lighting to exterior cool landscape emotional weight of observation conveyed through eyeline movement tracking fleet distribution across terrain

# Negative Prompt
blurry window frame extra characters blocking view wrong number of ships misplaced ships relative to hill crests crowded valley text overlays distorted anatomy static camera without movement intent bright interior shadows mismatching exterior light hound obstructing window view line of sight wrong banner designs missing devices on ship prows

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md, Scene SC001 breakdown, Hill crests depth axis continuity notes
- optional_refs: Interior lighting level warm contrast, Movement timing consistency with retreat urgency, Vertical axis hill base to crest scale reference
- visible_character_assets: Narrator, Green Warriors
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: interior warm to exterior cool maintained
- composition_type: Over-the-shoulder from narrator to fleet
- continuity_mode: insert
- starting_keyframe_strategy: Approach window position establish exterior view first
- dependency_policy: Dependent on CL002 for spatial positioning and ship crest alignment
- auto_advance_policy: dependent_on_window_frame_and_fleet_position
- fallback_strategy: insert_narrator_body_turn_detail
- consistency_assist_policy: maintain_ship_positions_relative_to_crests
- consistency_assist_method: banner_visibility_across_shots
- anatomy_repair_policy: fix_mismatched_lighting_distorted_skin_texture
- consistency_targets: ship_count_20_window_framing_elements_banner_designs_device_shapes
- style_profile: sci-fi_adventure_war_observation
- batch_role: scene_stage_authoring
- fix_of: SC001_CL003_fix_01_prompt
- beat_ref: BT002
- workflow_type: authoring.scene_stage

# Continuity Notes
- Maintain narrator's movement path from corridor to window without skipping steps.
- Ensure lighting contrast between interior room and exterior valley remains consistent across shots.
- Keep hound positioned nearby but not obstructing the window view line of sight.
- Ship positions relative to hill crests must remain consistent with CL002 wide exterior positioning.
- Banner designs must be identifiable across all shots maintaining visual continuity markers.
- Window framing and interior elements must stay consistent throughout clip sequence.
- Number of ships (twenty) must be maintained in wide shots and visible through narrator eyeline.

# Repair Notes
- Fix any mismatched shadows on narrator's face caused by interior vs exterior light sources.
- Remove accidental characters or objects blocking the window frame visibility.
- Correct distorted anatomy if copper skin texture appears unnatural under sunlight.
- Ensure ship count remains exactly twenty across all wide shots and over-the-shoulder compositions.
- Verify banner designs are consistent with established continuity markers from preceding clips.
- Address any lighting level inconsistencies between interior warm tones and exterior cool landscape.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
