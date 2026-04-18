# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T21:57:46.850693+00:00
- task: character_shared_prompts

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Work like a careful local planning assistant for chapter analysis and shot-prep authoring.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
Prefer short, concrete section bodies over long prose.
Follow the requested headings and record fields exactly.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
If information is missing, say so briefly instead of guessing.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Asset id: dejah_thoris

Task: write one reusable shared character-reference prompt draft for stable local generation.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: <value>

[[SECTION purpose]]
...purpose content...
[[/SECTION]]

[[SECTION positive_prompt]]
...positive_prompt content...
[[/SECTION]]

[[SECTION negative_prompt]]
...negative_prompt content...
[[/SECTION]]

[[SECTION inputs_markdown]]
...inputs_markdown content...
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
...continuity_notes_markdown content...
[[/SECTION]]

[[SECTION repair_notes_markdown]]
...repair_notes_markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Rules:

- purpose and inputs may use stable asset ids

- final positive and negative prompt bodies should avoid proper nouns and use descriptive noun phrases

- keep prompts concrete and visible

- prefer stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/dejah_thoris.md

# Dejah Thoris

## Display Name & Role
**Name:** Dejah Thoris  
**Role:** Princess / Prisoner

## Presence Status
**Status:** Referenced / Present (Close-up interaction)  
**Note:** Character is the central figure of interest in this chapter.

## Physical Description
**Supported Details:** 
- Slender, girlish figure similar to earthly women.
- Oval face.
- Coal black waving hair.
- Light reddish copper skin.
- Crimson cheeks.
- Ruby lips.
- Eyes large and lustrous.
- Wearing highly wrought ornaments but otherwise naked (at time of capture).

**Uncertainty Notes:** None regarding physical appearance in this chapter.

## Costume & Silhouette
**Details:** Highly wrought ornaments; otherwise naked at moment of discovery.  
**Continuity Traits:** Distinctive copper skin tone and black hair are key identifiers for Martian royalty.

## Render-Facing Prompt Phrases
- "Slender girlish figure with oval face"
- "Coal black waving hair"
- "Light reddish copper skin"
- "Crimson cheeks and ruby lips"
- "Large lustrous eyes"
- "Wearing highly wrought ornaments"

# Aliases

the prisoner, her



# Canonical Character ID

dejah_thoris



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/dejah_thoris_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: dejah_thoris

[[SECTION purpose]]
This prompt is designed to generate consistent close-up images of Dejah Thoris for character reference tasks. It focuses on physical identifiers such as skin tone, hair color, and ornamentation to maintain visual continuity across generations without relying on scene-specific blocking or proper nouns.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure with oval face, coal black waving hair, light reddish copper skin, crimson cheeks and ruby lips, large lustrous eyes, wearing highly wrought ornaments
[[/SECTION]]

[[SECTION negative_prompt]]
bad anatomy, text, watermark, signature, blurry, low quality, deformed hands, missing limbs, extra fingers, bad proportions, distorted face, cartoon, 3d render, painting, extra clothing, nudity
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/dejah_thoris.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Key identifiers for consistency include the light reddish copper skin tone and coal black waving hair. Ornaments should remain highly wrought and distinct from standard jewelry. Ensure facial features match the oval face description with large lustrous eyes.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
If skin tone appears too pale or dark, adjust to maintain the reddish copper hue. If hair color shifts towards brown or red, correct to coal black. Verify that ornaments are present and not replaced by standard clothing unless specified in a specific scene variant.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
