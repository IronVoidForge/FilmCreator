# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:33:23.937444+00:00
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

Chapter id: CH002

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

**Setting:** A cave in the Arizona mountains; transitions from dawn to a moonlit night.

**Characters:**
* **The Narrator:** A man rendered paralyzed by an unknown vapor, who undergoes a supernatural metamorphosis.
* **Apache Warriors:** A group of scouts who approach the cave but flee in terror from an unseen horror within.

**Key Events:**
* **Paralysis:** The narrator finds himself unable to move due to a mysterious gas in a cave, watching helplessly as Apache warriors approach the ledge.
* **The Terror in the Cave:** A low, terrifying moan emanates from the depths of the cave, causing the Apache warriors to flee in a panic, leaving the narrator alone with his fear.
* **Metamorphosis:** After hours of paralysis, the narrator breaks free through intense mental willpower, only to discover a supernatural reality: he sees his own lifeless, naked body lying on the cave floor while he stands as a separate entity.
* **Escape and Cosmic Pull:** Lacking weapons and fearing the unseen presence in the cave, the narrator escapes into the Arizona night. While gazing at the red star of Mars, he feels an overwhelming, magnetic pull from the planet that suddenly transports him through the cold darkness of space.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

* [narrator](#narrator)
* [apache_warriors](#apache_warriors)

[[/SECTION]]

[[FILMCREATORE_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH002 Narrator

aliases: Narrator, The Man, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance and clothing are not described prior to the discovery of his lifeless body.

clarification_required: true

clarification_reason: Need details regarding the narrator's original physical features and attire.

clarification_question: What were the narrator's facial features and what was he wearing before the paralysis?

[[SECTION markdown]]

# Narrator

**Role:** Protagonist

**Presence:** Physically present (as a paralyzed body and a separate, metaphysical entity).

**Physical Description:** A man whose lifeless, naked body is discovered lying on the cave floor. Following a metamorphosis, he exists as a separate, conscious entity capable of movement and observation.

**Costume/Silhouette:** The physical body is naked; the appearance of the "entity" version is undefined.

**Uncertainty Notes:** Initial clothing, hair, and facial characteristics are entirely unknown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH002 Apache Warriors

aliases: Apache Scouts, Warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical traits, clothing, or individual characteristics are provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Apache Warriors

**Role:** Secondary characters (Scouts)

**Presence:** Physically present (approaching the cave ledge).

**Physical Description:** A group of Apache warriors/scouts.

**Costume/Silhouette:** Undefined.

**Uncertainty Notes:** No details regarding their specific appearance, weaponry, or traditional attire are available in this chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
