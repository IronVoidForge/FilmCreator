# Title
CH008_SC001 CL004 Keyframe Prompt

# ID
CH008_SC001_CL004_keyframe_prompt

# Purpose
Establish John Carter's perspective and emotional state as he watches air craft descend from an upper floor window. Capture the shift from curiosity to growing concern/anticipation. Frame the boundary between built structures (window) and open valley floor below. Include observer figure reacting to distant aerial threat source visible in background. City architecture frames edges. Open ground horizon visible ahead. Dramatic lighting emphasizes urgency of enemy airship threat.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Close-up static shot of John Carter at upper floor window, face and upper torso visible. Window frame edge visible on left side. Background shows valley below with distant hills. Expression shifts to growing concern/anticipation. Lighting is daylight with smoke haze from battle. No motion blur. High resolution. Cinematic composition.

# Negative Prompt
Motion blur, moving forward, running, chaotic crowd, modern clothing, bright sunny sky, empty background, distorted anatomy, extra limbs, text, watermark, signature, low resolution, blurry face, green screen, cartoonish style, proper nouns, names, specific character IDs, armored procession, warriors in green attire pivoting.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: None
- visible_character_assets: John Carter (upper torso, face), window frame partial
- look_continuity_policy: static_opening_with_full_procession_visible_before_movement_change
- intended_lighting_change: dramatic_fire_illumination_emphasizing_urgency
- composition_type: close_up_face_window_frame_edge
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: dependent_on_CL003_reaction_clip_first
- auto_advance_policy: none
- fallback_strategy: standard_static_frame_generation
- consistency_assist_policy: enabled
- consistency_assist_method: anatomical_correction_and_lighting_match
- anatomy_repair_policy: strict_anatomical_integrity
- consistency_targets: green_attire_color_palette, gray_structure_tone, elevated_command_signal_visibility
- style_profile: cinematic_compositional
- batch_role: keyframe_generation
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled
- shared_character_refs: empty_list
- shared_environment_refs: deserted_city_buildings, city_plaza

# Continuity Notes
- Window frame must be visible on left edge to establish location.
- Carter's expression should shift from curiosity to concern over 5 seconds.
- Background valley/hills must remain stable for continuity with other shots.
- Lighting must match daylight with smoke haze from battle scene.
- Ensure no motion blur artifacts in static image generation.

# Repair Notes
- Correct any anatomical distortions on John Carter's face or upper torso.
- Remove any text, watermarks, or signatures from the frame.
- Ensure no modern clothing elements appear in the scene.
- Check that the open ground horizon is clearly visible without obstruction.
- Confirm dramatic lighting emphasizes urgency without overexposing details.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL004.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
