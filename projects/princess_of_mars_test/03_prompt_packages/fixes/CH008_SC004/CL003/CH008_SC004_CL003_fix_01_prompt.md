# Title
CH008_SC004 CL003 Fix 01 Prompt

# ID
CH008_SC004_CL003_fix_01_prompt

# Purpose
Correct local generation artifacts in the warrior dragging action while preserving the approved base composition and character appearance continuity for the prisoner reveal sequence.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green-skinned warriors dragging slender human woman prisoner, ship interior to exterior transition, dim industrial lighting, oval face visible, coal black hair, gray low-profile vessel hull, portal open, dragging motion trajectory, Martian city architecture background, restrained movement, focused intent on capture.

# Negative Prompt
morphing hands, extra limbs, wrong skin tone, blurry motion, incorrect anatomy, bright lighting, floating objects, distorted faces, green skin on prisoner, copper skin on warriors, excessive detail in background, static pose, unnatural grip, broken continuity, low resolution artifacts.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL003
- duration_seconds: 5
- required_refs: image_1
- optional_refs: image_2
- visible_character_assets: green-skinned warriors, human woman prisoner
- look_continuity_policy: preserve approved base style and character skin tones
- intended_lighting_change: maintain dim industrial ship interior lighting
- composition_type: medium shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: warriors approaching with intent
- dependency_policy: no hard dependencies
- auto_advance_policy: standard still generation flow
- fallback_strategy: use close-up prisoner figure if medium unavailable
- consistency_assist_policy: enable character appearance consistency
- consistency_assist_method: reference image alignment
- anatomy_repair_policy: fix hand grips and dragging mechanics
- consistency_targets: prisoner oval face, warrior green skin, ship gray hull
- style_profile: Martian city urban warfare aesthetic
- batch_role: still_fix
- fix_of: CL003_draft

# Continuity Notes
- Maintain green skin tone for all warrior figures to match approved base.
- Ensure prisoner retains copper skin and oval face shape throughout dragging action.
- Keep ship hull gray and low-profile consistent with previous shots in sequence.
- Preserve dim lighting conditions inside ship interior transitioning to exterior.
- Align dragging motion trajectory with established geography (vertical axis: prisoner low).

# Repair Notes
- Fix hand grips on prisoner to ensure natural dragging mechanics without morphing.
- Correct any skin tone bleeding between warrior and prisoner characters.
- Ensure portal visibility remains clear during transition from interior to exterior.
- Remove any static artifacts or blur that disrupts the sense of movement.
- Verify prisoner ornaments are visible and consistent with previous close-ups.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
