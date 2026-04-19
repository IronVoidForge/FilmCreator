# Title
CH008_SC004 CL006 Fix 01 Prompt

# ID
CH008_SC004_CL006_fix_01_prompt

# Purpose
Preserve wide shot composition of building portal while correcting local details including prisoner facial clarity, skin tone accuracy, and interior light contrast at threshold. Ensure female martian figures remain distinct from background environment.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide shot of building entrance portal with female martians dragging slender human woman prisoner inside. Green skin warriors holding prisoner by arms. Oval face visible with coal black hair flowing loosely. Light reddish copper skin tone on prisoner. Interior warm light glowing from behind portal threshold. Gray ship exterior context implied near ground level. Martians standing upright near portal edge.

# Negative Prompt
blurry, distorted anatomy, green skin blending into background, missing interior light, wrong skin tone, extra limbs, low resolution, text, watermark, dark shadows obscuring face, martian features merging with wall.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT002.md building portal entry beat
- optional_refs: Wide shot showing portal and Martians notes
- visible_character_assets: Female Martians, Human Woman Prisoner
- look_continuity_policy: Preserve green skin tone and prisoner copper skin
- intended_lighting_change: Enhance interior light contrast at portal threshold
- composition_type: Wide shot showing portal and Martians
- continuity_mode: cutaway
- starting_keyframe_strategy: Starting keyframe Martians in view
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: Standard still fix workflow
- fallback_strategy: Use POV dragging into building if wide unavailable
- consistency_assist_policy: Maintain prisoner appearance details
- consistency_assist_method: Reference approved still base image_1
- anatomy_repair_policy: Focus on facial clarity and limb positioning
- consistency_targets: Oval face, copper skin, green skin
- style_profile: Martian urban architecture aesthetic
- batch_role: Fix 01
- fix_of: CH008_SC004_CL006_fix_01_prompt

# Continuity Notes
- Maintain specific appearance details for prisoner (slender girlish figure, oval face, coal black hair).
- Ensure female martians do not melt into background structures within three minutes.
- Interior light must be visible through portal to indicate building depth.
- Green skin tone must remain consistent across all warrior figures.

# Repair Notes
- Correct any blurriness on prisoner's oval face to ensure expression is readable.
- Adjust lighting contrast at portal threshold to clearly separate interior from exterior.
- Verify martian green skin does not appear muddy or blending with shadows.
- Ensure prisoner ornaments are visible if present, maintaining description accuracy.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
