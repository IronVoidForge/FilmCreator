# Title
SC001 CL005 Scene Stage Prompt

# ID
SC001_CL005_scene_stage_prompt

# Purpose
Describe staging intent for scene stage of SC001 CL005

# Workflow Type
authoring.scene_stage

# Positive Prompt
narrator standing in interior corridor, female companion entering frame from doorway, hound following close at heel, upper floor window view showing deserted valley and hills, sunlight gleaming on exterior devices, interior lighting dimmer than exterior, stone vessels visible, silks and furs worn by characters, wide axis along corridor length, vertical transition from entrance to corridor level, emotional weight of abandonment conveyed, peaceful ceremony fading into tense retreat

# Negative Prompt
crowds in immediate area, green warriors close up, airships landing nearby, proper names visible, bright interior lighting, dark exterior view, chaotic movement, blurred faces, distorted anatomy, low resolution

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL005
- duration_seconds: 5
- required_refs: none
- optional_refs: none
- visible_character_assets: narrator, female companion, hound
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
- Maintain narrator's position and movement through building from previous beats.
- Ensure lighting consistency between interior corridor and exterior window view.
- Track female companion's entrance timing relative to scene progression.
- Keep hound's positioning consistent throughout the sequence.

# Repair Notes
- Correct any distortion in character anatomy if visible.
- Fix lighting mismatches between interior and exterior views.
- Adjust composition to match previous keyframes for continuity.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
