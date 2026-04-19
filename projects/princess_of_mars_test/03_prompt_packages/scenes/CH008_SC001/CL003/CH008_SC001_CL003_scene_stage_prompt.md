# Title
CH008_SC001 CL003 Scene Stage Prompt

# ID
CH008_SC001_CL003_scene_stage_prompt

# Purpose
Establish the arrival of enemy airships from the valley horizon. Capture the visual threat through wide exterior view from window. Maintain continuity with previous clips (Martians melting away) and transition environment from interior observation to exterior visual field.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide shot exterior valley view from window, clear sky environment, twenty gray low-profile airships sailing toward valley center, banners on stem/stern visible, glowing devices on prow visible, ships entering from horizon moving toward camera, daylight lighting, cinematic composition, atmospheric depth, no ships initially then ships appearing, interior window frame edge visible, green warrior figures in distance.

# Negative Prompt
blurry face, distorted anatomy, wrong skin tone, static image, missing command signal, protagonist wearing green attire, dark lighting, crowded city buildings in foreground, calm expression, low resolution, extra limbs, incorrect eye direction, foggy atmosphere, text overlay, ships too small to see details, ships not entering from horizon.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: twenty_gray_airships_sailing_toward_valley, banners_on_ships, glowing_devices_on_ships, sky_environment
- look_continuity_policy: match_previous_clip_transition
- intended_lighting_change: maintain_daylight_open_valley
- composition_type: wide_shot_exterior_valley_view_from_window
- continuity_mode: cutaway
- starting_keyframe_strategy: static_clear_valley_view_no_ships_visible_yet
- dependency_policy: follows_CL002_directly
- auto_advance_policy: standard_cut_on_arrival_completion
- fallback_strategy: cut_to_pov_tracking_ships_if_scale_issue
- consistency_assist_policy: enable_character_consistency_check
- consistency_assist_method: 
- anatomy_repair_policy: prioritize_vehicle_detail_accuracy
- consistency_targets: 
- style_profile: cinematic_barsoom_warfare
- batch_role: scene_stage_authoring
- fix_of: CH008_SC001_CL003_fix_01_prompt.md

# Continuity Notes
- Ensure valley view matches previous clip CL002 interior perspective.
- Maintain open ground valley floor environment consistent with BT003.md airship arrival beat.
- Airships must enter from horizon to justify wide shot composition.
- Green warrior figures in background should not obstruct ship clarity.
- Lighting must remain daylight to match preceding clips CL001 and CL002.

# Repair Notes
- If ships appear too small or distant, adjust scale to ensure banners and glowing devices are visible.
- If valley view shows city buildings instead of open valley, adjust environment to match BT003.md geography.
- If movement looks static despite arrival implication, introduce subtle camera pan or zoom tracking ships entering.
- If protagonist face is prominent in foreground blocking view, reduce prominence to maintain wide shot composition.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
