# Title
CH008_SC003 CL008 Scene Stage Prompt

# ID
CH008_SC003_CL008_scene_stage_prompt

# Purpose
Define staging intent for tracking shot of burning ship drifting southeast as funeral pyre within fortified Martian city valley. Focus on environmental context and subject placement regarding fire progression, smoke dispersion, and distant warrior observation without boarding the vessel. Ensure visual continuity with previous looting sequence and establish departure vector for next scene transition.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Gray low-profile vessel ablaze, smoke plume rising vertically then dispersing with wind, drifting southeast vector, distant green-skinned warriors observing from elevated positions, fortified city buildings in background providing scale, fire intensity increasing over time, ash and debris scattering on water surface, funeral pyre atmosphere, open valley setting, atmospheric haze.

# Negative Prompt
Static ship movement, modern technology elements, clear characters boarding burning vessel, smokeless fire, wrong drift direction (northwest), bright daylight without atmospheric haze, clean hull without burn damage progression, sharp focus on distant figures, urban clutter obscuring valley view.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL008
- duration_seconds: 5
- required_refs: BT003.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: None on vessel, Warriors (distant)
- look_continuity_policy: maintain drift vector and fire spread pattern
- intended_lighting_change: fire glow intensifies against ambient valley light
- composition_type: tracking shot
- continuity_mode: insert
- starting_keyframe_strategy: open on burning ship drift vector
- dependency_policy: depends on CL007
- auto_advance_policy: 
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ship axis must align with southeast drift vector throughout clip duration.
- Fire intensity progression must follow aft-to-forward sections without skipping damage zones.
- Distant warriors remain at safe observation distance, no boarding actions on burning hull.
- Background buildings provide scale reference for vessel size and smoke plume height.
- Ash scattering on water surface must match wind direction established in previous clips.

# Repair Notes
- If smoke density is insufficient, increase atmospheric haze or particle count without obscuring hull details.
- If drift vector appears static, adjust camera parallax to simulate smooth southeast movement.
- Ensure fire spread pattern matches aft-to-forward progression specified in beat bundle BT003.
- Verify distant warriors do not overlap with burning vessel silhouette in wide shots.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL008.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
