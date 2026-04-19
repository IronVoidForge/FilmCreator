# Title
CH008_SC002 CL003 Fix 01 Prompt

# ID
CH008_SC002_CL003_fix_01_prompt

# Purpose
Correct visual inconsistencies in the enemy airship swing sequence while preserving the established Martian battle aesthetic and continuity with the preceding volley fire beat. Maintain the dynamic aerial tracking perspective and ensure smoke trails align with previous frames.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
gray painted airship vessel rotating horizontally in sky valley, green humanoid figures firing weapons from elevated building windows, smoke plumes rising from ship deck cannons, tattered banners on stem stern showing flame damage, wide aerial tracking composition, cinematic lighting, photorealistic texture, open Martian architecture background, dynamic motion blur consistent with swing arc

# Negative Prompt
blurry motion, distorted ship shape, extra limbs, text, watermark, low resolution, wrong color palette, static frame, missing smoke trails, inconsistent banner damage, floating debris, oversaturated sky, flat lighting, green skin on enemy crew, human prisoner visible, building interior instead of exterior

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5
- required_refs: image_1, image_2
- optional_refs: BT002.md
- visible_character_assets: enemy fleet lead vessel, crew on deck, green warriors in windows
- look_continuity_policy: preserve swing arc completion and bullet drop consistency
- intended_lighting_change: maintain cinematic valley lighting with smoke glow
- composition_type: wide aerial tracking shot
- continuity_mode: dynamic aerial tracking
- starting_keyframe_strategy: open on ship in initial position
- dependency_policy: hard dependency on BT002 beat
- auto_advance_policy: none
- fallback_strategy: reblock_same_scene if swing arc timing needs adjustment
- consistency_assist_policy: enabled
- consistency_assist_method: smoke trail alignment and banner damage tracking
- anatomy_repair_policy: ensure ship geometry matches reference
- consistency_targets: ship rotation, smoke plumes, banner flame
- style_profile: cinematic action realism
- batch_role: still_fix
- fix_of: CH008_SC002_CL003_fix_01_prompt

# Continuity Notes
- Capture the continuity rules for this stage.
- Ensure the ship completes its 360-degree swing arc within the frame duration.
- Maintain consistency with bullet drop points from previous volley fire shots.
- Track progressive flame damage on banners to match BT002 beat state.
- Keep green warrior positions static in windows while ship moves dynamically.
- Verify smoke trails originate from deck cannons and align with swing direction.

# Repair Notes
- Capture any repair or corrective guidance for this stage.
- Fix local geometry of the airship to ensure low-profile shape is preserved.
- Adjust smoke density if previous frames show inconsistent plume thickness.
- Correct banner flame damage progression to match established burn rate.
- Ensure no human prisoner appears in this specific swing arc shot.
- Remove any static elements that contradict the dynamic tracking motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
