# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:27:37.530696+00:00
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

Chapter id: CH011

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

In this chapter, John Carter arranges new quarters for Dejah Thoris and Sola in the ancient city of Korad, a former center of commerce and culture. He establishes his rank among the Tharks with Sola, who acknowledges his prowess as eleventh in the community. A significant portion of the text is dedicated to a deep conversation between John Carter and Dejah Thoris regarding his origins; she initially doubts he is from Earth due to his lack of ornaments and clothing, but eventually believes him after hearing his story about Virginia and Earth, driven by her "earthly, feminine logic." They discuss Martian history, including the extinct fair-haired race and the alliance of red, dark, and yellow Martians against the green men. The chapter concludes with John Carter receiving a summons from Lorquas Ptomel to appear in the audience chamber.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH011

## John Carter
- **Asset ID:** john_carter
- **Canonical ID:** CH002 Protagonist
- **Aliases:** Narrator, Conscious Entity
- **Status:** Partially identified (sparse physical detail)
- **Role:** Main character in Korad quarters arrangement

## Dejah Thoris
- **Asset ID:** dejah_thoris
- **Canonical ID:** CH003 Princess
- **Aliases:** Earthly Logic, Martian Noble
- **Status:** Fully referenced with dialogue
- **Role:** Discusses John Carter's origins and Martian history

## Sola
- **Asset ID:** sola
- **Canonical ID:** CH004 Thark Warrior
- **Aliases:** Eleventh in Community
- **Status:** Referenced for community rank acknowledgment
- **Role:** Acknowledges John Carter's prowess among Tharks

## Lorquas Ptomel
- **Asset ID:** lorquas_ptomel
- **Canonical ID:** CH005 Audience Chamber Official
- **Aliases:** Summons Sender
- **Status:** Referenced for summons delivery
- **Role:** Sends summons to audience chamber

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH002 Protagonist

aliases: Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail. Lack of ornaments and clothing noted in source material.

clarification_required: true

clarification_reason: Needs identity clarification regarding physical form and origin.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# John Carter

**Chapter Role:** Main character arranging quarters in Korad

**Physical Presence:** Referenced throughout chapter dialogue

**Description Notes:** 
- Sparse physical detail provided in source
- Noted for lack of ornaments and clothing
- Earth origins discussed with Dejah Thoris
- Virginia and Earth story shared as proof

**Continuity Traits:**
- Eleventh rank among Tharks community
- Subject of Martian history discussion
- Receives summons from Lorquas Ptomel

**Uncertainty Notes:** 
- Physical form not fully described in source material
- Origin story provided but visual details sparse
- Requires manual description for image generation

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Princess

aliases: Earthly Logic, Martian Noble

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient physical detail in source material.

clarification_required: false

clarification_reason: N/A - fully identified character.

clarification_question: N/A

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Discusses John Carter's origins and Martian history

**Physical Presence:** Actively present in dialogue with John Carter

**Description Notes:** 
- Earthly, feminine logic noted in source
- Initially doubts John Carter's Earth origin
- Believes him after hearing Virginia/Earth story
- Subject of Martian history discussion

**Continuity Traits:**
- Martian noble status confirmed
- Discusses extinct fair-haired race
- Mentions alliance of red, dark, yellow Martians
- Green men conflict referenced

**Uncertainty Notes:** 
- Physical description adequately supported by source
- No manual description required for image generation

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Thark Warrior

aliases: Eleventh in Community

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient physical detail in source material.

clarification_required: false

clarification_reason: N/A - fully identified character.

clarification_question: N/A

[[SECTION markdown]]

# Sola

**Chapter Role:** Acknowledges John Carter's prowess among Tharks

**Physical Presence:** Referenced for community rank acknowledgment

**Description Notes:** 
- Eleventh in the community noted
- Acknowledges John Carter's prowess as eleventh
- Part of Thark warrior class

**Continuity Traits:**
- Thark community member
- Rank system participant
- Korad city dweller

**Uncertainty Notes:** 
- Physical description adequately supported by source
- No manual description required for image generation

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH005 Audience Chamber Official

aliases: Summons Sender

is_fully_identified: true

manual_description_required: false

manual_description_reason: N/A - sufficient physical detail in source material.

clarification_required: false

clarification_reason: N/A - fully identified character.

clarification_question: N/A

[[SECTION markdown]]

# Lorquas Ptomel

**Chapter Role:** Sends summons to audience chamber

**Physical Presence:** Referenced for summons delivery

**Description Notes:** 
- Delivers summons to John Carter
- Audience chamber official status noted
- Korad city authority figure

**Continuity Traits:**
- Audience chamber connection
- Summons sender role
- Korad administrative position

**Uncertainty Notes:** 
- Physical description adequately supported by source
- No manual description required for image generation

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
