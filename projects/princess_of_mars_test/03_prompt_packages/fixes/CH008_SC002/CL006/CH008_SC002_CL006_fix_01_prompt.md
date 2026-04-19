# Title
CH008_SC002 CL006 Fix 01 Prompt

# ID
CH008_SC002_CL006_fix_01_prompt

# Purpose
Fix CL006 to ensure accurate depiction of impact reactions on specific target points while maintaining visual continuity with previous shots and correcting local issues related to timing and placement consistency.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green-skinned warriors positioned for precision shots, active tracking device on stem, smoke at impact points, gunners and officers hit sequentially, banners dissolving in flame, progressive damage visible, medium shot of specific target points with impact reactions.

# Negative Prompt
Extra limbs, incorrect lighting, missing impact effects, static composition, unwanted artifacts, extra smoke trails, inconsistent banner damage, extra characters, distorted anatomy, poor texture details.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: Impact reaction shots coverage families
- visible_character_assets: Martians
- look_continuity_policy: preserve composition and look while fixing local issues
- intended_lighting_change: 
- composition_type: Medium shot of specific target points with impact reactions
- continuity_mode: Point-specific reaction shots showing impact effects
- starting_keyframe_strategy: Open on sighting apparatus, then cut to impact points
- dependency_policy: Hard dependency on CL005; must follow targeting sequence
- auto_advance_policy: 
- fallback_strategy: Use insert if need to emphasize impact timing
- consistency_assist_policy: preserve visual continuity across interval beats
- consistency_assist_method: 
- anatomy_repair_policy: ensure consistent character anatomy and proportions
- consistency_targets: 
- style_profile: Klein Distilled
- batch_role: still_fix
- fix_of: CL006

# Continuity Notes
- Bullet drops at explosion points (timing and placement consistency)
- Banners dissolving in flame (progressive damage tracking)
- Smoke trails must match impact timing precisely
- Targeting sequence must follow previous shots without deviation

# Repair Notes
- Ensure smoke trails match impact timing to correct local issues
- Ensure banners show progressive flame damage consistent with beat bundle
- Adjust bullet drop placement for consistency with explosion points
- Fix any inconsistencies in character anatomy or proportions from previous frames

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
