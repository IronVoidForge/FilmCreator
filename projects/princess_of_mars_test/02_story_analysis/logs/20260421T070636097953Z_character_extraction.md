# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:06:36.097953+00:00
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

Chapter id: CH009

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
- The protagonist receives a set of Martian warrior's arms and ornaments from a respectful yet menacing warrior.
- Sola and other women remodel the armor to fit the protagonist's smaller frame.
- The protagonist undergoes intensive combat training in the plaza with Martian youths, guided by Sola.
- Through persistent study, the protagonist masters the Martian language, allowing him to eavesdrop on the adults in his sleeping quarters.
- During a nighttime conversation, the protagonist learns through Sarkoja that the beautiful Red female prisoner is being taken to Thark to be executed in the great games rather than held for ransom.
- Sola expresses her sympathy for the prisoner and her disdain for the constant, senseless bloodshed of Martian life, causing a rift with the other women.
- The protagonist resolves to eventually ask Sola for help in escaping the Green Martians.

**Characters:**
- **The Protagonist:** An Earthman learning Martian combat skills and language; observant and calculating.
- **Sola:** A female Green Martian who shows maternal kindness to the protagonist and expresses empathy for the Red prisoner, despite social pressure to be ruthless.
- **Sarkoja:** An older, more hardened female Martian who reprimands Sola for her "weak" sentiments.
- **The Red Prisoner:** A beautiful captive of the Red Martians whose fate is to die in public games.
- **Other Women/Youths:** Members of the communal living quarters who serve as artisans and combat instructors.

**Settings:**
- **The Plaza:** The training ground where the protagonist practices with weapons.
- **The Sleeping Quarters:** A communal domicile shared by several females, young Martians, the protagonist, Sola, and Woola the hound.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH009

- [protagonist](#protagonist)
- [sola](#sola)
- [sarkoja](#sarkoja)
- [red_prisoner](#red_prisoner)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance and specific clothing/armor details are not described beyond being of a "smaller frame" than the Martian warrior.

clarification_required: true

clarification_reason: Needs confirmation of physical features to ensure consistency in renders.

clarification_question: What is the protagonist's hair color, eye color, and facial structure?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Learner

**Status:** Physically Present

**Physical Description:** 
An Earthman with a smaller frame compared to Martian warriors. He wears remodeled Martian warrior arms and ornaments that have been fitted to his size by Sola and the other women.

**Costume/Silhouette:** 
Modified Martian combat armor; ornamental pieces adapted for a human scale.

**Descriptive Noun Phrases:** 
Small-framed Earthman, learner of Martian arts, armored protagonist.

**Uncertainty Notes:** 
Specific facial features and hair/eye color are not provided in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: Female Green Martian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Mentor / Ally

**Status:** Physically Present

**Physical Description:** 
A female Green Martian. She exhibits maternal kindness and empathy, contrasting with the social norms of her people.

**Costume/Silhouette:** 
Green Martian female attire (implied communal living context).

**Descriptive Noun Phrases:** 
Empathetic Green Martian woman, mentor figure, skilled artisan.

**Uncertainty Notes:** 
Specific visual details regarding skin tone or exact clothing style are not explicitly detailed in this chapter beyond her species and temperament.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH006 Sarkoja

aliases: Older Female Martian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja
**Role:** Antagonist / Social Foil

**Status:** Physically Present

**Physical Description:** 
An older, hardened female Green Martian. She is characterized by a lack of sentimentality and adherence to Martian social norms regarding combat and ruthlessness.

**Costume/Silhouette:** 
Green Martian female attire.

**Descriptive Noun Phrases:** 
Hardened Martian woman, stern elder, traditionalist female.

**Uncertainty Notes:** 
Specific physical features are not detailed beyond her age-related temperament and species.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: red_prisoner

canonical_character_id: CH010 Red Prisoner

aliases: Beautiful Red Female

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is only referenced and described as "beautiful" without specific physical traits.

clarification_required: true

clarification_reason: Needs visual identification for a captive character.

clarification_question: What are the specific physical characteristics of the Red prisoner (hair, skin color, etc.)?

[[SECTION markdown]]

# Red Prisoner
**Role:** Victim / Plot Catalyst

**Status:** Referenced

**Physical Description:** 
Described as a beautiful female of the Red Martians. She is currently a captive.

**Costume/Silhouette:** 
Prisoner status (details unknown).

**Descriptive Noun Phrases:** 
Beautiful Red Martian captive, prisoner of war.

**Uncertainty Notes:** 
No specific physical features are provided other than her beauty and species.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
