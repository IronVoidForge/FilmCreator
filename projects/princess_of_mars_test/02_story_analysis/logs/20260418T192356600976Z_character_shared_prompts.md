# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T19:23:56.601476+00:00
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

Asset id: martian_prisoner

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/martian_prisoner.md

# Martian Prisoner (Chapter VIII)

## Display Name
Martian Prisoner

## Chapter Role
Captive

## Presence Status
Referenced (Dragged into building, signals Carter)

## Physical Description
Slender, girlish figure similar to earthly women; oval and beautiful face; finely chiseled features; large/lustrous eyes; coal black waving hair caught loosely into strange coiffure; light reddish copper skin; crimson glow of cheeks; ruby lips.

## Costume & Silhouette
Destitute of clothes, entirely naked save for highly wrought ornaments.

## Continuity-Critical Traits
Signals Carter with hope then dejection. Dragged by green Martian females.

## Descriptive Noun Phrases
Slender girlish figure, oval beautiful face, coal black waving hair, light reddish copper skin, ruby lips, highly wrought ornaments.

## Uncertainty Notes
Identity unknown (referred to as prisoner). Physical description is sufficient for image generation.

# Aliases

None



# Canonical Character ID

martian_prisoner



# Fully Identified

true

# Manual Description Input Required

No



# Manual Description Reason

None




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/martian_prisoner_manual_description.md

(missing)
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: martian_prisoner

[[SECTION purpose]]
Generate consistent visual representations of the Martian Prisoner character across image generation workflows. This prompt maintains physical continuity for slender girlish figure, oval beautiful face, coal black waving hair, light reddish copper skin, ruby lips, and highly wrought ornaments while avoiding scene-specific blocking or proper nouns that could interfere with stable local generation consistency.
[[/SECTION]]

[[SECTION positive_prompt]]
slender girlish figure, oval beautiful face, finely chiseled features, large lustrous eyes, coal black waving hair, loosely caught strange coiffure, light reddish copper skin, crimson glow cheeks, ruby lips, destitute of clothes, entirely naked save for highly wrought ornaments, ornamental jewelry pieces
[[/SECTION]]

[[SECTION negative_prompt]]
clothing, garments, fabric, human features inconsistent with slender girlish figure, proper nouns, names, scene-specific blocking, background elements, text, logos, brand marks, modern technology, realistic shadows that contradict light reddish copper skin tone
[[/SECTION]]

[[SECTION inputs_markdown]]
Asset ID: martian_prisoner
Source Path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/martian_prisoner.md
Character Role: Captive
Presence Status: Referenced (Dragged into building, signals Carter)
Continuity-Critical Traits: Signals Carter with hope then dejection. Dragged by green Martian females.
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Maintain slender girlish figure silhouette across all generations. Keep coal black waving hair with loosely caught strange coiffure consistent. Preserve light reddish copper skin tone without modern lighting that contradicts the crimson glow cheeks. Ensure highly wrought ornaments appear as decorative jewelry pieces rather than clothing elements. Face should show oval beautiful shape with finely chiseled features and large lustrous eyes. Ruby lips must remain visible and distinct from any ornamentation.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Monitor for prompt injection of proper nouns that could interfere with stable local generation. Ensure negative prompt blocks clothing references while allowing ornamental jewelry pieces. Verify skin tone consistency across different lighting conditions to maintain light reddish copper appearance without modern technology artifacts. Check that hair coiffure remains loosely caught strange style rather than becoming standardized human hairstyles.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
