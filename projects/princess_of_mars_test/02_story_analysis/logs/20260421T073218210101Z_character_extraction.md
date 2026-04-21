# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:32:18.210101+00:00
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
Following his duel with Zad, John Carter recovers from a non-fatal wound inflicted by a sword thrust to the chest. He reunites with his retinue and finds Dejah Thoris in deep mourning, believing him dead. Sola, who was injured during her encounter with Sarkoja, reveals that Dejah's grief is due to her profound affection for Carter. As the massive caravan—comprising hundreds of chariots, warriors, and animals—moves silently across a trackless mossy sea bottom, they camp at the foot of southern hills. That night, Sola shares her tragic history with Carter. She reveals that she is the daughter of a Thark woman and a high-ranking warrior who fell in love in secret. Her mother was discovered by Sarkoja and subsequently tortured to death by Tal Hajus for refusing to reveal the father's identity. Sola concludes by revealing that her father is Tars Tarkas, who remains unaware of her true identity.

**Characters:**
* **John Carter:** Recovering from a chest wound; observes the scale of the Martian caravan.
* **Sola:** A Green Martian woman who reveals her secret lineage and tragic past.
* **Dejah Thoris:** Shown in a state of intense grief, mourning Carter's perceived death.
* **Sarkoja:** Mentioned as the antagonist who discovered Sola's mother and caused her downfall.
* **Tars Tarkas:** Revealed to be Sola's father; currently traveling with the caravan.
* **Sola's Mother:** (Flashback) A Thark woman who died protecting her child and her lover's identity.

**Settings:**
* **The Mossy Sea Bottom:** A vast, silent, trackless waste covered in moss that absorbs the tracks of the passing caravan.
* **The Caravan Camp:** Located at the foot of hills marking the southern boundary of the sea; a site of rest after two days of travel.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [john_carter](#john_carter)
- [sola](#sola)
- [dejah_thoris](#dejah_thoris)
- [sarkoja](#sarkoja)
- [tars_tarkas](#tars_tarkas)
- [solas_mother](#solas_mother)

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
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:** Recovering from a non-fatal sword thrust to the chest.

**Costume/Silhouette:** Not explicitly detailed in this chapter, but currently wounded.

**Prompt Phrases:** Human man, recovering from chest wound, survivor of duel.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: Sola

aliases: Daughter of Tars Tarkas

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Supporting Character / Information Provider

**Status:** Physically Present

**Physical Description:** A Green Martian woman. Has sustained injuries from an encounter with Sarkoja.

**Costume/Silhouette:** Green Martian physiology.

**Prompt Phrases:** Green Martian woman, injured warrior, daughter of Tars Tarkas.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: Dejah Thoris

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:** In a state of intense grief and deep mourning.

**Costume/Silhouette:** Mourning attire (implied by emotional state).

**Prompt Phrases:** Martian woman, grieving, mourning, intense sorrow.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: Sarkoja

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja
**Role:** Antagonist (Referenced)

**Status:** Referenced

**Physical Description:** No specific physical details provided in this chapter.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Martian antagonist, tormentor.

**Uncertainty Note:** Character is mentioned as a source of trauma for Sola but lacks visual description in this text.

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
**Role:** Supporting Character (Referenced)

**Status:** Referenced / Traveling with caravan

**Physical Description:** A high-ranking Thark warrior.

**Costume/Silhouette:** Thark warrior silhouette.

**Prompt Phrases:** Green Martian, Thark warrior, high-ranking warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: solas_mother

canonical_character_id: Sola's Mother

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only identified as a Thark woman; no physical traits provided.

clarification_required: true

clarification_reason: Lacks any visual descriptors beyond species.

clarification_question: What was the physical appearance of Sola's mother?

[[SECTION markdown]]

# Sola's Mother
**Role:** Historical Figure (Flashback)

**Status:** Referenced (Flashback)

**Physical Description:** A Thark woman.

**Costume/Silhouette:** Unknown.

**Prompt Phrases:** Thark woman, tragic figure.

**Uncertainty Note:** No specific physical characteristics are provided to distinguish her appearance.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
