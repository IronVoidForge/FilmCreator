# Title
CH008_SC004 CL001 Keyframe Prompt

# ID
CH008_SC004_CL001_keyframe_prompt

# Purpose
Establish prisoner's vulnerable state and physical appearance within ship interior, setting up extraction sequence with dim industrial lighting and green-skinned figures approaching.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
dim industrial ship interior, slender girlish figure with oval face, light reddish copper skin, coal black waving hair, green-skinned warriors approaching, small vulnerable posture, low lighting, atmospheric shadows, no bright sunlight, detailed ornaments on prisoner, industrial texture walls.

# Negative Prompt
bright sunlight, clear sky, extra limbs, distorted face, text, logos, bright colors, cartoonish, blurry, deformed hands, wrong anatomy, human skin tone, red hair, clean white background, floating objects, excessive motion blur.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Scene lighting dim, industrial atmosphere
- visible_character_assets: Prisoner figure (slender girlish form), Green Warriors (2-3 figures approaching)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: none
- composition_type: Close-up of prisoner figure
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Starting keyframe shows prisoner inside ship, ending keyframe at ship exterior
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: standard
- fallback_strategy: Use medium shot warriors dragging if close-up unavailable
- consistency_assist_policy: enabled
- consistency_assist_method: 
- anatomy_repair_policy: strict
- consistency_targets: 
- style_profile: industrial sci-fi
- batch_role: keyframe_build
- fix_of: 

# Continuity Notes
- Match dim industrial lighting from previous frames to maintain atmosphere.
- Ensure prisoner skin tone remains light reddish copper, not pale or dark.
- Maintain green-skinned warriors appearance without shifting to human tones.
- Keep prisoner posture small and vulnerable within the frame composition.

# Repair Notes
- If skin tone is too pale, adjust to light reddish copper.
- If warriors look human, adjust to green-skinned figures.
- If lighting is too bright, darken shadows to match industrial interior.
- If prisoner face is distorted, refine oval face details and lustrous eyes.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
