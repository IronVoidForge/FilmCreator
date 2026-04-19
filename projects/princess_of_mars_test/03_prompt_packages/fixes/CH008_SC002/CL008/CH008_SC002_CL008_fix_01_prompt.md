# Title
CH008_SC002 CL008 Fix 01 Prompt

# ID
CH008_SC002_CL008_fix_01_prompt

# Purpose
Fix CL008 Damage Detail Close-ups during fleet retreat, preserving damage progression and visual continuity with previous shots (CL007). Ensure banners show flame damage and ships are limping correctly within the battle aftermath context.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Gray low-profile vessels retreating from valley floor, visible smoke trails, banners dissolving in flame, damaged hulls showing impact points, drifting southeast as funeral pyre, Martian city architecture background, open valleys and distant hills, battle haze atmosphere.

# Negative Prompt
human prisoners, green warriors firing directly, clear skies without smoke, intact hulls, bright daylight without battle haze, unrelated ground elements, perfect weather conditions.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5
- required_refs: CL007
- optional_refs: BT004.md
- visible_character_assets: Enemy Fleet, Banners with flame damage
- look_continuity_policy: Preserve battle aftermath visual style
- intended_lighting_change: 
- composition_type: Medium close-up of vessels showing damage indicators
- continuity_mode: Close-up progressive tracking of damage indicators
- starting_keyframe_strategy: Open on multiple vessels with visible damage indicators
- dependency_policy: Soft dependency on CL007; can follow retreat sequence
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
- Ensure damage indicators match previous shots in the fleet retreat sequence.
- Ship movement must follow retreat path away from valley floor.
- Smoke trails must be consistent with battle conclusion density.
- Banners must show progressive flame damage visible on multiple vessels.

# Repair Notes
- Correct any banner flame inconsistencies to match fire damage progression.
- Ensure ships are limping correctly rather than moving smoothly.
- Maintain smoke density for battle aftermath feel without overexposure.
- Fix local artifacts that break the continuity of the damaged fleet retreat.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
