# Title
CH008_SC002 CL002 Fix 01 Prompt

# ID
CH008_SC002_CL002_fix_01_prompt

# Purpose
Refine the still generation for Beat BT002 to ensure accurate depiction of humanoid volley fire from building windows while maintaining visual continuity with approved base frames and secondary references. Focus on muzzle flash intensity, projectile trajectory accuracy, and consistent green skin tone without introducing premature salvage elements.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green humanoid warriors positioned at multi-story building windows overlooking valley floor, gray painted airships approaching in distance, bright muzzle flashes erupting from weapon barrels, small projectiles arcing through air toward distant vessels, window frames visible in foreground, daylight illumination mixed with smoke haze, medium shot composition capturing shooter and target axis.

# Negative Prompt
Human skin tones, wrong ship color (not gray), missing muzzle flashes, cluttered interior details, distorted anatomy, incorrect projectile trajectory, excessive fire on buildings before salvage phase, wrong number of ships visible for this beat.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL002
- duration_seconds: 5.0
- required_refs: muzzle flashes, projectile impacts on ship hulls
- optional_refs: window frame
- visible_character_assets: green humanoid warriors at building windows (active), narrator observing from window
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium/Close-up
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: 
- dependency_policy: 
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Ensure twenty airships scale is represented in wide coverage shots.
- Maintain green skin tone consistency for humanoid warriors.
- Do not introduce loot items yet.
- Keep ship damage level consistent with BT002 (impact marks visible but hull intact).

# Repair Notes
- Correct any distorted window frames to match architectural style.
- Adjust muzzle flash brightness to match weapon intensity.
- Ensure projectile arcs follow gravity logic.
- Verify humanoid anatomy remains consistent with approved base stills.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
