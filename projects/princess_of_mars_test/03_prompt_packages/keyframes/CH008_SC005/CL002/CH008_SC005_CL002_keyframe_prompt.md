# Title
CH008_SC005 CL002 Keyframe Prompt

# ID
CH008_SC005_CL002_keyframe_prompt

# Purpose
Establish visual intent for medium two-shot keyframe where foreground observer remains stationary while background subject moves diagonally across building entrance threshold. This frame tightens spatial context from previous wide shots, focusing on character interaction and perspective without proper nouns, maintaining continuity of lighting and environment smoke effects from battle sequence. Frame captures forced movement vector with depth layering between foreground observers and background prisoner plane.

# Workflow Type
still.scene_build.four_ref.klein.distilled

# Positive Prompt
Medium two shot over-the-shoulder perspective, human male shoulder profile in foreground left facing right, slender figure full body upper body approaching from background right moving diagonally towards camera, dragging motion through building entrance threshold, daylight environment with smoke haze from battle aftermath, city building exterior corridor visible beyond, open ground plaza area visible in distance, muted gray tones with warm skin highlights, cinematic lighting, high detail, atmospheric depth, sharp focus on foreground silhouette and background subject movement vector

# Negative Prompt
blurry, low resolution, distorted anatomy, extra limbs, missing fingers, wrong perspective, flat lighting, overexposed, underexposed, text, watermark, signature, cartoonish, 3d render, painting, sketch, static pose, lack of movement vector, incorrect skin tone, oversaturated colors, proper nouns, character names, location names

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL002
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: Carter (shoulder/back profile), Sola (full face and upper body)
- look_continuity_policy: daylight with smoke haze from battle aftermath
- intended_lighting_change: none
- composition_type: Medium two shot, over-the-shoulder from foreground observer perspective
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: Shoulder of foreground observer in left frame, background subject entering from right
- dependency_policy: Depends on CL001 establishing spatial context; no reverse dependency
- auto_advance_policy: none
- fallback_strategy: If shoulder framing is unclear, shift to medium shot with both characters fully visible
- consistency_assist_policy: none
- consistency_assist_method: none
- anatomy_repair_policy: prioritize face clarity for background subject and shoulder silhouette for foreground observer
- consistency_targets: movement vector clear, lighting consistent with battle aftermath
- style_profile: cinematic_compositional
- batch_role: keyframe
- fix_of: none

# Continuity Notes
- note maintain foreground observer stationary position while background subject moves diagonally towards camera
- note ensure background matches city building exterior corridor lighting with daylight and smoke haze
- note keep character appearances consistent with chapter descriptions for physical presence and movement
- note preserve the diagonal movement vector established in the beat plan without obscuring foreground characters
- note avoid introducing new props or elements not present in the scene summary or battle aftermath context

# Repair Notes
- note if anatomy is distorted, prioritize face clarity for background subject and shoulder silhouette for foreground observer
- note ensure diagonal movement vector is clear in the still composition without obscuring character identification
- note correct any lighting mismatches between foreground shadow and background daylight smoke haze
- note verify smoke haze does not obscure critical facial features or character identification in background plane

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL002.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
