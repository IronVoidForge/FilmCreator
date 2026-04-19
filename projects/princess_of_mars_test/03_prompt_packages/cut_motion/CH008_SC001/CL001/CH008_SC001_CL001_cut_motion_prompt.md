# Title
CH008_SC001 CL001 Cut Motion Prompt

# ID
CH008_SC001_CL001_cut_motion_prompt

# Purpose
Establish wide exterior view of city perimeter with approaching procession and distant horizon anchor. Start State: Empty perimeter line visible with horizon stable, End State: Camera tracks forward along procession path maintaining eye-level perspective. Capture smooth progression of scene establishment while preserving established lighting and grade from approved keyframe.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
wide exterior shot showing city boundary line as visual anchor, approaching ground forces entering frame from distance, distant horizon figures visible, gray-painted airships in background with consistent color grading, strange banners on prow requiring specific prop placement, odd devices on prow needing continuity tracking, camera moves forward tracking procession path, natural daylight preserved, atmospheric depth maintained, static opening frame transitioning to gentle forward motion along procession

# Negative Prompt
morphing faces, flickering lights, close-up when wide exterior expected, distorted limbs, inconsistent color grading, sudden zooms, blurry text, extra characters, wrong background, low resolution, noise, anatomy errors, lighting shifts, jerky movement, inconsistent character placement, warping environment, incorrect horizon line, static camera when tracking expected, wrong composition type, missing procession elements

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: approaching ground forces, distant horizon figures, gray-painted airships background
- look_continuity_policy: preserve_keyframe_lighting_and_grade
- intended_lighting_change: none
- composition_type: wide_exterior_city_perimeter
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: horizon_anchor_with_city_perimeter_line
- dependency_policy: independent_no_prerequisites
- auto_advance_policy: smooth_forward_progression
- fallback_strategy: cut_to_alternate_wide_angle_if_needed
- consistency_assist_policy: enabled
- consistency_assist_method: motion_flow_matching
- anatomy_repair_policy: standard
- consistency_targets: character_placement_and_motion_smoothness
- style_profile: cinematic_warfare
- batch_role: clip_01
- fix_of: null
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Maintain city perimeter line as visual anchor throughout shot
- Preserve established lighting and color grade from approved keyframe
- Ensure background airships maintain consistent gray-painted appearance
- Monitor forward tracking motion along procession path
- Keep character count consistent (approaching forces, horizon figures only)
- Track strange banners on prow for prop placement continuity

# Repair Notes
- If composition shifts to close-up, revert to wide exterior angle
- If lighting changes occur, match keyframe grade exactly
- If camera movement is jerky, smooth interpolation along procession path
- If background warps, correct to city perimeter and horizon continuity
- If airship color grading inconsistent, restore gray-painted appearance

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
