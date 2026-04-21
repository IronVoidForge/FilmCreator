# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:51:13.771757+00:00
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

**Setting:** A cave in the Arizona mountains; a rocky gorge and canyon under moonlight; the vastness of space.

**Characters:**
- **The Protagonist:** A man who experiences physical paralysis due to a mysterious gas, undergoes a supernatural metamorphosis, and is eventually pulled toward Mars.
- **Apache Warriors:** A group of braves who approach the cave but flee in terror from an unseen moaning sound emanating from the cave's depths.
- **The Dead Friend:** The protagonist's companion, whose body lies near the cave entrance.

**Events:**
- **Paralysis:** The protagonist is rendered immobile by a pungent, tenuous vapor within the cave, leaving him conscious but unable to move.
- **The Apache Encounter:** A group of Apache warriors discovers the protagonist; however, they are terrified by a low moaning sound from the back of the cave and flee in a panic, causing one warrior to fall to his death.
- **Metamorphosis:** After hours of isolation, the protagonist exerts a massive mental effort to break his paralysis. Upon succeeding, he discovers he has undergone a strange transformation: he is standing naked, while his physical body remains lying on the cave floor, clothed and seemingly lifeless.
- **The Escape:** Fearing an unseen presence in the dark cave, the protagonist flees into the Arizona night.
- **The Call of Mars:** While observing the landscape, the protagonist becomes mesmerized by a large red star (Mars). He feels an irresistible pull toward the planet, closes his eyes, and is suddenly transported through space into darkness and cold.
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
- [The Dead Friend](#the-dead-friend)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Man

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance (age, build, hair, facial features) is not described; only the state of being naked and the occurrence of a metaphysical split are noted.

clarification_required: true

clarification_reason: The nature of the "metamorphosis" and the physical distinction between the two bodies needs definition.

clarification_question: What are the protagonist's specific physical traits, and how does the 'new' body differ visually from the 'old' lifeless body?

[[SECTION markdown]]

# Protagonist
**Role:** Central character undergoing metamorphosis.

**Presence:** Physically present (in two states).

**Physical Description:** 
- Currently naked following a supernatural transformation.
- Possesses a "lifeless" physical shell left on the cave floor.
- Experiences intense mental effort and sensory overload.

**Costume/Silhouette:** 
- Naked (post-transformation).
- Clothed (original body left in the cave).

**Prompting Nouns:** 
Naked man, paralyzed man, metaphysical duplicate, transformed human.

**Uncertainty Notes:** 
Specific facial features, hair color, ethnicity, and body type are entirely unstated. The visual distinction between the "conscious" entity and the "lifeless" shell is unknown.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH002 Apache Warriors

aliases: Braves

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical descriptions, clothing, or gear provided beyond their tribal identity.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Apache Warriors
**Role:** Group encountered by the protagonist; fleeing witnesses.

**Presence:** Physically present (briefly).

**Physical Description:** 
- A group of warriors/braves.

**Costume/Silhouette:** 
- Not specified.

**Prompting Nouns:** 
Apache braves, indigenous warriors, fleeing group.

**Uncertainty Notes:** 
No details regarding specific attire, weaponry, or individual features are provided in the text.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dead_friend

canonical_character_id: CH002 Dead Friend

aliases: Companion

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only mentioned as a corpse near the cave entrance; no physical description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Dead Friend
**Role:** Referenced companion of the protagonist.

**Presence:** Referenced (body located near cave entrance).

**Physical Description:** 
- Deceased.

**Costume/Silhouette:** 
- Unknown.

**Prompting Nouns:** 
Dead man, corpse, fallen companion.

**Uncertainty Notes:** 
No visual information is available regarding this character's appearance or clothing.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
