# Title
CH008_SC005 CL005 Scene Stage Prompt

# ID
CH008_SC005_CL005_scene_stage_prompt

# Purpose
Establish emotional anchor through eye contact between Carter and prisoner; show Carter's reaction to prisoner's state in background movement; medium shot composition with both characters visible for connection

# Workflow Type
authoring.scene_stage

# Positive Prompt
Carter face and upper body in foreground, eyes focused on prisoner in background, Martian city buildings with windows and roofs, daylight atmosphere, open ground plaza area, partial visibility of slender girlish figure with light reddish copper skin, coal black hair caught loosely into strange coiffure, highly wrought ornaments visible, green Martian warriors firing from buildings in distance, smoke from fire effects, missile impact flames spurt

# Negative Prompt
full body shots, other characters entering frame, excessive camera movement, close-up only on eyes, wide shot showing entire city, night lighting, indoor corridor setting, no prisoner visible, green Martian females dragging prisoner, air craft in foreground, explosion effects dominating frame

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL005
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT003, CH008_SC005/BT003.md Start State
- optional_refs: None
- visible_character_assets: Carter (face and upper body), Prisoner (background, partial visibility)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight with smoke from fire
- composition_type: Medium shot, both Carter and prisoner in frame for eye contact
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: Static frame showing Carter's face locked on prisoner's background movement
- dependency_policy: Depends on CL004 establishing conflict context; no reverse dependency
- auto_advance_policy: None
- fallback_strategy: If eye contact unclear, tighten to close-up on Carter's eyes or widen to show more of prisoner's expression
- consistency_assist_policy: None
- consistency_assist_method: None
- anatomy_repair_policy: None
- consistency_targets: Eye contact clarity, character identification
- style_profile: Action-oriented, awe-inspiring
- batch_role: scene_stage
- fix_of: None

# Continuity Notes
- Capture the continuity rules for this stage. Maintain eye line between Carter and prisoner throughout clip duration. Keep background movement consistent with previous shots showing prisoner being dragged into building. Ensure lighting matches daylight conditions with fire smoke effects from previous battle sequence. Character identification must remain clear - Carter as observer, prisoner as captive with distinctive reddish copper skin and coal black hair.

# Repair Notes
- Capture any repair or corrective guidance for this stage. If eye contact is not clearly established in initial render, tighten framing to close-up on Carter's eyes while maintaining background visibility of prisoner. If prisoner becomes too obscured by environment, widen shot slightly to show more of her upper body and distinctive features. Ensure no other characters enter frame during this emotional anchor moment.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
