# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:20:34.242512+00:00
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

Chapter id: CH015

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
Following a violent skirmish, John Carter recovers from a non-fatal wound inflicted by Zad. He is treated by his Martian retinue and reunites with Dejah Thoris and Sola. While Dejah Thoris mourns Carter (believing him dead), Carter observes her grief from a distance. That night, at the edge of a southern sea, Sola reveals her secret history to Carter. She recounts how her mother and a Thark warrior fell in love against tradition, leading to her mother's imprisonment and death under torture by Tal Hajus. Sola reveals that she was hidden among the community children to survive, and finally discloses the identity of her father: Tars Tarkas.

**Characters:**
- **John Carter:** Recovering from a chest wound; listener to Sola's confession.
- **Sola:** A green Martian woman who reveals her tragic lineage and her true parentage.
- **Dejah Thoris:** Mourning John Carter in silence.
- **Sola's Mother (deceased):** A Thark woman who died protecting the secret of her child and lover.
- **Sola's Father (Tars Tarkas):** Revealed to be the high-ranking green Martian warrior traveling with the caravan.
- **Sarkoja:** The antagonist from Sola's past who betrayed Sola's mother.
- **Tal Hajus:** The Thark chieftain responsible for the death of Sola's mother.

**Settings:**
- **The Ancient Sea Bottom:** A trackless, moss-covered expanse on Barsoom that leaves no tracks or dust.
- **The Caravan Camp:** A massive, colorful procession of two hundred and fifty chariots, warriors, and animals (thoats and zitidars) moving across the yellow landscape toward the southern hills.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH015

- [John Carter](#john_carter)
- [Sola](#sola)
- [Dejah Thoris](#dejah_thoris)
- [Sola's Mother](#sola_s_mother)
- [Tars Tarkas](#tars_tarkas)
- [Sarkoja](#sarkoja)
- [Tal Hajus](#tal_hajus)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: John Carter

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Recovering Warrior

**Status:** Physically Present

**Physical Description:** Currently recovering from a non-fatal chest wound inflicted by Zad.

**Costume/Silhouette:** Martian retinue attire (implied context of recovery).

**Prompt Phrases:** wounded human warrior, recovering from chest injury, listener.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: Sola

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Confidante / Secret Daughter of Tars Tarkas

**Status:** Physically Present

**Physical Description:** A green Martian woman.

**Costume/Silhouette:** Standard Martian attire (implied).

**Prompt Phrases:** green-skinned Martian woman, secret bearer, tragic lineage.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Love Interest / Mourner

**Status:** Physically Present

**Physical Description:** Martian woman (visual specifics not detailed in this chapter).

**Costume/Silhouette:** Martian noble attire (implied).

**Prompt Phrases:** mourning Martian woman, grieving in silence.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola_s_mother

canonical_character_id: Sola's Mother

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is deceased and only described through Sola's recollection; no specific physical traits provided.

clarification_required: true

clarification_reason: Needs visual identification for historical context.

clarification_question: What were the specific physical features of Sola's mother?

[[SECTION markdown]]

# Sola's Mother
**Role:** Deceased Parent / Tragic Figure

**Status:** Referenced (Deceased)

**Physical Description:** Unknown; described as a woman who fell in love with a Thark warrior.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** deceased Martian woman, victim of torture, tragic lover.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: Tars Tarkas

aliases: Sola's Father

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Secret Father / High-ranking Warrior

**Status:** Referenced (Present in caravan)

**Physical Description:** A high-ranking green Martian warrior.

**Costume/Silhouette:** Thark warrior regalia.

**Prompt Phrases:** high-ranking green Martian warrior, Thark chieftain, powerful presence.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: Sarkoja

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is mentioned as an antagonist from the past with no physical description provided.

clarification_required: true

clarification_reason: Needs visual identification.

clarification_question: What does Sarkoja look like?

[[SECTION markdown]]

# Sarkoja
**Role:** Antagonist (Past)

**Status:** Referenced

**Physical Description:** Unknown.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** betrayer, antagonist, Martian traitor.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: Tal Hajus

aliases: Thark Chieftain

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is mentioned as a chieftain responsible for death, but lacks physical description.

clarification_required: true

clarification_reason: Needs visual identification.

clarification_question: What are the physical characteristics of Tal Hajus?

[[SECTION markdown]]

# Tal Hajus
**Role:** Antagonist / Chieftain

**Status:** Referenced

**Physical Description:** Unknown; identified as a Thark chieftain.

**Costume/Silhouette:** Thark warrior attire (implied).

**Prompt Phrases:** Thark chieftain, violent leader, antagonist.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
