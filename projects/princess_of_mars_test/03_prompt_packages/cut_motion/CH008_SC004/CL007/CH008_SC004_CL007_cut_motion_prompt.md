# Title
CH008_SC004 CL007 Cut Motion Prompt

# ID
CH008_SC004_CL007_cut_motion_prompt

# Purpose
Generate extreme wide shot motion for vessel drift trajectory, preserving daylight grade and keyframe lighting while capturing full path from center to right side of frame.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Extreme wide shot of gray air vessel drifting toward valley edge, smoke trail expanding behind hull, roaring flames diminishing on surface, distant hills beyond city buildings, warriors on roofs watching from distance, daylight lighting preserved, camera captures full drift path trajectory, visible motion of vessel moving southeast, smoke plume rising steadily above vessel.

# Negative Prompt
distorted vessel shape, flickering smoke, wrong composition, text overlay, sudden lighting changes, close-up framing, static image, green skin distortion, fire color shift, camera shake, blurry details, extra limbs on warriors.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL007
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT002.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Vessel drifting toward valley edge, smoke trail visible behind vessel, warriors watching from distance with concern
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Extreme wide shot (context)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: action-oriented, awe-inspiring
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Vessel must drift from center toward right side of frame maintaining consistent trajectory.
- Smoke trail must remain continuous with previous impact plumes without reversing flow.
- Daylight lighting and grade must match approved keyframe exactly.
- Warriors on roofs must maintain observation positions without sudden movement during drift.
- Hull lightening by loot removal visible but vessel shape must not distort.

# Repair Notes
- Ensure vessel hull integrity remains consistent throughout motion sequence.
- Correct smoke flow direction if it appears to reverse or detach from hull.
- Adjust fire intensity if flames diminish too quickly or too slowly compared to interval beats.
- Verify warrior silhouettes do not flicker or morph during camera movement.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL007.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
