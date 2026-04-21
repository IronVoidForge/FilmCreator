# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:06:09.745823+00:00
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

Chapter id: CH007

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
The protagonist accompanies Sola and a massive military cavalcade—consisting of two hundred decorated chariots drawn by enormous animals—to a remote incubator located on a dead sea bottom. Upon arrival, the chieftain Lorquas Ptomel and Tars Tarkas oversee the hatching process. The protagonist performs a feat of physical prowess by leaping over parked chariots to impress the leaders. As the young Martians emerge from the incubator, they are captured in a ritualistic gauntlet formed by women and youths. The chapter details the brutal Martian child-rearing system: offspring are communal, raised by foster mothers without parental love, and trained solely for warfare and survival. Following the ceremony, the warriors transport eggs from subterranean vaults to the incubator, which will remain sealed for five years. Back at the dead city, the protagonist undergoes intensive training with Sola, learning the simple Martian language and developing telepathic abilities, while discovering that their own mind remains impenetrable to Martian telepathy.

**Characters:**
- **The Protagonist:** An Earthman learning Martian customs; possesses a unique mental immunity to telepathic reading.
- **Sola:** A female Martian who acts as the protagonist's guide and foster mother to a newly hatched Martian.
- **Tars Tarkas:** A Martian warrior/leader involved in the incubator ceremony.
- **Lorquas Ptomel, Jed:** The enormous chieftain overseeing the hatching.
- **The Young Martian:** A physically perfect, four-foot-tall male captured during the hatching, who becomes a rival to the protagonist during training.

**Settings:**
- **The Plaza/City:** The starting point of the journey, characterized by large chariots and communal activity.
- **The Dead Sea Bottom:** A level expanse where the incubator is located.
- **The Incubator:** A remote enclosure where Martian eggs are hatched via solar rays.
- **The Dead City:** The protagonist's base of operations during periods of idleness and training.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [Protagonist](#protagonist)
- [Sola](#sola)
- [Tars Tarkas](#tars-tarkas)
- [Lorquas Ptomel, Jed](#lorquas-ptomel-jed)
- [The Young Martian](#the-young-martian)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH001 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance (height, build, facial features) is not described in this chapter.

clarification_required: true

clarification_reason: Identity and physical form are unknown.

clarification_question: What is the protagonist's physical appearance and specific Earthly origin?

[[SECTION markdown]]

# Protagonist
**Role:** Observer, trainee, and outsider.

**Status:** Physically present.

**Physical Description:** 
Unknown. Character demonstrates high physical prowess (leaping over chariots) and possesses a unique mental immunity to Martian telepathy.

**Costume/Silhouette:** 
Not specified.

**Prompting Phrases:** 
Human male, Earthman, physically agile, mentally impenetrable.

**Uncertainty Notes:** 
No visual details provided regarding hair, eyes, build, or clothing.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH002 Sola

aliases: Guide, Foster Mother

is_fully_identified: false

manual_description_required: true

manual_description_reason: While identified as a female Martian, specific physical traits (height, skin color, facial features) are absent.

clarification_required: true

clarification_reason: Needs visual definition for consistent rendering.

clarification_question: What is Sola's specific physical appearance and Martian phenotype?

[[SECTION markdown]]

# Sola
**Role:** Guide and mentor to the protagonist.

**Status:** Physically present.

**Physical Description:** 
Female Martian. Acts as a foster mother to newly hatched Martians.

**Costume/Silhouette:** 
Not specified.

**Prompting Phrases:** 
Female Martian, guide, mentor, telepathic communicator.

**Uncertainty Notes:** 
Specific Martian physical characteristics (e.g., skin texture, eye shape, height) are not detailed in this text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Martian Leader, Warrior

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is a known leader but lacks specific physical description in this chapter.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Martian warrior and leader.

**Status:** Physically present.

**Physical Description:** 
Martian warrior/leader; oversees the hatching process at the incubator.

**Costume/Silhouette:** 
Not specified.

**Prompting Phrases:** 
Martian warrior, authoritative leader, commanding presence.

**Uncertainty Notes:** 
Visual details regarding his specific Martian physiology are not provided in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel_jed

canonical_character_id: CH004 Lorquas Ptomel, Jed

aliases: Chieftain

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described as "enormous," but lacks specific facial or anatomical detail.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel, Jed
**Role:** Chieftain overseeing the hatching ceremony.

**Status:** Physically present.

**Physical Description:** 
An enormous Martian chieftain.

**Costume/Silhouette:** 
Not specified.

**Prompting Phrases:** 
Enormous Martian, chieftain, imposing figure, ritual leader.

**Uncertainty Notes:** 
"Enormous" is the only descriptor; specific scale and appearance are undefined.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: young_martian

canonical_character_id: CH005 Young Martian

aliases: Rival

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described as "physically perfect" and "four-foot-tall," but lacks specific features.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Young Martian
**Role:** Rival to the protagonist during training.

**Status:** Physically present.

**Physical Description:** 
A male Martian, four feet tall, described as physically perfect.

**Costume/Silhouette:** 
Not specified.

**Prompting Phrases:** 
Young male Martian, four feet tall, physically perfect, athletic build.

**Uncertainty Notes:** 
"Physically perfect" is subjective; specific color, texture, and features are unknown.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
