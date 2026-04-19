# Title
CH008_SC002 CL002 Scene Stage Prompt

# ID
CH008_SC002_CL002_scene_stage_prompt

# Purpose
Define visual staging for medium close-up weapon discharge within building window frame, establishing downward firing angle and smoke initiation mechanics.

# Workflow Type
authoring.scene_stage

# Positive Prompt
green-skinned warrior hands gripping firearm inside stone window frame, downward angle to valley floor, smoke plume emerging from muzzle, dark interior background with rim light, medium close-up composition, cinematic lighting, high detail texture on weapon and skin, tension in grip before discharge

# Negative Prompt
deformed fingers, civilian faces, bright sunlight, static background, wrong weapon type, blurry focus, text overlays, logos, distorted smoke, floating debris unrelated to battle, wide shot perspective

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Close-up weapon discharge coverage families
- visible_character_assets: martian_warrior_hands, smoke_effects
- look_continuity_policy: maintain weapon position consistency with previous volley shots
- intended_lighting_change: dark interior with rim light from window edge
- composition_type: medium close-up
- continuity_mode: close-up detail work with focus on discharge mechanics
- starting_keyframe_strategy: open on weapon already positioned, ready for volley
- dependency_policy: soft dependency on CL001; can follow immediately after
- auto_advance_policy: none
- fallback_strategy: use insert if need to emphasize discharge timing
- consistency_assist_policy: ensure smoke originates from muzzle and impact points below match established geography
- consistency_assist_method: check downward angle consistent with window height
- anatomy_repair_policy: regenerate anatomy focus if hands look unnatural
- consistency_targets: bullet drop timing, weapon positioning, smoke progression
- style_profile: cinematic action detail
- batch_role: targeting close-up
- fix_of: CL001

# Continuity Notes
- Maintain weapon position consistency with previous volley shots.
- Ensure smoke originates from muzzle and impact points below match established geography.
- Keep downward angle consistent with window height.
- Verify bullet drop timing against explosion points in subsequent clips.
- Track banner flame damage progression if visible in background.

# Repair Notes
- If hands look unnatural, regenerate anatomy focus.
- If weapon type mismatches other clips, adjust to standard firearm used by green-skinned warriors.
- Check impact timing against bullet drop physics.
- Ensure smoke density matches previous discharge shots for continuity.
- Verify rim lighting does not overexpose interior details.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
