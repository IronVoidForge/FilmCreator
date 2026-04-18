# Title
SC001 CL003 Fix 01 Prompt

# ID
SC001_CL003_fix_01_prompt

# Purpose
Corrective still-generation for Clip CL003 Beat BT003, fixing local artifacts while preserving window view composition and emotional tone of abandonment.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
POV shot looking out from upper floor window frame, empty valley and hills visible in distance, natural sunlight gleaming on exterior landscape, interior room dimly lit, male narrator standing at window glass with anxious expression, hound resting nearby on floor but not blocking view, copper skin tone reference for context, high contrast between interior shadow and exterior light, cinematic depth of field

# Negative Prompt
blurry, low quality, distorted face, extra fingers, bad anatomy, text watermark, signature, noisy, overexposed, underexposed, wrong color palette, green tint on skin, floating objects, motion blur, dark vignette too heavy, window frame broken

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: image_1
- optional_refs: image_2
- visible_character_assets: narrator, hound
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV window view to close-up
- continuity_mode: insert
- starting_keyframe_strategy: approach window position
- dependency_policy: dependent on CL002
- auto_advance_policy: 
- fallback_strategy: static POV
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Preserve upper floor window frame geometry exactly.
- Maintain lighting consistency between interior shadow and exterior valley light.
- Ensure narrator expression matches anxious tone of abandonment.
- Keep hound in vicinity but not obstructing primary focal point.

# Repair Notes
- Fix any distortion on window glass or frame edges.
- Adjust exposure balance to prevent interior from being too dark relative to exterior view.
- Refine facial details on narrator to match approved still base.
- Ensure hound does not overlap key focal points in the composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
