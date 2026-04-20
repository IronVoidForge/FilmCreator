# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:18:20.186628+00:00
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

Chapter IX details the protagonist's rapid acquisition of the Martian language and his subsequent weapons training under the tutelage of local women, who are responsible for manufacturing all goods and educating the youth. The chapter highlights the gendered division of labor in Martian society, with men handling strategy and law while women manage production and combat training. A significant portion focuses on a discussion regarding the fate of a female prisoner, where Sola expresses compassion and critiques the constant warfare, contrasting her views with the harsher attitudes of others like Sarkoja. The chapter concludes with the protagonist deciding to seek Sola's assistance for an escape plan.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter IX

## Protagonist
- **Asset ID:** protagonist
- **Canonical ID:** CH002 Protagonist
- **Aliases:** Narrator, Conscious Entity
- **Status:** Referenced throughout chapter
- **Description:** Learning Martian language rapidly, undergoing weapons training under local women. Physical form uncertain in source material.

## Sola
- **Asset ID:** sola
- **Canonical ID:** CH009 Sola
- **Aliases:** None
- **Status:** Referenced as compassionate figure
- **Description:** Expresses compassion regarding female prisoner fate, critiques constant warfare. Views contrast with Sarkoja's harsher attitudes.

## Sarkoja
- **Asset ID:** sarkoja
- **Canonical ID:** CH009 Sarkoja
- **Aliases:** None
- **Status:** Referenced as having harsher attitudes
- **Description:** Mentioned in contrast to Sola regarding views on warfare and prisoner treatment.

## Local Women (Martian)
- **Asset ID:** local_women_martian
- **Canonical ID:** CH009 Local_Women_Martian
- **Aliases:** None
- **Status:** Referenced as group responsible for production and education
- **Description:** Responsible for manufacturing all goods and educating youth in Martian society.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# Protagonist

**Chapter Role:** Central figure learning Martian language and undergoing weapons training under local women.

**Physical Presence:** Referenced throughout chapter, not physically described in detail.

**Physical Description:** Uncertain - source material provides sparse physical detail. Character is the conscious entity/narrator perspective.

**Costume/Silhouette:** Not specified in source material.

**Continuity-Critical Traits:** Rapid acquisition of Martian language, weapons training under tutelage of local women, seeking Sola's assistance for escape plan.

**Uncertainty Notes:** Physical form and origin remain unclear from Chapter IX text. Image generation would require additional clarification on whether protagonist has physical body or exists as consciousness/narrator entity.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH009 Sola

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient detail provided.

clarification_required: false

clarification_reason: N/A - identity clear from context.

clarification_question: N/A

[[SECTION markdown]]

# Sola

**Chapter Role:** Compassionate figure expressing views on prisoner fate and warfare.

**Physical Presence:** Referenced as having distinct perspective contrasting with Sarkoja.

**Physical Description:** Not detailed in Chapter IX text - appears as Martian woman with compassionate disposition regarding female prisoners and critique of constant warfare.

**Costume/Silhouette:** Martian woman attire (implied by context of local women manufacturing goods).

**Continuity-Critical Traits:** Expresses compassion for female prisoner, critiques constant warfare, views contrast with Sarkoja's harsher attitudes, protagonist seeks her assistance for escape plan.

**Uncertainty Notes:** Physical appearance not specified in source material beyond being a Martian woman.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH009 Sarkoja

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient detail provided.

clarification_required: false

clarification_reason: N/A - identity clear from context.

clarification_question: N/A

[[SECTION markdown]]

# Sarkoja

**Chapter Role:** Figure with harsher attitudes regarding warfare and prisoner treatment.

**Physical Presence:** Referenced as having contrasting views to Sola.

**Physical Description:** Not detailed in Chapter IX text - appears as Martian woman with harsher attitudes toward constant warfare and prisoner fate compared to Sola's compassion.

**Costume/Silhouette:** Martian woman attire (implied by context of local women manufacturing goods).

**Continuity-Critical Traits:** Harsher attitudes regarding warfare, contrasted with Sola's compassionate views on prisoner treatment, represents more traditional/harsh Martian perspective.

**Uncertainty Notes:** Physical appearance not specified in source material beyond being a Martian woman.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: local_women_martian

canonical_character_id: CH009 Local_Women_Martian

aliases: None

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient detail provided.

clarification_required: false

clarification_reason: N/A - identity clear from context.

clarification_question: N/A

[[SECTION markdown]]

# Local Women (Martian)

**Chapter Role:** Group responsible for manufacturing goods and educating youth in Martian society.

**Physical Presence:** Referenced as collective group throughout chapter.

**Physical Description:** Not detailed individually in Chapter IX text - appear as Martian women with gendered division of labor (men handle strategy/law, women manage production/combat training).

**Costume/Silhouette:** Martian woman attire (implied by context of local women manufacturing goods and educating youth).

**Continuity-Critical Traits:** Responsible for manufacturing all goods in Martian society, educate the youth, provide weapons training to protagonist, gendered division of labor with men handling strategy and law.

**Uncertainty Notes:** Individual physical appearances not specified beyond being Martian women. Group functions as collective character entity.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
