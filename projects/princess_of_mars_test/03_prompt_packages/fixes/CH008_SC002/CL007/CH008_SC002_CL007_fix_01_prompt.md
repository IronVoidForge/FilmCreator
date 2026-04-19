# Title
CH008_SC002 CL007 Fix 01 Prompt

# ID
CH008_SC002_CL007_fix_01_prompt

# Purpose
Corrective still generation for fleet retreat sequence. Preserves battle conclusion visual state and damage progression from previous engagement beats while fixing local artifacts.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
gray low-profile vessels, damaged hulls, smoke trails, retreating from valley floor, banners on stem stern, glowing devices on prow, limping movement, wide aerial perspective, battle zone background, dusk lighting, cinematic composition

# Negative Prompt
upright ships, fresh paint, no smoke, wrong color palette, blurry motion, missing damage indicators, incorrect perspective, floating debris, bright daylight, clean hulls

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5
- required_refs: BT004.md
- optional_refs: wide retreat tracking shots coverage families
- visible_character_assets: Enemy Fleet (multiple vessels showing damage), Smoke trails
- look_continuity_policy: Hard dependency on BT004 beat; must show retreat completion
- intended_lighting_change: 
- composition_type: Wide aerial shot tracking fleet moving away from battle zone
- continuity_mode: Wide tracking shot following fleet departure from valley
- starting_keyframe_strategy: Open on fleet in damaged condition, several craft limping
- dependency_policy: Hard dependency on BT004 beat; must show retreat completion
- auto_advance_policy: 
- fallback_strategy: Use reblock_same_scene if need to adjust retreat path angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain damage progression consistent with BT004 beat bundle.
- Ensure ship swing arc and retreat path align with valley floor perspective.
- Verify smoke trails originate from damaged craft and match previous engagement effects.
- Preserve banner flame damage state from battle conclusion sequence.

# Repair Notes
- Fix ship posture to reflect limping retreat rather than upright positioning.
- Adjust banner flame damage to show progressive destruction consistent with battle end.
- Enhance smoke density on damaged vessels to match wide tracking shot requirements.
- Correct perspective distortion if ships appear floating or detached from valley floor.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
