# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:47:04.384715+00:00
- task: character_extraction

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

Chapter id: CH001

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Return exactly one Markdown packet using this outer envelope:
[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
...character_index_markdown content...
[[/SECTION]]

Repeat one FILMCREATOR_RECORD block for every extracted item of that type.

[[FILMCREATOR_RECORD]]
type: character
asset_id: <value>
canonical_character_id: <value>
aliases: <value>
is_fully_identified: <value>
manual_description_required: <value>
manual_description_reason: <value>
clarification_required: <value>
clarification_reason: <value>
clarification_question: <value>

[[SECTION markdown]]
...markdown content...
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- every character record must include a non-empty markdown section

- if details are sparse, still write a short markdown file explaining the uncertainty instead of omitting markdown

- never omit the markdown section for any character record



Asset id rules:

- lowercase snake_case

- stable across later reruns



Each character Markdown file should include:

- display name and chapter role

- whether the character is physically present, referenced, or uncertain

- physical description that is actually supported by the source

- costume, silhouette, and continuity-critical traits when known

- useful descriptive noun phrases for later render-facing prompt writing

- explicit uncertainty notes when important details are missing



Chapter summary:

# Chapter I: On The Arizona Hills

## Story Summary
John Carter reflects on his mortality and decision to write this chronicle. He recounts finding a gold vein with Captain James K. Powell in 1865. Powell leaves to purchase machinery while Carter guards the claim. Apaches ambush Powell's party. Carter discovers the tracks, pursues them at night, finds Powell dead surrounded by tepees, and charges the warriors. After rescuing Powell's body from mutilation, Carter's horse leads him into a defile toward a cave entrance where he collapses from exhaustion.

## Visual Continuity Facts
- **Lighting:** Clear Arizona mornings, bright moonlight at night, sudden daylight in cave.
- **Props:** Colt revolvers (two), carbine, saddle horse, burros (seen earlier), canteen, cartridge belts.
- **Locations:** Arizona hills, mountainside, valley, water hole, plateau with tepees, gorge, cave entrance (4ft high, 3-4ft wide).
- **Characters:** John Carter (wearing military attire implied by commission), Powell (dead body), Apaches (warriors in tepees).
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - Chapter I: On The Arizona Hills

## Characters Identified

| Asset ID | Canonical Character ID | Display Name | Status |
|----------|------------------------|--------------|--------|
| john_carter | CH001_JC | John Carter | Physically Present |
| captain_powell | CH001_CP | Captain James K. Powell | Referenced (Dead) |
| apache_warriors | CH001_AW | Apache Warriors | Referenced |

## Notes

- All characters have limited physical description support for image generation
- Manual descriptions required for reliable render-facing prompts
- Apaches represent multiple warriors with sparse individual identification
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001_JC
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical description limited to "military attire implied by commission" - no specific uniform details, facial features, or distinguishing marks provided in source material for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

## Display Name
John Carter

## Chapter Role
Main protagonist reflecting on mortality and decision to write chronicle

## Physical Presence
Physically present - actively narrating chapter events

## Physical Description (Source-Supported)
- Wearing military attire implied by commission
- No specific uniform details, facial features, or distinguishing marks provided in source material
- Appears as a man of the 1860s era based on historical context

## Costume & Silhouette
- Military clothing (specific type uncertain)
- Commissioned officer status implied
- No detailed costume elements documented for render-facing prompts

## Continuity-Critical Traits
- Colt revolvers (two) - carried
- Carbine weapon - carried
- Saddle horse - mounted during pursuit
- Canteen and cartridge belts - equipment visible

## Render-Facing Noun Phrases
- "1860s military officer"
- "Arizona terrain explorer"
- "Commissioned man with Colt revolvers"
- "Man of the Arizona hills"

## Uncertainty Notes
Physical description is sparse for dependable image generation. Manual description required to support later render-facing prompts. Specific uniform type, facial features, and distinguishing marks not documented in source material.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: captain_powell
canonical_character_id: CH001_CP
aliases: Captain James K. Powell
is_fully_identified: true
manual_description_required: true
manual_description_reason: Only described as "dead body" with no physical appearance details, facial features, or distinguishing marks provided in source material for dependable image generation
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Captain James K. Powell

## Display Name
Captain James K. Powell

## Chapter Role
Deceased companion found by John Carter after ambush

## Physical Presence
Referenced only - body discovered dead in cave entrance area

## Physical Description (Source-Supported)
- Described as dead body surrounded by tepees
- No physical appearance details, facial features, or distinguishing marks provided in source material
- Historical figure from 1865 era based on timeline context

## Costume & Silhouette
- Military attire implied by captain rank and commission
- Specific uniform type uncertain - no detailed costume elements documented for render-facing prompts

## Continuity-Critical Traits
- Found dead after Apaches ambush Powell's party
- Body rescued from mutilation before Carter charges warriors
- Horse leads Carter to cave entrance where he collapses

## Render-Facing Noun Phrases
- "1860s military captain"
- "Deceased Arizona companion"
- "Captain with Colt revolvers (historical context)"
- "Man found in tepee camp"

## Uncertainty Notes
Physical description is extremely sparse for dependable image generation. Only described as dead body with no appearance details. Manual description required to support later render-facing prompts. Specific uniform type, facial features, and distinguishing marks not documented in source material.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apache_warriors
canonical_character_id: CH001_AW
aliases: Apaches, warriors in tepees
is_fully_identified: false
manual_description_required: true
manual_description_reason: Multiple warriors referenced collectively with no individual physical descriptions, facial features, or distinguishing marks provided for dependable image generation of specific characters
clarification_required: true
clarification_reason: Chapter references "Apaches" as collective group in tepees - unclear if representing single warrior character or multiple distinct individuals for render-facing purposes
clarification_question: Should Apache warriors be rendered as a single representative warrior character or multiple distinct individual warriors, and what physical description details are needed for each?

[[SECTION markdown]]
# Apache Warriors

## Display Name
Apache Warriors (Collective)

## Chapter Role
Antagonist group found in tepees after ambush on Powell's party

## Physical Presence
Referenced only - warriors discovered in cave entrance area with tepees

## Physical Description (Source-Supported)
- Collective reference to "Apaches" and "warriors in tepees"
- No individual physical descriptions, facial features, or distinguishing marks provided in source material
- Historical context suggests 1860s era indigenous warriors based on timeline

## Costume & Silhouette
- Warriors associated with tepee camp
- Specific costume elements uncertain - no detailed clothing or equipment documented for render-facing prompts
- Traditional warrior attire implied by historical context but not specified

## Continuity-Critical Traits
- Apaches ambush Powell's party
- Carter discovers tracks and pursues at night
- Finds Powell dead surrounded by tepees
- Carter charges warriors after rescue attempt

## Render-Facing Noun Phrases
- "1860s Apache warrior" (collective)
- "Warrior in tepee camp"
- "Arizona indigenous antagonist group"
- "Multiple warriors in historical setting"

## Uncertainty Notes
Physical description is extremely sparse for dependable image generation. Multiple warriors referenced collectively with no individual details. Manual description required to support later render-facing prompts. Specific uniform type, facial features, and distinguishing marks not documented in source material. Clarification needed on whether representing single character or multiple distinct individuals for rendering purposes.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
