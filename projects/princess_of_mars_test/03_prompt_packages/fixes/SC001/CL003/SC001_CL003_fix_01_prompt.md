# Title
SC001 CL003 Fix 01 Prompt

# ID
SC001_CL003_fix_01_prompt

# Purpose
Corrective still-generation preserving window view composition and emotional tone

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Close-up facial shot of human male figure standing at window glass, three-quarter profile view, interior room dimly lit with polished stone tiles visible, exterior valley and hills bathed in natural sunlight, upper floor window frame geometry intact, warm skin tones matching reference base, neutral expression with slight smile of interest visible on face, hound resting nearby on floor without obstructing focal point, cinematic depth of field, high contrast between interior shadow and exterior light

# Negative Prompt
blurry, low quality, distorted face, extra fingers, bad anatomy, text watermark, signature, noisy, overexposed, underexposed, wrong color palette, green tint on skin, floating objects, motion blur, dark vignette too heavy, window frame broken, interior too dark relative to exterior

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: image_1
- optional_refs: image_2
- visible_character_assets: human male figure, hound
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up facial
- continuity_mode: insert
- starting_keyframe_strategy: approach window position
- dependency_policy: dependent on CL002
- auto_advance_policy: static hold
- fallback_strategy: static POV
- consistency_assist_policy: preserve geometry
- consistency_assist_method: reference alignment
- anatomy_repair_policy: facial refinement
- consistency_targets: window frame, lighting balance
- style_profile: cinematic depth of field
- batch_role: fix
- fix_of: local artifacts

# Continuity Notes
- Preserve upper floor window frame geometry exactly.
- Maintain lighting consistency between interior shadow and exterior valley light.
- Ensure human male figure expression matches neutral tone with slight smile.
- Keep hound in vicinity but not obstructing primary focal point.

# Repair Notes
- Fix any distortion on window glass or frame edges.
- Adjust exposure balance to prevent interior from being too dark relative to exterior view.
- Refine facial details on human male figure to match approved still base.
- Ensure hound does not overlap key focal points in the composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
