# Title
CH008_SC002 CL001 Fix 01 Prompt

# ID
CH008_SC002_CL001_fix_01_prompt

# Purpose
Corrective still generation for BT001, preserving window POV composition and ship scale while fixing local artifacts based on approved image_1 anchor.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Narrator eye extreme close-up window frame foreground twenty gray airships approaching valley floor daylight dramatic tension green-skinned warriors aesthetic deserted city buildings hills beyond

# Negative Prompt
distorted anatomy extra limbs wrong lighting blurry details inconsistent style missing ships incorrect geography wrong character count

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5.0
- required_refs: Window frame, twenty gray airships, valley floor
- optional_refs: Martians (not yet active)
- visible_character_assets: Narrator (window observer)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV/Wide
- continuity_mode: reblock_same_scene
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
- Maintain 20 ship count exactly
- Window POV angle fixed relative to building frame
- Valley floor visible below window level
- Daylight lighting state preserved

# Repair Notes
- Preserve image_1 composition strictly
- Fix local artifacts only (anatomy, lighting consistency)
- Ensure Klein distilled consistency with anchor
- Do not alter ship scale or approach trajectory

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
