# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:40:52.895800+00:00
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

**Setting:** A cave in the Arizona mountains; a rocky gorge under a clear starlight night.

**Characters:** 
- The Protagonist (experiencing paralysis, metamorphosis, and astral projection).
- Apache Warriors (who flee the cave in terror).
- The Protagonist's deceased friend (lying on the cave ledge).

**Events:**
- **Paralysis:** The protagonist wakes in a cave to find himself physically paralyzed by a mysterious, pungent vapor. 
- **The Apache Encounter:** A group of Apache warriors approaches the cave but are terrified by a low moaning sound coming from the darkness behind the protagonist; they flee in panic, causing one warrior to fall to his death.
- **Metamorphosis:** After hours of isolation, the protagonist exerts immense mental will to break the paralysis. Upon succeeding, he discovers he has undergone a metamorphosis: he is standing naked and alive, while his physical body remains lying on the cave floor, clothed and seemingly dead.
- **The Escape:** Fearing the unseen presence in the cave, the protagonist flees into the Arizona night. 
- **The Call of Mars:** While admiring the moonlit landscape, the protagonist becomes mesmerized by a large red star—Mars. He feels an irresistible pull toward the planet and, through a sudden surge of will, is transported through space via an instant of cold and darkness.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH002

- [Protagonist](#protagonist)
- [Apache Warriors](#apache-warriors)
- [Deceased Friend](#deceased-friend)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance is not described; the character undergoes a metamorphosis where they are naked, but no facial or bodily features are provided.

clarification_required: true

clarification_reason: Identity and physical traits are unknown.

clarification_question: What is the protagonist's age, ethnicity, hair color, eye color, and general build?

[[SECTION markdown]]

# Protagonist
**Role:** Central Character / POV

**Presence:** Physically present (undergoes metamorphosis/astral projection).

**Physical Description:** 
- Currently naked following a metamorphosis.
- Physical body is described as lying on the cave floor, clothed and seemingly dead, while a new version of the character stands alive.

**Costume/Silhouette:** 
- Post-metamorphosis: Naked.
- Pre-metamorphosis: Clothed (specifics unknown).

**Prompting Nouns:** Naked human, survivor, astral traveler.

**Uncertainty Notes:** No facial features, hair, or specific body type are established in this chapter. The distinction between the "dead" physical body and the "living" metamorphosed entity is critical for continuity.
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH002 Apache Warriors

aliases: Warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only identified by group affiliation and reaction; no specific physical traits or clothing details provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Apache Warriors
**Role:** Minor Characters / Antagonistic Presence (Fleeing)

**Presence:** Physically present (approaching the cave).

**Physical Description:** 
- Group of warriors.
- React with terror to a mysterious moaning sound.

**Costume/Silhouette:** Unknown.

**Prompting Nouns:** Apache warriors, group of men, fleeing in panic.

**Uncertainty Notes:** Specific attire or physical characteristics are not detailed beyond their tribal identity.
[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: deceased_friend

canonical_character_id: CH002 Deceased Friend

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only mentioned as a corpse on a ledge; no physical description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Deceased Friend
**Role:** Referenced Character

**Presence:** Referenced (lying on the cave ledge).

**Physical Description:** 
- Deceased.

**Costume/Silhouette:** Unknown.

**Prompting Nouns:** Corpse, deceased man, lying on cave ledge.

**Uncertainty Notes:** No visual details are provided for this character; they serve as a narrative element to establish the protagonist's history or situation.
[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
