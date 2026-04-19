# Title
CH008_SC004 CL011 Keyframe Prompt

# ID
CH008_SC004_CL011_keyframe_prompt

# Purpose
Establish the visual intent for the close-up detail shot of a warrior carrying loot during the return to plaza sequence. This keyframe defines the composition and subject focus for the still generation workflow, ensuring consistency with the preceding battle aftermath beats.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close-up detail shot of green-skinned humanoid warrior carrying small items in hands or on shoulders. Background shows clearing smoke plume fading into valley air. Lighting is daylight with smoke haze. Composition focuses on upper body and held objects. Loot visible as small containers or weapons. Warrior skin tone consistent with established green hue. No facial expression visible, focus on loot consolidation.

# Negative Prompt
Blurry details, wrong skin tone, excessive fire, incorrect composition wide shot, missing loot items, distorted anatomy, dark lighting, heavy smoke obscuring subject, facial features if not intended, background clutter from previous battle debris.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL011
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Warriors carrying weapons, empty hands, Loot small items containers
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Close-up detail
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Smoke clearing significantly compared to previous beats, visible in valley air but not obscuring subject.
- Loot consolidated or being carried toward plaza entrance, visible on warrior shoulders or hands.
- Lighting remains daylight with smoke haze, no sudden shifts to night or heavy shadow.
- Warrior skin tone consistent with green hue, avoiding blue or red variations.
- Focus remains on upper body and held objects, avoiding full body wide shot composition.

# Repair Notes
- If anatomy looks distorted, adjust mesh to match humanoid warrior structure.
- If smoke is too dense, reduce opacity to maintain subject visibility.
- If lighting changes drastically, revert to daylight base with smoke haze overlay.
- Ensure loot items are small and distinct, not oversized props.
- Verify consistency with previous beat visuals regarding vessel drift and plaza location context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL011.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
