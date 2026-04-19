# Title
CH008_SC003 CL007 Keyframe Prompt

# ID
CH008_SC003_CL007_keyframe_prompt

# Purpose
Establish keyframe visual intent for burning vessel sequence within scene build workflow.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
wide shot gray low-profile vessel ablaze drifting southeast fire spreading aft to forward smoke plume rising green-skinned figures retreating from immediate danger distant green warriors observing water surface ash debris buildings background scale reference intense fire glow illuminating hull and sky smoke obscuring parts of horizon

# Negative Prompt
blurry low resolution distorted faces extra limbs missing hands wrong skin tone static image no motion artifacts text watermark signature bad anatomy green skin on human wrong color palette dark shadows overexposed fire not burning correctly

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL007
- duration_seconds: 5
- required_refs: BT003.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (retreating), Warriors (distant safety)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: intense fire glow illuminating hull and sky
- composition_type: wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on missile ignition point
- dependency_policy: none
- auto_advance_policy: insert if needed
- fallback_strategy: insert if needed
- consistency_assist_policy: maintain fire intensity consistency with ignition point
- consistency_assist_method: visual match to previous burn frames
- anatomy_repair_policy: ensure green-skinned anatomy clarity
- consistency_targets: drift vector southeast, fire spread aft to forward
- style_profile: still.scene_build.four_ref.klein.distilled
- batch_role: keyframe
- fix_of: none

# Continuity Notes
- Drift vector continues southeast from previous beat.
- Fire spread pattern moves from aft sections toward forward hull.
- Smoke plume rises vertically then disperses with wind against sky backdrop.
- Buildings in background provide scale reference for burning vessel size.
- Green-skinned figures retreat from immediate danger zone while ship burns.

# Repair Notes
- Ensure green-skinned anatomy clarity on retreating figures to avoid distortion.
- Maintain fire intensity consistency with ignition point strategy at start.
- Verify ash and debris scatter matches water surface physics in wide shot.
- Confirm smoke obscuring horizon does not hide critical vessel details.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
