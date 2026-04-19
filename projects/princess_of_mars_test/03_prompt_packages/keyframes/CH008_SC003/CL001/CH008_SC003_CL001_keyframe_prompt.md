# Title
CH008_SC003 CL001 Keyframe Prompt

# ID
CH008_SC003_CL001_keyframe_prompt

# Purpose
Establish aftermath and vertical axis for boarding action, static opening keyframe showing drifting craft positioned centrally with building roofs as elevated approach point, wide angle composition from rooftop position.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Green-skinned warriors positioned on upper building rooftops, long low gray vessels floating in plain below, smoke rising from damaged craft, daylight illumination, arched doorway visible on building facade, distant hills beyond valley floor, wide shot composition, static camera position, deserted urban environment with battle aftermath.

# Negative Prompt
human female facial features, earthling male face, motion blur, night lighting, fire glow, wrong skin tones, extra characters, text overlays, close-up details, interior shadows too deep, copper flooring reflections, plaza ground surface, narrator presence.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md, CH008_SC003/BEAT_INDEX.md
- optional_refs: plaza_environment_assets.md
- visible_character_assets: green_warriors_on_building_roofs, drifting_craft_in_plain_below
- look_continuity_policy: independent_opening_keyframe_with_contextual_reference_to_bodies_strewn_about
- intended_lighting_change: daylight with smoke haze
- composition_type: wide_angle
- continuity_mode: tracking_shot_of_drifting_craft
- starting_keyframe_strategy: establishing_wide_frame_from_building_roof_position
- dependency_policy: independent
- auto_advance_policy: none
- fallback_strategy: reframe_same_moment_if_tracking_fails_to_show_vertical_axis
- consistency_assist_policy: cinematic_compositional
- consistency_assist_method: literal_descriptive
- anatomy_repair_policy: sparse_conservative
- consistency_targets: vertical_axis_between_roof_and_plain
- style_profile: still.scene_build.four_ref.klein.distilled
- batch_role: opening_keyframe
- fix_of: null

# Continuity Notes
- Camera positioned at rooftop elevation looking down toward plain below.
- Vertical axis emphasized between building roofs and drifting craft in plain.
- Warriors visible on upper floors with arched doorways, craft floating centrally in frame.
- Static camera position for opening keyframe establishing spatial relationship.
- Smoke from battle damage creates atmospheric haze across scene.
- Distant hills provide directional context beyond valley floor.

# Repair Notes
- Ensure green skin tone matches Martian warriors without over-saturation.
- Avoid motion blur in static opening keyframe.
- Verify vertical axis between roof and plain is clearly visible.
- Confirm daylight lighting with smoke haze creates proper atmospheric depth.
- Check that drifting craft shows battle damage from missile impacts.
- Ensure no human facial features appear in frame.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
