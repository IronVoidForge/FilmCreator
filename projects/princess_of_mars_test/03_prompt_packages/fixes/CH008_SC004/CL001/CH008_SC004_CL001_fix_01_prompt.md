# Title
CH008_SC004 CL001 Fix 01 Prompt

# ID
CH008_SC004_CL001_fix_01_prompt

# Purpose
Corrective still-generation for CL001 in CH008_SC004. Preserve close-up composition of prisoner figure being extracted from disabled ship. Fix local anatomy and lighting continuity issues while maintaining dim industrial atmosphere consistent with Martian city setting. Ensure green warrior skin tone matches established Martians and prisoner's copper skin tone is accurate.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
slender girlish figure oval face large lustrous eyes coal black waving hair loose coiffure light reddish copper skin crimson cheeks ruby lips destitute of clothes save for ornaments being dragged by green warriors gray ship interior dim industrial lighting low profile vessel banners on stem stern glowing devices on prow building portal visible exterior ship hull texture

# Negative Prompt
blurry extra limbs human skin tone modern clothing bright sunlight clean white background distorted anatomy wrong facial features floating objects clean edges high contrast shadows unrealistic physics

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Scene lighting dim, industrial atmosphere
- visible_character_assets: Prisoner figure, Green Warriors
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Close-up of prisoner figure
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Starting keyframe shows prisoner inside ship interior, small and vulnerable
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: 
- fallback_strategy: Use medium shot warriors dragging if close-up unavailable
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_insert.two_ref.klein.distilled

# Continuity Notes
- Maintain dim industrial lighting consistent with scene.
- Ensure green warrior skin tone matches established Martians.
- Keep prisoner's copper skin tone accurate.
- Preserve ship gray low-profile appearance.
- Align movement trajectory from interior to exterior transition.

# Repair Notes
- Fix any anatomy distortions on the prisoner's face or hands.
- Ensure ship hull texture is gray and low-profile.
- Correct lighting contrast between interior and exterior transition if visible.
- Verify warrior grip on prisoner is natural without extra limbs.
- Maintain banner and glowing device details on ship prow/stern.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
