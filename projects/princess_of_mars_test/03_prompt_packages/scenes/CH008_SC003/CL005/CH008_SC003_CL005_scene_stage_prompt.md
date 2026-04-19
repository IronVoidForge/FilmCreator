# Title
CH008_SC003 CL005 Scene Stage Prompt

# ID
CH008_SC003_CL005_scene_stage_prompt

# Purpose
Define the visual staging intent for CL005 within SC003, establishing continuity for close-up item removal actions during boarding and looting operations. This stage sets up the specific framing for valuables tracking (food containers, water carboys) to ensure consistency with BT002 looting sequence and dependency on CL004.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green-skinned Martian hands removing jewelry from ship cargo hold, gray hull interior details, dead sailors lying on deck background, daylight lighting conditions, close-up composition focusing on item removal action, Martians wearing traditional attire, ship structure showing battle damage signs, specific focus on food containers and water carboys being emptied.

# Negative Prompt
Human faces visible, modern technology elements, wrong skin tone for Martians, blurry hand movements, extra limbs or fingers, bright indoor artificial lighting, clean ship hull without damage, prisoner figure present, text or logos on items, excessive smoke obscuring action.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC003
- clip_id: CL005
- duration_seconds: 5
- required_refs: BT002.md, Scene Summary
- optional_refs: Continuity Notes
- visible_character_assets: Martians (hands), Dead Sailors (stationary)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: close-up
- continuity_mode: insert
- starting_keyframe_strategy: open on specific item removal detail
- dependency_policy: depends on CL004
- auto_advance_policy: 
- fallback_strategy: cutaway if needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Track food containers emptied at 0:2 mark for visual consistency with BT002 looting sequence.
- Ensure water carboys dumped at 0:4 mark match previous shot item placement and quantity.
- Maintain ship interior background alignment with CL004 over-the-shoulder looting shots.
- Keep dead sailors stationary in designated areas to avoid continuity errors during removal actions.

# Repair Notes
- Verify Martian hand anatomy consistency with previous clips (CL004) regarding finger count and skin texture.
- Adjust lighting intensity to match daylight conditions established in SC003 wide shots.
- Ensure ship hull damage patterns align with BT001 drifting ship state for visual coherence.
- Check that removed items do not overlap or duplicate assets from adjacent clips in the sequence.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CL005.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC003.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC003/CH008_SC003_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
