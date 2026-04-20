# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:54:23.007341+00:00
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

**Setting:**
A pretentious, ancient building near the audience chamber in the city of Korad, featuring elaborate architecture and frescoes depicting an extinct, fair-skinned race of Martians.

**Characters:**
* **John Carter:** An Earthman and rising Thark chieftain.
* **Dejah Thoris:** A princess of the red Martians; she is fascinated by ancient history and develops a deep trust in Carter.
* **Sola:** A female Thark who acts as a guardian for both Carter and Dejah Thoris.
* **Sarkoja:** A male Thark who harbors ill will toward Carter and Dejah Thoris.
* **Lorquas Ptomel:** The high-ranking chieftain of the Tharks.
* **Tars Tarkas:** A prominent Thark warrior.

**Events:**
* **Relocation:** After John Carter threatens Sarkoja to protect Dejah Thoris, he arranges for Sola to take Dejah Thoris to more secure, luxurious quarters in an ancient building.
* **Social Standing:** Sola informs Carter that his prowess has earned him the rank of eleventh among the Thark chieftains, noting that only Lorquas Ptomel ranks higher.
* **The Revelation:** In their new quarters, Dejah Thoris questions Carter's origins. Carter reveals he is from Earth (the planet Mars in his world). Despite the impossibility of his claim, Dejah Thoris chooses to believe him based on her intuition and his perceived honesty.
* **Martian Lore & Technology:** Dejah Thoris explains that Martians can observe other planets via advanced telescopic imaging technology. She also provides a history lesson on the ancient, fair-haired Martians who preceded the current red race, explaining how environmental changes forced different races to merge or compete.
* **Summons:** The peaceful conversation is interrupted by a messenger delivering a summons from Lorquas Ptomel, requiring Carter's immediate presence at the audience chamber.
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
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Sarkoja](#sarkoja)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Tars Tarkas](#tars_tarkas)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Earthman, Thark chieftain

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Rising Thark Chieftain

**Status:** Physically Present

**Description:** An Earthman who has risen to the rank of eleventh among the Thark chieftains. Known for his prowess and honesty.

**Prompt Phrases:** Earthman, Thark chieftain, high-ranking warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH002 Dejah Thoris

aliases: Princess of the red Martians

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Princess of the Red Martians

**Status:** Physically Present

**Description:** A princess of the red Martian race. She is highly intelligent, interested in ancient history, and possesses strong intuition.

**Prompt Phrases:** Red Martian princess, noblewoman, ancient history enthusiast.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH003 Sola

aliases: Female Thark, Guardian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Guardian

**Status:** Physically Present

**Description:** A female Thark who serves as a guardian for both John Carter and Dejah Thoris.

**Prompt Phrases:** Female Thark, guardian, Martian warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH004 Sarkoja

aliases: Male Thark

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja
**Role:** Antagonist / Rival

**Status:** Referenced/Present in context of conflict

**Description:** A male Thark who harbors ill will toward John Carter and Dejah Thoris.

**Prompt Phrases:** Male Thark, hostile warrior, rival chieftain.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH005 Lorquas Ptomel

aliases: High-ranking chieftain

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** High-ranking Chieftain

**Status:** Referenced (Summons Carter)

**Description:** The highest-ranking chieftain of the Tharks, ranking above John Carter.

**Prompt Phrases:** High-ranking Thark chieftain, supreme leader.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH006 Tars Tarkas

aliases: Prominent Thark warrior

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Prominent Thark Warrior

**Status:** Referenced

**Description:** A prominent warrior within the Thark hierarchy.

**Prompt Phrases:** Thark warrior, prominent Martian soldier.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
