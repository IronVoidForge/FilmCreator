# Title
CH008_SC004 CL001 Scene Stage Prompt

# ID
CH008_SC004_CL001_scene_stage_prompt

# Purpose
Establish the staging intent for CL001 within BT001 (Missile Launch Sequence). Focus on the medium shot composition of a Green Martian warrior preparing to deploy a missile from a building roof. Define the vertical spatial relationship between the roof level and the distant valley floor where the vessel is located. Ensure the opening keyframe captures the warrior's readiness with the missile visible in hands or on shoulders, maintaining the observer perspective (Carter below) through downward-directed eyelines without including human features in the frame.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green Martian warrior, medium shot, front-facing, holding missile, hands, shoulders, roof surface, daylight, smoke plume, distant valley floor, green skin, ornaments, spears, static position, vertical axis from roofs down to valley, missile deployment begins.

# Negative Prompt
Human faces, Air Fleet ships, debris on roof, night lighting, close-up of face only, night sky, explosion in immediate frame, Carter visible in shot, flying objects, close-range combat, chaotic movement.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL001
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: green_martian_warrior
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Vertical axis from roofs down to valley floor.
- Eyelines directed downward at vessel position.
- Line of sight unobstructed by terrain features.
- Camera positioned at plaza level looking up and across.
- Warriors maintain static positions during launch for stability.
- No character movement until post-launch observation phase.
- Vessel lightened by loot removal visible in distance.

# Repair Notes
- Ensure anatomy consistency for warrior hands holding missile.
- Maintain green skin tone accuracy without desaturation.
- Avoid accidental inclusion of human observer features in the frame.
- Verify roof surface texture matches established city building style.
- Check smoke plume density aligns with previous impact events.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
