# Title
CH008_SC002 CL001 Keyframe Prompt

# ID
CH008_SC002_CL001_keyframe_prompt

# Purpose
Establish defensive firing position and scale of approaching threat through wide two-shot composition. Depict warriors positioned on ridge with weapons charged while maintaining valley-to-ridge eyeline perspective. Show twenty gray airships entering frame from distance during daylight conditions.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Ridge positioning, weapons charged in defensive stance, valley floor visible below, twenty gray airships entering frame from distance, daylight illumination, atmospheric tension, horizontal firing vector across open space, banners fluttering in wind, distant hills beyond city buildings, smoke from previous damage marks visible on valley floor.

# Negative Prompt
No text overlays, no ship damage at this stage, no flames or fire effects, no smoke from current battle, no crew figures on deck, no interior room details, no fire pyre elements, no warm color temperature shift, no explosion artifacts, no banner dissolution.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5.0
- required_refs: ridge positioning, twenty gray airships, valley floor, banners
- optional_refs: distant hills, previous damage marks
- visible_character_assets: Green Warriors (ridge position)
- look_continuity_policy: 
- intended_lighting_change: daylight_without_fire_illumination
- composition_type: Wide two-shot
- continuity_mode: cut
- starting_keyframe_strategy: static_hold_on_ridge_eyeline
- dependency_policy: sequential_to_next_beat_shot
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
- Ship count must remain exactly twenty throughout sequence.
- Warriors positioned on ridge with weapons charged in defensive stance.
- Valley floor visible below maintaining horizontal firing vector.
- Lighting state remains daylight without fire illumination at this stage.
- No damage marks visible on airship hulls at this keyframe point.
- Banners fluttering in wind must be consistent across shots.

# Repair Notes
- Correct any ship damage artifacts if present in generation.
- Ensure correct number of ships is rendered (twenty).
- Verify warriors are positioned on ridge with weapons charged.
- Maintain daylight color temperature without warm fire glow.
- Remove any explosion or flame effects from this keyframe.
- Check banner dissolution and restore intact banners.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
