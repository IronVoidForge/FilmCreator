# Title
SC001 CL005 Cut Motion Prompt

# ID
SC001_CL005_cut_motion_prompt

# Purpose
Generate cut motion for clip CL005 in scene SC001, continuing from approved opening frame with preserved lighting and grade. Focus on detail insert of devices on ship prows while maintaining continuity with previous banner shot. Ensure camera behavior aligns with visible motion requirements and environment change constraints.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Close examination of mysterious devices mounted on individual ship prows. Strange banner designs visible in periphery. Gray airship hulls maintain formation over hill crests. Earth human observer eyeline shifts from horizontal fleet distribution to vertical prow details. Daylight remains consistent with morning brightness. Smoke drifts naturally from distant vessel. Green Martians visible on decks remain static. Camera slowly zooms in on device details while maintaining ship formation context.

# Negative Prompt
morphing device shapes, flickering banner designs, wrong color grade, extra limbs, distorted anatomy, sudden lighting changes, blurry textures, static image, noise artifacts, green skin morphing on observer, incorrect ship count, mismatched hill crest positions, unnatural smoke movement, camera shake, inconsistent weather conditions.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: SC001 beat bundle BT003.md, Device shapes continuity markers across shots
- optional_refs: Hill crests depth context for close-ups, Lighting consistency notes
- visible_character_assets: Green Warriors (static on selected vessels), Earth human observer (eyeline shifts)
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None (morning brightness maintained)
- composition_type: Detail insert of devices on ship prows
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_device_detail_focus
- dependency_policy: dependent_on_banner_visibility_and_device_shapes
- auto_advance_policy: standard
- fallback_strategy: cutaway_to_ship_prow_detail
- consistency_assist_policy: enabled
- consistency_assist_method: visual_reference_matching
- anatomy_repair_policy: strict
- consistency_targets: ship positions relative to hill crests, banner designs, device shapes
- style_profile: sci_fi_adventure
- batch_role: detail_insert
- fix_of: SC001_CL005_scene_stage_prompt.md
- workflow_type: video.cut_motion.wan.i2v
- shared_character_refs: 
- shared_environment_refs: 

# Continuity Notes
- Maintain keyframe lighting and grade by default
- Preserve Earth human observer position relative to window frame
- Keep Green Warriors consistent in distance and formation
- Ensure smoke movement is natural and not glitchy
- Match ship positions relative to hill crests exactly
- Verify banner designs remain identifiable across shots

# Repair Notes
- Fix any lighting leaks from exterior view
- Correct anatomy if characters morph during motion
- Ensure camera movement matches approved frame trajectory
- Adjust device shapes if they appear distorted or inconsistent with previous shot

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
