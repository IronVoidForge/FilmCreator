# Title
CH008_SC003 CL002 Fix 01 Prompt

# ID
CH008_SC003_CL002_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Assume image_1 is the approved still base and image_2 is a secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Green warrior medium shot approaching drifting gray airship, low profile vessel with banners on stem stern glowing devices on prow, urban Martian architecture background open valleys distant hills, green skin warriors elevated positions observation, daylight lighting continuity, cinematic composition, smooth approach motion blur, detailed fabric textures, atmospheric depth.

# Negative Prompt
distorted anatomy, extra limbs, wrong skin color, floating objects, text, watermark, blurry, low resolution, inconsistent lighting, mismatched ship design, human faces on warriors, incorrect background elements, oversaturated colors, noise, artifacts, deformed hands, bad geometry.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Green Warriors (approaching), Martians (elevated)
- look_continuity_policy: match_previous_clips
- intended_lighting_change: none
- composition_type: medium shot
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: open on warrior eyeline tracking ship
- dependency_policy: depends on CL001
- auto_advance_policy: manual
- fallback_strategy: insert if needed
- consistency_assist_policy: enabled
- consistency_assist_method: image_comparison
- anatomy_repair_policy: strict
- consistency_targets: character_anatomy, environment_layout, color_grading
- style_profile: cinematic_klein
- batch_role: fix_01
- fix_of: CL002_draft

# Continuity Notes
- Ensure ship drift vector matches CL001 trajectory southeast.
- Maintain green skin tone consistency with previous warrior shots.
- Align background urban architecture scale and perspective with established environment index.
- Preserve lighting direction and intensity from approved still base image_1.
- Keep warrior eyeline focused on ship movement without breaking composition.

# Repair Notes
- Fix any local distortion in ship hull geometry to match low profile design.
- Correct hand anatomy on approaching warriors to avoid extra fingers or deformities.
- Adjust background blur depth to ensure focus remains on warrior and ship interaction.
- Remove any unintended artifacts from previous generation runs.
- Ensure banners and glowing devices are visible but not overexposed.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
