# Title
CH008_SC004 CL004 Keyframe Prompt

# ID
CH008_SC004_CL004_keyframe_prompt

# Purpose
Establish observer perspective of battle conclusion from plaza level looking up at rooftop warriors and burning vessel, insert shot for missile launch sequence.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Over-the-shoulder view of human observer below, green-skinned warriors positioned on building roofs above, gray air craft hull burning in valley distance, smoke plume rising, daylight illumination, vertical axis from roofs to valley floor, partial view of rooftop structures, missiles in flight or preparing deployment.

# Negative Prompt
blurry, distorted anatomy, extra characters, proper nouns, indoor lighting, night scene, close-up only, wide shot only, static camera movement, wrong vessel color, smoke too dense, flames missing.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL004
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: human observer, green-skinned warriors
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: over-the-shoulder shot
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Vessel must show burning damage and smoke density consistent with previous impacts.
- Warriors on roofs maintain static positions during launch phase.
- Observer remains stationary below.
- Loot removal visible on vessel hull.
- Smoke plume rising steadily from valley floor.
- Vertical eyeline directed downward at vessel position.

# Repair Notes
- Ensure anatomy repair policy is applied to observer shoulder and warrior figures.
- Maintain consistency targets for vessel drift path and smoke plume shape.
- Verify daylight illumination matches previous scene beats.
- Check that no proper nouns appear in generated assets.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
