# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T23:36:08.882939+00:00
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

Asset id: prisoner

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/prisoner.md

# prisoner

## Display Name
The Prisoner

## Chapter Role
Captive / Subject of Interest

## Physical Presence
Present (Being dragged into a building)

## Physical Description
*   **Supported by Source:** Detailed visual description provided in Visual Continuity notes.
    *   **Figure:** Slender, girlish.
    *   **Skin:** Light reddish copper color.
    *   **Face:** Oval face with large and lustrous eyes.
    *   **Features:** Cheeks have crimson glow; Lips are ruby.
    *   **Hair:** Coal black, waving, caught loosely into a strange coiffure.
*   **Attire:** Naked except for highly wrought ornaments.

## Costume & Silhouette
*   **Supported by Source:** Highly wrought ornaments (jewelry/accessories).
*   **Continuity Traits:** Distinctive copper skin tone and glowing cheeks are key visual markers.

## Uncertainty Notes
*   **Status:** Visual identity is fully defined within the context of this chapter. No manual description required for image generation based on current text.

# Aliases

None



# Canonical Character ID

prisoner



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/prisoner_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: prisoner

[[SECTION purpose]]
Generate stable character reference images for a slender, girlish figure with distinctive copper-toned skin and ornamental jewelry. Focus on consistent physical markers including oval face shape, large lustrous eyes, crimson-glowing cheeks, ruby lips, and coal black waving hair in loose coiffure. Maintain nude presentation with highly wrought ornaments as key costume elements.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure, light reddish copper skin tone, oval face shape, large lustrous eyes, crimson glow on cheeks, ruby colored lips, coal black waving hair, loose coiffure, nude presentation, highly wrought ornamental jewelry, distinctive copper skin markers, glowing cheek features, ornate accessories, slender body type
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, character names, scene blocking, background details, clothing garments, fabric textures, scene-specific lighting, environmental elements, complex poses, dynamic movement, shadows, reflections, blur, distortion, low resolution, inconsistent anatomy, mismatched skin tone, dull features, plain hair, simple accessories, obscured face, covered body
[[/SECTION]]

[[SECTION inputs_markdown]]
Character ID: prisoner
Display Name: The Prisoner
Chapter Role: Captive / Subject of Interest
Physical Description: Slender girlish figure with light reddish copper skin, oval face, large lustrous eyes, crimson glow on cheeks, ruby lips, coal black waving hair in loose coiffure. Attire: Nude except for highly wrought ornaments. Costume & Silhouette: Highly wrought ornamental jewelry and accessories. Key visual markers: Distinctive copper skin tone and glowing cheeks.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Visual identity fully defined within chapter context. No manual description required for image generation based on current text. Status: Visual identity is fully defined within the context of this chapter. No manual description required for image generation based on current text. Key visual markers include distinctive copper skin tone and glowing cheeks. Maintain consistent physical presence across generated images.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Ensure prompts avoid proper nouns and use descriptive noun phrases only. Verify stable face, hair, body type, costume logic, silhouette, and recurring materials are prioritized over scene-specific blocking. Confirm continuity notes reflect fully defined visual identity within chapter context. Check that copper skin tone and glowing cheeks remain consistent across all generated images.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
