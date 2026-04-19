# Title
CH008_SC001 CL002 Fix 01 Prompt

# ID
CH008_SC001_CL002_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Image_1 serves as approved base, image_2 as secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Group of Green Martian warriors entering dark doorways in deserted city buildings. Medium shot composition showing synchronized entry motion from exterior perspective. Doorway frames visible with interior shadows swallowing figures. Deserted valley city architecture surrounding entrances. Martians wearing green attire moving inward into darkness. Over-the-shoulder angle from doorway threshold looking into building interiors. Synchronized steps maintaining formation integrity as they vanish within three minutes.

# Negative Prompt
Anatomical errors, inconsistent lighting, wrong character count, misplaced elements, blurred details, incorrect color palette, anatomical distortions, extra limbs, missing weapons, wrong environmental state, inconsistent motion blur, poor depth of field, low resolution artifacts, facial expression mismatches, weapon placement errors, background element intrusions, Carter, Earthling Woman, bright daylight interiors, open ground valley floor.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md building_entry_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Green Martian warriors group_clusters_entrance
- look_continuity_policy: preserve_building_entry_motion_and_architecture_style
- intended_lighting_change: maintain_valley_transition_atmosphere_dark_interiors
- composition_type: medium_shot_over_the_shoulder
- continuity_mode: insert
- starting_keyframe_strategy: follow_group_entry_from_doorway_threshold
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: composition_lock
- anatomy_repair_policy: strict
- consistency_targets: character_placement_environment_state_motion_logic
- style_profile: cinematic_warfare_valley_transition
- batch_role: still_fix_stage_01
- fix_of: CL002_medium_tracking_shot

# Continuity Notes
- Martians enter doorways in groups maintaining formation integrity
- Green attire visible against dark building interiors
- Doorway frames clear and accessible with no obstacles
- Interior shadows swallowing figures as they vanish
- Deserted city buildings frame the entrance axis
- Valley terrain visible beyond building exteriors
- Motion logic follows forward progression into darkness

# Repair Notes
- Preserve overall composition and architectural style while correcting local issues
- Maintain character placement consistency with approved base image
- Fix any anatomical errors or misplaced elements without altering motion logic
- Ensure lighting continuity matches dark interior atmosphere
- Correct environmental state transitions between exterior and doorway interiors
- Repair any inconsistent details while preserving cinematic warfare aesthetic

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
