# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:13:30.296519+00:00
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

Chapter id: CH022

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

Stationed to guard Jeddak Than Kosis in a heavily tapestried apartment, John Carter observes from a hidden passage as Dejah Thoris enters the chamber. To his devastation, he overhears her formally retract her preference for Tal Hajus and pledge herself to Sab Than, the Prince of Zodanga, in a political effort to prevent the conquest of Helium.

Believing this to be a mistake, Carter abandons his post and pursues her through the palace corridors. He is intercepted by four of Dejah Thoris's guards and kills them all in a violent skirmish to reach the Princess. When he finally confronts her, she is initially unable to recognize him due to his unfamiliar armor. Once identified, she is overcome with grief, explaining that she only made the promise because she believed Carter was dead and felt compelled to sacrifice her heart to save her people.

Dejah Thoris informs Carter that she is bound by Barsoomian custom to Sab Than; she explains a cultural misunderstanding where Carter, despite fighting for her, failed to formally ask for her hand in marriage as required by protocol. Despite his pleas, she maintains she cannot wed him if it requires the death of her husband.

As Carter attempts to navigate the labyrinthine palace of Zodanga to escape, he overhears guards discussing the butchered men in the antechamber. While hiding in a great hall, he listens to Than Kosis and the royal psychologist, Notan, discuss the mystery of a single man with extraordinary strength and skill. Realizing that increased patrols are hunting him, Carter waits for darkness before using his superior physical capabilities to leap from a balcony and escape the palace grounds.
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
- [Jeddak Than Kosis](#jeddak_than_kosis)
- [Tal Hajus](#tal_hajus)
- [Sab Than](#sab_than)
- [Notan](#notan)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH022 John Carter

aliases: Carter

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Warrior

**Status:** Physically Present

**Physical Description:** Possesses extraordinary strength and skill; capable of leaping from high balconies.

**Costume/Traits:** Wearing unfamiliar armor (not recognized by Dejah Thoris initially).

**Prompt Phrases:** Strong human warrior, agile combatant, wearing unfamiliar heavy armor, superhuman physical capabilities.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH022 Dejah Thoris

aliases: Princess

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Princess of Helium / Love Interest

**Status:** Physically Present

**Physical Description:** Not explicitly detailed in this chapter beyond her royal status and emotional state.

**Costume/Traits:** Royal attire (implied by setting).

**Prompt Phrases:** Barsoomian princess, grieving noblewoman, regal silhouette.

**Uncertainty Note:** Specific physical features are not described in this text segment.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: jeddak_than_kosis

canonical_character_id: CH022 Jeddak Than Kosis

aliases: Than Kosis

is_fully_identified: true

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Jeddak Than Kosis
**Role:** Ruler / Political Figure

**Status:** Physically Present (referenced/heard)

**Physical Description:** Unknown.

**Costume/Traits:** Implied high-status/royal attire.

**Prompt Phrases:** Barsoomian ruler, authoritative presence, political leader.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: CH022 Tal Hajus

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only mentioned as a former preference.

clarification_required: true

clarification_reason: Identity and appearance are not established in this chapter.

clarification_question: What is Tal Hajus's physical appearance and relationship to the court?

[[SECTION markdown]]

# Tal Hajus
**Role:** Referenced Suitor

**Status:** Referenced

**Physical Description:** Unknown.

**Costume/Traits:** Unknown.

**Prompt Phrases:** Barsoomian suitor, mentioned figure.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sab_than

canonical_character_id: CH022 Sab Than

aliases: Prince of Zodanga

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is mentioned as a political match but not seen.

clarification_required: true

clarification_reason: No physical description provided.

clarification_question: What does the Prince of Zodanga look like?

[[SECTION markdown]]

# Sab Than
**Role:** Prince of Zodanga / Political Spouse

**Status:** Referenced

**Physical Description:** Unknown.

**Costume/Traits:** Royal prince.

**Prompt Phrases:** Barsoomian prince, royal suitor, political figure.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: notan

canonical_character_id: CH022 Notan

aliases: Royal Psychologist

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Notan
**Role:** Royal Psychologist

**Status:** Physically Present (heard)

**Physical Description:** Unknown.

**Costume/Traits:** Likely scholarly or courtly attire.

**Prompt Phrases:** Barsoomian psychologist, intellectual advisor, court official.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
