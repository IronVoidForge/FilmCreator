# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:18:27.998448+00:00
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

- [john_carter](#john_carter)
- [dejah_thoris](#dejah_thoris)
- [sola](#sola)
- [sarkoja](#sarkoja)
- [lorquas_ptomel](#lorquas_ptomel)
- [tars_tarkas](#tars_tarkas)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
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
**Description:** An Earthman living among the Tharks. He lacks the typical "unsightly" clothing and ornaments associated with most Earthmen seen via Barsoomian telescopes.
**Prompt Phrases:** Human male, Earthling, warrior status, lack of Martian ornamentation.
[[/SECTION]]
[[/FILMCREATOR_RECORD]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Noblewoman of the Red Martians
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Noblewoman / Love interest.
**Status:** Physically Present.
**Description:** A noblewoman of the Red Martian race. Possesses deep intuition and knowledge of Barsoomian history.
**Prompt Phrases:** Red Martian noblewoman, empathetic expression, historical scholar.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: Thark woman, protector, attendant
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Attendant and guard for Dejah Thoris.
**Status:** Physically Present.
**Description:** A Thark woman assigned to protect and serve the noblewoman.
**Prompt Phrases:** Thark female, protector, attendant.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: Hostile Thark female
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja
**Role:** Antagonist / Potential threat.
**Status:** Referenced/Present in context.
**Description:** A Thark female characterized by her hostility toward the main group.
**Prompt Phrases:** Hostile Thark woman, aggressive demeanor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: Chieftain
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: true
clarification_reason: Physical appearance and Thark-specific features are unknown.
clarification_question: What is the physical appearance of Lorquas Ptomel?
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** High-ranking leader/Chieftain.
**Status:** Referenced (Summoning Carter).
**Description:** A high-ranking figure within the Thark hierarchy who summons John Carter to appear before him.
**Uncertainty Note:** Physical appearance and specific Thark features are not described in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Prominent Thark warrior
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Prominent Thark warrior.
**Status:** Present during summons.
**Description:** A significant and well-known Thark warrior.
**Prompt Phrases:** Thark warrior, prominent Martian figure.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
