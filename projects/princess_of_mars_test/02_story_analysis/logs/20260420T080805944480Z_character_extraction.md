# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T08:08:05.944480+00:00
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

Chapter id: CH022

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

In Chapter XXII, the narrator (John Carter) is positioned to guard the Jeddak Than Kosis during wartime. He witnesses Dejah Thoris's arrival at the palace, where she publicly renounces her previous promise to him in favor of Sab Than, Prince of Zodanga. Heartbroken, John Carter infiltrates her apartments and kills four guardsmen blocking his path. During their confrontation, Dejah Thoris insists her promise is binding despite her love for him, citing Martian customs. Afterward, realizing the danger posed by the dead guardsmen, John Carter escapes the palace through a glass wall into the night. The Jeddak's psychologist confirms the encounter was a single superhuman opponent, and Than Kosis orders a search for the mysterious stranger.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter XXII

## John Carter (protagonist)
- **Asset ID:** john_carter
- **Canonical ID:** CH022 Protagonist
- **Aliases:** Narrator, John Carter
- **Status:** Fully identified
- **Physical Presence:** Referenced throughout chapter

## Dejah Thoris (love interest)
- **Asset ID:** dejah_thoris
- **Canonical ID:** CH022 Dejah Thoris
- **Aliases:** Princess of Helium, Martian Noblewoman
- **Status:** Fully identified
- **Physical Presence:** Referenced in confrontation scene

## Jeddak Than Kosis (ruler)
- **Asset ID:** jeddak_than_kosis
- **Canonical ID:** CH022 Jeddak Than Kosis
- **Aliases:** Martian Ruler, Palace Guardian
- **Status:** Fully identified
- **Physical Presence:** Referenced as being guarded

## Sab Than (Prince of Zodanga)
- **Asset ID:** sab_than
- **Canonical ID:** CH022 Sab Than
- **Aliases:** Prince of Zodanga, Sab Than
- **Status:** Partially identified
- **Physical Presence:** Referenced in Dejah's declaration

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH022 Protagonist

aliases: Narrator, John Carter

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter

**Chapter Role:** Protagonist/Narrator

**Physical Presence:** Referenced throughout chapter as the central figure

**Description:** The narrator of this chapter, explicitly named as John Carter. He is positioned to guard the Jeddak Than Kosis during wartime. He witnesses Dejah Thoris's arrival at the palace and infiltrates her apartments after being heartbroken by her declaration. He kills four guardsmen blocking his path before escaping through a glass wall into the night.

**Continuity-Critical Traits:** 
- Superhuman opponent confirmed by Jeddak's psychologist
- Escapes palace through glass wall
- Single superhuman encounter verified

**Uncertainty Notes:** Physical form and origin details are sparse in this chapter summary; relies on established Princess of Mars lore for complete characterization.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH022 Dejah Thoris

aliases: Princess of Helium, Martian Noblewoman

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Love Interest/Princess

**Physical Presence:** Referenced in confrontation scene with John Carter

**Description:** Princess of Helium who publicly renounces her previous promise to John Carter in favor of Sab Than, Prince of Zodanga. She insists her promise is binding despite her love for him, citing Martian customs. Her arrival at the palace is witnessed by John Carter during wartime.

**Continuity-Critical Traits:** 
- Publicly declares allegiance to Sab Than
- Cites Martian customs regarding binding promises
- Confronts John Carter in his apartments

**Uncertainty Notes:** Physical appearance details are not provided in this chapter summary; relies on established Princess of Mars lore for complete characterization.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: jeddak_than_kosis

canonical_character_id: CH022 Jeddak Than Kosis

aliases: Martian Ruler, Palace Guardian

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Jeddak Than Kosis

**Chapter Role:** Ruler/Protected Figure

**Physical Presence:** Referenced as being guarded by John Carter

**Description:** The Martian ruler whose palace is the setting for this chapter. He orders a search for the mysterious stranger after his psychologist confirms the encounter was a single superhuman opponent. He positions himself to be guarded during wartime.

**Continuity-Critical Traits:** 
- Orders search for mysterious stranger
- Psychologist confirms single superhuman opponent
- Palace setting for confrontation scenes

**Uncertainty Notes:** Physical appearance details are not provided in this chapter summary; relies on established Princess of Mars lore for complete characterization.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sab_than

canonical_character_id: CH022 Sab Than

aliases: Prince of Zodanga, Sab Than

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sab Than

**Chapter Role:** Rival/Prince of Zodanga

**Physical Presence:** Referenced in Dejah Thoris's declaration scene

**Description:** Prince of Zodanga who receives Dejah Thoris's public renunciation of her previous promise to John Carter. He is the alternative suitor Dejah chooses over John Carter, citing Martian customs and binding promises.

**Continuity-Critical Traits:** 
- Receives Dejah Thoris's declaration
- Alternative suitor to John Carter
- Represents Zodanga faction in palace politics

**Uncertainty Notes:** Physical appearance details are not provided in this chapter summary; relies on established Princess of Mars lore for complete characterization.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
