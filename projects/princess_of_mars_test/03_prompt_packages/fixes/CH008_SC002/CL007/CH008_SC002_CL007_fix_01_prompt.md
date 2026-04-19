# Title
CH008_SC002 CL007 Fix 01 Prompt

# ID
CH008_SC002_CL007_fix_01_prompt

# Purpose
Corrective still-generation preserving composition and look while fixing local issues. Ensure fire illumination consistency, smoke texture volume, and absence of crew members on unmanned ship deck. Maintain established solemnity of funeral pyre ritual from valley floor perspective.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
burning gray warship fully ablaze, fire consuming ship structure, thick smoke rising into valley sky, green warriors surrounding funeral pyre, solemn atmosphere, wide shot from valley floor perspective, medium shots of Martians around fire, human observer window POV context, no visible crew on deck, dramatic fire illumination, volumetric smoke effects, desert city background with hills beyond

# Negative Prompt
text, watermark, blurry, distorted anatomy, extra limbs, modern objects, crew members, visible people on ship deck, bright daylight without fire glow, low resolution, deformed faces, bad hands, floating debris, unnatural lighting, cartoonish style

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5.0
- required_refs: Ship fully ablaze, smoke rising, fire consuming ship structure, no visible crew remaining
- optional_refs: Window frame
- visible_character_assets: Martians surrounding burning ship; Narrator observing pyre ritual
- look_continuity_policy: preserve_style_profile
- intended_lighting_change: fire_illumination_dominant
- composition_type: Wide/Medium/POV
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: pan_across
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
- Ensure single burning ship is focal point without other vessels in immediate frame
- Martians must be present around pyre but not obstructing view of flames
- Narrator POV context should be subtle if window frame included
- Fire intensity must match ritual solemnity, not chaotic explosion
- Smoke density should increase as burn progresses within clip duration

# Repair Notes
- Fix fire lighting consistency on green warrior faces to avoid flat shading
- Verify no crew members appear on ship deck during salvage or burning sequence
- Adjust smoke texture to be volumetric and not flat gray overlay
- Ensure window frame obstruction is handled naturally if present in composition
- Maintain valley floor perspective for wide shots of burning ship

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
