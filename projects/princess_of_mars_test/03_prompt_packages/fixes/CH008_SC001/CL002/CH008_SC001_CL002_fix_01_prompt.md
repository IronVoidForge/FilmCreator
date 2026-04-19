# Title
CH008_SC001 CL002 Fix 01 Prompt

# ID
CH008_SC001_CL002_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Image_1 serves as approved base, image_2 as secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Wide establishing shot showing twenty large gray air craft descending from upper sky toward city building facade. Long low vessels with strange banners visible on prows. Valley below and hills beyond maintain continuity. Figures crowd forward decks of vessels. Downward diagonal movement from upper sky to lower city level. Gray-painted vessels with odd devices on prows.

# Negative Prompt
Anatomical errors, inconsistent lighting, wrong character count, misplaced elements, blurred details, incorrect color palette, anatomical distortions, extra limbs, missing weapons, wrong environmental state, inconsistent motion blur, poor depth of field, low resolution artifacts, facial expression mismatches, weapon placement errors, background element intrusions, John Carter, Earthling Woman, bright daylight interiors, open ground valley floor.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md air_craft_descending_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: air_craft_fleet_20_vessels
- look_continuity_policy: preserve_air_craft_descending_motion_and_architecture_style
- intended_lighting_change: maintain_valley_transition_atmosphere_daylight
- composition_type: wide_establishing_shot_from_pov
- continuity_mode: insert
- starting_keyframe_strategy: show_first_air_craft_visible_in_distance
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: cut_to_wide_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: composition_lock
- anatomy_repair_policy: strict
- consistency_targets: character_placement_environment_state_motion_logic
- style_profile: cinematic_warfare_valley_transition
- batch_role: still_fix_stage_01
- fix_of: CL002_wide_establishing_shot

# Continuity Notes
- Air craft appear consistent (long, low, gray-painted with strange banners)
- Number of vessels tracked at 20
- Valley terrain visible beyond building exteriors
- Hills beyond maintain directional context
- Downward diagonal movement from upper sky to lower city level
- Figures crowd forward decks of vessels

# Repair Notes
- Preserve overall composition and architectural style while correcting local issues
- Maintain character placement consistency with approved base image
- Fix any anatomical errors or misplaced elements without altering motion logic
- Ensure lighting continuity matches daylight atmosphere
- Correct environmental state transitions between exterior and valley/hills
- Repair any inconsistent details while preserving cinematic warfare aesthetic

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
