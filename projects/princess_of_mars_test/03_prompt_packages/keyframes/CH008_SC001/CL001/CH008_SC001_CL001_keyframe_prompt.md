# Title
CH008_SC001 CL001 Keyframe Prompt

# ID
CH008_SC001_CL001_keyframe_prompt

# Purpose
Establish tactical context and enemy threat scale. Start State: Martians moving in calm procession across valley floor. End State: Enemy airships visible on horizon, urgency begins.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Wide establishing shot of Green Martian warriors in green attire marching in synchronized formation across valley floor. Deserted city buildings frame left and right with upper floors visible. Hills beyond create depth. Horizon shows distant gray airships approaching. Lighting suggests high stakes anticipation. Cinematic composition, detailed textures, atmospheric depth, red planet atmosphere, dramatic shadows.

# Negative Prompt
blurry, low resolution, modern clothing, extra characters, distorted faces, wrong color palette (blue sky instead of red planet atmosphere), static image without motion cues, crowded composition, text, watermark, deformed limbs, bright daylight, green sky, white clouds, urban transit vehicles, civilian structures, blue-tinted lighting.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: Green Martian warriors (group formation 5-7 Martians)
- look_continuity_policy: reblock_same_scene
- intended_lighting_change: daylight_to_dramatic_fire_illumination
- composition_type: wide_establishing
- continuity_mode: independent_no_prerequisites
- starting_keyframe_strategy: valley_floor_axis_with_procession_movement_visible
- dependency_policy: standalone_tactical_context
- auto_advance_policy: none
- fallback_strategy: cut_to_alternate_wide_angle_if_needed
- consistency_assist_policy: maintain_warrior_count_and_formation
- consistency_assist_method: visual_reference_matching
- anatomy_repair_policy: fix_distorted_limb_positions
- consistency_targets: warrior_group_size_building_locations
- style_profile: cinematic_compositional
- batch_role: establishing_shot
- fix_of: none
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain procession axis perpendicular to valley entrance.
- Keep warrior formation consistent with previous shots.
- Ensure enemy airships appear on horizon at 2.5s mark.
- Transition from city plaza to open ground must be visible in background.
- Preserve red planet atmosphere throughout all frames.

# Repair Notes
- Fix any anatomy distortions on warriors.
- Ensure lighting matches high-stakes atmosphere.
- Correct color grading to match red planet environment if needed.
- Verify airship visibility timing aligns with beat schedule.
- Check that building locations remain consistent across shots.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
