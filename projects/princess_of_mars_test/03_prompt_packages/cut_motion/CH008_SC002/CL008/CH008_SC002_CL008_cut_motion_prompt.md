# Title
CH008_SC002 CL008 Cut Motion Prompt

# ID
CH008_SC002_CL008_cut_motion_prompt

# Purpose
Resolve scene through wide shot showing ship being towed away with finality; maintain window POV perspective while capturing motion of towing equipment and fading fire effects on hull.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
wide shot of gray airship moving away from valley floor, green figures operating towing equipment attached to hull, smoke rising from burning structure, fire glow diminishing on ship surface, camera holds static wide angle, background shows deserted city buildings under daylight, lighting shifts from dramatic fire illumination to natural daylight.

# Negative Prompt
morphing, flickering, extra limbs, distorted faces, text, watermark, blurry, low resolution, sudden lighting changes, inconsistent anatomy, ship deformation, fire effects inconsistency, window frame distortion.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Ship fully consumed by fire, towing equipment deployed, ship moving away from building
- optional_refs: Window frame
- visible_character_assets: Martians operating towing equipment; Narrator watching resolution
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide/POV
- continuity_mode: cutaway
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain consistent green warrior appearance and human narrator visibility throughout motion sequence.
- Preserve fire glow intensity on ship hull while transitioning to daylight background illumination.
- Ensure ship movement trajectory aligns with towing equipment deployment state from previous keyframe.
- Keep window frame obstruction consistent if visible in foreground perspective.

# Repair Notes
- Fix any morphing of green warrior limbs or hands during towing operation.
- Correct fire effects on ship hull to match fading intensity without flickering artifacts.
- Adjust lighting balance to ensure daylight background does not overpower residual fire glow on subject.
- Repair ship deformation if hull appears stretched or compressed during motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
