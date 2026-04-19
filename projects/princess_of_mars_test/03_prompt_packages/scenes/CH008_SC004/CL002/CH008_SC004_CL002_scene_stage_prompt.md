# Title
CH008_SC004 CL002 Scene Stage Prompt

# ID
CH008_SC004_CL002_scene_stage_prompt

# Purpose
Define the staging intent for the wide ship exterior shot during the prisoner extraction sequence. Establish environmental context and character placement for narrator observation within the Martian city architecture. Ensure visual continuity with interior shots while transitioning to exterior industrial lighting state.

# Workflow Type
authoring.scene_stage

# Positive Prompt
gray low-profile vessel with banners on stem stern, green-skinned warriors dragging slender figure, open portal entrance, dim industrial lighting, slender human woman with ornaments, Martian city architecture background, wide composition showing ship hull boundary, vertical axis prisoner low warriors standing, eyeline narrator looking down at prisoner.

# Negative Prompt
bright daylight, floating debris, distorted warrior anatomy, extra limbs, wrong skin tone on prisoner, text overlays, blurry faces, excessive smoke obscuring subjects, mechanical movement artifacts, bright sun glare, incorrect banner placement, missing glowing devices on prow.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md, Environmental state dim lighting industrial texture
- optional_refs: Wide shot warriors dragging action notes
- visible_character_assets: Green Warriors, Ship hull, Portal/opening
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide ship exterior showing portal
- continuity_mode: cutaway
- starting_keyframe_strategy: Starting keyframe interior to exterior transition
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: 
- fallback_strategy: Use medium shot warriors dragging if wide unavailable
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ensure prisoner appearance matches previous close-ups (oval face, copper skin, ornaments).
- Maintain ship design consistency with fleet description (gray, low profile, banners).
- Lighting should transition from interior dim to exterior industrial without sudden brightness spikes.
- Warrior anatomy must remain consistent across cutaway shots (green skin, standard build).
- Portal visibility must be clear to show entry point into building structure.

# Repair Notes
- If warrior anatomy is unclear, use standard green warrior model reference.
- If prisoner is obscured by ship hull, adjust angle to show face and ornaments clearly.
- If lighting is too bright, reduce exposure to match industrial dim state.
- Ensure banners and glowing devices are present on vessel prow/stern.
- Fix any floating debris or mechanical artifacts in movement trajectory.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
