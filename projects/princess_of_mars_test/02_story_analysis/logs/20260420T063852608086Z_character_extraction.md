# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:38:52.608086+00:00
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



Important rules:

- if a character does not have enough physical or visual description in the supplied material to support dependable later image generation, set manual_description_required to true

- explain exactly why in manual_description_reason

- do not guess ornate missing details just to avoid the flag

- if the chapter names a character without enough stable identification, set is_fully_identified to false

- use aliases for alternate names or partial labels seen in the chapter

- if the character might already exist under another name or is too weakly identified, set clarification_required to true and ask a targeted question

- if clarification is not required, still include clarification_reason and clarification_question as empty values

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

Chapter II details the protagonist's awakening from paralysis in a cave, unable to move despite mental clarity. Apache warriors approach but flee in terror from an unseen presence behind the narrator. After regaining movement, the narrator finds their physical body dead and naked while they remain conscious. Fleeing the cave, the narrator gazes at Mars and is pulled through space.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index - Chapter II

## protagonist
- **Asset ID:** protagonist
- **Canonical Character ID:** CH002 Protagonist
- **Aliases:** Narrator, Conscious Entity
- **Is Fully Identified:** false
- **Manual Description Required:** true
- **Manual Description Reason:** The chapter summary provides no physical description of the protagonist's body, appearance, or identity beyond being paralyzed then regaining movement. No stable identification markers exist to support dependable image generation.
- **Clarification Required:** true
- **Clarification Reason:** The character is too weakly identified for reliable later rendering without additional context about their origin, species, or physical form.
- **Clarification Question:** What is the protagonist's physical form and origin? Are they human, alien, or something else?

## apache_warriors
- **Asset ID:** apache_warriors
- **Canonical Character ID:** CH002 Apache Warriors
- **Aliases:** Apache Tribe Members, Approaching Warriors
- **Is Fully Identified:** false
- **Manual Description Required:** true
- **Manual Description Reason:** The chapter summary only describes their action (approaching then fleeing) without any physical description of their appearance, clothing, or distinguishing features. No stable identification markers exist to support dependable image generation.
- **Clarification Required:** true
- **Clarification Reason:** The character group is too weakly identified for reliable later rendering without additional context about their specific appearance, cultural markers, or individual traits.
- **Clarification Question:** What are the Apache warriors' physical appearance and distinguishing features? Are they wearing traditional regalia or modern clothing?

## unseen_presence
- **Asset ID:** unseen_presence
- **Canonical Character ID:** CH002 Unseen Presence
- **Aliases:** Terrifying Entity, Behind Narrator
- **Is Fully Identified:** false
- **Manual Description Required:** true
- **Manual Description Reason:** The chapter summary describes this entity only as an "unseen presence" that causes terror. No physical description exists at all - it is literally unseen. This makes manual description absolutely required for any image generation.
- **Clarification Required:** true
- **Clarification Reason:** An unseen presence cannot be reliably rendered without knowing what form it takes when visible, or if it has a visible form at all. The entity's nature is too ambiguous for dependable image generation.
- **Clarification Question:** Does the unseen presence have a visible form? If so, what does it look like? Is it humanoid, shadowy, energy-based, or something else entirely?

[[/SECTION]]
[[/FILMCREATOR_PACKET]]
````
