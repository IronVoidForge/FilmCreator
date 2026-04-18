# Title
SC001 CL006 Cut Motion Prompt

# ID
SC001_CL006_cut_motion_prompt

# Purpose
Cutaway detail shot maintaining continuity markers from previous clips while transitioning from device detail perspective back to wider fleet context. Eyeline shifts from wide formation to close examination of banners and devices on individual ship prows, preserving window framing consistency and daylight grade throughout sequence.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
green warrior stands at upper floor window frame in profile view, hands resting on dark wood sill with metal accents, observing distant gray airships swinging slowly over hill crests, sunlight brightens midday exterior, smoke rises from burning vessel in background, camera slowly pushes forward while focus axis shifts from fleet-wide formation to individual ship prows, banners dissolve in spurts of flame, green figures drop at bullet explosions, close examination of strange devices on vessel prows, curiosity focused on mysterious objects

# Negative Prompt
distorted faces, extra limbs, flickering lights, dark shadows, night time, blurry motion, inconsistent anatomy, text overlays, watermark, morphing artifacts, ship count changes, window frame color shift, interior lighting grade deviation, banner design inconsistency, device shape variation, unmanned vessel appearance

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL006
- duration_seconds: 5
- required_refs: SC001 beat bundle BT003.md, banner designs continuity markers across all shots, device shapes continuity markers across all shots, ship prow details visible in frame
- optional_refs: Hill crests depth context for close-ups, Lighting consistency notes, Interior lighting level warm contrast from CL001
- visible_character_assets: green warrior, gray airships, burning vessel
- look_continuity_policy: window_frame_consistent
- intended_lighting_change: daylight brightens midday exterior
- composition_type: medium_profile_cutaway
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_continuity_marker_detail
- dependency_policy: dependent_on_all_previous_clip_continuity_elements
- auto_advance_policy: cutaway_to_hill_crest_context
- fallback_strategy: cutaway_to_hill_crest_context
- consistency_assist_policy: maintain_banner_device_continuity
- consistency_assist_method: visual_reference_markers
- anatomy_repair_policy: fix_morphing_on_face_if_expression_shifts_fast
- consistency_targets: ship_count_20, window_framing_elements, banner_designs, device_shapes
- style_profile: sci_fi_adventure_war_observation
- batch_role: cut_motion_clip
- fix_of: SC001_CL006_cut_motion_prompt
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Green warrior attire remains consistent throughout clip with dark wood window frame and metal accents
- Window frame color matches dark wood with metal accents from previous clips
- Daylight transitions from soft morning to bright midday exterior grade
- Fleet formation and positioning consistency maintained across hill crests
- Ship count of twenty gray airships must remain consistent in wide shots
- Banner designs must be identifiable across all shots for continuity markers
- Device shapes on vessel prows establish visual reference points throughout sequence
- Interior lighting level warm contrast from CL001 preserved in window observation point

# Repair Notes
- Fix morphing on face if expression shifts too fast during eyeline movement
- Ensure ship count remains consistent at twenty in background wide shots
- Correct lighting shift if grade deviates from bright midday daylight exterior
- Maintain banner design consistency across all visible ships in frame
- Verify device shapes on individual vessel prows match continuity markers
- Check interior window framing elements stay consistent with previous clips
- Repair any morphing artifacts on green warrior profile view

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
