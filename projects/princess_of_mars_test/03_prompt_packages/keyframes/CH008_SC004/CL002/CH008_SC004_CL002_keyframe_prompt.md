# Title
CH008_SC004 CL002 Keyframe Prompt

# ID
CH008_SC004_CL002_keyframe_prompt

# Purpose
Establish wide exterior view of gray vessel with open portal, capturing transition from interior to exterior lighting, featuring green-skinned figures dragging slender human figure.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Gray low-profile vessel hull, open rectangular portal, dim industrial lighting, green-skinned warriors standing near exit, slender human figure being dragged backward, oval face visible, copper skin tone, loose dark hair, ornamental jewelry, banners on stem, glowing devices on prow, valley background, distant hills.

# Negative Prompt
bright sunlight, clear blue sky, distorted anatomy, missing limbs, blurry details, high contrast shadows, modern technology, text, logos, proper names, white skin tone, red hair, clean interior walls.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Wide shot warriors dragging action notes
- visible_character_assets: Green Warriors (2-3 figures), Ship hull as environmental boundary, Portal/opening visible
- look_continuity_policy: dim lighting, industrial texture
- intended_lighting_change: interior to exterior transition
- composition_type: wide ship exterior showing portal
- continuity_mode: cutaway
- starting_keyframe_strategy: Starting keyframe interior to exterior transition
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: N/A
- fallback_strategy: Use medium shot warriors dragging if wide unavailable
- consistency_assist_policy: N/A
- consistency_assist_method: N/A
- anatomy_repair_policy: N/A
- consistency_targets: N/A
- style_profile: N/A
- batch_role: N/A
- fix_of: N/A

# Continuity Notes
- Cutaway mode, maintain dim lighting consistency, ensure portal alignment matches previous frames.

# Repair Notes
- Fix anatomy of dragging figures, correct skin tone saturation, adjust lighting gradients for interior-to-exterior transition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
