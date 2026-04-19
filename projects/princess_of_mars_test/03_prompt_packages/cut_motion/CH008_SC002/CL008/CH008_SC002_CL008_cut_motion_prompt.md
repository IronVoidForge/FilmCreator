# Title
CH008_SC002 CL008 Cut Motion Prompt

# ID
CH008_SC002_CL008_cut_motion_prompt

# Purpose
Medium shot of Martian Fleet Crews realigning weapons as their damaged gray airship swings broadside to maximize firepower during engagement with Green Warriors.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
medium shot of crew members on gray painted airship hull, ship rotating on damaged thrusters swinging broadside, crew adjusting weapons to new firing angles, smoke rising from scorched hull, daylight background showing city buildings and valley floor, fire glow diminishing on ship surface, camera holds static medium angle, lighting shifts from dramatic fire illumination to natural daylight.

# Negative Prompt
morphing, flickering, extra limbs, distorted faces, text, watermark, blurry, low resolution, sudden lighting changes, inconsistent anatomy, ship deformation, fire effects inconsistency, window frame distortion, green warrior appearance change.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Fleet in staggered formation, damaged hulls visible, crew in defensive positions
- optional_refs: Hull damage visible, smoke density increasing
- visible_character_assets: Martian Fleet Crews; Green Warriors (distant)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Medium/Action
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: slight sway on damaged thrusters
- dependency_policy: parallel to wide shot for coverage
- auto_advance_policy: 
- fallback_strategy: insert crew adjusting angles if movement erratic
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain consistent green Martian Fleet Crew appearance and damaged gray airship hull throughout motion sequence.
- Preserve fire glow intensity on ship hull while transitioning to daylight background illumination.
- Ensure ship rotation trajectory aligns with broadside maneuver state from previous keyframe.
- Keep thruster sway consistent if visible in foreground perspective.

# Repair Notes
- Fix any morphing of crew limbs or hands during weapon realignment operation.
- Correct fire effects on ship hull to match fading intensity without flickering artifacts.
- Adjust lighting balance to ensure daylight background does not overpower residual fire glow on subject.
- Repair ship deformation if hull appears stretched or compressed during rotation motion.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
