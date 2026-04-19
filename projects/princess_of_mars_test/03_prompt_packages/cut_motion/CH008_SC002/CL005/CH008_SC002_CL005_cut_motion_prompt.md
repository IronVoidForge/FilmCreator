# Title
CH008_SC002 CL005 Cut Motion Prompt

# ID
CH008_SC002_CL005_cut_motion_prompt

# Purpose
Focus on precision targeting mechanics and impact tracking within established grade. Describe slight zoom motion on apparatus, reticle movement, and smoke accumulation at target points while preserving keyframe lighting and environment continuity.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Green-skinned Martian targeting team, mechanical sighting apparatus, optical lens tracking, smoke trails from impact points, building window background, valley battle zone below, slight zoom motion, reticle movement, explosion smoke rises, gray airship silhouette, green skin texture, metallic apparatus details.

# Negative Prompt
blurry focus, wrong color palette, human skin texture on Martians, static image without motion, overexposed highlights, distorted apparatus mechanics, bright sunlight, indoor lighting mismatch, low resolution, morphing anatomy, floating debris unrelated to impact.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: Close-up targeting shots coverage families
- visible_character_assets: Martians (targeting team), Sighting apparatus active
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Medium close-up of sighting apparatus visible and active
- continuity_mode: Close-up precision detail work on targeting mechanics
- starting_keyframe_strategy: Open on targeting team positioned, apparatus tracking targets
- dependency_policy: Soft dependency on BT003 beat; can stand alone for precision focus
- auto_advance_policy: None
- fallback_strategy: Use reframe_same_moment if need to adjust targeting angle
- consistency_assist_policy: None
- consistency_assist_method: None
- anatomy_repair_policy: Ensure green skin tone matches keyframe
- consistency_targets: Apparatus tracking, smoke density, target impact points
- style_profile: Cinematic action detail
- batch_role: Action/Impact tracking
- fix_of: None

# Continuity Notes
- Preserve keyframe lighting and grade by default for visible motion.
- Focus on camera behavior (slight zoom/static) and environment change (smoke accumulation, target impact).
- Ensure green skin texture remains consistent with established Martian warrior assets.
- Maintain smoke density consistency at impact points without overexposing highlights.
- Verify apparatus tracking mechanics align with precision targeting beat intent.

# Repair Notes
- If green skin tone drifts, adjust to match keyframe reference exactly.
- If smoke density is too low, increase particle accumulation at target points.
- If motion appears static, introduce slight zoom or reticle movement to indicate tracking.
- If lighting shifts, revert to original keyframe grade without introducing new shadows.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
