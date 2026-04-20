# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:56:15.258756+00:00
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

Chapter id: CH018

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

# Chapter 18 Summary: CHAINED IN WARHOON

## Major Events
- Narrator regains consciousness after capture, discovering he is alive among Warhoon warriors
- Dak Kova (the jed who captured him) reveals plans to use narrator as sport for the great games
- Narrator is strapped to a wild thoat and pursued after the main column toward Warhoon
- Upon reaching Warhoon camp, narrator is taken before Bar Comas, young jeddak of Warhoon
- Dak Kova displays insubordination toward Bar Comas, leading to brutal hand-to-hand combat
- Bar Comas wins but is killed by Dak Kova, who then assumes title of Jeddak of Warhoon
- Expedition abandoned until after great games; ten thousand warriors turn back toward Warhoon
- Narrator imprisoned in dark dungeon, chained to floor and walls for indeterminate period
- Narrator kills his jailer with a chain, retrieves keys from dead man's neck
- Six pairs of eyes watch narrator retreat into darkness as he gains freedom

## Characters Introduced
- **Dak Kova**: The jed who captured the narrator, now Jeddak of Warhoon after killing Bar Comas
- **Bar Comas**: Young jeddak of Warhoon, killed by Dak Kova in a brutal fight
- **Ancient Female Warrior**: Attends to narrator's wounds, reveals therapeutic skills
- **Narrator**: Captured outsider experiencing captivity and eventual escape

## Settings
- Small room with sleeping silks and furs (initial capture location)
- Warhoon camp where main column makes night stop
- Dark dungeon in city of Warhoon, filled with creeping things and fiery eyes

## Key Themes
- Brutality of Warhoon culture (more ferocious than Tharks despite smaller horde)
- Power struggles within warrior societies
- Narrator's resilience and cunning in captivity
- Horror of darkness and unseen threats
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter 18

| Asset ID | Canonical Character ID | Aliases | Fully Identified | Description Required | Reason |
|----------|------------------------|---------|------------------|----------------------|--------|
| dak_kova | CH003 Dak Kova | Jeddak of Warhoon, The Jed | false | true | Sparse physical detail |
| bar_comas | CH004 Bar Comas | Young Jeddak | false | true | Sparse physical detail |
| ancient_female_warrior | CH005 Ancient Female Warrior | - | false | true | Sparse physical detail |
| narrator | CH002 Narrator | Captured Outsider, Conscious Entity | false | true | Sparse physical detail |

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dak_kova

canonical_character_id: CH003 Dak Kova

aliases: Jeddak of Warhoon, The Jed

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is Dak Kova's physical form and origin?

[[SECTION markdown]]

# Dak Kova

**Chapter Role**: The jed who captured the narrator, now Jeddak of Warhoon after killing Bar Comas

**Physical Presence**: Referenced throughout chapter

**Physical Description**: Not specified in source material

**Costume/Silhouette**: Unknown - no visual details provided

**Continuity-Critical Traits**: 
- Killed Bar Comas in brutal hand-to-hand combat
- Assumes title of Jeddak of Warhoon
- Displays insubordination toward Bar Comas initially
- Imprisoned narrator in dark dungeon before assuming power

**Uncertainty Notes**: Physical appearance and origin are not described in the supplied chapter material. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: bar_comas

canonical_character_id: CH004 Bar Comas

aliases: Young Jeddak

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is Bar Comas's physical form and origin?

[[SECTION markdown]]

# Bar Comas

**Chapter Role**: Young jeddak of Warhoon, killed by Dak Kova in a brutal fight

**Physical Presence**: Referenced throughout chapter

**Physical Description**: Not specified in source material

**Costume/Silhouette**: Unknown - no visual details provided

**Continuity-Critical Traits**: 
- Young jeddak of Warhoon
- Killed by Dak Kova in hand-to-hand combat
- Subject of insubordination display from Dak Kova
- Death leads to Dak Kova assuming title of Jeddak

**Uncertainty Notes**: Physical appearance and origin are not described in the supplied chapter material. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ancient_female_warrior

canonical_character_id: CH005 Ancient Female Warrior

aliases: -

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the ancient female warrior's physical form and origin?

[[SECTION markdown]]

# Ancient Female Warrior

**Chapter Role**: Attends to narrator's wounds, reveals therapeutic skills

**Physical Presence**: Referenced throughout chapter

**Physical Description**: Not specified in source material

**Costume/Silhouette**: Unknown - no visual details provided

**Continuity-Critical Traits**: 
- Attends to narrator's wounds
- Reveals therapeutic skills
- Part of Warhoon warrior society

**Uncertainty Notes**: Physical appearance and origin are not described in the supplied chapter material. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH002 Narrator

aliases: Captured Outsider, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the narrator's physical form and origin?

[[SECTION markdown]]

# Narrator

**Chapter Role**: Captured outsider experiencing captivity and eventual escape

**Physical Presence**: Referenced throughout chapter

**Physical Description**: Not specified in source material

**Costume/Silhouette**: Unknown - no visual details provided

**Continuity-Critical Traits**: 
- Regains consciousness after capture
- Discovers he is alive among Warhoon warriors
- Strapped to wild thoat and pursued toward Warhoon
- Taken before Bar Comas, then imprisoned in dark dungeon
- Kills jailer with chain, retrieves keys from dead man's neck
- Six pairs of eyes watch narrator retreat into darkness

**Uncertainty Notes**: Physical appearance and origin are not described in the supplied chapter material. Manual description required for later image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
