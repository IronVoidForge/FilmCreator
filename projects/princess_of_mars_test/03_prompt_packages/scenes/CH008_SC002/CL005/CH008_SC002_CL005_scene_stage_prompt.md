# Title
CH008_SC002 CL005 Scene Stage Prompt

# ID
CH008_SC002_CL005_scene_stage_prompt

# Purpose
Depict counter-battery discharge from damaged fleet ships in valley environment, focusing on close-up weapon muzzle flash during Martian crew firing sequence. Subject placement centers on Green Martian crew members huddled behind ship structures with weapons elevated and firing toward ridge positions. Environmental context includes daylight illumination with fire glow from hull burns and smoke trails visible against valley background. Intended visible opening frame setup establishes static focus on weapon barrel and muzzle flash intensity, ensuring continuity of return fire arcs before debris field expands.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian crew members firing weapons from damaged ship structures, close-up on weapon muzzle flash with glow build, smoke trails visible against valley background, hull fires burning with banners partially dissolved, daylight illumination with subtle fire glow, hills beyond in distance, vertical firing angle from lower elevation, crew huddled behind ship structures, weapons elevated and discharging, debris falling from impact points, low gray-painted airship design with scorched hulls.

# Negative Prompt
Human crew members on airship deck, Earthling woman present in frame, intact hulls without damage or fire ignition, green Martian skin appearing human tone or brown, excessive flames consuming hull prematurely, missing smoke trails obscuring visibility, wrong number of ships visible, ship structure collapsing before debris field expands, boarding equipment visible, food supplies gathered, water containers filled, funeral pyre ritual initiated.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5.0
- required_refs: BT002 index, CL004 medium shot
- optional_refs: smoke trails visible
- visible_character_assets: Martian crew members firing weapons from ship structures
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static on weapon muzzle
- dependency_policy: parallel to medium shot for coverage
- auto_advance_policy: 
- fallback_strategy: cutaway to fire arcs if flash timing varies
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- opening_keyframe_intent: focus on counter-battery discharge intensity
- cut_motion_intent: match cut to return vector
- interval_beats: 0-1s glow build, 1-3s muzzle flash burst, 3-5s recoil shake

# Continuity Notes
- Maintain consistent hull damage state as scorched with burning fires for this beat.
- Ensure number of ships visible aligns with wide shot showing single unmanned focal point among damaged ones.
- Verify smoke trails are visible against valley background without excessive obscuring.
- Track forward keyframe strategy ensures smooth transition from window POV to ship deck coverage.
- Keep lighting consistent with daylight transitioning to salvage focus, avoiding full pyre illumination.

# Repair Notes
- Fix skin tone to green if appearing human or brown in generated frames.
- Ensure no fire effects are present on hull before this specific beat sequence initiates.
- Verify weapon barrel and muzzle flash visible during close-up shot.
- Correct ship orientation to match low, gray-painted airship design specifications.
- Remove any Earthling woman figures from frame as she belongs to different narrative context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
