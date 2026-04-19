# Title
CH008_SC001 CL002 Scene Stage Prompt

# ID
CH008_SC001_CL002_scene_stage_prompt

# Purpose
Establish visual staging for wide establishing shot from John Carter's upper floor window perspective showing twenty large gray air craft vessels descending toward city building facade. Focus on vessel appearance consistency (long, low, gray-painted with strange banners and odd devices on prows). Capture the downward diagonal movement trajectory from upper sky to lower city level. Frame should show valley below and hills beyond for geographic continuity. The opening keyframe intent is to show first air craft visible in distance, then fleet expands during clip duration. This sets stage for coming conflict between Green Martians firing from buildings and Air Fleet returning fire.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide establishing shot from upper floor window perspective, twenty large gray air craft vessels descending toward city building facade, long low gray-painted vessels with strange banners visible on prows, odd devices on vessel fronts, figures crowding forward decks, downward diagonal movement trajectory from upper sky to lower city level, valley below visible in background, hills beyond maintaining geographic continuity, daylight lighting, smoke from fire spurt visible from missile impact flames, anticipation building atmosphere, John Carter observer POV eyeline directed downward toward valley/city, vertical axis from upper floor to ground level.

# Negative Prompt
Close-up facial details, indoor setting only, night time, static pose, wrong faction colors (non-gray vessel paint), forward progression into valley terrain, sudden halt or reverse movement within clip duration, blurred background, incorrect character count, missing strange banners on vessels, missing odd devices on prows, characters not crowding forward decks, abrupt cuts breaking continuity, Carter position inconsistent in window frame.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md air_craft_descending_beat_documentation, CH008_SC001_scene_breakdown
- optional_refs: CH008_SC001_clip_roster
- visible_character_assets: Air craft fleet twenty vessels (long low gray-painted with strange banners), Green Martian figures crowding forward decks
- look_continuity_policy: maintain vessel appearance consistency across shots, valley/hills background stable
- intended_lighting_change: daylight consistent with establishing shots
- composition_type: wide_establishing_shot_from_window_pov
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_hold_first_craft_visible_in_distance
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: insert_if_movement_disrupted
- consistency_assist_policy: vessel banner and device appearance tracking
- consistency_assist_method: literal_descriptive_appearance_verification
- anatomy_repair_policy: focus on vessel silhouette and movement flow
- consistency_targets: twenty vessels tracked, valley/hills background continuity
- style_profile: cinematic_compositional
- batch_role: establishing_shot_fleet_arrival
- fix_of: none

# Continuity Notes
- Maintain tracking shot consistency with downward diagonal vessel movement throughout the 5-second duration.
- Ensure location transition cues (upper sky to lower city level) are visible in background/environment without abrupt cuts.
- Keep air craft appearance consistent (long, low, gray-painted vessels with strange banners and odd devices on prows).
- Position valley below and hills beyond stable across shots for geographic continuity.
- Track vessel count at twenty throughout clip duration.
- Maintain daylight lighting consistency with previous establishing shots.

# Repair Notes
- If vessel lacks physical description details, focus on silhouette and movement flow rather than facial features.
- Ensure air craft are distinct from any other factions present (Green Martians separate).
- Verify that the downward descent momentum is maintained until the end of the clip.
- Check for correct lighting consistency with previous establishing shots (daylight).
- If vessel count appears incorrect, adjust to show twenty vessels visible during interval beats.
- Ensure strange banners and odd devices on prows are visible in each shot.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
