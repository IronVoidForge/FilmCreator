# Title
CH008_SC002 CL006 Keyframe Prompt

# ID
CH008_SC002_CL006_keyframe_prompt

# Purpose
Depict the immediate visual reaction to precision targeting impacts within the aerial battle zone. Focus on the sighting apparatus tracking and smoke effects at specific points like gunners or officers, maintaining consistency with the preceding targeting sequence.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
green-skinned figure positioned in elevated building window, gray-painted vessel visible below, smoke plume rising from impact point, active sighting apparatus on prow, banners dissolving in flame, downward line of sight to valley floor, medium shot composition, static camera with slight pan following impact points, battle zone atmosphere, dark lighting conditions.

# Negative Prompt
blurry focus, distorted anatomy, extra limbs, modern technology, bright sunlight, wrong ship color, clean windows without smoke, floating debris unrelated to impact, visible faces of enemy crew, text or logos on banners, daylight shadows inconsistent with battle time.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC002
- clip_id: CL006
- duration_seconds: 5
- required_refs: BT003.md
- optional_refs: Impact reaction shots coverage families
- visible_character_assets: Martians (targeting team), Impact smoke at target points
- look_continuity_policy: Hard dependency on CL005 targeting sequence
- intended_lighting_change: Consistent with battle zone darkness and smoke glow
- composition_type: Medium shot of specific target points
- continuity_mode: Point-specific reaction shots showing impact effects
- starting_keyframe_strategy: Open on sighting apparatus, then cut to impact points
- dependency_policy: Hard dependency on CL005; must follow targeting sequence
- auto_advance_policy: Manual review required for impact timing consistency
- fallback_strategy: Use insert if need to emphasize impact timing
- consistency_assist_policy: Enable for bullet drop placement verification
- consistency_assist_method: Visual alignment with previous clip frames
- anatomy_repair_policy: Enable for green-skinned figure structural integrity
- consistency_targets: Ship swing arc completion, smoke trail continuity
- style_profile: still.scene_build.four_ref.klein.distilled
- batch_role: Impact Reaction Points
- fix_of: CL005 targeting sequence

# Continuity Notes
- Maintain strict alignment with gray vessel profile from previous clips to ensure visual identity consistency.
- Ensure smoke plumes originate exactly at impact points shown in the sighting apparatus tracking sequence.
- Verify that banners dissolving in flame progress logically from contact points established in prior shots.
- Keep green-skinned figure anatomy consistent with established warrior design across all window positions.
- Bullet drop timing must match explosion points visible in the valley below without temporal jumps.

# Repair Notes
- If ship color appears off, adjust to match the gray-painted vessel standard from the fleet roster.
- Correct any anatomy distortions on green-skinned figures by referencing the warrior design bundle.
- Ensure smoke density matches the battle intensity level established in the opening volley shots.
- Fix banner flame damage progression if it does not align with the impact point sequence.
- Adjust lighting contrast if the battle zone darkness is inconsistent with the smoke glow effects.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CL006.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC002.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC002/CH008_SC002_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
