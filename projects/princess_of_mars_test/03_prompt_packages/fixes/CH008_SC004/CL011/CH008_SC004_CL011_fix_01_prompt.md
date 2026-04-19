# Title
CH008_SC004 CL011 Fix 01 Prompt

# ID
CH008_SC004_CL011_fix_01_prompt

# Purpose
Generate a corrective still prompt for CL011 within CH008_SC004, preserving the close-up detail composition of a green-skinned warrior carrying loot during the battle aftermath. Ensure continuity with established lighting (daylight with fire glow) and environmental elements (valley smoke, plaza background) while fixing local anatomical or texture inconsistencies identified in previous iterations.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
green-skinned warrior close-up detail shot, carrying small loot items in hands or on shoulders, daylight lighting with orange fire glow background, smoke clearing in valley air, ornate body decorations visible, green skin tone consistent, urban building structures blurred background, plaza ground visible below, high resolution, cinematic composition, Barsoom aesthetic

# Negative Prompt
distorted anatomy, missing limbs, wrong skin color, blurry details, extra fingers, inconsistent lighting, dark shadows on face, floating objects, text, watermark, low resolution, interior room background, close-up of human observer, bright sunlight without fire glow

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL011
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT003.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Warriors carrying weapons or empty hands, Loot visible on some warriors (small items, containers)
- look_continuity_policy: Preserve established Barsoom lighting and color grading from scene base
- intended_lighting_change: Maintain daylight with fire glow consistency
- composition_type: Close-up (detail)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: standard
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: texture_refinement
- anatomy_repair_policy: strict
- consistency_targets: skin_tone, ornament_style, smoke_density
- style_profile: cinematic_action_adventure
- batch_role: fix_of_previous_iteration
- fix_of: 

# Continuity Notes
- Maintain green skin saturation consistent with previous Green Martian shots in scene.
- Ensure loot is consolidated or being carried toward plaza as per beat logic.
- Smoke should be diminishing but still visible in valley air, not completely cleared.
- Background must show urban structures and valley/hills, not interior spaces.
- Lighting must reflect daylight conditions with fire glow from burning vessel in distance.

# Repair Notes
- Fix any anatomy errors on hands holding loot items to ensure natural grip.
- Ensure fire glow matches intensity of previous shots showing burning vessel.
- Check for consistent ornament style on warrior body (highly wrought ornaments).
- Verify smoke texture is not too dense or too thin compared to valley air state.
- Correct any color bleeding from fire onto skin that looks unnatural.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL011.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
