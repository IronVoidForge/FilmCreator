# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-18T16:07:12.047243+00:00
- task: character_shared_prompts

## System Prompt
````text
You are FilmCreator's local authoring analyst.
Return exactly one FILMCREATOR packet in Markdown.
Do not return JSON.
Do not use markdown fences.
Do not add commentary before or after the packet.
Preserve uncertainty instead of inventing hidden facts.
When asked to write Markdown file contents, place the complete file body inside the requested SECTION tags.
When asked to extract render-facing facts, focus on visible, continuity-relevant details.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Asset id: john_carter

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



Character breakdown path: projects/princess_of_mars_test/02_story_analysis/character_breakdowns/john_carter.md

# John Carter

## Display Name
John Carter

## Chapter Role
Human protagonist, witness to prisoner capture in CH001

## Physical Presence
Physically present - returns to city plaza after incubator ceremony, witnesses captured female being dragged into building

## Physical Description (Source-Supported)
- Human species
- No specific physical features documented in source material

## Costume & Silhouette
- No costume details available in source material
- Silhouette not described

## Continuity-Critical Traits
- Witness to prisoner capture event
- Returns to city plaza location
- Shows ignorance of local customs regarding captured female

## Render-Facing Prompt Noun Phrases
- human protagonist
- witness character
- city plaza observer
- ignorant of local customs

## Uncertainty Notes
**CRITICAL:** No physical description available in source material. Cannot generate reliable images without manual description of:
- Facial features and structure
- Height and body build
- Hair color and style
- Eye color
- Distinguishing marks or scars
- Clothing details (if any)

This character requires manual description before dependable image generation can proceed.

# Manual Description Input Required

Yes



# Manual Description Reason

Source material only identifies John Carter as "human" with no specific physical features, facial structure, height, build, or distinguishing marks. Cannot support dependable later image generation without manual description of these fundamental visual elements.




Manual character description path: projects/princess_of_mars_test/01_source/character_descriptions/john_carter_manual_description.md

<!-- FILMCREATOR_MANUAL_PLACEHOLDER -->

# Asset ID
john_carter

# Purpose
Paste a stable manual visual description for this character so later shared reference generation can use it.

# Why This Is Needed
Source material only identifies John Carter as "human" with no specific physical features, facial structure, height, build, or distinguishing marks. Cannot support dependable later image generation without manual description of these fundamental visual elements.

# Guidance
- describe face, hair, body type, age impression, silhouette, skin tone, costume logic, and any continuity-critical marks
- prefer visible facts over backstory
- if multiple looks exist, describe the default look for this chapter

# Manual Description

````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_shared_prompts
version: 1

[[FILMCREATOR_RECORD]]
type: character_prompt
asset_id: john_carter

[[SECTION purpose]]
Shared reference prompt for human protagonist witness character in city plaza setting, supporting stable local generation with continuity-critical visual traits and costume logic for later shared reference use.
[[/SECTION]]

[[SECTION positive_prompt]]
human protagonist, witness character, city plaza observer, standing figure, neutral expression, simple clothing, basic silhouette, visible face structure, average height build, natural hair style, skin tone consistent with human species, casual attire, grounded stance, urban environment background, no exotic markings, standard proportions.
[[/SECTION]]

[[SECTION negative_prompt]]
proper nouns, character names, specific brand logos, fantasy elements, alien features, exaggerated proportions, distorted face, missing limbs, excessive makeup, costume details not specified, scene-specific blocking, dynamic action poses, complex lighting effects, background characters, text overlays, watermarks.
[[/SECTION]]

[[SECTION inputs_markdown]]
projects/princess_of_mars_test/02_story_analysis/character_breakdowns/john_carter.md
projects/princess_of_mars_test/01_source/character_descriptions/john_carter_manual_description.md
[[/SECTION]]

[[SECTION continuity_notes_markdown]]
Witness to prisoner capture event, returns to city plaza location, shows ignorance of local customs regarding captured female, human species identification only, no costume details available in source material, silhouette not described in source material.
[[/SECTION]]

[[SECTION repair_notes_markdown]]
Manual description required for facial features and structure, height and body build, hair color and style, eye color, distinguishing marks or scars, clothing details if any. Source material only identifies as human with no specific physical features documented. Cannot generate reliable images without manual description of these fundamental visual elements.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
