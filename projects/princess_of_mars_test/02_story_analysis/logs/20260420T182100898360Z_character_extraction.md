# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:21:00.898862+00:00
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

Chapter id: CH024

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

While flying over an ancient dead city, John Carter's craft is shot down during a massive battle between thousands of green warriors. After crashing into the combat, Carter intervenes to save Tars Tarkas from being killed by three Warhoons, and the two fight side-by-side until the enemy retreats. Upon returning to Thark, Carter is reunited with Woola, but faces immediate political peril when the jeddak, Tal Hajus, orders him to be brought before the council for punishment. After a brief encounter with Sarkoja, Carter is brought to the palace where Tal Hajus reacts with rage and orders his torture.

Carter successfully appeals to the Thark council, challenging Tal Hajus's legitimacy by accusing him of cowardice and proposing Tars Tarkas as a superior leader. Following a duel in which Tars Tarkas kills the jeddak, Tars Tarkas is proclaimed the new jeddak and Carter is elevated to the rank of chieftain. To capitalize on the warriors' desire for plunder, Carter proposes an alliance to rescue Princess Dejah Thoris from Zodanga. Tars Tarkas assembles a massive expeditionary force of 150,000 Tharks, which marches under the cover of night to reach the walls of Zodanga. Once there, Carter leads an infiltration team that scales the city's carborundum walls. Having secured knowledge on how to open the gates, Carter coordinates a plan to seize the great gates while leading a detachment toward the palace to strike at the heart of the city.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john_carter)
- [Tars Tarkas](#tars_tarkas)
- [Woola](#woola)
- [Tal Hajus](#tal_hajus)
- [Sarkoja](#sarkoja)
- [Dejah Thoris](#dejah_thoris)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Carter

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Chieftain

**Status:** Physically Present

**Physical Description:** Human male, capable of high-intensity combat and scaling carborundum walls.

**Costume/Traits:** Combatant, leader of an infiltration team.

**Prompt Phrases:** human warrior, agile combatant, infiltrator, leader of Thark expedition.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** New Jeddak / Ally

**Status:** Physically Present

**Physical Description:** Green warrior, large-scale combatant.

**Costume/Traits:** Thark warrior, leader of a massive expeditionary force.

**Prompt Phrases:** green warrior, Thark jeddak, powerful alien soldier, massive expedition leader.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: Woola

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola
**Role:** Companion

**Status:** Physically Present

**Physical Description:** Non-human companion (implied creature).

**Costume/Traits:** Reunited with Carter.

**Prompt Phrases:** loyal alien companion, Thark beast.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: Tal Hajus

aliases: Jeddak (former)

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tal Hajus
**Role:** Antagonist / Former Jeddak

**Status:** Physically Present (deceased by end of chapter)

**Physical Description:** Green warrior, high-ranking Thark.

**Costume/Traits:** Royal/Political attire of a Jeddak, prone to rage.

**Prompt Phrases:** green warrior leader, angry jeddak, fallen ruler.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: Sarkoja

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Minimal physical description provided in text.

clarification_required: true

clarification_reason: Physical appearance and specific Thark sub-type unknown.

clarification_question: What is Sarkoja's physical appearance and role within the palace?

[[SECTION markdown]]

# Sarkoja
**Role:** Political figure / Palace resident

**Status:** Physically Present

**Physical Description:** Unknown.

**Costume/Traits:** Associated with the Thark palace.

**Prompt Phrases:** Thark political figure, palace inhabitant.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Princess Dejah Thoris

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is referenced as a captive but not visually described in this chapter.

clarification_required: true

clarification_reason: Visual identity and costume for the rescue mission are not established here.

clarification_question: What is Princess Dejah Thoris's physical appearance and attire?

[[SECTION markdown]]

# Dejah Thoris
**Role:** Objective / Princess

**Status:** Referenced (Captive in Zodanga)

**Physical Description:** Unknown.

**Costume/Traits:** Princess of Zodanga.

**Prompt Phrases:** captive princess, royal figure of Zodanga.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
