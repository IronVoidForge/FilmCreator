# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T00:43:25.521645+00:00
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

**Story Summary:**
Carter waits for mining partner James K. Powell to return from the valley after leaving to purchase machinery. Apaches attack Powell. Carter pursues, finds Powell dead in a cave after being pursued by Indians. He enters the cave and collapses due to fatigue.

**Visual Continuity:**
Arizona landscape (hills, moonlight), horse tracks (unshod ponies), Indian tepees (white with warriors), cave interior (smooth floor, shadows), Powell's body (bristling with arrows). Carter is armed with two Colt revolvers and a carbine. The setting transitions from open valley to narrow gorge to large chamber within the cave.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH001

| Character | Role | Status | Description Available |
|-----------|------|--------|---------------------|
| Carter | Protagonist | Physically Present | Partial (armed with revolvers and carbine) |
| James K. Powell | Mining Partner | Deceased | Partial (body found with arrows) |
| Apaches/Indians | Antagonists | Physically Present | Group reference only |

**Note:** Detailed physical descriptions are limited in source material. Manual descriptions may be required for reliable image generation.
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: carter
canonical_character_id: carter
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source material only confirms Carter is armed with two Colt revolvers and a carbine. Height, build, hair color, age, facial features, and other physical traits are not described in the chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# carter.md

## Display Name
Carter

## Chapter Role
Protagonist / Main Character

## Physical Presence
Physically Present - Active throughout chapter

## Physical Description (Supported by Source)
- Armed with two Colt revolvers and a carbine rifle
- Appears to be in mining context (waiting for partner, pursuing through valley)

## Costume & Silhouette
- Mining attire implied by context
- Carrying firearms prominently

## Continuity-Critical Traits
- Two Colt revolvers on person
- One carbine weapon
- Pursuing through Arizona landscape

## Render-Facing Prompt Notes
"mining man armed with two Colt revolvers and a carbine rifle, standing in Arizona valley landscape, moonlight, mining context, fatigue visible later in chapter"

## Uncertainty Notes
**Important:** Height, build, hair color, age, facial features, skin tone, and other detailed physical characteristics are NOT described in source material. Manual description required for reliable image generation. Source only confirms weapon carry and general mining context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: james_k_powell
canonical_character_id: james_k_powell
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Source material only confirms Powell's body was found bristling with arrows in a cave. Height, build, hair color, age, facial features, and other physical traits are not described in the chapter summary.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# james_k_powell.md

## Display Name
James K. Powell

## Chapter Role
Mining Partner / Deceased Character

## Physical Presence
Deceased - Body found in cave after attack

## Physical Description (Supported by Source)
- Body bristling with arrows from Apache/Indian attack
- Found dead in cave interior

## Costume & Silhouette
- Mining attire implied by context
- Lying on cave floor (smooth surface mentioned)

## Continuity-Critical Traits
- Multiple arrows embedded in body
- Located in Arizona cave interior
- Victim of Apache/Indian pursuit

## Render-Facing Prompt Notes
"mining man's body found dead in Arizona cave, bristling with multiple arrows, lying on smooth cave floor, shadows present, mining context"

## Uncertainty Notes
**Important:** Height, build, hair color, age, facial features, skin tone, and other detailed physical characteristics are NOT described in source material. Manual description required for reliable image generation. Source only confirms arrow wounds and general mining context.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: apaches_indians
canonical_character_id: apaches_indians
aliases: indians, apache warriors
is_fully_identified: false
manual_description_required: true
manual_description_reason: Source material only references Apaches/Indians as a group attacking and pursuing. No individual physical descriptions, names, or specific character details are provided in the chapter summary.
clarification_required: true
clarification_reason: Character might already exist under another name or is too weakly identified for reliable image generation without clarification
clarification_question: Are Apaches/Indians meant to be treated as a single group entity or should individual warrior characters be created with specific descriptions?

[[SECTION markdown]]
# apaches_indians.md

## Display Name
Apaches / Indians

## Chapter Role
Antagonists / Attackers

## Physical Presence
Physically Present - Active throughout chapter (attack and pursuit)

## Physical Description (Supported by Source)
- Group of warriors attacking Powell
- Associated with white tepees mentioned in visual continuity
- Pursuing through valley to cave interior

## Costume & Silhouette
- Warrior attire implied by context
- Associated with Apache/Indian cultural markers

## Continuity-Critical Traits
- Multiple warriors (count not specified)
- White tepees visible in landscape
- Armed and attacking
- Pursuing victim through terrain

## Render-Facing Prompt Notes
"Apache/Indian warrior group, multiple figures, white tepees visible in Arizona landscape, moonlight, mining valley context, pursuing attack"

## Uncertainty Notes
**Important:** Individual physical descriptions are NOT provided in source material. Only group reference exists. Height, build, hair color, age, facial features, and other detailed physical characteristics for individual warriors are unknown. Manual description required for reliable image generation. Source only confirms group presence and cultural markers (tepees).

## Identification Status
**Partially Identified:** Character names alternate between "Apaches" and "Indians" in source material. Group entity rather than individual characters. Clarification recommended for consistent rendering approach.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
