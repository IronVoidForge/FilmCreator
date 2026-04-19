# Title
CH008_SC002 CL001 Keyframe Prompt

# ID
CH008_SC002_CL001_keyframe_prompt

# Purpose
Establish narrator's vantage point and scale of approaching threat through window POV shots. Depict twenty gray airships entering frame from distance while maintaining foreground obstruction of building window.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Window frame foreground obstruction, valley floor visible below, twenty gray airships entering frame from distance, daylight illumination, atmospheric tension, human observer presence implied.

# Negative Prompt
No text overlays, no ship damage, no flames, no smoke, no crew figures on deck, no interior room details beyond window frame, no fire pyre elements.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL001
- duration_seconds: 5.0
- required_refs: Window frame, twenty gray airships, valley floor
- optional_refs: Martians (not yet active)
- visible_character_assets: Narrator (window observer)
- look_continuity_policy: 
- intended_lighting_change: 
- composition_type: POV/Wide
- continuity_mode: reblock_same_scene
- starting_keyframe_strategy: static_hold
- dependency_policy: linear_sequence
- auto_advance_policy: 
- fallback_strategy: cut_to_previous_angle
- consistency_assist_policy: 
- consistency_assist_method: 
- anatomy_repair_policy: 
- consistency_targets: 
- style_profile: 
- batch_role: 
- fix_of: 

# Continuity Notes
- Ship count must remain exactly twenty throughout sequence.
- Window frame obstruction must be consistent in foreground.
- Lighting state remains daylight without fire illumination.
- No damage marks visible on airship hulls at this stage.

# Repair Notes
- Correct any ship damage artifacts if present in generation.
- Ensure correct number of ships is rendered (twenty).
- Verify window frame does not obscure critical action area.
- Maintain daylight color temperature without warm fire glow.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL001.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
