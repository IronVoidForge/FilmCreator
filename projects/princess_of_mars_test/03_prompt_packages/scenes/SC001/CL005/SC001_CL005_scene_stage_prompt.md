# Title
SC001 CL005 Scene Stage Prompt

# ID
SC001_CL005_scene_stage_prompt

# Purpose
Describe staging intent for scene stage of SC001 CL005

# Workflow Type
authoring.scene_stage

# Positive Prompt
human male warrior standing at upper floor window observing gray airships approaching deserted city valley and hills, interior stone floor visible, dark wood window frame with metal accents, daylight view showing fleet formation across landscape, soft morning light transitioning to brighter midday, emotional weight of anticipation conveyed, wide axis along window plane

# Negative Prompt
crowds in immediate area, enemy combatants close up, airships landing nearby, text labels, readable signage, bright interior lighting, dark exterior view, chaotic movement, blurred faces, distorted anatomy, low resolution

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: none
- optional_refs: none
- visible_character_assets: narrator human male warrior
- look_continuity_policy: match previous beats
- intended_lighting_change: interior dimmer than exterior
- composition_type: medium tracking to close-up
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: establish interior space
- dependency_policy: none
- auto_advance_policy: none
- fallback_strategy: none
- consistency_assist_policy: enabled
- consistency_assist_method: reference frames
- anatomy_repair_policy: enabled
- consistency_targets: character positions, lighting consistency
- style_profile: cinematic realism
- batch_role: scene_stage
- fix_of: none

# Continuity Notes
- Maintain narrator's position relative to window frame throughout sequence.
- Ensure fleet formation and positioning consistency across shots.
- Track lighting shift from soft morning to bright midday as scene progresses.
- Keep interior stone floor material consistent in medium shots.
- Align eyelines with narrator's shoulder height (approximately 5'8" camera level).

# Repair Notes
- Correct any distortion in character anatomy if visible.
- Fix lighting mismatches between interior and exterior views.
- Adjust composition to match previous keyframes for continuity.
- Ensure window frame shadows deepen slightly as light changes.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
