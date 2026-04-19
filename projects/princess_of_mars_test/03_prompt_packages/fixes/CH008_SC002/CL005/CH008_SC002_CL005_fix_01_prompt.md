# Title
CH008_SC002 CL005 Fix 01 Prompt

# ID
CH008_SC002_CL005_fix_01_prompt

# Purpose
Corrective still generation for Martian targeting apparatus close-up, preserving composition and look while fixing local issues such as anatomy clarity, lighting consistency, and alignment with approved base frame. Ensures precision detail work on sighting mechanics active tracking targets within building window environment.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green-skinned Martian targeting team positioned in building window, mechanical sighting apparatus active tracking targets, smoke at impact points visible, valley battle zone background, gray airships swinging below, precision detail work, medium close-up composition, elevated firing positions with clear line of sight, specific points targeted sequentially, impact smoke at target points visible

# Negative Prompt
blurry, distorted anatomy, extra limbs, wrong lighting, text, watermark, low resolution, inconsistent color grading, floating elements, missing weapons, incorrect ship orientation, out of focus, noise artifacts, bad geometry, unnatural skin texture, misplaced background objects

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT003.md, Close-up targeting shots coverage families
- optional_refs: None
- visible_character_assets: martian_warrior, sighting_apparatus
- look_continuity_policy: preserve green skin tone and mechanical device texture
- intended_lighting_change: maintain elevated window lighting consistency
- composition_type: medium close-up of sighting apparatus visible and active
- continuity_mode: close-up precision detail work on targeting mechanics
- starting_keyframe_strategy: open on targeting team positioned, apparatus tracking targets
- dependency_policy: soft dependency on BT003 beat; can stand alone for precision focus
- auto_advance_policy: none
- fallback_strategy: reframe_same_moment if need to adjust targeting angle
- consistency_assist_policy: enabled
- consistency_assist_method: alignment with approved base frame
- anatomy_repair_policy: strict correction of green skin warrior anatomy
- consistency_targets: bullet drops at explosion points, ship swing arc completion
- style_profile: still_fix_klein_distilled
- batch_role: corrective_still_insert
- fix_of: CL005_initial_draft

# Continuity Notes
- Capture the continuity rules for this stage. Ensure bullet drops at explosion points maintain timing and placement consistency. Verify ship swing arc completion matches full circle verification. Maintain green skin tone and mechanical device texture across shots. Align elevated window lighting with previous action shots from windows.

# Repair Notes
- Capture any repair or corrective guidance for this stage. Fix local issues such as distorted anatomy on green-skinned warriors. Correct lighting inconsistencies between building interior and exterior battle zone. Ensure sighting apparatus tracking mechanics are clear and not obscured by smoke artifacts. Align composition with approved base frame to preserve medium close-up framing.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
