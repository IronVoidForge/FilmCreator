# Title
CH008_SC003 CL006 Scene Stage Prompt

# ID
CH008_SC003_CL006_scene_stage_prompt

# Purpose
Define visual staging intent for wide shot looting sequence within disabled vessel recovery scene. Establish subject placement, environmental context, and opening frame setup for multiple Martians working on main deck during systematic search operations. Capture authoring-only description of visible elements without rendering artifacts.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Wide interior deck of disabled gray vessel, multiple green-skinned warrior figures working simultaneously, looting cargo items including arms silks jewels food containers, dead sailors clustered in designated areas, Martian architectural details visible on hull, fortified city structures in background, open valleys and distant hills context, natural daylight with battle aftermath lighting, smooth movement across deck, simultaneous looting operations visible.

# Negative Prompt
Human faces, non-Martian technology, specific character names, render artifacts, blurry text, close-up facial expressions, interior lighting mismatch, floating debris inconsistent with scene continuity, unauthorized background elements, mechanical limbs, modern weaponry, bright artificial light sources.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians, Dead Sailors
- look_continuity_policy: maintain ship interior layout consistency
- intended_lighting_change: natural daylight with smoke/ash effects
- composition_type: wide shot
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: open on main deck with multiple Martians
- dependency_policy: none
- auto_advance_policy: standard interval beats
- fallback_strategy: insert if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: check green skin clarity
- consistency_targets: 
- style_profile: Martian city urban warfare aesthetic
- batch_role: 
- fix_of: 

# Continuity Notes
- Track item removal consistency for arms silks jewels and food containers across shots.
- Maintain ship interior layout alignment with previous beat BT001 drifting sequence.
- Ensure warrior positions relative to dead sailor clusters remain stable.
- Verify background city structures match established Martian architecture index.
- Confirm lighting transitions reflect battle aftermath without sudden shifts.

# Repair Notes
- Check anatomy clarity for green-skinned figures if rendering appears inconsistent.
- Verify specific items (arms, silks) are visible to support continuity tracking.
- Ensure dead sailors remain stationary and do not move unexpectedly.
- Confirm background environment matches disabled ship recovery context.
- Review lighting intensity against previous scene stage prompts for consistency.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
