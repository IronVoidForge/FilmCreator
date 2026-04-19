# Title
CH008_SC004 CL004 Cut Motion Prompt

# ID
CH008_SC004_CL004_cut_motion_prompt

# Purpose
Generate cut motion video from approved keyframe. Maintain observer perspective of human protagonist watching vessel burn and drift. Introduce slight camera forward lean as missiles approach target. Ensure continuity with rooftop warriors and valley environment. Transition to next beat while preserving lighting and grade.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Over-the-shoulder view of human observer below plaza edge, Green Martian warriors on building roofs above, long gray air craft vessel burning and drifting in valley floor, smoke plume rising, orange flames spurt from hull, daylight lighting, slight camera forward lean motion, vessel moving southeast across frame, rooftop warriors watching trajectory, Martian city buildings background.

# Negative Prompt
static image, morphing faces, extra characters, wrong vessel shape, blurry, distorted anatomy, inconsistent lighting, dark shadows, text, watermark, low resolution, jittery motion, sudden cuts, incorrect perspective, human observer face distortion, rooftop warrior count mismatch.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL004
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Carter positioned below on plaza edge observing entire sequence, partial view of rooftop warriors
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Over-the-shoulder shot (observer perspective)
- continuity_mode: cutaway
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: action-oriented
- batch_role: observer
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain observer perspective from plaza level looking up and across.
- Vessel trajectory must follow drift path southeast/southwesterly.
- Smoke density increases over time as vessel burns.
- Lighting remains daylight with fire glow on hull.
- No character movement until post-launch observation phase.

# Repair Notes
- If vessel shape distorts, revert to keyframe geometry.
- If lighting shifts too dark, add fire glow compensation.
- Ensure camera lean is subtle and matches interval beat timing.
- Fix any morphing of observer face or body structure.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
