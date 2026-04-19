# Title
CH008_SC002 CL005 Scene Stage Prompt

# ID
CH008_SC002_CL005_scene_stage_prompt

# Purpose
Define the visual staging intent for the tactical boarding sequence within the valley city environment, capturing the transition from building windows to the unmanned airship deck while establishing the salvage operation context without initiating the funeral pyre ritual. Subject placement focuses on Green Martian warriors moving onto the vessel with boarding equipment deployed. Environmental context includes daylight illumination with subtle fire glow from distant battle and the gray airship hull intact but vulnerable. Intended visible opening frame setup establishes the boarding trajectory from window perspective to ship deck medium shots, ensuring continuity of the salvage phase before loot collection begins.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian warriors transitioning from building windows to gray airship deck, tactical boarding equipment deployed, unarmed ship hull intact, daylight illumination with subtle fire glow from distant battle, loot items visible in storage areas, valley city background with hills beyond, wide shot composition showing boarding trajectory, medium shots of individual Martians moving onto vessel, arms and weapons secured on deck, food supplies gathered, water containers filled, no active flames consuming hull yet.

# Negative Prompt
Human crew members on airship deck, active funeral pyre flames consuming hull, Earthling woman present in frame, damaged hulls inconsistent with salvage phase, excessive smoke obscuring visibility, wrong number of ships visible, green Martian skin appearing human tone, fire effects starting before loot collection, ship structure collapsing prematurely, boarding equipment missing or broken.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: ship deck accessible, boarding equipment deployed
- optional_refs: window frame
- visible_character_assets: Martians transitioning from windows to ship deck
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: 
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: track_forward
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
- Maintain consistent hull state as intact but vulnerable without fire ignition for this beat.
- Ensure number of ships visible aligns with wide shot showing single unmanned focal point among damaged ones.
- Verify boarding equipment is present and deployed before Martians step onto deck.
- Keep lighting consistent with daylight transitioning to salvage focus, avoiding full pyre illumination.
- Track forward keyframe strategy ensures smooth transition from window POV to ship deck coverage.

# Repair Notes
- Fix skin tone to green if appearing human or brown in generated frames.
- Ensure no fire effects are present on the hull for this specific beat sequence.
- Verify boarding equipment is visible and functional before character movement onto vessel.
- Correct ship orientation to match low, gray-painted airship design specifications.
- Remove any Earthling woman figures from frame as she belongs to different narrative context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
