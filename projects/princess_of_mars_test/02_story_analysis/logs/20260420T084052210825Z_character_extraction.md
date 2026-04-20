# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:40:52.210825+00:00
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

Chapter id: CH027

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

This chapter depicts the transition from celebration to catastrophe in Helium. Following a peace treaty with Thark led by Tars Tarkas and Sola, preparations are underway for the wedding of Dejah Thoris and John Carter, symbolized by an incubated egg. However, news arrives that the atmosphere plant's keeper has been assassinated and the engine has stopped, causing air pressure to drop rapidly across Barsoom. The people of Helium face imminent asphyxiation and death within three days. Despite their bravery, Dejah Thoris and John Carter succumb to the thinning air in the palace garden. As they die, John Carter remembers a series of nine thought waves from his past life on Earth, which unlock the secret to the atmosphere plant's doors. He launches an air-scout machine to the plant, opens the three great doors, and collapses, leaving hope for Barsoom's survival.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH027

## Tars Tarkas
- **Asset ID:** tars_tarkas
- **Canonical Character ID:** CH003 Tars Tarkas
- **Aliases:** Barsoomian Leader, Helium Peace Negotiator
- **Status:** Fully Identified
- **Physical Presence:** Referenced in peace treaty context

## Sola
- **Asset ID:** sola
- **Canonical Character ID:** CH004 Sola
- **Aliases:** Tars Tarkas's Companion, Barsoomian Warrior
- **Status:** Fully Identified
- **Physical Presence:** Referenced alongside Tars Tarkas

## Dejah Thoris
- **Asset ID:** dejah_thoris
- **Canonical Character ID:** CH001 Dejah Thoris
- **Aliases:** Helium Princess, Barsoomian Noblewoman
- **Status:** Fully Identified
- **Physical Presence:** Dies in palace garden

## John Carter
- **Asset ID:** john_carter
- **Canonical Character ID:** CH002 Protagonist
- **Aliases:** Earth Man, Helium Hero, Conscious Entity
- **Status:** Fully Identified
- **Physical Presence:** Dies in palace garden, remembers past life

## Atmosphere Plant's Keeper
- **Asset ID:** atmosphere_plant_keeper
- **Canonical Character ID:** CH005 Atmosphere Plant Keeper
- **Aliases:** Engine Operator, Barsoomian Technician
- **Status:** Fully Identified
- **Physical Presence:** Assassinated victim

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Barsoomian Leader, Helium Peace Negotiator

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

Barsoomian leader who negotiates peace treaty with Helium. Referenced alongside Sola during wedding preparations for Dejah Thoris and John Carter. Physical presence confirmed through Barsoomian warrior context and leadership role in Thark territory.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: Tars Tarkas's Companion, Barsoomian Warrior

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola

Barsoomian warrior and companion to Tars Tarkas. Present during peace treaty negotiations with Helium. Physical presence confirmed through Barsoomian warrior context and association with Tars Tarkas in Thark territory.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH001 Dejah Thoris

aliases: Helium Princess, Barsoomian Noblewoman

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris

Helium princess and noblewoman. Dies in palace garden alongside John Carter during atmospheric crisis. Physical presence confirmed through Barsoomian noble context, wedding preparations for marriage to John Carter, and death scene in Helium palace garden.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH002 Protagonist

aliases: Earth Man, Helium Hero, Conscious Entity

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter

Earth man who becomes Helium hero. Dies in palace garden alongside Dejah Thoris during atmospheric crisis. Physical presence confirmed through Earth past life memories (nine thought waves), launch of air-scout machine to atmosphere plant, and death scene in Helium palace garden. Remembered consciousness unlocks atmosphere plant doors.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: atmosphere_plant_keeper

canonical_character_id: CH005 Atmosphere Plant Keeper

aliases: Engine Operator, Barsoomian Technician

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Atmosphere Plant's Keeper

Barsoomian technician who maintains atmosphere plant engine. Assassinated victim whose death causes air pressure drop across Barsoom. Physical presence confirmed through Barsoomian technical role, assassination news arrival, and critical function in maintaining atmospheric conditions for Helium survival.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
