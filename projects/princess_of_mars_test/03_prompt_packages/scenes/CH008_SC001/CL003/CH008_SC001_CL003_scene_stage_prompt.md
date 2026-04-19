# Title
CH008_SC001 CL003 Scene Stage Prompt

# ID
CH008_SC001_CL003_scene_stage_prompt

# Purpose
Establish the sudden retreat order given upon entering open ground. Capture the protagonist male emotional shift from anticipation to urgency via reaction shot and visible command signal above horizon. Maintain continuity with procession movement while transitioning environment from city boundary to valley floor.

# Workflow Type
authoring.scene_stage

# Positive Prompt
protagonist male face, medium close up, expression of shock and urgency, open valley terrain background, vertical command signal visible above horizon, green warrior figures in distance, daylight lighting, cinematic composition, human observer reaction, sudden halt movement implied, atmospheric depth, clear focus on facial emotion.

# Negative Prompt
blurry face, distorted anatomy, wrong skin tone, static image, missing command signal, protagonist wearing green attire, dark lighting, crowded city buildings in foreground, calm expression, low resolution, extra limbs, incorrect eye direction, foggy atmosphere, text overlay.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL003
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter face_reaction, implied_command_signal_source
- look_continuity_policy: match_previous_procession_movement
- intended_lighting_change: maintain_daylight_open_valley
- composition_type: medium_close_up_reaction
- continuity_mode: cutaway
- starting_keyframe_strategy: static_on_carter_face_with_command_signal_visible_above
- dependency_policy: independent_can_follow_any_previous_clip
- auto_advance_policy: standard_cut_on_signal_completion
- fallback_strategy: cut_to_wide_halt_if_reaction_misread
- consistency_assist_policy: enable_character_consistency_check
- consistency_assist_method: 
- anatomy_repair_policy: prioritize_facial_expression_accuracy
- consistency_targets: 
- style_profile: cinematic_barsoom_warfare
- batch_role: scene_stage_authoring
- fix_of: 

# Continuity Notes
- Ensure protagonist male position matches previous procession rear placement.
- Maintain open ground valley floor environment consistent with BT002.md retreat order beat.
- Command signal must be visible above horizon to justify reaction shot.
- Green warrior figures in background should not obstruct protagonist face clarity.
- Lighting must remain daylight to match preceding clips CL001 and CL002.

# Repair Notes
- If protagonist expression appears too calm, increase urgency indicators in facial muscle tension.
- If command signal is missing or obscured, add vertical light source above horizon.
- If background shows city buildings instead of open valley, adjust environment to match BT002.md geography.
- If movement looks static despite retreat order implication, introduce subtle camera shake or shift.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
