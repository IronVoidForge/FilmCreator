# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:12:31.432253+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: princess_of_mars_test

Chapter id: CH011

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question sections=markdown



Output format:

[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

...index markdown...

[[/SECTION]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- emit one explicit character record per meaningful character mention

- every character record must have a FILMCREATOR_RECORD wrapper with type character

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

**Events:**
John Carter secures Dejah Thoris's safety by assigning Sola as her guardian and issuing a threat to the cruel Sarkoja. He moves Dejah Thoris and Sola into more luxurious, ancient quarters in a building featuring elaborate frescoes of a long-extinct, fair-skinned race. During their time in the new quarters, John Carter reveals his true origin—that he is from Earth—and explains how Martian technology allows them to observe other planets via advanced imaging. Dejah Thoris accepts his claim through "feminine logic," despite the impossibility of it. The chapter concludes with a messenger delivering a summons from Lorquas Ptomel, requiring John Carter to appear before the council.

**Characters:**
- **John Carter:** A man from Earth (Virginia) who is navigating his rising status among the Tharks and his growing feelings for Dejah Thoris.
- **Dejah Thoris:** A noblewoman of the red race; she is curious, intelligent, and shows a deep connection to her planet's history.
- **Sola:** An ally to John Carter who takes on the role of protector/attendant for Dejah Thoris.
- **Sarkoja:** A hostile figure who remains a threat despite John Carter's warnings.
- **Lorquas Ptomel:** The high-ranking leader of the community who summons John Carter.
- **Tars Tarkas:** A prominent Thark chieftain present during the council sessions.

**Settings:**
- **The New Quarters:** A pretentious, ancient building near the audience chamber, characterized by marble ceilings, gold chains, and magnificent frescoes depicting a lost, fair-haired civilization.
- **The Audience Chamber:** The location where Lorquas Ptomel and Tars Tarkas preside over the community.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [john_carter](#john_carter)
- [dejah_thoris](#dejah_thoris)
- [sola](#sola)
- [sarkoja](#sarkoja)
- [lorquas_ptomel](#lorquas_ptomel)
- [tars_tarkas](#tars_tarkas)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Man from Earth, Virginian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Earthman

**Status:** Physically Present

**Description:** A man from Earth (Virginia) navigating Martian society. He possesses knowledge of advanced imaging technology and is establishing himself among the Tharks and the red race.

**Prompting Keywords:** human male, earthling, virginian, martian setting.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Noblewoman of the red race

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Noblewoman / Love Interest

**Status:** Physically Present

**Description:** A noblewoman of the red race. She is characterized by her intelligence, curiosity, and deep connection to Martian history.

**Prompting Keywords:** red race woman, martian noblewoman, intelligent expression.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: Sola

aliases: Guardian, Attendant

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Ally / Protector of Dejah Thoris

**Status:** Physically Present

**Description:** An ally to John Carter who has been assigned as the guardian and attendant for Dejah Thoris.

**Prompting Keywords:** martian woman, protector, attendant.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: Sarkoja

aliases: Cruel figure

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja
**Role:** Antagonist / Hostile Figure

**Status:** Referenced/Present in context of threat

**Description:** A hostile and cruel figure who remains a threat to the protagonists.

**Prompting Keywords:** hostile martian, cruel expression.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: Lorquas Ptomel

aliases: High-ranking leader

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** Community Leader

**Status:** Referenced (Summoning character)

**Description:** A high-ranking leader of the community who issues a summons for John Carter to appear before the council.

**Prompting Keywords:** martian leader, authoritative.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: Thark chieftain

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Chieftain

**Status:** Referenced (Present during council)

**Description:** A prominent Thark chieftain who presides over the community sessions.

**Prompting Keywords:** Thark chieftain, martian warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
