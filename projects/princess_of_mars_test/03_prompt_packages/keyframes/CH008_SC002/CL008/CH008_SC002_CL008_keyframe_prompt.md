# Title
CH008_SC002 CL008 Keyframe Prompt

# ID
CH008_SC002_CL008_keyframe_prompt

# Purpose
Depict fleet ships swinging broadside to maximize firepower and reposition, showing crew realigning on damaged vessels with thrusters swaying.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Medium shot of gray-painted airship hull rotating on damaged thrusters, crew members moving to new firing positions, weapons realigned, smoke density increasing, debris scattered around vessel base, daylight mixed with orange fire illumination, valley city background with hills beyond.

# Negative Prompt
wide shot perspective, intact ship structure, dark night sky, close-up shots only, indoor lighting, human faces without green skin, modern technology, text overlays, blurry details, missing thruster damage, unburned cargo, floating debris unrelated to battle.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL008
- duration_seconds: 5.0
- required_refs: Ship rotation mechanism visible, crew silhouettes moving, smoke trails increasing
- optional_refs: Hull damage visible, valley geography beyond
- visible_character_assets: Crew members realigning weapons; Green-skinned warriors operating equipment
- look_continuity_policy: 
- intended_lighting_change: None
- composition_type: Medium shot
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: slight sway on damaged thrusters
- dependency_policy: parallel to wide shot for coverage
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
- Maintain medium shot perspective showing ship rotation.
- Ensure thruster sway is visible and consistent with damage state.
- Keep crew movement aligned with new firing angles.
- Preserve valley city geography with hills beyond.

# Repair Notes
- If ship looks static, increase thruster sway animation cues in still.
- If crew missing, add silhouettes of figures moving to positions.
- Ensure green skin tone consistency on warriors.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
