# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:51:53.324348+00:00
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

Chapter id: CH004

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

The narrator and Tars Tarkas arrive at a massive, ancient city situated on a table land near a dried sea. The city is populated by hundreds of Green Martians, a violent race characterized by their large size, tusks, and lack of clothing. Upon entering the central plaza, the group meets with the local Chieftain in a magnificent marble hall that appears to have been built by a much older, more advanced race. During an audience, the narrator demonstrates his physical strength through "sak" (jumping) and earns the respect of the warriors by punching a Martian who treated him roughly. Seeking food and water, the narrator is led away by Sola, a female Martian in Tars Tarkas's retinue, to a decorated sleeping chamber where he encounters a strange, ten-legged creature.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

- [Narrator](#narrator)
- [Tars Tarkas](#tars_tarkas)
- [Chieftain](#chieftain)
- [Sola](#sola)
- [Ten-Legged Creature](#ten_legged_creature)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: narrator

canonical_character_id: CH004 Narrator

aliases: Protagonist

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance, species, and clothing are not described.

clarification_required: true

clarification_reason: Identity and physical form are unknown.

clarification_question: What is the narrator's physical appearance, species, and attire?

[[SECTION markdown]]

# Narrator

**Role:** Protagonist / Observer  
**Presence:** Physically present  
**Physical Description:** Demonstrates significant physical strength through jumping ("sak") and combat.  
**Uncertainty Notes:** No visual details regarding species, size, or clothing are provided in this chapter.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH004 Tars Tarkas

aliases: []

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# Tars Tarkas

**Role:** Companion to the narrator  
**Presence:** Physically present  
**Physical Description:** A Green Martian; large-bodied, possessing tusks, and unclothed.  
**Uncertainty Notes:** None beyond general racial traits.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: chieftain

canonical_character_id: CH004 Chieftain

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: No unique physical identifiers provided beyond membership in the Green Martian race.

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# Chieftain

**Role:** Local leader of the city  
**Presence:** Physically present  
**Physical Description:** A Green Martian; large-bodied, possessing tusks, and unclothed.  
**Uncertainty Notes:** No specific individual features or distinguishing marks are mentioned.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: []

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# Sola

**Role:** Member of Tars Tarkas's retinue  
**Presence:** Physically present  
**Physical Description:** A female Green Martian; large-bodied, possessing tusks, and unclothed.  
**Uncertainty Notes:** None beyond general racial traits.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: ten_legged_creature

canonical_character_id: CH004 Ten-Legged Creature

aliases: []

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only the number of legs is known; no other visual information exists.

clarification_required: false

clarification_reason: ""

clarification_question: ""

[[SECTION markdown]]

# Ten-Legged Creature

**Role:** Encountered entity  
**Presence:** Physically present  
**Physical Description:** A strange creature characterized by having ten legs.  
**Uncertainty Notes:** Size, color, texture, and head/body shape are entirely unknown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
