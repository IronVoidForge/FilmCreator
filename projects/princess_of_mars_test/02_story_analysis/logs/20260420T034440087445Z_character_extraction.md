# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T03:44:40.087445+00:00
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

Chapter id: CH011

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

**Scene 1: Arrival & Threat.** John Carter arrives with Dejah Thoris and Sola to new quarters near the audience chamber. He waves away Sarkoja's guards and threatens her death if she harms Dejah again (threat ineffective on Mars).
**Scene 2: Hierarchy Discussion.** Sola explains Thark chieftain ranks to John, noting he is currently eleventh. She mentions Tars Tarkas's rank and the possibility of John becoming first by killing Lorquas Ptomel.
**Scene 3: New Quarters Tour.** They inspect a building with ancient Martians' frescoes depicting fair-haired humans. Dejah Thoris admires the art; Sola does not notice. The room has swinging metal beds and gold chains.
**Scene 4: Origin Debate.** Dejah Thoris questions John's claim of being from Earth (Virginia). She explains Barsoomian viewing technology that shows Earth clearly. John explains he is from another world (Earth) and describes the planet.
**Scene 5: Martian History.** Discussion on the three great Martian races (fair-haired, red, dark/black) and their alliance due to drying seas. Dejah Thoris relates legends of the lost fair-haired race.
**Ending:** A messenger summons John Carter to Lorquas Ptomel in the audience chamber.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH011

## John Carter
- **Role**: Protagonist, visitor from Earth (claimed)
- **Status**: Physically present in scenes 1-5
- **Description**: No physical details provided in source material

## Dejah Thoris
- **Role**: Noblewoman, companion of John Carter
- **Status**: Physically present in scenes 1, 3-5
- **Description**: No physical details provided in source material

## Sola
- **Role**: Guide/Companion
- **Status**: Physically present in scenes 1-3
- **Description**: No physical details provided in source material

## Sarkoja
- **Role**: Antagonist, guard commander
- **Status**: Referenced in scene 1
- **Description**: No physical details provided in source material

## Lorquas Ptomel
- **Role**: High-ranking Martian official
- **Status**: Referenced in scenes 2, 5; summoned at ending
- **Description**: No physical details provided in source material

## Tars Tarkas
- **Role**: Thark chieftain (mentioned by rank)
- **Status**: Referenced in scene 2
- **Description**: No physical details provided in source material
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH011_John_Carter
aliases: John
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (height, hair color, build) provided in chapter summary. Cannot support dependable image generation without additional details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# John Carter

## Display Name
John Carter

## Chapter Role
Protagonist, visitor from Earth (claimed)

## Physical Presence
Physically present in scenes 1-5

## Physical Description
No physical description provided in source material. Cannot determine height, hair color, build, or other visual traits without additional information.

## Costume & Silhouette
Unknown. No costume details mentioned in chapter summary.

## Continuity-Critical Traits
Claimed origin: Earth (Virginia). Dejah Thoris questions this claim.

## Descriptive Noun Phrases
- "John Carter"
- "visitor from Earth"
- "Earthling"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH011_Dejah_Thoris
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (height, hair color, build) provided in chapter summary. Cannot support dependable image generation without additional details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Dejah Thoris

## Display Name
Dejah Thoris

## Chapter Role
Noblewoman, companion of John Carter

## Physical Presence
Physically present in scenes 1, 3-5

## Physical Description
No physical description provided in source material. Cannot determine height, hair color, build, or other visual traits without additional information.

## Costume & Silhouette
Unknown. No costume details mentioned in chapter summary.

## Continuity-Critical Traits
Barsoomian noblewoman. Questions John's Earth origin claim.

## Descriptive Noun Phrases
- "Dejah Thoris"
- "noblewoman"
- "companion of John Carter"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH011_Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (height, hair color, build) provided in chapter summary. Cannot support dependable image generation without additional details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola

## Display Name
Sola

## Chapter Role
Guide/Companion

## Physical Presence
Physically present in scenes 1-3

## Physical Description
No physical description provided in source material. Cannot determine height, hair color, build, or other visual traits without additional information.

## Costume & Silhouette
Unknown. No costume details mentioned in chapter summary.

## Continuity-Critical Traits
Explains Thark chieftain ranks to John. Does not notice frescoes of fair-haired humans.

## Descriptive Noun Phrases
- "Sola"
- "guide/companion"
- "Thark rank explainer"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH011_Sarkoja
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (height, hair color, build) provided in chapter summary. Cannot support dependable image generation without additional details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sarkoja

## Display Name
Sarkoja

## Chapter Role
Antagonist, guard commander

## Physical Presence
Referenced in scene 1 (guards waved away)

## Physical Description
No physical description provided in source material. Cannot determine height, hair color, build, or other visual traits without additional information.

## Costume & Silhouette
Unknown. No costume details mentioned in chapter summary.

## Continuity-Critical Traits
Threatened with death if she harms Dejah again (threat ineffective on Mars).

## Descriptive Noun Phrases
- "Sarkoja"
- "antagonist"
- "guard commander"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH011_Lorquas_Ptomel
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (height, hair color, build) provided in chapter summary. Cannot support dependable image generation without additional details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Lorquas Ptomel

## Display Name
Lorquas Ptomel

## Chapter Role
High-ranking Martian official

## Physical Presence
Referenced in scenes 2, 5; summoned at ending

## Physical Description
No physical description provided in source material. Cannot determine height, hair color, build, or other visual traits without additional information.

## Costume & Silhouette
Unknown. No costume details mentioned in chapter summary.

## Continuity-Critical Traits
John could become first by killing him. Summoned to audience chamber at ending.

## Descriptive Noun Phrases
- "Lorquas Ptomel"
- "high-ranking official"
- "first-in-line target"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH011_Tars_Tarkas
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description (height, hair color, build) provided in chapter summary. Cannot support dependable image generation without additional details.
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Tars Tarkas

## Display Name
Tars Tarkas

## Chapter Role
Thark chieftain (mentioned by rank)

## Physical Presence
Referenced in scene 2

## Physical Description
No physical description provided in source material. Cannot determine height, hair color, build, or other visual traits without additional information.

## Costume & Silhouette
Unknown. No costume details mentioned in chapter summary.

## Continuity-Critical Traits
Mentioned as example of Thark chieftain rank. John's current rank is eleventh.

## Descriptive Noun Phrases
- "Tars Tarkas"
- "Thark chieftain"
- "rank reference"
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
````
