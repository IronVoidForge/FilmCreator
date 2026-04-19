# Title
CH008_SC004 CL002 Scene Stage Prompt

# ID
CH008_SC004_CL002_scene_stage_prompt

# Purpose
Define staging intent for Clip CL002 within Scene CH008_SC004. Establish wide shot composition across three roof levels during missile launch sequence. Contextualize environmental setting with Martian city roofs and valley floor visibility. Set visible opening frame to show warriors in static observation posture with missiles ready, ensuring vertical axis from roofs down to valley floor remains unobstructed.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green warriors distributed across multiple building roof levels. Missiles visible in hands or on shoulders. Valley floor visible below. Smoke rising from previous impacts. Daylight conditions. Static observation posture. Vertical axis from roofs down to valley.

# Negative Prompt
Close-up shots of individual faces. Night time lighting. Heavy debris on roof surfaces. Moving characters during launch sequence. Human female prisoner in frame. Air craft hulls directly adjacent.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Green Warriors distributed across 3 roof levels (approximately 4 per level), partial view of valley floor
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot (establishing multiple warriors)
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert
- dependency_policy: standalone
- auto_advance_policy: 
- fallback_strategy: reframe_same_moment
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Vertical axis from roofs to valley floor must remain consistent throughout clip.
- Unobstructed line of sight between camera and valley floor is required.
- Warriors maintain static positions during launch phase for stability.
- Smoke density should match previous impact plumes without sudden expansion.
- Vessel visibility in distance must align with drift trajectory from prior beats.

# Repair Notes
- Ensure warriors do not shift weight excessively during observation phase.
- Verify missile visibility on shoulders or hands is clear and consistent.
- Check smoke plume consistency with previous impacts to avoid visual discontinuity.
- Confirm valley floor remains visible without obstruction from building geometry.
- Adjust lighting if smoke obscures background too heavily for continuity tracking.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
