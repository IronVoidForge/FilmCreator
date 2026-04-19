# Title
CH008_SC002 CL003 Keyframe Prompt

# ID
CH008_SC002_CL003_keyframe_prompt

# Purpose
Depict aerial conflict and resourcefulness in salvaging supplies from a building window perspective. Show consequence of battle through visible damage to airships in wide coverage shots, focusing on single undamaged ship becoming focal point.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
wide shot of damaged gray vessels hovering over valley floor, visible hull breaches and smoke rising from multiple ships, single intact vessel remains centered in frame, green-skinned warriors positioned at building windows observing scene, distant hills beyond city plaza, daylight illumination with dramatic fire glow on damaged hulls, window frame establishes foreground obstruction

# Negative Prompt
no visible crew members on deck, no complete ship destruction, no close-up facial expressions, no modern machinery, no text overlays, no blurry focus, no excessive fire consuming entire hull immediately, no earthling figures present, no close-up of loot items yet

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL003
- duration_seconds: 5.0
- required_refs: Hull breaches visible, smoke rising from damaged ships, one ship remains unmanned
- optional_refs: Window frame
- visible_character_assets: Martians observing from windows, Narrator noting damage progression
- look_continuity_policy: insert
- intended_lighting_change: daylight with dramatic fire glow on damaged hulls
- composition_type: Wide/Medium
- continuity_mode: insert
- starting_keyframe_strategy: pan_across
- dependency_policy: linear_sequence
- auto_advance_policy: none
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: enabled
- consistency_assist_method: visual_reference
- anatomy_repair_policy: strict
- consistency_targets: green-skinned warriors, ship hulls, smoke density
- style_profile: cinematic_warfare
- batch_role: keyframe_build
- fix_of: none

# Continuity Notes
- maintain visible count of damaged vessels consistent with previous shots
- ensure single undamaged ship remains focal point throughout frame
- preserve hull breach details without overexaggeration
- keep window POV framing consistent with narrator vantage point
- avoid showing crew activity on the drifting warship

# Repair Notes
- correct any anatomical inconsistencies in green-skinned warriors
- ensure smoke density matches damage level accurately
- adjust fire glow intensity to match daylight base illumination
- verify ship hull integrity aligns with battle progression state

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
