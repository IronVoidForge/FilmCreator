# Title
CH008_SC004 CL003 Cut Motion Prompt

# ID
CH008_SC004_CL003_cut_motion_prompt

# Purpose
Bridge starting keyframe warriors approaching to ending keyframe at ship exit. Focus on visible motion, camera behavior, and environment change from interior to exterior. Maintain continuity of lighting and grade by default.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Medium shot green warriors dragging slender human woman figure backward from dim ship interior toward open portal exterior. Ship hull visible as boundary. Camera follows movement trajectory. Warriors standing high, prisoner low. Gray vessel banners and glowing devices visible. Dim industrial lighting transitioning to brighter exterior light at exit.

# Negative Prompt
static image, extra limbs, distorted face, sky background, bright sunlight inside ship, narrator face, close-up only, wide shot only, morphing, blurry, low resolution, wrong anatomy, green skin on prisoner.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Medium shot warriors dragging action notes
- visible_character_assets: Green Warriors, Human Woman Prisoner
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium shot warriors dragging action
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Warriors approaching with intent
- dependency_policy: No hard dependencies
- auto_advance_policy: 
- fallback_strategy: 
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Preserve dim industrial interior lighting transitioning to brighter exterior light at portal.
- Maintain Green Warriors standing high and prisoner low vertical axis.
- Ensure ship hull visible as environmental boundary throughout motion.
- Keep camera following movement trajectory from interior toward exit.

# Repair Notes
- If lighting is too bright inside ship, darken interior first before transition.
- If anatomy is distorted on prisoner, prioritize facial structure and slender form.
- If warriors appear static, emphasize dragging motion and intent in prompt.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
