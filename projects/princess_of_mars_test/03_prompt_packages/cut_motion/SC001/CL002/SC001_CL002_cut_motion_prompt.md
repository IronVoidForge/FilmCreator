# Title
SC001 CL002 Cut Motion Prompt

# ID
SC001_CL002_cut_motion_prompt

# Purpose
Execute cut motion transition establishing fleet scale and formation while maintaining spatial continuity from upper floor observation point. Transition from window perspective to exterior wide shot showing twenty gray airships positioned at base of first hill crest, then distributed across multiple crests in coordinated retreat formation. Preserve keyframe lighting and grade by default. Focus on visible fleet movement pattern across terrain with elevation changes.

# Workflow Type
video.cut_motion.wan.i2v

# Positive Prompt
Wide establishing shot cutting from interior window POV to distant horizon view. Twenty gray airships forming synchronized pattern across sky above hill crests. Ships positioned at base of first crest then distributed across multiple reference points in formation. Strange banners visible on ship prows with odd devices on individual vessels. Morning light brightening throughout sequence. Camera maintains subject-object relationship while tracking fleet movement along horizontal plane with slight elevation variations. Minimal character movement; focus on fleet formation and relationship to landscape. Hill crests create depth axis for ship positioning.

# Negative Prompt
static image, sudden jump cut, distorted anatomy, extra limbs, flickering lights, wrong color grade, exterior sunlight bleeding into interior, blurry motion, morphing characters, static background, incorrect camera angle, narrator figure walking through entrance, interior corridor space, doorway frame, building entrance, interior corridor, ship count less than twenty, missing banners, missing devices, wrong hill crest positioning, inconsistent lighting levels

# Inputs
- project_id: princess_of_mars_test
- scene_id: SC001
- clip_id: CL002
- duration_seconds: 5
- required_refs: SC001 beat bundle BT001.md and BT002.md, Ship positions relative to hill crests continuity notes, Banner visibility markers across shots
- optional_refs: Hill crest depth axis reference points, Movement timing consistency notes, Interior lighting level contrast warm versus cool
- visible_character_assets: Green Martian Warriors fleet, Airships
- look_continuity_policy: Preserve keyframe lighting and grade by default
- intended_lighting_change: None
- composition_type: Wide exterior establishing shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: insert_fleet_position_base
- dependency_policy: dependent_on_window_frame_continuity
- auto_advance_policy: 
- fallback_strategy: cutaway_to_individual_ship_detail
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: Ship count twenty, window framing elements, banner designs, device shapes
- style_profile: 
- batch_role: 
- fix_of: 
- workflow_type: video.cut_motion.wan.i2v

# Continuity Notes
- Preserve the keyframe lighting and grade by default.
- Focus on visible motion, camera behavior, and environment change.
- Start from upper floor window frame.
- Maintain spatial continuity from previous clip.
- Fleet approaches in steady formation with twenty ships maintained throughout sequence.
- Hill crests create depth reference points for ship positioning across multiple shots.
- Banner designs must be identifiable across shots.
- Window framing and interior elements must stay consistent.

# Repair Notes
- Fix any anatomy distortions if movement is too fast.
- Ensure lighting remains consistent with interior observation point baseline.
- Correct color grade drift towards exterior sunlight.
- Smooth out camera push-in speed inconsistencies.
- Verify ship count of twenty maintained in wide shots.
- Check banner visibility markers across interval frames.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/SC001.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/SC001/SC001_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
