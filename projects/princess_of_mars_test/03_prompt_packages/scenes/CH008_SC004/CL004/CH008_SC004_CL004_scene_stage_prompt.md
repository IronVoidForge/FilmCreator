# Title
CH008_SC004 CL004 Scene Stage Prompt

# ID
CH008_SC004_CL004_scene_stage_prompt

# Purpose
Define the staging intent, subject placement, and environmental context for the generation pipeline to understand the scene composition before rendering keyframes or video. This authoring-only section establishes the spatial relationships between the observer on the plaza and the action occurring on the rooftops and in the valley distance.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Observer perspective from plaza level looking up at rooftop warriors launching missiles, burning vessel in valley distance, daylight with smoke effects, partial view of building upper floors, green skin visible on distant figures, open ground plaza foreground, vertical axis from roofs down to valley floor, eyelines directed downward at vessel position.

# Negative Prompt
No close-up of face, no ground level view, no explosion obscuring main action, no green skin on observer, no character movement until post-launch observation phase, no debris present on roof surfaces, no smoke clearing significantly during beat.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC004
- clip_id: CL004
- duration_seconds: 5
- required_refs: CH008_SC004/BEAT_INDEX.md/BT001.md
- optional_refs: projects/princess_of_mars_test/02_story_analysis/beat_bundles/CH008_SC004/BEAT_INDEX.md
- visible_character_assets: Carter positioned below on plaza edge observing entire sequence, partial view of rooftop warriors
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Over-the-shoulder shot (observer perspective)
- continuity_mode: cutaway
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
- workflow_type: authoring.scene_stage

# Continuity Notes
- Carter remains stationary as observer throughout beat, positioned below on plaza edge observing entire sequence
- Warriors maintain static positions during launch for stability, no character movement until post-launch observation phase
- Vessel visible in valley floor distance, drifting away from engagement zone with smoke plume expanding rapidly
- Vertical axis from roofs down to valley floor, eyelines directed downward at vessel position
- Roof surfaces intact, no debris present, daylight with smoke effects consistent across frames

# Repair Notes
- Ensure Carter does not move into the frame or change expression during observation phase
- Verify vessel remains visible in distance without being obscured by foreground elements
- Check that smoke effects are consistent with previous impacts and do not clear too quickly
- Confirm rooftop warriors maintain their distribution across roof levels as per beat plan

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC004.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC004/CH008_SC004_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
