# Title
CH008_SC002 CL006 Cut Motion Prompt

# ID
CH008_SC002_CL006_cut_motion_prompt

# Purpose
Fill in the stage intent here. Depict impact reaction points at specific target locations on the gray vessel hull while maintaining static window perspective and slight camera pan to follow damage progression. Preserve lighting and grade from approved keyframe.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
gray vessel hull with smoke puffs expanding at specific points, green-skinned warrior figure in window frame static, banners dissolving slightly in flame, slight camera pan following impact locations, battle zone sky background, valley floor below, cinematic lighting, high contrast smoke effects, medium shot composition, point-specific reaction shots continuity mode

# Negative Prompt
distorted anatomy, flickering lights, wrong color palette, static image, extra limbs, blurry text, smokeless impact, incorrect ship shape, low resolution, morphing windows, jittery camera motion, overexposed highlights, underexposed shadows

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: Impact reaction shots coverage families
- visible_character_assets: martian_warrior
- look_continuity_policy: preserve lighting and grade from approved keyframe
- intended_lighting_change: 
- composition_type: medium shot
- continuity_mode: point-specific reaction shots
- starting_keyframe_strategy: open on sighting apparatus, then cut to impact points
- dependency_policy: hard dependency on CL005
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
- Match lighting and color grade from previous clip (CL005) to ensure visual consistency.
- Ensure impact timing aligns with targeting sequence defined in BT003.md.
- Maintain static window perspective for the warrior figure while allowing camera pan for impact tracking.
- Verify smoke expansion speed matches cinematic action profile.

# Repair Notes
- If smoke is too faint, increase opacity and contrast in generation parameters.
- If ship shape distorts during motion, anchor to keyframe geometry from approved video.
- If camera pan is jerky, smooth the motion interpolation for visible movement.
- If impact points are misplaced, adjust targeting focus based on sighting apparatus alignment.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
