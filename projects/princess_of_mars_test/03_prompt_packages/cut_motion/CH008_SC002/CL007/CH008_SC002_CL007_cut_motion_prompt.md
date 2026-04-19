# Title
CH008_SC002 CL007 Cut Motion Prompt

# ID
CH008_SC002_CL007_cut_motion_prompt

# Purpose
Track the retreating fleet movement away from the valley floor while maintaining continuity of damage and smoke trails. Ensure camera follows departure path without cutting to static angles, preserving keyframe lighting and grade throughout the motion sequence.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
wide aerial tracking shot following damaged gray vessels limping away from valley floor, smoke trails increasing density, banners dissolving in flame, urban architecture background visible, camera moving forward along retreat path, consistent lighting grade preserved, low profile ships swinging majestically then erratically, distant hills fading into background haze.

# Negative Prompt
static camera angle, close-up facial details, intact undamaged ships, clear weather without smoke, sudden cuts, bright daylight without atmospheric haze, new clean vessels, green-skinned warriors in foreground, sharp focus on individual crew members, explosion effects not matching damage progression.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL007
- duration_seconds: 5
- required_refs: BT004.md
- optional_refs: Wide retreat tracking shots coverage families
- visible_character_assets: Enemy Fleet, Smoke trails
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Wide aerial shot tracking fleet moving away from battle zone
- continuity_mode: Wide tracking shot following fleet departure from valley
- starting_keyframe_strategy: Open on fleet in damaged condition, several craft limping
- dependency_policy: Hard dependency on BT004 beat; must show retreat completion
- auto_advance_policy: 
- fallback_strategy: Use reblock_same_scene if need to adjust retreat path angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: Martian urban warfare aesthetic
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Ensure damage progression on vessels matches previous engagement state from BT004 beat.
- Maintain smoke trail density consistent with retreating damaged craft.
- Verify banner flame damage is progressive and not reset to pristine condition.
- Camera movement must follow retreat path without abrupt directional changes.

# Repair Notes
- If vessels appear new or clean, increase damage indicators in prompt or adjust generation parameters.
- If lighting shifts too much from keyframe, reinforce consistent grade instructions.
- If smoke trails disappear prematurely, add atmospheric haze descriptors to positive prompt.
- Ensure ship swing arc completes without cutting to static wide shot mid-motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
