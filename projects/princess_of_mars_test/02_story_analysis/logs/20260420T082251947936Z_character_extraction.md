# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:22:51.947936+00:00
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

Chapter id: CH025

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

Chapter XXV: The Looting of Zodanga. John Carter leads fifty Tharks into the impregnable palace of Zodanga to interrupt a state ceremony where Prince Sab Than is to marry Princess Dejah Thoris. Inside the throne room, Carter shatters the window and attacks the assembly, killing Than Kosis and then Sab Than while defending Dejah Thoris from the guards. With Tars Tarkas's help, they clear the hall. Carter secures Kantos Kan from the dungeons and finds him in a dark recess. After searching for keys to release Kantos Kan, they regroup with Dejah Thoris. In the throne room, amidst the chaos of war outside, Dejah Thoris promises herself to John Carter in marriage.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter XXV: The Looting of Zodanga

## John Carter (Protagonist)
- **Role:** Leader of the assault, defender of Dejah Thoris
- **Status:** Physically present in throne room
- **Description:** Sparse physical detail in source material

## Prince Sab Than (Antagonist)
- **Role:** Groom-to-be at state ceremony
- **Status:** Killed during confrontation
- **Description:** Noble prince, victim of Carter's attack

## Princess Dejah Thoris (Love Interest)
- **Role:** Bride-to-be, defended by Carter
- **Status:** Physically present throughout chapter
- **Description:** Noble princess, promises marriage to Carter

## Than Kosis (Victim)
- **Role:** Attendant at ceremony
- **Status:** Killed during confrontation
- **Description:** Palace attendant, killed in throne room

## Tars Tarkas (Ally)
- **Role:** Helper clearing the hall
- **Status:** Physically present assisting Carter
- **Description:** Creature ally, aids in battle

## Kantos Kan (Prisoner)
- **Role:** Dungeon inmate rescued by Carter
- **Status:** Found in dark recess of dungeons
- **Description:** Prisoner awaiting rescue from dungeons

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# John Carter

**Chapter Role:** Leader of assault on Zodanga palace, defender of Dejah Thoris  
**Physical Presence:** Present in throne room throughout chapter  
**Description:** Sparse physical detail provided in source material. Noble warrior leading fifty Tharks into impregnable palace. Shatters window and attacks assembly during state ceremony. Kills Than Kosis and Sab Than while defending Dejah Thoris from guards. With Tars Tarkas's help, clears the hall. Secures Kantos Kan from dungeons. Finds him in dark recess. Searches for keys to release prisoner.  
**Continuity Traits:** Warrior leader, defender of princess, rescuer of prisoners  
**Uncertainty Notes:** Physical form and origin details sparse in supplied chapter material.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: prince_sab_than

canonical_character_id: CH025 Sab Than

aliases: Groom-to-be, Prince of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Prince Sab Than

**Chapter Role:** Groom-to-be at state ceremony  
**Physical Presence:** Present in throne room until killed  
**Description:** Noble prince of Zodanga, scheduled to marry Princess Dejah Thoris. Killed during Carter's attack on assembly. Victim of confrontation in throne room.  
**Continuity Traits:** Royal groom, palace noble, ceremony participant  
**Uncertainty Notes:** None - physical presence and role clearly established in chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: princess_dejah_thoris

canonical_character_id: CH025 Dejah Thoris

aliases: Bride-to-be, Princess of Zodanga

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Princess Dejah Thoris

**Chapter Role:** Bride-to-be, defended by John Carter  
**Physical Presence:** Present throughout throne room scenes  
**Description:** Noble princess of Zodanga, scheduled to marry Prince Sab Than. Defended by John Carter from guards during attack. In throne room amidst chaos of war outside, promises herself to John Carter in marriage.  
**Continuity Traits:** Royal princess, love interest, bride-to-be, marriage promise recipient  
**Uncertainty Notes:** None - physical presence and role clearly established in chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: than_kosis

canonical_character_id: CH025 Than Kosis

aliases: Attendant, Palace Servant

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Than Kosis

**Chapter Role:** Attendant at state ceremony  
**Physical Presence:** Present in throne room until killed  
**Description:** Palace attendant at Zodanga ceremony. Killed during Carter's attack on assembly in throne room. Victim of confrontation alongside Sab Than.  
**Continuity Traits:** Royal servant, ceremony attendant, victim of attack  
**Uncertainty Notes:** None - physical presence and role clearly established in chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH025 Tars Tarkas

aliases: Creature Ally, Helper

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role:** Helper clearing the hall  
**Physical Presence:** Present assisting Carter in throne room  
**Description:** Creature ally who helps clear the hall during confrontation. Assists John Carter and Dejah Thoris after killing Than Kosis and Sab Than. Helps secure Kantos Kan from dungeons.  
**Continuity Traits:** Creature ally, battle helper, dungeon rescuer  
**Uncertainty Notes:** None - physical presence and role clearly established in chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: kantos_kan

canonical_character_id: CH025 Kantos Kan

aliases: Prisoner, Dungeon Inmate

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Kantos Kan

**Chapter Role:** Dungeon inmate rescued by John Carter  
**Physical Presence:** Found in dark recess of dungeons  
**Description:** Prisoner held in Zodanga dungeons. Found in dark recess after hall is cleared. Search for keys to release prisoner conducted. Regroups with Dejah Thoris after rescue attempt.  
**Continuity Traits:** Dungeon prisoner, rescue target, key recipient  
**Uncertainty Notes:** None - physical presence and role clearly established in chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
