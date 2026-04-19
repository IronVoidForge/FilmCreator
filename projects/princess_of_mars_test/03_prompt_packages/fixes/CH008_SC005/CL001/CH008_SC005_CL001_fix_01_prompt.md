# Title
CH008_SC005 CL001 Fix 01 Prompt

# ID
CH008_SC005_CL001_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Assume image_1 is the approved still base and image_2 is a secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot exterior corridor threshold, Sola entering from left edge moving right with urgency, Carter standing center-right partial profile observing, city buildings upper floors windows roofs background, open ground plaza daylight smoke from fire missile impact flames, Barsoom setting action-oriented awe-inspiring tense during combat sequences, long low gray-painted vessels with strange banners distant hills beyond, Green Martians firing from windows roofs, slender girlish figure prisoner dragged through view background right-to-left, highly wrought ornaments on characters, coal black hair waving caught loosely into strange coiffure, crimson cheeks ruby lips.

# Negative Prompt
distorted anatomy, extra limbs, inconsistent lighting, blurry text, wrong composition, static background movement, missing characters, overexposed, underexposed, low resolution, watermark, signature, bad hands, fused fingers, disfigured faces, morphing objects, poor detail on ornaments, incorrect skin tone, mismatched shadows.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md Start State
- optional_refs: None
- visible_character_assets: Sola (full body), Carter (center-right, partial profile)
- look_continuity_policy: preserve_composition_and_look_while_fixing_local_issues
- intended_lighting_change: daylight_with_fire_smoke_effects
- composition_type: Wide shot, exterior corridor threshold
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Static wide frame, Sola entering from left edge of frame
- dependency_policy: No dependencies; standalone establishing shot
- auto_advance_policy: Hold on wide frame for 3-4 seconds
- fallback_strategy: If Sola entry is unclear, tighten to medium wide and emphasize her movement path
- consistency_assist_policy: enabled
- consistency_assist_method: image_1_base_preservation
- anatomy_repair_policy: strict
- consistency_targets: character_placement_movement_path_lighting_consistency
- style_profile: Barsoom_action_oriented_awe_inspiring_tense_combat_sequences
- batch_role: still_fix_corrective
- fix_of: CH008_SC005_CL001_base_still

# Continuity Notes
- Preserve composition and look while fixing local issues. Assume image_1 is the approved still base.
- Maintain spatial relationship between Sola entering from left and Carter standing center-right.
- Ensure background elements (city buildings, fire smoke, distant hills) remain consistent with chapter visual continuity.
- Keep character movement path clear for Sola's urgent approach trajectory.

# Repair Notes
- Ensure Sola movement path is clear and speed increases as she nears Carter.
- Maintain lighting consistency with fire smoke effects from missile impacts in background.
- Fix any local distortion on ornaments or skin tones to match canonical character descriptions.
- Verify that the wide frame holds for 3-4 seconds before cut motion intent.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
