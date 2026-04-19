# Title
CH008_SC004 CL005 Scene Stage Prompt

# ID
CH008_SC004_CL005_scene_stage_prompt

# Purpose
Define the visual staging for CL005 within SC004, ensuring the prisoner's face details (oval, copper skin) are prominent and consistent with BT002, while capturing the dragging motion into the building portal. This stage focuses on authoring the scene-level context for the clip, establishing emotional tone (Awe/Depression -> Hope/Fear) and environmental continuity between ship exterior and building interior.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Close-up of slender human woman face, oval lustrous eyes, coal black hair, light reddish copper skin, ornaments, being dragged by green-skinned female Martians, background ship exterior and building portal with interior light visible, steampunk sci-fi style, high detail, cinematic lighting.

# Negative Prompt
blurry face, wrong anatomy, human male face, bright sunlight, dark shadows, distorted ornaments, low resolution, text, watermark, green skin on prisoner, blue eyes, messy hair.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT002.md, CL004.md
- optional_refs: Close-up of prisoner face notes, Interior light from building visible through portal
- visible_character_assets: Prisoner figure (oval face details), Female Martians in view approaching portal, Narrator POV established
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: Portal interior light contrast with exterior dimness
- composition_type: Close-up of prisoner face (oval face details)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Starting keyframe oval face visible, ending keyframe entering portal with interior light visible
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: None specified
- fallback_strategy: Use POV dragging into building if close-up unavailable
- consistency_assist_policy: Ensure face consistency with CL004
- consistency_assist_method: 
- anatomy_repair_policy: Fix morphing of prisoner face to canonical description
- consistency_targets: 
- style_profile: Steampunk Sci-Fi, A Princess of Mars aesthetic
- batch_role: Scene Stage Authoring
- fix_of: 

# Continuity Notes
- Maintain green skin tone for Martians and copper skin for prisoner across all frames.
- Ensure oval face shape remains consistent with CL004 and BT002 references.
- Lighting must transition from ship exterior dimness to building portal interior light contrast.
- Dragging motion should be rough but controlled, reflecting the Martians' dominance.
- Avoid introducing new character assets not listed in visible_character_assets.

# Repair Notes
- If prisoner face morphs during reblock, revert to canonical description (oval, copper skin, ornaments).
- If lighting shifts incorrectly, adjust portal interior light intensity to match BT002 reference.
- Ensure Martians' green skin does not bleed into the prisoner's features.
- Verify that the background ship exterior remains consistent with previous clips in SC004.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
