# Title
CH008_SC003 CL006 Keyframe Prompt

# ID
CH008_SC003_CL006_keyframe_prompt

# Purpose
Generate a frozen still representing the opening keyframe for a wide shot of simultaneous looting operations on the main deck of the disabled vessel, ensuring continuity with Beat BT002.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide angle view of gray vessel main deck interior, multiple green-skinned warriors moving systematically across open space, clusters of pale dead sailors stationary in background, natural daylight illuminating scene, cinematic stillness, detailed textures on hull and clothing

# Negative Prompt
modern weapons, text, blurry faces, human skin tone on warriors, distorted anatomy, floating objects, bright artificial lighting, crowded composition, wrong ship color, modern clothing, visible names

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (multiple), Dead Sailors (clusters)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on main deck with multiple Martians
- dependency_policy: none
- auto_advance_policy: 
- fallback_strategy: insert if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain ship drift vector southeast throughout sequence.
- Ensure all green-skinned warriors are consistent in skin tone and anatomy.
- Keep dead sailors stationary in designated areas within the vessel interior.
- Track item removal consistency across shots for looting operations.
- Avoid showing modern weaponry or clothing on any character.

# Repair Notes
- Fix skin tone if too pale or mismatched with green-skinned warriors.
- Ensure no modern weapons appear in the scene.
- Correct anatomy if limbs look distorted during movement across deck.
- Adjust lighting to match natural daylight conditions of the valley setting.
- Remove any text or labels that may be generated unintentionally.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
