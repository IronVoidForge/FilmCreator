# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:11:26.755651+00:00
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
- Sola and other women remodel the gear to fit the protagonist, who then begins training with the Martian youth in the plaza.
- The protagonist observes the social structure: women are the primary manufacturers and educators, while men handle strategy and law.
- Through persistent study, the protagonist masters the Martian language, allowing him to eavesdrop on the adults in his sleeping quarters.
- During a nighttime conversation, the protagonist learns through Sarkoja that the beautiful Red Martian prisoner is being taken to Thark to be executed at the great games rather than held for ransom.
- A heated argument breaksence between Sola and Sarkoja; Sola expresses sympathy for the prisoner and criticizes the constant, senseless bloodshed of Green Martian culture.
- The protagonist resolves to eventually confide in Sola to plan an escape.

**Characters:**
- **The Protagonist:** An Earthman learning Martian combat skills and language; observant and calculating.
- **Sola:** A female Green Martian who is kind to the protagonist and expresses unconventional empathy for the Red prisoner, much to the disapproval of her peers.
- **Sarkoja:** An older, more hardened female Green Martian who reprimands Sola for her "weak" sentiments.
- **The Prisoner:** A beautiful Red Martian woman being transported to Thark for execution.
- **The Women/Young Martians:** The community members providing training and social context.

**Settings:**
- **The Plaza:** Where the protagonist practices combat with the young Martians.
- **The Sleeping Quarters:** A communal living space shared by several females, young Martians, the protagonist, Sola, and Woola the hound.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH009

- [protagonist](#protagonist)
- [sola](#sola)
- [sarkoja](#sarkoja)
- [red_martian_prisoner](#red_martian_prisoner)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance and specific clothing details are not described beyond the fact that he is wearing remodeled Martian warrior gear.

clarification_required: true

clarification_reason: Needs confirmation of physical features to ensure consistency in renders.

clarification_question: What are the protagonist's hair color, eye color, facial structure, and build?

[[SECTION markdown]]

# Protagonist
**Role:** Main Character / Observer

**Status:** Physically Present

**Physical Description:** 
An Earthman currently outfitted in remodeled Martian warrior arms and ornaments. He is undergoing combat training in the plaza.

**Costume/Silhouette:** 
Martian warrior gear, modified by Sola and other women to fit his human frame. Includes various arms (weapons) and ornaments.

**Descriptive Noun Phrases:** 
Earthman in Martian armor, trainee, observant outsider, calculating survivor.

**Uncertainty Notes:** 
Specific facial features and physical build are unknown. The exact appearance of the "remodeled" gear is not detailed.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical traits (hair, eyes, skin tone, height) are provided in the text.

clarification_required: true

clarification_reason: Physical appearance is missing.

clarification_question: What does Sola look like?

[[SECTION markdown]]

# Sola
**Role:** Supporting Character / Ally

**Status:** Physically Present

**Physical Description:** 
A female Green Martian. She is skilled in craftsmanship/remodeling gear and shows empathy toward the Red Martian prisoner.

**Costume/Silhouette:** 
Green Martian attire (implied).

**Descriptive Noun Phrases:** 
Kind Green Martian woman, empathetic artisan, unconventional thinker.

**Uncertainty Notes:** 
No visual details provided regarding her physical appearance or specific clothing style.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH006 Sarkoja

aliases: None

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided.

clarification_required: true

clarification_reason: Physical appearance is missing.

clarification_question: What are Sarkoja's physical characteristics and age indicators?

[[SECTION markdown]]

# Sarkoja
**Role:** Supporting Character / Antagonist (Social)

**Status:** Physically Present

**Physical Description:** 
An older, hardened female Green Martian. She adheres strictly to the cultural norms of her people.

**Costume/Silhouette:** 
Green Martian attire.

**Descriptive Noun Phrases:** 
Hardened elder female, traditionalist Green Martian, stern authority figure.

**Uncertainty Notes:** 
Physical appearance and specific age-related features are not described.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: red_martian_prisoner

canonical_character_id: CH012 Red Martian Prisoner

aliases: The beautiful Red Martian prisoner

is_fully_identified: false

manual_description_required: true

manual_description_reason: Described only as "beautiful," with no specific physical features or color details provided.

clarification_required: true

clarification_reason: Needs visual specifics to distinguish from Green Martians.

clarification_question: What are the specific physical traits that define her beauty and her Red Martian identity?

[[SECTION markdown]]

# Red Martian Prisoner
**Role:** Referenced Character

**Status:** Referenced (Not physically present in this chapter)

**Physical Description:** 
Described as a "beautiful" Red Martian woman. She is currently a prisoner being transported to Thark for execution.

**Costume/Silhouette:** 
Unknown; likely prisoner status.

**Descriptive Noun Phrases:** 
Beautiful Red Martian, doomed prisoner, captive of the Green Martians.

**Uncertainty Notes:** 
Extremely sparse description. No details on hair, eyes, or specific "Red" skin tones/features.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
