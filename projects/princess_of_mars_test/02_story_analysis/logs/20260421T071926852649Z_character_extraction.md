# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:19:26.852649+00:00
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

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- still emit explicit character records; do not collapse them into index bullets only



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

**Summary:**
Following his rise in status among the Tharks, John Carter secures better living conditions for Dejah Thoris by assigning Sola to guard her. Carter moves them into a more prestigious building featuring ancient, elaborate architecture and frescoes depicting a long-extinct, fair-skinned race of Martians. During their time in the new quarters, Carter and Dejah Thoris share an intimate conversation where he reveals his true origin: he is from Earth, not the mysterious valley of Dor. Dejah Thoris expresses skepticism but ultimately chooses to believe him based on her intuition. She explains that while Barsoomians can observe Earth through advanced telescopic technology, they did not recognize Carter because he lacks the typical "unsightly" clothing and ornaments worn by most Earthmen. The chapter concludes with Dejah Thoris providing historical context regarding the evolution of the Red Martian race and the ancient civilization of Korad, just before Carter is summoned to appear before Lorquas Ptomel.

**Characters:**
- **John Carter:** An Earthman who has established himself as a high-ranking warrior among the Tharks; he reveals his extraterrestrial origins to Dejah Thoris.
- **Dejah Thoris:** A noblewoman of the Red Martians; she displays deep curiosity and empathy toward Carter and shares much of Barsoom's history.
- **Sola:** A Thark woman who acts as a protector and attendant for Dejah Thoris.
- **Sarkoja:** A hostile Thark female who remains a potential threat to the group.
- **Lorquas Ptomel:** A high-ranking leader/chieftain who summons Carter.
- **Tars Tarkas:** A prominent Thark warrior present during the summons.

**Settings:**
- **The New Quarters:** A pretentious, ancient building near the audience chamber, featuring marble ceilings, gold chains, and elaborate frescoes of a lost Martian race.
- **The Plaza/Audience Chamber:** The central hub of the Thark community where political power is wielded.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH011

- [John Carter](#john_carter)
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Sarkoja](#sarkoja)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Tars Tarkas](#tars_tarkas)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Earthman

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / High-ranking Thark warrior.

**Status:** Physically Present.

**Physical Description:** An Earthman; lacks the typical "unsightly" clothing and ornaments of most Earthmen.

**Prompting Phrases:** Human male, Earthling, lack of Martian ornamentation, high-status Thark warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Dejah Thoris

aliases: Noblewoman of the Red Martians

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Noblewoman of the Red Martians.

**Status:** Physically Present.

**Physical Description:** Red Martian noblewoman; possesses deep intuition and historical knowledge.

**Prompting Phrases:** Red Martian woman, noble attire, empathetic expression, Barsoomian nobility.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH004 Sola

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sola
**Role:** Thark woman / Protector and attendant to Dejah Thoris.

**Status:** Physically Present.

**Physical Description:** Thark female.

**Prompting Phrases:** Thark woman, guardian, attendant, martial posture.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH005 Sarkoja

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja
**Role:** Hostile Thark female.

**Status:** Referenced/Present in context.

**Physical Description:** Thark female; hostile demeanor.

**Prompting Phrases:** Hostile Thark woman, aggressive expression, Thark warrior.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH006 Lorquas Ptomel

aliases: Chieftain

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** High-ranking leader/chieftain.

**Status:** Referenced (Summons Carter).

**Physical Description:** High-ranking Thark leader.

**Prompting Phrases:** Thark chieftain, authoritative presence, high-ranking Martian leader.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH007 Tars Tarkas

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Prominent Thark warrior.

**Status:** Physically Present (during summons).

**Physical Description:** Prominent Thark warrior.

**Prompting Phrases:** Large Thark warrior, prominent martial figure, Green Martian.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
