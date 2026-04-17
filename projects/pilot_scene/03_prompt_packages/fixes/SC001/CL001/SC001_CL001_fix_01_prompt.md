# Title
SC001 CL001 Fix 01 Prompt

# ID
SC001_CL001_fix_01_prompt

# Purpose
Generate a corrective still pass from the approved opening duel frame while preserving composition, chamber layout, and cold sculptural lighting.

# Workflow Type
still.scene_insert.two_ref.klein.distilled

# Positive Prompt
Use the approved duel frame as the base image and preserve the exact camera angle, crossed-blade staging, pale alien chamber architecture, cold overhead lighting, and overall composition. Tighten likeness, facial structure, costume silhouette, and hand clarity for the dark-haired human duelist using the provided character reference image. Keep both combatants in the same positions, keep the monumental circular platform, preserve the restrained dramatic tension, and improve small hand, grip, and blade-contact details without redesigning the scene.

# Negative Prompt
composition change, camera angle change, room redesign, lighting change, blue cast, extra limbs, extra fingers, merged hands, duplicate characters, duplicate weapons, costume redesign, anatomy drift, face drift, blur, text, watermark

# Inputs
- project_id: pilot_scene
- scene_id: SC001
- clip_id: CL001
- duration_seconds: 0
- required_refs: image_2
- optional_refs:
- visible_character_assets: ulurani3
- look_continuity_policy: preserve_keyframe_look
- intended_lighting_change:
- composition_type: two_shot
- continuity_mode: reframe_same_moment
- starting_keyframe_strategy: approved_keyframe_to_reframe
- dependency_policy: soft_ref_previous
- auto_advance_policy: manual
- fallback_strategy: regenerate_from_approved_keyframe
- consistency_assist_policy: off
- consistency_assist_method: reference_img2img
- anatomy_repair_policy: still_only
- consistency_targets: dark-haired human duelist hands, face, costume silhouette
- style_profile:
- batch_role:
- fix_of:

# Continuity Notes
- Use the approved keyframe as the base image for the corrective pass.
- Preserve the cold pale chamber lighting, the duel axis, the crossed blades, and the existing framing.
- Do not redesign the room, move the camera, or restage the duel.

# Repair Notes
- Correct local hand and grip issues first.
- Tighten likeness and facial stability for the dark-haired human duelist using the provided reference image.
- Keep the scene frozen as a still correction, not a new shot design.

# Sources
- projects/pilot_scene/02_story_analysis/clip_plans/SC001/CL001.md
