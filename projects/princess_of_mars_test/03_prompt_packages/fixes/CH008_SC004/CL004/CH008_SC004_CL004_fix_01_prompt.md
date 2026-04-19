# Title
CH008_SC004 CL004 Fix 01 Prompt

# ID
CH008_SC004_CL004_fix_01_prompt

# Purpose
Corrective still-generation that preserves composition and look while fixing local issues. Uses image_1 as approved still base and image_2 as secondary reference when needed. Focuses on continuity sensitivities for specific appearance details including oval face, slender girlish figure, coal black hair, light reddish copper skin, building portal with interior light visible through portal. Maintains horizontal axis movement toward portal while fixing any distorted facial features or inconsistent lighting from building interior.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
slender girlish figure, oval face, large lustrous eyes, coal black waving hair loose coiffure, light reddish copper skin, crimson cheeks, ruby lips, female Martians dragging action, building portal threshold, interior light visible through portal, horizontal axis movement toward entrance, dim industrial atmosphere, vertical axis prisoner low warriors standing, narrator POV established, ship exterior to building entrance transition

# Negative Prompt
distorted facial features, missing limbs, inconsistent lighting from building interior, distorted hair texture, wrong skin tone, floating artifacts, overexposed portal area, underexposed figure, blurred movement trajectory, incorrect eyeline direction, mismatched character proportions, inconsistent banner placement, wrong ship profile shape, missing glowing devices on prow

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md building portal entry beat
- optional_refs: POV dragging into building notes, interior light from building visible through portal
- visible_character_assets: Female Martians (2-3 figures), Prisoner figure being dragged forward
- look_continuity_policy: preserve oval face details, maintain horizontal axis movement toward portal, keep interior light visible through portal
- intended_lighting_change: none - maintain dim industrial atmosphere with portal interior light contrast
- composition_type: POV of dragging into building
- continuity_mode: insert
- starting_keyframe_strategy: Starting keyfigure at ship exterior, ending keyframe entering portal
- dependency_policy: no hard dependencies - can be shot independently
- auto_advance_policy: none
- fallback_strategy: use close-up prisoner face if POV unavailable
- consistency_assist_policy: maintain specific appearance details throughout dragging action
- consistency_assist_method: preserve oval face and hair texture while fixing local issues
- anatomy_repair_policy: fix any distorted facial features or limb proportions
- consistency_targets: slender girlish form, coal black hair, light reddish copper skin, building portal interior light
- style_profile: still_fix corrective generation with Klein distilled workflow
- batch_role: still_fix
- fix_of: CL004 Building Portal POV

# Continuity Notes
- Capture the continuity rules for this stage. Preserve oval face details including large lustrous eyes and coal black waving hair loose coiffure throughout dragging action. Maintain horizontal axis movement toward building portal entrance with interior light visible through portal. Keep prisoner slender girlish form consistent while fixing any local distortions. Ensure female Martians maintain control over prisoner without breaking composition. Interior lighting from building must remain visible as environmental focal point. Horizontal axis movement trajectory must be preserved for continuity with previous beats.

# Repair Notes
- Capture any repair or corrective guidance for this stage. Fix any distorted facial features on oval face while maintaining large lustrous eyes and coal black hair texture. Correct inconsistent lighting from building interior to match dim industrial atmosphere. Ensure prisoner slender form remains consistent throughout dragging action without breaking proportions. Repair any missing glowing devices on ship prow if visible in frame. Maintain correct banner placement on stem/stern of ship exterior. Fix any floating artifacts or overexposed portal area while preserving interior light contrast.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
