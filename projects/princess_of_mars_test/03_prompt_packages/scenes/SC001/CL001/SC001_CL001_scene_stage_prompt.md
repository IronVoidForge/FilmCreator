# Title
SC001 CL001 Scene Stage Prompt

# ID
SC001_CL001_scene_stage_prompt

# Purpose
Define stage intent for Clip CL001 within Scene SC001, establishing fleet arrival and initial combat engagement between ships and city defenders from Carter's vantage point at upper floor window. The scene depicts the procession retreating to the city following an incubator ceremony, with a fleet of twenty gray airships arriving from the hills bearing strange banners. Green Martians fire volleys from building windows; ships return fire but suffer heavy damage due to suddenness and targeting tactics.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Medium shot from interior looking through dark wood window frame with metal accents. Carter standing static at polished stone window sill, hands resting on surface. Profile view facing outward toward horizon. Soft morning light illuminating interior dust motes and exterior sky. Distant formation of twenty gray-painted airships visible over hill crests in background. Each ship carrying strange banners and odd devices on prows. Rooftops and valley vista providing scale reference. Clear natural daylight contrasting warm interior with cool exterior. Green Martians visible firing from upper windows of buildings. Smoke trails beginning to appear on hulls indicating combat engagement.

# Negative Prompt
Crowds blocking path, vehicles obstructing street, sudden appearance of female character, interior lighting mismatch, chaotic movement, close-up facial expressions, dark shadows obscuring foreground, floating debris, unnatural color grading, wrong number of ships visible, airships appearing too close or too far, green martian warriors on balcony ledge (should be in windows), over-the-shoulder view instead of profile shot, companion standing beside observer, ship count not exactly twenty.

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, BT002.md, BT003.md, Scene SC001 overview
- optional_refs: Valley floor geography map
- visible_character_assets: Carter (stationary at window frame), Green Warriors fleet (distant formation)
- look_continuity_policy: Window Frame Consistent
- intended_lighting_change: Soft morning light transitioning to brighter midday as scene progresses
- composition_type: Medium Shot - Establishing fleet presence and observer reactions
- continuity_mode: Window Frame Consistent
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
- Maintain Carter's stationary position at window frame throughout clip.
- Ensure gray airships are distant and not overlapping foreground characters.
- Keep window wiper in upper right position unchanged for continuity.
- Preserve vertical axis (Carter elevated above city).
- Verify natural daylight consistency across stone structures and sky.
- Floor material: polished stone tiles visible in medium shots.
- Window frame color: dark wood with metal accents.
- Camera axis parallel to window plane for profile shots.
- Ship count continuity marker: exactly twenty vessels over hill crests.
- Banner positions must remain consistent across shots.
- Damage progression tracked across shots (smoke trails, hull breaches).

# Repair Notes
- Adjust lighting if interior window frame becomes too dark compared to exterior view.
- Ensure Carter does not move or stop abruptly during observation sequence.
- Verify distant airships do not overlap foreground characters incorrectly.
- Check aspect ratio remains consistent for medium profile shot.
- Maintain 2-3 feet distance from window frame throughout scene.
- Correct ship count if model generates fewer than twenty vessels.
- Fix banner orientation if they appear twisted or inconsistent.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
