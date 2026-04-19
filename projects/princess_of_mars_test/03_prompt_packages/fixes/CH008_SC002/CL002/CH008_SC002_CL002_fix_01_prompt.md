# Title
CH008_SC002 CL002 Fix 01 Prompt

# ID
CH008_SC002_CL002_fix_01_prompt

# Purpose
Corrective still-generation task that preserves established visual style and composition while addressing local generation issues in weapon discharge close-up sequence from green warrior hands firing volley fire from elevated building windows with smoke effects and battle zone below visible.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
green-skinned warrior hands gripping weapon, discharge moment with smoke effects, elevated window position, battle zone below visible, slight zoom motion, cinematic lighting matching scene continuity, medium close-up composition, green skin tone consistency, weapon mechanics clear, smoke progression from impact points, valley floor perspective from building height.

# Negative Prompt
proper nouns, unrealistic anatomy, wrong color palette, inconsistent lighting, distorted weapon mechanics, missing smoke effects, incorrect composition angles, overexposed smoke, distorted hands, mismatched skin tone, wrong weapon type, inconsistent scale, blurred details, unnatural shadows, incorrect perspective from window height.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL002
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: weapon discharge coverage families
- visible_character_assets: green_warriors_hands_weapon
- look_continuity_policy: match established style
- intended_lighting_change: 
- composition_type: medium_close_up
- continuity_mode: close_up_detail_work
- starting_keyframe_strategy: open on weapon positioned
- dependency_policy: soft_dependency_on_CL001
- auto_advance_policy: none
- fallback_strategy: use_insert_if_needed
- consistency_assist_policy: maintain smoke progression
- consistency_assist_method: progressive_damage_tracking
- anatomy_repair_policy: fix hand_weapon_grip
- consistency_targets: green_skin_tone, weapon_discharge_timing, smoke_effects
- style_profile: cinematic_action_detail
- batch_role: still_fix_corrective
- fix_of: CL002_initial_generation

# Continuity Notes
- Maintain green warrior skin tone consistency with established palette from BT001.md
- Weapon discharge timing must align with interval beats 0-5 seconds
- Smoke effects should progress from impact points below visible in frame
- Elevated window perspective must match previous shots from building height
- Slight zoom motion on discharge moment to emphasize action detail
- Battle zone below maintains proper scale and distance from window position
- Green warrior hands grip weapon with realistic anatomy for close-up detail

# Repair Notes
- Address any hand_weapon_grip inconsistencies in anatomy repair policy
- Ensure smoke effects don't overexpose or obscure weapon discharge mechanics
- Verify weapon discharge timing matches established beat intervals from BT001.md
- Check that battle zone below maintains proper scale and distance from window height
- Confirm green skin tone consistency with previous shots in scene continuity
- Fix any distorted weapon mechanics to match cinematic action detail style profile

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
