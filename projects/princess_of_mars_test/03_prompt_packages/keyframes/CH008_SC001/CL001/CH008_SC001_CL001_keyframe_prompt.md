# Title
CH008_SC001 CL001 Keyframe Prompt

# ID
CH008_SC001_CL001_keyframe_prompt

# Purpose
Establish observer figure position at interior window and initial calm observation state before action begins. Show valley view below with horizon visible for ship arrival.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Medium shot of observer figure standing at interior window frame, looking out towards distant valley landscape. Room interior dimly lit with warm ambient light. Through window, valley floor visible with low-lying gray vessels entering from horizon line. Observer posture relaxed but attentive. Architectural details of fortified urban structure visible in foreground. Cinematic composition, atmospheric depth, red planet environment lighting.

# Negative Prompt
blurry, low resolution, modern clothing, extra characters, distorted faces, wrong color palette (blue sky), static image without motion cues, crowded composition, text, watermark, deformed limbs, exterior plaza view, procession, green attire marching, martians melting into mist.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC001
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: CH008_SC001_scene_breakdown
- visible_character_assets: narrator_standing_at_window, interior_window_frame, cityscape_below_view
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: medium_shot_interior
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: static_opening_with_subtle_body_shift
- dependency_policy: standalone_initial_test_clip
- auto_advance_policy: 
- fallback_strategy: cut_to_alternate_wide_angle_if_needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: still.scene_build.four_ref.klein.distilled

# Continuity Notes
- Maintain window frame visibility.
- Ensure interior lighting matches warm ambient mood.
- Keep ship entry timing consistent with valley view.
- Avoid showing martians melting in this specific keyframe.

# Repair Notes
- Fix any anatomy distortions on observer figure.
- Ensure room geometry is consistent.
- Correct color grading to match red planet environment if needed.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC001/CH008_SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
