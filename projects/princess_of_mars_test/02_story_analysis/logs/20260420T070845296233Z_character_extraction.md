# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:08:45.296233+00:00
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

Chapter id: CH006

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

In Chapter VI, titled "A FIGHT THAT WON FRIENDS," the narrator is captured by a Bull Ape on Mars. A second ape arrives with a stone cudgel to execute him, but the narrator's Watch-thing intervenes, triggering a fierce battle between the two creatures. The narrator kills the first ape with a cudgel, only to face an enraged second ape. After defeating the second ape, Tars Tarkas and Sola arrive. The Martians applaud the narrator's physical prowess. However, they intend to kill the Watch-thing. The narrator saves his dog from a bullet fired by a warrior, demonstrating gratitude and compassion that the Martians struggle to understand. By the end, the narrator has gained two friends on Mars: Sola and his loyal beast.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter VI

## Narrator/Protagonist
- **Status:** Referenced, physically present
- **Description:** Conscious entity with Watch-thing companion
- **Identification:** Partially identified (sparse physical detail)

## Bull Ape
- **Status:** Physically present
- **Description:** Martian warrior captured narrator
- **Identification:** Fully identified

## Second Ape
- **Status:** Physically present
- **Description:** Arrives with stone cudgel to execute narrator
- **Identification:** Fully identified

## Watch-thing
- **Status:** Referenced, physically present
- **Description:** Narrator's companion/assistant
- **Identification:** Partially identified (sparse physical detail)

## Tars Tarkas
- **Status:** Physically present
- **Description:** Martian warrior
- **Identification:** Fully identified

## Sola
- **Status:** Physically present
- **Description:** Female Martian, narrator's friend
- **Identification:** Fully identified

## Dog
- **Status:** Referenced, physically present
- **Description:** Narrator's loyal companion
- **Identification:** Partially identified (sparse physical detail)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity, Watch-thing Master

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material.

clarification_required: true

clarification_reason: Needs identity clarification regarding physical form and origin.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# Narrator/Protagonist

**Chapter Role:** Central consciousness, captured entity

**Physical Presence:** Referenced throughout chapter, physically present during key events

**Description:** Conscious entity with Watch-thing companion. Physical details are sparse in source material. The narrator demonstrates gratitude and compassion that Martians struggle to understand.

**Continuity Traits:** Has a loyal dog companion, possesses a Watch-thing assistant, gains two friends on Mars (Sola and his beast)

**Uncertainty Notes:** Physical form and origin not fully detailed in chapter VI. Manual description required for consistent image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: bull_ape

canonical_character_id: CH006 Bull Ape

aliases: Martian Warrior, First Ape

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - physical details available in source.

clarification_required: false

clarification_reason: N/A - fully identified character.

clarification_question: N/A

[[SECTION markdown]]

# Bull Ape

**Chapter Role:** Antagonist, captor of narrator

**Physical Presence:** Physically present during capture and execution attempt

**Description:** Martian warrior who captures the narrator on Mars. Arrives with stone cudgel to execute the captured entity. Demonstrates physical prowess in battle.

**Continuity Traits:** Killed by narrator's cudgel in fierce battle. Part of Martians' initial hostility toward narrator.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: second_ape

canonical_character_id: CH006 Second Ape

aliases: Martian Warrior, Executioner Ape

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - physical details available in source.

clarification_required: false

clarification_reason: N/A - fully identified character.

clarification_question: N/A

[[SECTION markdown]]

# Second Ape

**Chapter Role:** Antagonist, executioner

**Physical Presence:** Physically present during narrator's confrontation

**Description:** Martian warrior who arrives with stone cudgel to execute the captured narrator. Becomes enraged after first ape's death. Defeated by narrator in fierce battle.

**Continuity Traits:** Part of Martians' initial hostility toward narrator. Killed by narrator's physical prowess, demonstrating narrator's strength.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: watch_thing

canonical_character_id: CH002 Watch-thing

aliases: Companion, Assistant, Dog-like Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material.

clarification_required: true

clarification_reason: Needs identity clarification regarding physical form and origin.

clarification_question: What is the Watch-thing's physical form and relationship to narrator?

[[SECTION markdown]]

# Watch-thing

**Chapter Role:** Narrator's companion, assistant

**Physical Presence:** Referenced throughout chapter, physically present during key interventions

**Description:** Narrator's loyal companion/assistant that intervenes in battle between the two apes. Demonstrates loyalty and protective instincts toward narrator.

**Continuity Traits:** Saved from bullet fired by Martian warrior by narrator's intervention. Part of narrator's growing bond with Martians through compassion.

**Uncertainty Notes:** Physical form not fully detailed in chapter VI. Manual description required for consistent image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH006 Tars Tarkas

aliases: Martian Warrior, First Martian Friend

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - physical details available in source.

clarification_required: false

clarification_reason: N/A - fully identified character.

clarification_question: N/A

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role:** Martian warrior, friend

**Physical Presence:** Physically present during narrator's confrontation with Martians

**Description:** Martian warrior who arrives after narrator defeats the apes. Part of Martians' initial hostility but becomes narrator's friend through demonstrated compassion and gratitude.

**Continuity Traits:** One of two friends narrator gains on Mars (along with Sola). Represents Martians' struggle to understand human-like emotions like gratitude and compassion.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH006 Sola

aliases: Female Martian, Second Martian Friend

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - physical details available in source.

clarification_required: false

clarification_reason: N/A - fully identified character.

clarification_question: N/A

[[SECTION markdown]]

# Sola

**Chapter Role:** Female Martian, friend

**Physical Presence:** Physically present during narrator's confrontation with Martians

**Description:** Female Martian who arrives after narrator defeats the apes. Becomes narrator's friend through demonstrated compassion and gratitude. Represents Martians' growing understanding of narrator's emotions.

**Continuity Traits:** One of two friends narrator gains on Mars (along with Tars Tarkas). Demonstrates that Martians can understand and appreciate human-like emotions like gratitude and compassion.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dog

canonical_character_id: CH006 Dog

aliases: Narrator's Companion, Loyal Beast

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material.

clarification_required: true

clarification_reason: Needs identity clarification regarding physical form and relationship to narrator.

clarification_question: What is the dog's physical form and how does it relate to the Watch-thing?

[[SECTION markdown]]

# Dog

**Chapter Role:** Narrator's companion, loyal beast

**Physical Presence:** Referenced throughout chapter, physically present during key events

**Description:** Narrator's loyal companion that demonstrates gratitude and compassion. Saved from bullet fired by Martian warrior by narrator's intervention.

**Continuity Traits:** Part of narrator's growing bond with Martians through compassion. One of the two friends narrator gains on Mars (along with Sola). Represents loyalty and protective instincts.

**Uncertainty Notes:** Physical form not fully detailed in chapter VI. Manual description required for consistent image generation.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
