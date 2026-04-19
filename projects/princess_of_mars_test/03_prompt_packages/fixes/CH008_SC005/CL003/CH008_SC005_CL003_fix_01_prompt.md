# Title
CH008_SC005 CL003 Fix 01 Prompt

# ID
CH008_SC005_CL003_fix_01_prompt

# Purpose
Corrective still generation for CL003 close-up on human female companion. Preserves emotional urgency and visual continuity while addressing local artifacts or anatomical inconsistencies in the approved base image. Ensures facial expression clarity and lighting consistency with previous shots (daylight, corridor shadows).

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Close up portrait of human female companion, coal black hair loosely caught into strange coiffure, crimson cheeks, ruby lips, expression of urgency and determination, daylight lighting with corridor shadows, focus on eyes locked forward, high fidelity facial details, green skin context implied by environment, minimal background clutter, sharp focus on face.

# Negative Prompt
distorted face, extra fingers, wrong hair color, text, watermark, blurry, low resolution, mismatched lighting, green skin on human unless context requires, extra limbs, facial asymmetry, poor anatomy, low contrast, noisy background.

# Inputs
- project_id: princess_of_mars_test
- scene_id: CH008_SC005
- clip_id: CL003
- duration_seconds: 5
- required_refs: CH008_SC005/BEAT_INDEX.md BT001, CH008_SC005/BT001.md End State
- optional_refs: None
- visible_character_assets: Sola (face, eyes, upper body)
- look_continuity_policy: Maintain emotional intensity and lighting consistency with CL002
- intended_lighting_change: None
- composition_type: Close Up
- continuity_mode: insert
- starting_keyframe_strategy: Static close frame on face showing urgency
- dependency_policy: Depends on CL002 establishing spatial context
- auto_advance_policy: Standard
- fallback_strategy: Tighten to extreme close-up on eyes if expression unclear
- consistency_assist_policy: Enable
- consistency_assist_method: Face focus
- anatomy_repair_policy: Strict
- consistency_targets: Facial features, hair coiffure, lighting direction
- style_profile: Action-oriented, awe-inspiring
- batch_role: Fix 01
- fix_of: CL003 Base Image

# Continuity Notes
- Sola's expression must convey both desperation and purpose.
- Lighting should match daylight with smoke effects from nearby battle.
- Hair coiffure must remain consistent with canonical style (loose, strange).
- Composition remains close-up on face and upper body only.
- Eye contact prepares for cut to CL004 reaction shot.

# Repair Notes
- Fix any distorted facial features or asymmetry in the base image.
- Ensure eyes are sharp and focused forward, not looking away.
- Correct lighting shadows to match corridor environment consistency.
- Verify hair strands do not blend into background incorrectly.
- Maintain skin tone consistency with human female companion profile.

# Sources
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CL003.md
- projects/princess_of_mars_test/02_story_analysis/scene_breakdowns/CH008_SC005.md
- projects/princess_of_mars_test/02_story_analysis/clip_plans/CH008_SC005/CH008_SC005_clip_roster.md
- projects/princess_of_mars_test/02_story_analysis/character_breakdowns/CHARACTER_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/environment_breakdowns/ENVIRONMENT_INDEX.md
- projects/princess_of_mars_test/02_story_analysis/story_summary/project_summary.md
