# Title
CH008_SC003 CL001 Fix 01 Prompt

# ID
CH008_SC003_CL001_fix_01_prompt

# Purpose
Preserve composition and look while fixing local issues for the wide tracking shot of the drifting ship. Use image_1 as the approved still base and image_2 as a secondary reference when needed to maintain continuity with the disabled vessel trajectory and unmanned state.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Gray low-profile vessel, long shape, banners on stem and stern, glowing devices on prow, drifting southeast vector, unmanned state, distant green-skinned warriors, elevated observation positions, urban Martian architecture background, open valleys, distant hills, wide tracking shot composition, smooth motion blur, atmospheric lighting, cinematic scale.

# Negative Prompt
Human female prisoner, green skin on humans, extra limbs, distorted hull, wrong color ship, crowded buildings, close-up details, visible crew members, fire effects, smoke plume, burning ship, dead sailors, looting actions, missile ignition, close-range view.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (distant), Martians (elevated observation)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide tracking shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on ship drift vector from distance
- dependency_policy: none
- auto_advance_policy: 
- fallback_strategy: insert if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- note Ship axis follows southeast drift vector with unmanned state visible from south position.
- note Warriors approach from north/south positions toward ship drift path without boarding in this shot.
- note Environment shows urban Martian architecture and open valleys providing scale reference for vessel size.

# Repair Notes
- note Ensure banners on stem/stern are clearly visible to identify vessel type.
- note Maintain hull integrity as disabled but intact, avoiding battle damage distortion.
- note Avoid including any crew members or human figures on the ship deck in this wide shot.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
