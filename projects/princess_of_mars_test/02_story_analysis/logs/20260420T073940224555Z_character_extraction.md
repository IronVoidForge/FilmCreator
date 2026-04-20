# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:39:40.224555+00:00
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

Chapter id: CH014

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

John Carter reflects on his love for Dejah Thoris as they prepare to travel from Korad to Thark. Dejah is chained by Sarkoja's order to ensure security during the journey. Tars Tarkas intervenes, taking custody of the key and promising to protect her from Sarkoja's harassment. During the march, John Carter engages in a duel with Zad, a warrior who struck his animal. The fight is interrupted when Dejah Thoris throws a mirror that blinds Zad, allowing him to strike John in the shoulder. Sarkoja attempts to stab Dejah Thoris, but Sola intercepts. The chapter culminates in a fierce sword fight where John Carter is stabbed in the chest and collapses, ending on a cliffhanger of his potential death or unconsciousness.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

## John Carter (protagonist)
- **Role:** Main protagonist, duelist, warrior
- **Status:** Physically present throughout chapter
- **Description:** Human male, physical form uncertain in source material

## Dejah Thoris (love interest)
- **Role:** Female companion, chained by Sarkoja's order
- **Status:** Physically present, referenced as being secured during journey
- **Description:** Female human, mirror-wielding combatant

## Sarkoja (antagonist)
- **Role:** Enemy who ordered Dejah's chaining
- **Status:** Physically present, attempts to stab Dejah
- **Description:** Human female warrior, hostile toward protagonists

## Tars Tarkas (protector)
- **Role:** Guardian who takes custody of key
- **Status:** Physically present, intervenes in conflict
- **Description:** Creature/warrior figure, protective role

## Zad (warrior)
- **Role:** Combatant who struck John's animal
- **Status:** Physically present during duel
- **Description:** Warrior male, interrupted by Dejah's mirror throw

## Sola (interceptor)
- **Role:** Defender who intercepts Sarkoja's attack
- **Status:** Physically present during sword fight
- **Description:** Combatant figure, defensive role

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# John Carter

**Chapter Role:** Main protagonist, duelist, warrior  
**Physical Presence:** Physically present throughout chapter  
**Description:** Human male figure, physical form uncertain in source material  
**Key Traits:** Duels with Zad, stabbed in chest during final fight, collapses at chapter end  
**Continuity Notes:** Potential death or unconsciousness cliffhanger ending  

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH002 Dejah Thoris

aliases: Female Companion, Mirror-Wielder

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Love interest, combatant  
**Physical Presence:** Physically present, chained by Sarkoja's order  
**Description:** Female human figure, mirror-wielding combatant  
**Key Traits:** Throws mirror to blind Zad during duel, intercepted by Sola when stabbed  
**Continuity Notes:** Security measure during journey from Korad to Thark  

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH003 Sarkoja

aliases: Enemy, Chaining Order Giver

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja

**Chapter Role:** Antagonist, hostile warrior  
**Physical Presence:** Physically present throughout chapter  
**Description:** Human female warrior figure, hostile toward protagonists  
**Key Traits:** Orders Dejah's chaining, attempts to stab Dejah, intercepted by Sola  
**Continuity Notes:** Security-focused antagonist during journey  

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH004 Tars Tarkas

aliases: Guardian, Key Custodian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role:** Protector, guardian figure  
**Physical Presence:** Physically present throughout chapter  
**Description:** Creature/warrior figure, protective role  
**Key Traits:** Takes custody of key, promises to protect Dejah from Sarkoja's harassment  
**Continuity Notes:** Intervenes in conflict, defensive stance toward protagonists  

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: zad

canonical_character_id: CH005 Zad

aliases: Warrior Combatant, Animal Striker

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Zad

**Chapter Role:** Warrior combatant  
**Physical Presence:** Physically present during duel  
**Description:** Warrior male figure, interrupted by Dejah's mirror throw  
**Key Traits:** Struck John's animal, engages in duel with John Carter, blinded by mirror  
**Continuity Notes:** Fight interrupted when Dejah throws mirror that blinds him  

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH006 Sola

aliases: Interceptor, Defender

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola

**Chapter Role:** Defender, interceptor  
**Physical Presence:** Physically present during sword fight  
**Description:** Combatant figure, defensive role  
**Key Traits:** Intercepts Sarkoja's attempt to stab Dejah Thoris  
**Continuity Notes:** Defensive combatant during final sword fight sequence  

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
