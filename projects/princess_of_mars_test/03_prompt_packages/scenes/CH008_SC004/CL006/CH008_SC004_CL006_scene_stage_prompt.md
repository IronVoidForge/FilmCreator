# Title
CH008_SC004 CL006 Scene Stage Prompt

# ID
CH008_SC004_CL006_scene_stage_prompt

# Purpose
Establish the environmental context of the building entrance and narrator's observation point. Define the staging intent for a wide shot composition showing female Martians dragging a human figure into a portal with interior light visible. Authoring-only description focusing on subject placement, environmental transition from ship exterior to building interior, and the intended visible opening frame setup including light contrast at the threshold.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide shot Martian building portal entrance, female green-skinned warriors dragging slender human woman figure forward, oval face with large lustrous eyes, coal black waving hair, light reddish copper skin, crimson cheeks, ruby lips, destitute of clothes save for ornaments, interior building light visible through portal threshold, gray ship hull exterior context, banners on stem stern, glowing devices on prow, urban Martian architecture, open valley background, dim lighting industrial texture, vertical axis movement toward entrance, horizontal axis dragging trajectory, narrator observation perspective.

# Negative Prompt
human anatomy for Martians, modern technology, clear sky, bright daylight without contrast, extra characters, floating debris, distorted face features, missing ornaments, wrong skin tone, interior light too dim or too bright, ship hull missing, banners dissolving incorrectly, vertical axis misalignment, horizontal movement stopping abruptly, proper nouns, text overlays, watermarks.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT002.md building portal entry beat, Environmental state portal threshold light contrast
- optional_refs: Wide shot showing portal and Martians notes, Interior light from building visible through portal
- visible_character_assets: Female Martians (2-3 figures), Prisoner figure being dragged forward, Building portal as environmental focal point, Interior light from building visible
- look_continuity_policy: cutaway continuity mode, starting keyframe Martians in view, ending keyframe figure entering building with interior light visible
- intended_lighting_change: dim exterior to bright interior contrast at portal threshold
- composition_type: Wide shot showing portal and Martians
- continuity_mode: cutaway
- starting_keyframe_strategy: Starting keyframe Martians in view. Ending keyframe figure entering building with interior light visible
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: None specified for this stage
- fallback_strategy: Use POV dragging into building if wide unavailable
- consistency_assist_policy: Maintain character appearance details (slender girlish figure, oval face)
- consistency_assist_method: 
- anatomy_repair_policy: Adjust Martian anatomy if human-like features appear
- consistency_targets: 
- style_profile: Authoring scene stage prompt package
- batch_role: Planning phase
- fix_of: None specified for this stage

# Continuity Notes
- Capture the continuity rules for this stage. Ensure female Martians maintain green skin tone and warrior anatomy consistent with previous beats. Prisoner figure must match specific appearance details (oval face, copper skin, ornaments) exactly. Lighting contrast at portal threshold must show interior brightness against exterior dimness. Movement trajectory must follow dragging action from ship exterior toward building entrance without stopping. Camera positioning must reflect narrator observation perspective looking down at prisoner.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If Martians appear human-like, adjust anatomy to match warrior description. If interior light is not visible through portal, increase brightness contrast at threshold. If prisoner face features are distorted, correct oval face and eye details. Ensure banners and glowing devices on ship hull remain consistent with previous shots if visible in frame.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
