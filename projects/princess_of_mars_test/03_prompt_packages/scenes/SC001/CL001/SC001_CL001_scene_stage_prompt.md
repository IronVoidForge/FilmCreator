# Title
SC001 CL001 Scene Stage Prompt

# ID
SC001_CL001_scene_stage_prompt

# Purpose
Define the stage intent for Clip CL001 within Scene SC001, establishing Earthman leader's vantage point at upper floor window observing distant gray airships approaching deserted city in daylight

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide shot of tactical observer standing at upper floor window frame, hands on polished stone sill, observing distant horizon. Three-quarter angle showing observer's profile to camera. Dark wood window frame with metal accents visible in foreground. Soft morning light illuminating scene with dust motes visible in beam. Polished stone tiles visible on floor. Distant gray-painted airships visible in sky approaching valley and hills vista. Rooftops visible in background for scale reference. Plaza street level becoming clearer as ships approach. Clear natural daylight illuminating stone structures and sky. Companion standing beside observer, right side of frame, maintaining eye contact with fleet.

# Negative Prompt
Crowds blocking path, vehicles obstructing street, sudden appearance of female character, interior lighting mismatch, chaotic movement, close-up facial expressions, dark shadows obscuring foreground, floating debris, unnatural color grading, wrong number of ships visible, airships appearing too close or too far, green martian warriors on balcony ledge, over-the-shoulder view instead of profile shot

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, Scene SC001 overview
- optional_refs: 
- visible_character_assets: Earthman leader (stationary at window frame), Companion (standing beside Earthman leader)
- look_continuity_policy: Window Frame Consistent
- intended_lighting_change: Soft morning light transitioning to brighter midday as scene progresses
- composition_type: Wide Shot - Establishing fleet presence and observer reactions
- continuity_mode: Window Frame Consistent - Earthman leader maintains 2-3 feet from window frame throughout scene
- starting_keyframe_strategy: Static hold on Carter at window, hands on sill, observing distant horizon with neutral expression
- dependency_policy: Window frame color: dark wood with metal accents. Window faces plaza at 15-degree angle toward street level. Camera positioned inside looking through window.
- auto_advance_policy: 
- fallback_strategy: If Carter's hand placement varies, maintain sill position for first 3 seconds, allow slight movement during observation phase
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain Earthman leader's stationary position at window frame throughout clip.
- Ensure gray airships are distant and not overlapping foreground characters.
- Keep window wiper in upper right position unchanged for continuity.
- Preserve vertical axis (Earthman leader elevated above city).
- Verify natural daylight consistency across stone structures and sky.
- Floor material: polished stone tiles visible in medium shots.
- Window frame color: dark wood with metal accents.
- Camera axis parallel to window plane for profile shots.

# Repair Notes
- Adjust lighting if interior window frame becomes too dark compared to exterior view.
- Ensure Earthman leader does not move or stop abruptly during observation sequence.
- Verify distant airships do not overlap foreground characters incorrectly.
- Check aspect ratio remains consistent for medium profile shot.
- Maintain 2-3 feet distance from window frame throughout scene.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
