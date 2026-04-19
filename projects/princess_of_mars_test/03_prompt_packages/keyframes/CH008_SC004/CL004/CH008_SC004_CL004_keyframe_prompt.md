# Title
CH008_SC004 CL004 Keyframe Prompt

# ID
CH008_SC004_CL004_keyframe_prompt

# Purpose
Establish the starting visual state for the observer point of view sequence, depicting the slender human figure being moved toward the structure entrance by green-skinned figures. Define the initial composition and lighting contrast between exterior dimness and interior glow.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Observer point of view looking down at slender human figure with oval face and copper skin being dragged forward by two green-skinned figures. Horizontal movement trajectory toward structure entrance portal. Interior light glowing warmly from inside building. Dim exterior lighting on ship hull background. Focus on facial features and limb tension during dragging action.

# Negative Prompt
blurry, distorted anatomy, extra limbs, text, watermark, wrong perspective, static image, no motion blur, incorrect lighting, missing face details, bright exterior sun, dark interior shadow only, obscured eyes, unnatural skin tone, floating elements, structural distortion.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md building portal entry beat
- optional_refs: POV dragging into building notes
- visible_character_assets: Female Martians, Prisoner figure, Building portal
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV of dragging into building
- continuity_mode: insert
- starting_keyframe_strategy: Starting keyfigure at ship exterior, oval face visible
- dependency_policy: No hard dependencies - can be shot independently
- auto_advance_policy: 
- fallback_strategy: Use close-up prisoner face if POV unavailable
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain green skin tone consistency across all figures.
- Ensure oval face shape is distinct and visible in starting frame.
- Keep building interior light warm and contrasting with exterior dimness.
- Preserve horizontal movement axis toward portal without vertical deviation.
- Match prisoner attire details (ornaments) to previous shots if applicable.

# Repair Notes
- If face is obscured, adjust camera angle slightly downward.
- If dragging action unclear, emphasize limb tension and grip points.
- If lighting contrast is weak, increase interior glow intensity relative to exterior.
- Ensure green skin tone does not shift to blue or brown during generation.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
