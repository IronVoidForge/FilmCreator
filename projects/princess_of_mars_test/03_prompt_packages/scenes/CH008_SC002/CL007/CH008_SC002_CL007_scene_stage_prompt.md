# Title
CH008_SC002 CL007 Scene Stage Prompt

# ID
CH008_SC002_CL007_scene_stage_prompt

# Purpose
Describe the stage intent for CL007 within CH008_SC002, focusing on visualizing the conclusion of the aerial engagement with a wide tracking shot following the damaged fleet departing from the Martian valley floor. The subject placement centers on multiple gray vessels moving away from the battle zone, emphasizing damage indicators and smoke trails to maintain continuity with the BT004 beat.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Gray low-profile vessels with banners on stem and stern, glowing devices on prow, smoke trails rising from damaged craft, multiple ships limping in retreat, wide aerial perspective tracking movement away from valley floor, battle zone visible in background, damage indicators on hulls, long shape profile, gray painted surface, drifting southeast trajectory.

# Negative Prompt
Close-up of faces, static camera angle, intact or new vessels, wrong color palette, close-range shots, bright sunny lighting, single ship only, green skin warriors in foreground, building interiors visible, vertical composition, low-angle shot, explosion effects not from damage.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5
- required_refs: BT004.md - Fleet Retreat with Damage beat bundle
- optional_refs: Wide retreat tracking shots coverage families
- visible_character_assets: Enemy Fleet (multiple vessels showing damage), Smoke trails
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide aerial shot tracking fleet moving away from battle zone
- continuity_mode: Wide tracking shot following fleet departure from valley
- starting_keyframe_strategy: Open on fleet in damaged condition, several craft limping
- dependency_policy: Hard dependency on BT004 beat; must show retreat completion
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ensure damage progression is consistent with BT004 beat; smoke trails must persist throughout the clip.
- Retreat path must lead away from valley exit without looping back to engagement point.
- Avoid showing intact ships in fleet; all vessels must display visible damage indicators.
- Maintain wide aerial perspective; do not cut to close-ups of individual ship components.

# Repair Notes
- If ships look too new, add damage overlays or adjust hull texture to show scorch marks.
- If movement is too static, increase tracking motion intensity to match fleet departure velocity.
- Ensure smoke trails do not dissipate completely before clip end; maintain atmospheric consistency.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
