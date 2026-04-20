# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:52:42.404843+00:00
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

In Chapter II, titled "The Escape of the Dead," the narrator wakes up paralyzed in a cave, unable to move despite being mentally alert. He observes approaching Apache warriors who are initially cautious but then flee in terror from an unseen horror behind him. After regaining his physical form and realizing he is naked and unarmed, he escapes the cave into the Arizona night. From the ledge, he gazes at the moonlit landscape and spots a red star, Mars, which fascinates him. Overpowered by its pull, he feels himself drawn through space, ending in darkness and cold.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter II

## Protagonist
- **Role:** Narrator/Conscious Entity
- **Status:** Referenced, physically present (paralyzed then regaining form)
- **Description:** Wakes up paralyzed in a cave, observes Apache warriors, escapes into Arizona night, drawn to Mars. Physical details sparse (naked, unarmed).

## Apache Warriors
- **Role:** Approaching threat
- **Status:** Referenced, physically present (cautious then fleeing)
- **Description:** Group of Apache warriors who initially approach cautiously but flee in terror from unseen horror behind protagonist.

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

**Chapter Role:** Narrator/Conscious Entity  
**Physical Presence:** Referenced, physically present (paralyzed then regaining form)  
**Description:** Wakes up paralyzed in a cave, mentally alert but unable to move. Observes approaching Apache warriors who initially approach cautiously but flee in terror from unseen horror behind protagonist. Regains physical form and realizes he is naked and unarmed. Escapes the cave into Arizona night. From ledge, gazes at moonlit landscape and spots red star Mars which fascinates him. Overpowered by its pull, feels himself drawn through space ending in darkness and cold.  
**Physical Details:** Sparse - described as naked, unarmed, paralyzed then regaining form. No ornate physical description provided.  
**Costume/Silhouette:** Unknown - no costume details available. Continuity-critical trait: transition from paralyzed state to mobile state.  
**Uncertainty Notes:** Physical form and origin unclear. Needs clarification for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH002 Apache Warriors

aliases: Apache, Warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: No detailed physical description in source.

clarification_required: false

clarification_reason: 

clarification_question: 



[[SECTION markdown]]

# Apache Warriors

**Chapter Role:** Approaching threat  
**Physical Presence:** Referenced, physically present (cautious then fleeing)  
**Description:** Group of Apache warriors who initially approach protagonist cautiously but flee in terror from unseen horror behind him. No individual names or detailed descriptions provided.  
**Physical Details:** Sparse - no ornate physical description available. Only group behavior noted (cautious approach, fearful retreat).  
**Costume/Silhouette:** Unknown - no costume details available. Continuity-critical trait: collective fear response to unseen threat.  
**Uncertainty Notes:** Individual warriors not distinguished. Group character only. No detailed visual information for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



[[FILMCREATOR_PACKET]]
````
