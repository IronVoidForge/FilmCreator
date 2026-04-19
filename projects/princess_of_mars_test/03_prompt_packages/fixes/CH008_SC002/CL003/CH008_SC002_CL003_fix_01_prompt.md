# Title
CH008_SC002 CL003 Fix 01 Prompt

# ID
CH008_SC002_CL003_fix_01_prompt

# Purpose
Refine still generation for clip CL003 (BT003) to ensure accurate depiction of damaged airships and salvage context while maintaining visual continuity with preceding shots. Focus on hull breaches, smoke progression, and the single intact unmanned ship as focal point. Correct local artifacts such as distorted Martian figures or inconsistent lighting between window POV and valley floor view.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot of twenty gray airships approaching valley floor, hull breaches visible, smoke rising from damaged vessels, one ship remains intact and unmanned, Martian warriors observing from building windows, deserted city buildings in background, daylight lighting with dramatic fire illumination on ships, advanced airship design, Green Martian armor details.

# Negative Prompt
crew visible on deck, extra ships beyond count, wrong ship color, distorted anatomy, text overlays, logos, blurry details, inconsistent lighting, floating debris not part of salvage, human faces in Martian group, incorrect weapon placement, smoke obscuring key damage marks.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5.0
- required_refs: Hull breaches visible, smoke rising from damaged ships, one ship remains unmanned
- optional_refs: Window frame
- visible_character_assets: Martians observing from windows, Narrator noting damage progression
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/Medium
- continuity_mode: insert
- starting_keyframe_strategy: 
- dependency_policy: 
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Maintain shot scale consistent with BT002 and BT004 to ensure smooth transition in damage progression.
- Ensure ship count matches scene context (twenty total) while highlighting the single intact vessel as focal point.
- Preserve lighting consistency between window POV and valley floor view for seamless insert continuity.
- Verify hull damage marks align with previous shots to avoid resetting battle state.

# Repair Notes
- Correct any distorted Martian figures in window frames to match established armor design.
- Adjust smoke density to ensure it highlights damage without obscuring ship identification.
- Fix lighting mismatches between interior window view and exterior ship view for consistent exposure.
- Ensure the single intact ship is clearly distinguishable from damaged vessels for continuity tracking.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
