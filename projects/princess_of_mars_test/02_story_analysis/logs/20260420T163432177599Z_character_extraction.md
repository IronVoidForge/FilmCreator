# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:34:32.177599+00:00
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

# Character Index

* [narrator](narrator)
* [apache_warriors](apache_warriors)
* [unseen_horror](unseen_horror)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH002 Narrator

aliases: Protagonist, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance of the post-metamorphosis entity is not described; only his lifeless corpse is visible.

clarification_required: true

clarification_reason: The physical nature of the narrator's consciousness after breaking free from paralysis is unknown.

clarification_question: Does the narrator's new entity possess a human form, or is it purely incorporeal?

[[SECTION markdown]]

# Narrator

**Role:** Protagonist

**Presence:** Physically present (as both a paralyzed body and a separate entity).

**Physical Description:** 
Initially described as a man rendered paralyzed by vapor. A "lifeless, naked body" is seen lying on the cave floor, which is identified as his own.

**Costume/Silhouette:** 
The physical body is naked. The silhouette of the post-metamorphosis entity is undefined.

**Prompt Phrases:** 
naked man lying lifeless, paralyzed man in a cave, detached consciousness, cosmic traveler.

**Uncertainty Notes:** 
The visual appearance of the narrator's consciousness/entity after the metamorphosis is entirely unstated.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH002 Apache Warriors

aliases: Scouts

is_fully_identified: true

manual_description_required: true

manual_description_reason: No specific clothing, physical features, or equipment are detailed in the text.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Apache Warriors

**Role:** Scouts

**Presence:** Physically present (approaching the cave).

**Physical Description:** 
Identified as Apache warriors/scouts. No specific facial features or physical builds are provided.

**Costume/Silhouette:** 
No costume details or silhouettes are mentioned.

**Prompt Phrases:** 
Apache scouts, group of warriors approaching a cave ledge, fleeing in terror.

**Uncertainty Notes:** 
Visuals for clothing, weaponry, and specific ethnic features are missing from the source text.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: unseen_horror

canonical_character_id: CH002 Unseen Horror

aliases: Terror in the Cave

is_fully_identified: false

manual_description_required: true

manual_description_reason: The entity is explicitly described as unseen; only its sound is known.

clarification_required: true

clarification_reason: The character is purely an auditory presence in this chapter.

clarification_question: What is the visual manifestation or physical form of the creature causing the moan?

[[SECTION markdown]]

# Unseen Horror

**Role:** Antagonist/Presence

**Presence:** Referenced (Auditory only).

**Physical Description:** 
No visual description exists; the entity is characterized by a "low, terrifying moan."

**Costume/Silhouette:** 
N/A.

**Prompt Phrases:** 
terrifying low moan from cave depths, unseen presence in darkness, source of terror.

**Uncertainty Notes:** 
The character has no visual components provided in the text; it is a purely sensory/auditory element.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
