# Title
CH008_SC001 CL002 Fix 01 Prompt

# ID
CH008_SC001_CL002_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Image_1 serves as approved base, image_2 as secondary reference when needed. Focus on Martians melting into mist within interior room space transitioning to exterior view. Narrator at window remains stationary. Ensure dissolve timing marker is preserved.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Martians visible in lower room space beginning to fade into mist. Dissolution progresses upward outward. Martians becoming translucent. Room empty except for narrator at window. Interior lighting establishes mood. Mist moisture effect critical for continuity. Wide shot interior to exterior blend. Narrator positioned at interior window with clear line of sight to valley. Martians occupy floor level before dissolving upward outward into mist. No physical movement, only state change.

# Negative Prompt
Anatomical errors, inconsistent lighting, wrong character count, misplaced elements, blurred details, incorrect color palette, anatomical distortions, extra limbs, missing weapons, wrong environmental state, inconsistent motion blur, poor depth of field, low resolution artifacts, facial expression mismatches, weapon placement errors, background element intrusions, martians appearing solid instead of translucent, narrator moving from window position, mist effect missing.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT002.md martians_melting_away_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: martians_visible_in_lower_room_space, mist_moisture_dissolve_effect, narrator_at_window_periphery
- look_continuity_policy: preserve_melting_transition_and_architecture_style
- intended_lighting_change: maintain_valley_transition_atmosphere
- composition_type: wide_shot_interior_to_exterior_blend
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: follow_martian_presence_beginning_dissolve
- dependency_policy: dependent_on_CL001_wide_establishing_first
- auto_advance_policy: none
- fallback_strategy: cut_to_medium_static_if_movement_disrupted
- consistency_assist_policy: enabled
- consistency_assist_method: composition_lock
- anatomy_repair_policy: strict
- consistency_targets: character_placement_environment_state_motion_logic
- style_profile: cinematic_warfare_valley_transition
- batch_role: still_fix_stage_01
- fix_of: CL002_melting_transition_shot

# Continuity Notes
- Martians visible in lower room space, beginning to fade into mist
- Dissolution progresses upward outward, martians becoming translucent
- Martians fully dissolved; room empty except for narrator at window
- Interior lighting establishes mood consistent with dissolve effect
- Narrator remains stationary at window position throughout transition

# Repair Notes
- Preserve overall composition and architectural style while correcting local issues
- Maintain character placement consistency with approved base image
- Fix any anatomical errors or misplaced elements without altering motion logic
- Ensure lighting continuity matches dissolve atmosphere
- Correct environmental state transitions between interior room and exterior view
- Repair any inconsistent details while preserving cinematic warfare aesthetic

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
