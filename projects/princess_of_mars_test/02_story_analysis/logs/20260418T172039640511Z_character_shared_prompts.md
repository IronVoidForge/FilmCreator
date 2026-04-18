# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T17:20:39.640511+00:00
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

Asset id: captive_ch001

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/captive_ch001.md

# Captive (CH001)

## Display Name
Captive

## Chapter Role
Subject of Discovery / Witnessed Victim

## Physical Presence
Present being dragged into building by green Martian females

## Physical Description
- **Skin:** Light reddish copper
- **Hair:** Coal black, loosely caught
- **Face:** Oval face, large lustrous eyes, finely chiseled features
- **Attire:** Destitute of clothes except ornaments

## Costume & Silhouette
- Minimal clothing with ornamental pieces
- Slender, girlish figure
- Being dragged by force into building interior

## Continuity-Critical Traits
- Observed from distance by narrator during return to plaza
- Looks at narrator with hope then loathing
- Skin tone and features distinguish from human characters
- Ornamentation may indicate cultural or personal significance

## Render-Facing Prompt Notes
- Sufficient physical description for dependable image generation
- Focus on slender girlish proportions
- Light reddish copper skin tone (distinctive)
- Coal black hair loosely caught
- Oval face with large lustrous eyes
- Finely chiseled facial features
- Ornamental pieces rather than full clothing

## Uncertainty Notes
**NO CRITICAL UNCERTAINTY:** Physical description is complete and sufficient for reliable image generation. No additional manual description required.

# Aliases

-



# Canonical Character ID

captive



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

-




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/captive_ch001_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: captive_ch001

[[SECTION purpose]]
Reusable shared prompt for generating consistent visual representation of Captive character across scenes. Focuses on stable physical traits including skin tone, hair, facial features, and ornamental costume elements rather than scene-specific blocking or narrative context.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure, light reddish copper skin tone, coal black hair loosely caught, oval face with large lustrous eyes, finely chiseled facial features, minimal clothing with ornamental pieces, slender proportions, distinctive non-human skin coloration, ornamental jewelry and decorative accessories, flowing loose hair texture, delicate facial structure
[[/SECTION]]

[[SECTION negative_prompt]]
full clothing, complete garments, human skin tones, short cropped hair, round face, small eyes, heavy makeup, elaborate costumes, detailed scene blocking, narrative context, background elements, environmental details, proper nouns, character names, specific location markers, complex poses, dynamic action sequences
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/captive_ch001.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Character observed from distance by narrator during return to plaza. Looks at narrator with hope then loathing. Skin tone and features distinguish from human characters. Ornamentation may indicate cultural or personal significance. Physical description complete and sufficient for reliable image generation. No additional manual description required.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Physical description is complete and sufficient for dependable image generation. Focus on stable face, hair, body type, costume logic, silhouette, and recurring materials over scene-specific blocking. Avoid proper nouns in final prompt bodies. Use descriptive noun phrases only.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
