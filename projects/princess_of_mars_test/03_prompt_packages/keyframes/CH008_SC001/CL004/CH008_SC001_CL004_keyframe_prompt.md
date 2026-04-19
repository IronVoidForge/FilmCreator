# Title
CH008_SC001 CL004 Keyframe Prompt

# ID
CH008_SC001_CL004_keyframe_prompt

# Purpose
Establish sudden halt and reverse movement of armored procession upon receiving retreat order. Capture shift from calm anticipation to urgent tactical response within wide composition. Frame the boundary between built structures and open valley floor where warriors pivot toward rearward direction. Include observer figure reacting to elevated command signal source visible above terrain. City architecture frames left and right edges. Open ground horizon visible ahead. Dramatic lighting emphasizes urgency of enemy airship threat.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide static shot of armored procession halting abruptly on boundary between built structures and open valley floor. Central column of warriors in green attire pivots toward rearward direction. Observer figure positioned at rear reacts to elevated command signal source visible above terrain. City architecture frames left and right edges. Open ground horizon visible ahead. Dramatic lighting emphasizes urgency.

# Negative Prompt
Motion blur, moving forward, running, chaotic crowd, modern clothing, bright daylight, sunny sky, empty background, distorted anatomy, extra limbs, text, watermark, signature, low resolution, blurry face, green screen, cartoonish style, proper nouns, names, specific character IDs.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL004
- duration_seconds: 5
- required_refs: BT002.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Carter rear_position, Warriors central_column
- look_continuity_policy: static_opening_with_full_procession_visible_before_movement_change
- intended_lighting_change: dramatic_fire_illumination_emphasizing_urgency
- composition_type: wide_halt_reverse
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_full_procession_visible_before_movement_change
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
- Procession must fully cross threshold before halt command executes.
- Reverse movement must be coordinated toward city boundary.
- Command signal source must remain visible in elevated position.
- Character placement maintains rear observer at back, warriors in central column.
- Lighting continuity matches previous reaction clip.
- Ensure static image quality without motion blur artifacts.
- Correct any anatomical distortions on warrior armor or observer figure.
- Maintain consistent color palette for green attire and gray structures.
- Verify command signal visibility matches elevated source reference.

# Repair Notes
- Ensure static image quality without motion blur artifacts.
- Correct any anatomical distortions on warrior armor or observer figure.
- Maintain consistent color palette for green attire and gray structures.
- Verify command signal visibility matches elevated source reference.
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
