# Title
CH008_SC002 CL009 Keyframe Prompt

# ID
CH008_SC002_CL009_keyframe_prompt

# Purpose
Show close-up of damaged ship rotation mechanism with crew hands adjusting thrusters during broadside repositioning sequence

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
close-up shot, metallic ship rotation mechanism, corroded thruster housings, crew hands gripping control levers, smoke rising from hull damage, debris scattered on deck surface, daylight illumination, industrial warship texture, mechanical alignment vector visible, damaged propulsion system, crew adjusting for new firing angle

# Negative Prompt
proper nouns, character faces, detailed facial features, full body shots, wide landscape views, interior cabin scenes, pristine hull condition, undamaged machinery, bright clear weather, peaceful atmosphere, civilian vessels, modern technology, clean surfaces, no smoke or fire effects, static composition without movement indicators

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL009
- duration_seconds: 5
- required_refs: BT003 index, CL008 medium shot
- optional_refs: hull damage visible, smoke density increasing
- visible_character_assets: Ship rotation mechanism, crew hands
- look_continuity_policy: sequential to crew realignment medium shot
- intended_lighting_change: daylight with smoke shadows
- composition_type: close-up
- continuity_mode: cutaway
- starting_keyframe_strategy: static on rotation mechanism
- dependency_policy: sequential to crew realignment medium shot
- auto_advance_policy: none
- fallback_strategy: insert debris scattered if rotation heavy
- consistency_assist_policy: enabled
- consistency_assist_method: reference alignment vector
- anatomy_repair_policy: mechanical focus only
- consistency_targets: thruster housing, control levers, hull damage
- style_profile: industrial warship aesthetic
- batch_role: keyframe generation
- fix_of: none

# Continuity Notes
- Ship rotation mechanism must show damaged but functional state with visible mechanical stress indicators
- Crew hands should appear in defensive positioning consistent with fleet limping condition
- Smoke density should increase from previous beat to maintain visual progression
- Debris field on deck surface must align with damage patterns from earlier shots
- Thruster housings should show corrosion and battle wear matching established continuity
- Control levers must be gripped firmly indicating crew adjusting for new firing angle
- Hull damage visible on surrounding structure must match damage from return fire sequence
- Mechanical alignment vector should be clearly visible showing broadside repositioning intent

# Repair Notes
- If rotation mechanism appears too pristine, add surface corrosion and battle wear textures
- Ensure crew hands show fatigue consistent with damaged ship condition
- Verify smoke trails align with previous beat's fire arcs from return fire sequence
- Check that debris field matches damage patterns established in earlier shots
- Confirm mechanical stress indicators visible on thruster housings match continuity requirements
- If alignment vector unclear, enhance mechanical movement lines showing broadside repositioning
- Ensure hull damage visible matches damage from return fire sequence in previous beats

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL009.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
