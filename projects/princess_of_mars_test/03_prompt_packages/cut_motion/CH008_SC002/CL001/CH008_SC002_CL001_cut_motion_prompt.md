# Title
CH008_SC002 CL001 Cut Motion Prompt

# ID
CH008_SC002_CL001_cut_motion_prompt

# Purpose
Depict Green Martian warriors firing a coordinated volley from city buildings at the approaching fleet in the valley. Camera captures the discharge sequence and impact reactions on the airships, maintaining daylight illumination and wide two-shot composition to establish scale of engagement.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green Martian warriors on upper floors, weapons charged, firing volley across valley floor, twenty gray airships approaching, explosions erupting on fleet hulls, smoke rising from impact points, daylight illumination, wide two-shot composition, city buildings framing action, distant hills beyond, atmospheric tension building, missile impact flames spurt.

# Negative Prompt
John Carter visible, window frame obstruction, close-up on narrator face, static camera, night lighting, calm atmosphere, no fire on warriors, intact fleet hulls before impact, loot items, boarding equipment, crew visible on ships (close-up), damage to hulls (premature), burning (on buildings).

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5.0
- required_refs: city buildings, green warriors, gray airships, valley floor
- optional_refs: distant hills
- visible_character_assets: Green Warriors, Fleet Crews (distant)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: wide two-shot
- continuity_mode: cut
- starting_keyframe_strategy: static_hold_on_eyeline
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
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain daylight lighting grade throughout motion.
- Ensure warriors are positioned on upper floors/buildings.
- Keep fleet movement consistent with approaching valley path.
- Do not introduce Carter or window frame in this beat.
- Explosions should occur only on fleet hulls at impact points, not on buildings.

# Repair Notes
- If camera drifts from wide two-shot, re-anchor to buildings and valley eyeline.
- If fire appears on warriors prematurely, remove it (only impact fires allowed).
- If fleet hulls are intact at end of clip, ensure explosions occur as per beat plan.
- If Carter or window frame appears, remove them from composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
