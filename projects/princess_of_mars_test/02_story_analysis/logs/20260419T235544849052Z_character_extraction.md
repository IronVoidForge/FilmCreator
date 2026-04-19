# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-19T23:55:44.849052+00:00
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

Chapter id: CH005

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

**Scene 1: Guardian Establishment.** Sola departs the chamber leaving the Watch Dog to guard the Narrator. The dog's loyalty is confirmed as it surveys the room and exits with the Narrator later.
**Scene 2: Room Inspection.** Narrator examines the room while Sola is away. Murals depict mountains, rivers, and gardens but lack animal representations.
**Scene 3: Sustenance and Rest.** Sola returns with food (cheese-like substance) and drink (plant-milk). Narrator eats, sleeps through a cold night, and receives fur coverings.
**Scene 4: Martian Environment.** Detailed description of Martian nights, moon distances/phases, and artificial lighting methods used by Martians.
**Scene 5: Loyalty Test.** Narrator decides to test the Watch Dog's reaction to leaving the room. The dog follows him outside the building.
**Scene 6: City Edge Confrontation.** At the city edge, the dog attacks. Narrator jumps over the charging beast and leaps into a window 30 feet high.
**Scene 7: Recapture.** A Colossal Ape-like Creature grabs the Narrator from behind and drags him back inside the room.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
task: character_extraction
version: 1

[[SECTION character_index_markdown]]
# Character Index - CH005

| Character | Role | Physical Description Support | Identification Status |
|-----------|------|------------------------------|----------------------|
| Sola | Guardian/Companion | Limited (no appearance details) | Fully Identified |
| Narrator | Main Character | None (no physical description) | Fully Identified |
| Watch Dog | Guardian Animal | Limited (dog, guardian traits) | Fully Identified |
| Colossal Ape-like Creature | Antagonist | Limited (ape-like creature) | Fully Identified |

*Note: All characters require manual descriptions due to sparse physical details in source material.*
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical appearance details provided in chapter summary (no height, build, hair, eyes, skin tone, or distinguishing features mentioned)
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Sola - CH005

**Display Name:** Sola  
**Chapter Role:** Guardian/Companion to Narrator  
**Physical Presence:** Referenced throughout scenes (departs chamber, returns with food)  
**Physical Description:** Unknown - no appearance details in source material  
**Costume/Silhouette:** Not described  
**Continuity-Critical Traits:** Confirmed loyalty to Narrator, guardian of the room  
**Uncertainty Notes:** Requires manual description for image generation. No physical features documented in chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: narrator
canonical_character_id: Narrator
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: No physical description provided in chapter summary (no height, build, hair, eyes, skin tone, or distinguishing features mentioned)
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Narrator - CH005

**Display Name:** The Narrator  
**Chapter Role:** Main Character/Protagonist  
**Physical Presence:** Physically present throughout all scenes (examining room, eating, sleeping, being tested)  
**Physical Description:** Unknown - no appearance details in source material  
**Costume/Silhouette:** Not described  
**Continuity-Critical Traits:** Subject of guardian test, jumps 30 feet into window, dragged by Colossal Ape-like Creature  
**Uncertainty Notes:** Requires manual description for image generation. No physical features documented in chapter summary.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: watch_dog
canonical_character_id: Watch Dog
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Limited physical description (only identified as dog with guardian traits, no breed, size, coat color, or distinguishing features mentioned)
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Watch Dog - CH005

**Display Name:** The Watch Dog  
**Chapter Role:** Guardian Animal/Companion to Narrator  
**Physical Presence:** Physically present (surveys room, follows outside, attacks at city edge)  
**Physical Description:** Unknown beyond being a dog - no breed, size, coat color, or distinguishing features mentioned  
**Costume/Silhouette:** Not described  
**Continuity-Critical Traits:** Confirmed loyalty, follows Narrator outside building, attacks at city edge, jumps 30 feet high  
**Uncertainty Notes:** Requires manual description for image generation. Limited physical details in source material (only guardian dog traits documented).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: colossal_ape_like_creature
canonical_character_id: Colossal Ape-like Creature
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: Limited physical description (only identified as ape-like creature, no height, build, fur color, facial features, or distinguishing marks mentioned)
clarification_required: false
clarification_reason: 
clarification_question: 

[[SECTION markdown]]
# Colossal Ape-like Creature - CH005

**Display Name:** The Colossal Ape-like Creature  
**Chapter Role:** Antagonist/Recapture Agent  
**Physical Presence:** Physically present (grabs Narrator from behind, drags inside room)  
**Physical Description:** Unknown beyond being ape-like creature - no height, build, fur color, facial features, or distinguishing marks mentioned  
**Costume/Silhouette:** Not described  
**Continuity-Critical Traits:** Attacks at city edge, grabs Narrator from behind, drags back inside room  
**Uncertainty Notes:** Requires manual description for image generation. Limited physical details in source material (only ape-like creature designation documented).
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
