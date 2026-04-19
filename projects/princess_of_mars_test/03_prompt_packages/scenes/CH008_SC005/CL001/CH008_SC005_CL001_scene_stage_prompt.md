# Title
CH008_SC005 CL001 Scene Stage Prompt

# ID
CH008_SC005_CL001_scene_stage_prompt

# Purpose
Define spatial setup for wide establishing shot of CL001 within CH008_SC005. Focus on female figure entry trajectory and male observer observation point at corridor threshold. Establish urgency through movement path and gaze alignment without proper nouns.

# Workflow Type
authoring.scene_stage

# Positive Prompt
wide exterior shot, building corridor entrance threshold, slender female figure entering from left edge moving diagonally toward center-right, human male observer standing stationary at center-right facing camera, daylight atmosphere with distant smoke haze, full body female figure visible, partial profile male figure visible, urgent movement speed increasing as she nears, open ground plaza background context.

# Negative Prompt
air fleet ships, green martian warriors in foreground, close up faces, wrong movement direction, blurry figures, extra characters, indoor lighting, static background elements unrelated to corridor, proper nouns, specific names, dark shadows obscuring movement.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL001
- duration_seconds: 5
- required_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC005/BEAT_INDEX.md, projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC005/BT001.md
- optional_refs: None
- visible_character_assets: female companion full body, male observer upper body
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide_two_shot
- continuity_mode: cutaway_to_action
- starting_keyframe_strategy: insert_from_distance
- dependency_policy: reblock_same_scene
- auto_advance_policy: 
- fallback_strategy: If Sola entry is unclear, tighten to medium wide and emphasize her movement path
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain axis where female figure enters from left and moves toward center-right.
- Keep male observer stationary at center-right facing camera for observation.
- Ensure background implies city buildings or valley context consistent with Chapter 8 environment index.
- Preserve urgency in movement speed as female figure approaches male observer.

# Repair Notes
- If female figure entry is unclear, tighten to medium wide and emphasize her movement path.
- If gaze alignment fails, adjust eyeline to ensure both characters lock eyes during final meters of approach.
- If lighting appears inconsistent with daylight/smoke context, correct exposure to match distant fire haze.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
