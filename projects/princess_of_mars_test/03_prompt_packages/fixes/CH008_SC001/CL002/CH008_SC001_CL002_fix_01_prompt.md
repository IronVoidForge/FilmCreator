# Title
CH008_SC001 CL002 Fix 01 Prompt

# ID
CH008_SC001_CL002_fix_01_prompt

# Purpose
Corrective still-generation prompt that preserves composition and look while fixing local issues. Image_1 serves as approved base, image_2 as secondary reference when needed.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Procession of warriors marching in formation through city plaza transitioning to open ground valley. Carter positioned at rear of procession with synchronized forward movement. Green Martians warriors in central column wearing green attire. City architecture frames left and right sides. Open terrain visible ahead showing boundary between built environment and natural valley floor. Anticipation building among figures as they approach threshold. Medium tracking composition following Carter's position from behind.

# Negative Prompt
Anatomical errors, inconsistent lighting, wrong character count, misplaced elements, blurred details, incorrect color palette, anatomical distortions, extra limbs, missing weapons, wrong environmental state, inconsistent motion blur, poor depth of field, low resolution artifacts, facial expression mismatches, weapon placement errors, background element intrusions.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md processions_return_beat_documentation
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter rear_position, Warriors central_column visible
- look_continuity_policy: preserve_procession_movement_and_architecture_style
- intended_lighting_change: maintain_valley_transition_atmosphere
- composition_type: medium_tracking
- continuity_mode: insert
- starting_keyframe_strategy: follow_carter_position_from_rear_of_procession
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
- Procession moves forward with synchronized steps maintaining formation integrity
- Carter remains at rear position throughout tracking shot
- Warriors occupy central column visible in medium frame
- City plaza architecture transitions to open ground valley terrain
- Anticipation builds as procession approaches boundary threshold
- Movement logic follows forward progression toward valley entrance
- Environmental state shifts from built environment to natural terrain

# Repair Notes
- Preserve overall composition and architectural style while correcting local issues
- Maintain character placement consistency with approved base image
- Fix any anatomical errors or misplaced elements without altering motion logic
- Ensure lighting continuity matches valley transition atmosphere
- Correct environmental state transitions between city plaza and open ground
- Repair any inconsistent details while preserving cinematic warfare aesthetic

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
