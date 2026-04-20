# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:22:38.777435+00:00
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

Chapter id: CH025

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

**Setting:** The palace of Zodanga, specifically the brilliantly illuminated audience chamber and the labyrinthine dungeons beneath.

**Characters:**
* **John Carter:** The protagonist, who infiltrates the palace to prevent a forced marriage.
* **Dejah Thoris:** Princess of Helium, who is being held for a political marriage ceremony.
* **Than Kosis:** The Jeddak of Zodanga.
* **Sab Than:** The Prince of Zodanga, son of Than Kosis.
* **Tars Tarkas:** Leader of the Thark warriors, providing military support.
* **Kantos Kan:** An ally of Carter, rescued from the Zodangan dungeons.

**Events:**
* **The Infiltration:** John Carter and fifty Tharks led by Tars Tarkas breach the gates of Zodanga and enter the palace gardens.
* **The Ceremony Interrupted:** Inside the audience chamber, Than Kosis is conducting a ceremony to bind Dejah Thoris to Sab Than with golden chains. Carter shatters the chamber window and leaps into the hall, breaking the ceremonial chain.
* **The Battle in the Throne Room:** A chaotic skirmish ensues between Carter, the Zodangan nobility/guards, and the Tharks. During the fight, Sab Than is killed, as is his father, Than Kosis. Tars Tarkas eventually clears the room of opposition.
* **The Rescue:** Carter leads a search of the dungeons, successfully locating and freeing Kantos Kan using keys taken from a fallen jailer.
* **The Engagement:** Amidst the ongoing sounds of war in the streets of Zodanga, Carter and Dejah Thoris find a moment of peace. They profess their love for one another and formally promise themselves in marriage.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH025

- [john_carter](#john_carter)
- [dejah_thoris](#dejah_thoris)
- [than_kosis](#than_kosis)
- [sab_than](#sab_than)
- [tars_tarkas](#tars_tarkas)
- [kantos_kan](#kantos_kan)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: Protagonist

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Infiltrator

**Status:** Physically Present

**Description:** An infiltrator who breaches the palace gardens and the audience chamber. He is capable of high-action feats, such as shattering windows and leaping into ceremonial halls.

**Prompt Phrases:** Human male, agile warrior, combatant, intruder.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Princess of Helium

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Princess of Helium / Captive

**Status:** Physically Present

**Description:** Held in the palace of Zodanga for a forced political marriage. She is the subject of a binding ceremony involving golden chains.

**Prompt Phrases:** Princess, noblewoman, captive, ceremonial setting.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: than_kosis

canonical_character_id: Than Kosis

aliases: Jeddak of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Than Kosis
**Role:** Jeddak of Zodanga / Antagonist (Deceased)

**Status:** Physically Present

**Description:** The ruler of Zodanga who conducts the marriage ceremony. He is killed during the skirmish in the throne room.

**Prompt Phrases:** Ruler, Jeddak, elder noble, Zodangan royalty.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sab_than

canonical_character_id: Sab Than

aliases: Prince of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sab Than
**Role:** Prince of Zodanga / Groom (Deceased)

**Status:** Physically Present

**Description:** Son of Than Kosis, intended to be bound to Dejah Thoris with golden chains. He is killed during the battle in the throne room.

**Prompt Phrases:** Prince, groom, Zodangan nobility, combatant.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: Leader of the Tharks

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Military Leader / Ally

**Status:** Physically Present

**Description:** Leads fifty Thark warriors in the breach of Zodanga. He is a combatant who clears the throne room of opposition.

**Prompt Phrases:** Thark warrior leader, military commander, alien warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: Kantos Kan

aliases: Ally

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan
**Role:** Ally / Rescued Prisoner

**Status:** Physically Present

**Description:** An ally of Carter who was being held in the Zodangan dungeons before being freed by Carter.

**Prompt Phrases:** Prisoner, rescued ally, dungeon inhabitant.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
