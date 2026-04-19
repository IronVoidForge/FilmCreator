# Title
CH008_SC002 CL003 Scene Stage Prompt

# ID
CH008_SC002_CL003_scene_stage_prompt

# Purpose
Establish window point of view overlooking valley floor where multiple gray airships display visible structural damage including hull breaches and rising smoke. One ship remains intact among damaged vessels serving as focal point for salvage preparation. Green warriors positioned at building windows observe scene progression. Lighting maintains daylight quality with smoke haze adding atmospheric depth. Opening frame setup requires wide coverage showing scale of destruction before narrowing focus to single undamaged craft.

# Workflow Type
authoring.scene_stage

# Positive Prompt
window point of view overlooking valley floor, multiple gray airships displaying visible structural damage including hull breaches and rising smoke, one ship remains intact among damaged vessels serving as focal point for salvage preparation, green warriors positioned at building windows observing scene progression, daylight quality with smoke haze adding atmospheric depth, wide coverage showing scale of destruction before narrowing focus to single undamaged craft, deserted city buildings in background, hills beyond valley

# Negative Prompt
crew visible on deck, intact airships without damage, bright sunlight without smoke haze, close up on narrator face, interior building shots, night scene, fire consuming ship yet, extra vessels not part of battle count

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5.0
- required_refs: hull breaches visible, smoke rising from damaged ships, one ship remains unmanned
- optional_refs: window frame
- visible_character_assets: Martians observing from windows, Narrator noting damage progression
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/Medium
- continuity_mode: insert
- starting_keyframe_strategy: pan_across
- dependency_policy: linear_sequence
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
- Maintain count of damaged versus intact ships throughout sequence.
- Ensure hull breaches are clearly visible in wide shots to convey battle consequence.
- Do not show crew activity on deck of focal undamaged ship.
- Keep lighting consistent with daylight transitioning toward fire glow as salvage begins.

# Repair Notes
- If damage is too subtle, increase smoke opacity and hull breach visibility in generation parameters.
- If ship count is incorrect, adjust framing to exclude extra vessels or include only the intended damaged group.
- If focal point is unclear, tighten composition on single undamaged ship after initial wide pan.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
