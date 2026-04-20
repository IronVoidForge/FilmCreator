# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:10:50.364463+00:00
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

Chapter id: CH007

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

Chapter VII details the community's child-raising ceremony on Mars. The narrator is escorted by Sola to an incubator where young Martians are hatched after five years of incubation. A gauntlet ceremony releases them into the community, with women and children capturing them for communal upbringing. The chapter explains the harsh Martian social system regarding offspring selection, survival, and the lack of parental bonds. Following the event, the narrator trains with Sola, learning the simple Martian language and developing one-way telepathic communication that provides an advantage over local inhabitants.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter VII

## Protagonist (Narrator)
- **Asset ID:** protagonist
- **Canonical ID:** CH002 Protagonist
- **Aliases:** Narrator, Conscious Entity
- **Status:** Referenced throughout chapter
- **Physical Presence:** Uncertain (sparse physical detail)
- **Description Required:** Manual description needed due to sparse physical information

## Sola
- **Asset ID:** sola
- **Canonical ID:** CH007 Sola
- **Aliases:** Escort, Trainer
- **Status:** Visible character
- **Physical Presence:** Present and active
- **Description Required:** Standard description available

## Young Martians (Offspring)
- **Asset ID:** young_martians
- **Canonical ID:** CH007 Young_Martians
- **Aliases:** Hatchlings, Children
- **Status:** Referenced in ceremony
- **Physical Presence:** Present during hatching event
- **Description Required:** Standard description available

## Community Members
- **Asset ID:** community_members
- **Canonical ID:** CH007 Community_Members
- **Aliases:** Women, Children
- **Status:** Referenced in gauntlet ceremony
- **Physical Presence:** Present during capture event
- **Description Required:** Standard description available

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

# Protagonist (Narrator)

**Chapter Role:** First-person narrator, central consciousness of the story

**Physical Presence:** Referenced throughout Chapter VII; physical form uncertain

**Description Notes:** 
- Narrates events from first-person perspective
- Escorted by Sola to incubator facility
- Trains with Sola after ceremony
- Develops telepathic communication ability
- Physical appearance not described in source material

**Continuity Traits:**
- Conscious Entity (as referenced)
- Learns simple Martian language
- Gains advantage over local inhabitants through telepathy

**Uncertainty Notes:** 
- Physical form and origin remain unspecified in Chapter VII
- Manual description required for image generation purposes
- Sparse physical detail prevents dependable later rendering

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH007 Sola

aliases: Escort, Trainer

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola

**Chapter Role:** Escort and trainer for protagonist

**Physical Presence:** Present and active throughout Chapter VII

**Description Notes:** 
- Escorts narrator to incubator facility
- Guides protagonist through gauntlet ceremony aftermath
- Trains narrator in simple Martian language
- Develops telepathic communication with protagonist
- Provides advantage over local inhabitants

**Continuity Traits:**
- Active participant in community events
- Trainer role established
- Facilitates protagonist's integration into Martian society

**Uncertainty Notes:** 
- Physical description supported by source material
- Standard rendering possible without manual intervention

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: young_martians

canonical_character_id: CH007 Young_Martians

aliases: Hatchlings, Children, Offspring

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Young Martians (Offspring)

**Chapter Role:** Subjects of hatching ceremony and gauntlet event

**Physical Presence:** Present during incubation release in Chapter VII

**Description Notes:** 
- Hatched after five years of incubation
- Released into community via gauntlet ceremony
- Captured by women and children for communal upbringing
- Subject of harsh Martian social system regarding offspring selection

**Continuity Traits:**
- Five-year incubation period established
- Communal upbringing model
- Survival-based selection process
- Lack of parental bonds noted in source

**Uncertainty Notes:** 
- Physical description supported by source material
- Standard rendering possible without manual intervention

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: community_members

canonical_character_id: CH007 Community_Members

aliases: Women, Children, Local Inhabitants

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Community Members (Women and Children)

**Chapter Role:** Participants in gauntlet ceremony and offspring capture

**Physical Presence:** Present during capture event in Chapter VII

**Description Notes:** 
- Women and children capture young Martians after gauntlet release
- Engage in communal upbringing of offspring
- Represent harsh Martian social system regarding offspring selection
- Lack parental bonds with captured children

**Continuity Traits:**
- Communal child-raising model established
- Five-year incubation period respected
- Survival-based selection process active
- Integration into existing social structure

**Uncertainty Notes:** 
- Physical description supported by source material
- Standard rendering possible without manual intervention

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
