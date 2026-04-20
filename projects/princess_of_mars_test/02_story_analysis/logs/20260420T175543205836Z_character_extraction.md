# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:55:43.205836+00:00
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

Chapter id: CH012

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
John Carter is summoned to an audience with Lorquas Ptomel, a Tharkian leader. Ptomel confronts Carter regarding his status as a prisoner who nonetheless commands respect, and accuses him of plotting an escape with Dejah Thoris (the "red girl"). Ptomel warns that while they do not wish to fight among themselves, Carter will be killed if he attempts to escape or attacks a Thark in self-defense. Carter realizes that Sarkoja, a powerful female figure, has been spying on him and reporting his intentions to undermine him.

Following the audience, Tars Tarkas approaches Carter and offers him quarters within the Tharkian buildings. Carter selects a room on the third floor of an adjoining building to remain close to Dejah Thoris. He receives his spoils of war—weapons, silks, furs, and food—from the retinues of the two chieftains he previously defeated. Carter also takes responsibility for the women and youths belonging to those fallen chieftains, assigning them duties within his new quarters.

**Characters:**
* **John Carter:** A Tharkian chieftain and human; increasingly focused on escaping with Dejah Thoris.
* **Lorquas Ptomel:** A fierce Tharkian leader who issues a formal warning to Carter regarding escape and combat.
* **Sarkoja:** Mentioned as a powerful female influence behind Tars Tarkas, suspected of betraying Carter.
* **Tars Tarkas:** A Tharkian warrior who treats Carter with respect and assists him in settling into his new quarters.
* **Dejah Thoris:** The captive red Martian princess; the primary motivation for Carter's escape plans.

**Settings:**
* **The Audience Chamber:** Where Lorquas Ptomel delivers his warning.
* **The Tharkian Plaza/Buildings:** A complex of structures featuring winding corridors, multi-story apartments, and an overgrown central court filled with fountains and statuary. The setting reflects a once-beautiful civilization now characterized by martial austerity.
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
- [Lorquas Ptomel](#lorquas_ptomel)
- [Sarkoja](#sarkoja)
- [Tars Tarkas](#tars_tarkas)
- [Dejah Thoris](#dejah_thoris)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Human, Tharkian chieftain

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance (height, build, facial features) is not detailed in this chapter.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Tharkian Chieftain

**Status:** Physically Present

**Physical Description:** 
A human man living among the Tharks. Specific physical traits (height, hair color, eye color) are not provided in this text.

**Costume/Silhouette:** 
Currently in possession of spoils of war including silks and furs.

**Prompt Phrases:** 
Human male, martial attire, silk and fur garments, Tharkian chieftain.

**Uncertainty Notes:** 
Physical appearance is entirely unstated in this chapter; requires baseline character model reference.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH012 Lorquas Ptomel

aliases: Tharkian leader

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is described as a "fierce Tharkian leader" but lacks specific physical or anatomical details.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** Antagonistic Leader

**Status:** Physically Present

**Physical Description:** 
A fierce Tharkian leader. Specific anatomical details of the Thark species are not provided in this text.

**Costume/Silhouette:** 
Tharkian martial attire.

**Prompt Phrases:** 
Fierce Tharkian, warrior leader, martial silhouette.

**Uncertainty Notes:** 
Specific physical features and Tharkian anatomy must be defined by series standard.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH012 Sarkoja

aliases: Powerful female figure

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described only as a "powerful female figure" with no physical or visual details.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja
**Role:** Spy / Manipulator

**Status:** Referenced

**Physical Description:** 
A powerful female figure within the Tharkian hierarchy. No visual details provided.

**Costume/Silhouette:** 
Unknown.

**Prompt Phrases:** 
Powerful female Thark, influential figure.

**Uncertainty Notes:** 
Character is only mentioned as a source of intelligence/betrayal; no physical presence in this chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH012 Tars Tarkas

aliases: Tharkian warrior

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is identified as a Tharkian warrior but lacks specific physical descriptions.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Ally / Warrior

**Status:** Physically Present

**Physical Description:** 
A Tharkian warrior. Specific anatomical details are not provided in this text.

**Costume/Silhouette:** 
Tharkian warrior attire.

**Prompt Phrases:** 
Tharkian warrior, martial presence, respected leader.

**Uncertainty Notes:** 
Requires species-specific anatomical definition for Tharks.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH012 Dejah Thoris

aliases: Red girl, Martian princess

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described as a "red girl" and "princess," but lacks specific facial features or detailed costume.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Captive Princess / Motivation

**Status:** Referenced

**Physical Description:** 
Described as a "red girl" and a Martian princess.

**Costume/Silhouette:** 
Unknown (currently captive).

**Prompt Phrases:** 
Red-skinned female, Martian princess, captive.

**Uncertainty Notes:** 
"Red girl" likely refers to skin tone or hair; requires clarification on specific shade and facial features.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
