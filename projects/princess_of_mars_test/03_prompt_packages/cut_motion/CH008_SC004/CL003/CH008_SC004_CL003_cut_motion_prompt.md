# Title
CH008_SC004 CL003 Cut Motion Prompt

# ID
CH008_SC004_CL003_cut_motion_prompt

# Purpose
Define extreme wide shot motion capturing missile trajectory toward distant vessel while maintaining valley floor lighting and smoke continuity from previous impacts. Focus on visible projectile movement, camera observation behavior, and environmental change during flight sequence.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
extreme wide shot of gray missiles traveling through air toward distant burning vessel, thick smoke rising from valley floor, city building roofs visible in upper frame, daylight illumination, camera positioned at plaza level looking across landscape, motion of projectiles mid-flight, orange flames spurt from hull damage, dark gray smoke trail behind vessel, warriors watching trajectory from distance

# Negative Prompt
static image, close-up shot, indoor scene, night time, green skin texture visible, human faces clearly defined, explosion without missiles, dark shadows, low resolution, distorted geometry, missing smoke, wrong color palette, sudden lighting shifts, incorrect vessel position

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Missiles in flight, vessel visible in valley floor distance, smoke rising from previous impacts
- look_continuity_policy: preserve_valley_lighting_and_smoke_density
- intended_lighting_change: none
- composition_type: Extreme wide shot (action context)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: standard
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: enabled
- consistency_assist_method: 
- anatomy_repair_policy: disabled
- consistency_targets: 
- style_profile: action_context
- batch_role: clip_3
- fix_of: 

# Continuity Notes
- Preserve valley floor lighting and smoke density from previous impacts during motion.
- Maintain camera position at plaza level looking up and across throughout the sequence.
- Ensure missile trajectory remains consistent with launch sequence without sudden deviation.
- Do not introduce new characters or change vessel damage state significantly during motion.
- Keep vessel drift path aligned with valley floor geography.

# Repair Notes
- If smoke appears too thin, increase opacity to match previous impact plumes.
- If vessel drifts incorrectly, anchor position to valley floor center relative to frame.
- Ensure missile count matches launch sequence (multiple projectiles visible in flight).
- Correct any lighting shifts that deviate from daylight grade established in keyframe.
- Fix geometry distortions on missiles or vessel hull during motion blur.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
