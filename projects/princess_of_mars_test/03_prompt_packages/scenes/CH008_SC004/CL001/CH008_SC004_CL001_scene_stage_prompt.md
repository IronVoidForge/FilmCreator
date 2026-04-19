# Title
CH008_SC004 CL001 Scene Stage Prompt

# ID
CH008_SC004_CL001_scene_stage_prompt

# Purpose
Fill in the stage intent here. Establish prisoner's vulnerable state inside ship interior transitioning to exterior portal. Introduce human woman and her fate within Martian industrial aesthetic.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Slender girlish figure with oval face and large lustrous eyes, coal black waving hair loose coiffure, light reddish copper skin tone, crimson cheeks, ruby lips, destitute of clothes save for ornaments, gray low profile vessel interior dim industrial lighting, green warriors approaching from ship interior toward exit, vertical axis prisoner low warriors standing, environmental boundary ship hull visible.

# Negative Prompt
Human male narrator visible, bright sunlight, modern clothing, weapons in hands of prisoner, blue sky, white buildings, clean studio lighting, detailed facial expressions other than oval face, green skin on prisoner.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Ship interior/exterior transition notes
- visible_character_assets: Prisoner figure (slender girlish form), Green Warriors (2-3 figures approaching)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: dim industrial atmosphere
- composition_type: Close-up of prisoner figure
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Starting keyframe shows prisoner inside ship, ending keyframe at ship exterior
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

# Continuity Notes
- Maintain prisoner appearance details (oval face, copper skin) across frames.
- Keep ship interior dim and industrial texture consistent.
- Ensure warriors are green-skinned and approach from interior toward exit.
- Avoid showing human male narrator in frame.
- Preserve vertical axis where prisoner is low and warriors stand.

# Repair Notes
- If prisoner looks too large, scale down to slender girlish form.
- If lighting is too bright, add shadows to match dim industrial atmosphere.
- If anatomy is unclear on warriors, simplify to silhouette or standard warrior form.
- Ensure ship hull boundary is visible as environmental context.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
