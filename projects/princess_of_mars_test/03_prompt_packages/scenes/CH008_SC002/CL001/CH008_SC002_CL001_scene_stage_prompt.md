# Title
CH008_SC002 CL001 Scene Stage Prompt

# ID
CH008_SC002_CL001_scene_stage_prompt

# Purpose
Establish opening conflict with clear window positioning and firing sequence from an elevated perspective. Focus on static composition of green-skinned warriors in building windows, loaded weapons visible, and environmental context of urban Martian architecture overlooking the valley floor. Intended visible opening frame setup includes minimal camera movement to maintain continuity with subsequent action beats.

# Workflow Type
authoring.scene_stage

# Positive Prompt
Green-skinned warriors positioned in elevated building windows, loaded weapons visible, static elevated perspective looking down at open valley floor, urban Martian architecture, distant hills, smoke rising from impact points below, green skin tone consistent, weapon loading states ready for volley fire, architectural details showing window frames and structural supports.

# Negative Prompt
Human faces in foreground, motion blur, incorrect ship positions above windows, empty window frames, wrong skin tones, disheveled weapons, bright daylight without atmospheric haze, close-up facial expressions, civilian clothing on warriors, modern technology elements, floating debris unrelated to battle impact.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5
- required_refs: BT001.md
- optional_refs: Scene breakdown for building window positioning
- visible_character_assets: Green Warriors, Weapons
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: Wide shot from building window looking down at valley floor
- continuity_mode: Static elevated perspective with minimal camera movement
- starting_keyframe_strategy: Open on warriors positioned in windows, weapons visible and loaded
- dependency_policy: No hard dependencies; can stand alone as opening beat
- auto_advance_policy: 
- fallback_strategy: Use reframe_same_moment if timing adjustment needed
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Maintain consistent warrior positioning across window shots to ensure volley fire alignment.
- Track bullet drop timing at explosion points for visual consistency with impact reactions.
- Ensure banner damage progression matches fleet retreat status in subsequent beats.
- Keep atmospheric haze consistent with valley depth perception.

# Repair Notes
- Apply anatomy repair policy for green skin warriors to ensure structural integrity of limbs and torsos.
- Verify weapon loading states match intended volley fire readiness before discharge.
- Check consistency targets for window frame details against architectural reference models.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
