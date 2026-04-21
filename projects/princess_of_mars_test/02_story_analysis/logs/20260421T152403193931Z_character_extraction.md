# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:24:03.193931+00:00
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

Chapter id: CH023

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
John Carter infiltrates the guarded quarters of Kantos Kan to inform him of Dejah Thoris's engagement to Sab Than. Upon hearing the news, a distraught Kantos Kan vows to assassinate Sab Than using a secret palace entrance. The two men devise a plan: Kantos Kan will infiltrate the palace to kill the usurper, while Carter will attempt to fly to Helium. 

Carter performs a perilous climb up the Zodanga barracks, using a grappling hook to reach the roof and neutralizing a sentry to secure two air machines. As Carter and Kantos Kan depart, they are intercepted by a Zodangan air patrol. After a high-speed chase through the Martian sky, Carter uses a Heliumite speed-gearing trick to outrun his pursuers, but his machine is struck by a projectile from a cruiser. The resulting crash leaves him flying blind without a compass or speedometer. After six hours of flight over a dead sea bottom, Carter realizes he is lost; despite seeing several large cities, none match the distinct twin-city architecture and scarlet/yellow towers of Helium.

**Characters:**
* **John Carter:** A resourceful adventurer and airman who executes a dangerous climb and high-speed aerial escape.
* **Kantos Kan:** A Heliumite air-scout who vows to kill Sab Than to avenge Dejah Thoris's honor.
* **Sab Than (Mentioned):** The ruler of Zodanga to whom Dejah Thoris is promised.
* **Dejah Thoris (Mentioned):** The Princess of Helium.
* **Zodangan Sentry:** A guard at the barracks neutralized by Carter.

**Settings:**
* **Zodanga:** A heavily guarded city characterized by high-rise buildings and active air patrols.
* **The Barracks:** An enormous, thousand-foot tall building in Zodanga.
* **The Martian Sky:** The setting for a high-speed pursuit involving air-scout craft and cruisers.
* **Dead Sea Bottom:** A vast, desolate expanse Carter flies over while lost.
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
- [Kantos Kan](#kantos_kan)
- [Sab Than](#sab_than)
- [Dejah Thoris](#dejah_thoris)
- [Zodangan Sentry](#zodangan_sentry)

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
**Role:** Protagonist / Adventurer

**Status:** Physically Present

**Physical Description:** Resourceful adventurer and skilled airman. Capable of extreme physical feats including climbing thousand-foot barracks and neutralizing sentries.

**Costume/Traits:** Uses a grappling hook and operates Martian air machines. Demonstrates high proficiency with Heliumite speed-gearing.

**Prompt Phrases:** Resourceful human adventurer, Martian airman, pilot of an air machine, skilled climber.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: Kantos Kan

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan
**Role:** Supporting Character / Heliumite Air-scout

**Status:** Physically Present

**Physical Description:** A distraught Heliumite air-scout. Driven by vengeance and honor regarding Dejah Thoris.

**Costume/Traits:** Associated with Heliumite aerial combat/scouting.

**Prompt Phrases:** Heliumite air-scout, distraught warrior, Martian pilot.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sab_than

canonical_character_id: Sab Than

aliases: Usurper

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only mentioned as a ruler/usurper; no physical description provided.

clarification_required: true

clarification_reason: Needs visual identification for character design.

clarification_question: What is Sab Than's physical appearance and attire?

[[SECTION markdown]]

# Sab Than
**Role:** Antagonist (Mentioned)

**Status:** Referenced

**Physical Description:** Unknown. Described as the ruler of Zodanga and a usurper.

**Costume/Traits:** Associated with the ruling class of Zodanga.

**Prompt Phrases:** Zodangan ruler, usurper, Martian noble.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: Princess of Helium

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only mentioned as a princess; no physical description provided.

clarification_required: true

clarification_reason: Needs visual identification for character design.

clarification_question: What does Dejah Thoris look like?

[[SECTION markdown]]

# Dejah Thoris
**Role:** Supporting Character (Mentioned)

**Status:** Referenced

**Physical Description:** Unknown. Identified as the Princess of Helium.

**Costume/Traits:** Royal status in Helium.

**Prompt Phrases:** Heliumite princess, Martian royalty.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: zodangan_sentry

canonical_character_id: Zodangan Sentry

aliases: Guard

is_fully_identified: false

manual_description_required: true

manual_description_reason: Generic guard role with no specific physical or costume details provided.

clarification_required: true

clarification_reason: Needs uniform and physical description to distinguish from other Zodgan citizens.

clarification_question: What is the standard uniform and appearance of a Zodangan barracks sentry?

[[SECTION markdown]]

# Zodangan Sentry
**Role:** Minor Character

**Status:** Physically Present (Neutralized)

**Physical Description:** A guard stationed at the Zodanga barracks.

**Costume/Traits:** Part of the Zodangan military/security force.

**Prompt Phrases:** Zodangan guard, barracks sentry, Martian soldier.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
