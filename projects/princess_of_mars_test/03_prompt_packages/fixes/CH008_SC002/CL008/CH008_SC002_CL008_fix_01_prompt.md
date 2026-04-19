# Title
CH008_SC002 CL008 Fix 01 Prompt

# ID
CH008_SC002_CL008_fix_01_prompt

# Purpose
Resolve scene through wide shot showing ship being towed away with finality. Maintain continuity with burning ship state from BT007. Ensure Martians operate towing equipment while Narrator observes from window POV.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot, valley city background, gray warship fully consumed by fire but being towed away, Martian figures operating towing equipment, Narrator POV from window secondary ref, dramatic fire illumination mixed with daylight, deserted buildings in valley, hills beyond horizon.

# Negative Prompt
No crew on ship, no undamaged ships visible, no sudden movement breaking continuity, no modern elements, no excessive smoke obscuring the ship entirely, no green Martian anatomy errors, no floating debris unrelated to salvage.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Ship fully consumed by fire, towing equipment deployed, ship moving away from building
- optional_refs: Window frame
- visible_character_assets: 
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/POV
- continuity_mode: cutaway
- starting_keyframe_strategy: static_hold
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
- Only the one being towed should be prominent in frame
- Martians engaged in towing not just standing
- Narrator position window POV consistent with previous beats
- Fire intensity allows visibility for towing action

# Repair Notes
- Ensure ship is clearly moving away across valley floor
- Fire intensity matches BT007 climax but allows visibility for towing
- Martians engaged in towing not just standing around fire
- Avoid anatomy errors on Martian figures operating equipment

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
