# Title
CH008_SC003 CL006 Fix 01 Prompt

# ID
CH008_SC003_CL006_fix_01_prompt

# Purpose
Fix CL006 wide shot during looting operations (BT002) to ensure multiple green-skinned Martians are distinct and working on the gray airship deck with correct continuity items visible. Preserve composition while correcting local anatomy and item tracking issues.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
wide shot gray airship deck multiple green skinned martian warriors looting removing arms silks jewels dead sailors clusters background valley architecture dramatic lighting smoke effects cinematic war drama style

# Negative Prompt
distorted anatomy wrong skin tone blue red missing items cluttered deck modern elements blurry low resolution single figure merged blob floating limbs incoherent hands

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (multiple), Dead Sailors (clusters)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: none
- composition_type: wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on main deck with multiple Martians
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: insert if needed
- consistency_assist_policy: none
- consistency_assist_method: none
- anatomy_repair_policy: standard
- consistency_targets: green skin, gray ship hull
- style_profile: cinematic war drama
- batch_role: fix
- fix_of: CL006

# Continuity Notes
- Martians must maintain green skin tone consistent with previous shots.
- Ship hull remains gray low-profile with banners visible if in frame.
- Looting actions (arms, silks) must be tracked across interval frames.
- Dead sailors remain stationary clusters on deck.

# Repair Notes
- Ensure multiple Martians are distinct figures, not merged into a single mass.
- Correct any anatomy distortions on hands holding items.
- Verify lighting matches battle aftermath (dramatic shadows).
- Check that carboy dumping point is visible at interval beat 0:4.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
