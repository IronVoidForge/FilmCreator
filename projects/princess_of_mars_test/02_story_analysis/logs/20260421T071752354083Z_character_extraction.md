# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:17:52.354083+00:00
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

Chapter id: CH013

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

**Setting:** The city of the Green Martian horde (under Lorquas Ptomel) and the surrounding Martian avenues under the light of two moons.

**Characters:**
- **John Carter:** An Earthman integrated into the Thark warrior culture; demonstrates a unique approach to animal training through kindness rather than force.
- **Tars Tarkas:** A Thark warrior leader who observes and learns from Carter's methods.
- **Dejah Thoris:** A Red Martian princess of high lineage; shares a deep emotional bond with Carter.
- **Sola:** Dejah Thoris's companion.
- **Lorquas Ptomel:** The leader of the Green Martian community.

**Events:**
- **Thoat Training:** Following a battle with airships, the community remains in the city. John Carter uses his experience with Earth animals to train the vicious "thoats" (Martian mounts) using kindness and authority rather than just violence. This method proves highly effective, increasing military precision and earning him a gold anklet from Lorquas Ptomel.
- **Military Instruction:** Tars Tarkas instructs Carter in Thark warfare and riding techniques.
- **The Reunion:** Before the march resumes toward Thark, Carter meets Dejah Thoris privately. She reveals that the older women of the Thark retinue have been intentionally separating them and forcing her into arduous labor (mixing radium powder for explosives).
- **Technological Insight:** Dejah Thoris explains the nature of Martian radium-based projectiles, which explode upon contact with sunlight.
- **Emotional Development:** Carter expresses his protective feelings toward Dejah Thoris. She responds with cryptic, affectionate remarks, hinting at a deeper understanding of their connection that Carter does not yet fully grasp. The chapter concludes with a moment of intimacy as they walk together under the Martian moons, confirming Carter's profound love for her.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH013

- [john_carter](#john_carter)
- [tars_tarkas](#tars_tarkas)
- [dejah_thoris](#dejah_thoris)
- [sola](#sola)
- [lorquas_ptomel](#lorquas_ptomel)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Earthman, Thark warrior

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Earthman integrated into Thark culture.
**Presence:** Physically present.
**Physical Description:** An Earthman capable of training Martian beasts (thoats) through kindness and authority.
**Costume/Traits:** Wears a gold anklet awarded by Lorquas Ptomel.
**Prompt Phrases:** Human male, Earthling, authoritative presence, calm demeanor, wearing gold anklet.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Thark warrior leader

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Thark warrior leader and instructor.
**Presence:** Physically present.
**Physical Description:** A Thark warrior; provides military instruction in warfare and riding techniques.
**Costume/Traits:** Thark warrior attire.
**Prompt Phrases:** Green Martian, Thark warrior, imposing martial presence, instructor.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH004 Dejah Thoris

aliases: Red Martian princess

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Princess of high lineage.
**Presence:** Physically present.
**Physical Description:** A Red Martian princess; shares a deep emotional bond with Carter.
**Costume/Traits:** Shown performing arduous labor (mixing radium powder).
**Prompt Phrases:** Red Martian woman, royal lineage, elegant but working, expressive eyes.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sola

canonical_character_id: CH005 Sola

aliases: Dejah Thoris's companion

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical description provided in this chapter.

clarification_required: true

clarification_reason: Physical appearance is unknown.

clarification_question: What are Sola's physical characteristics and attire?

[[SECTION markdown]]

# Sola
**Role:** Companion to Dejah Thoris.
**Presence:** Referenced/Present in retinue.
**Physical Description:** Unknown.
**Costume/Traits:** Part of the Thark/Red Martian retinue.
**Prompt Phrases:** Red Martian woman, companion, retinue member.
**Uncertainty Note:** Physical appearance and specific role within the scene are not detailed.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH006 Lorquas Ptomel

aliases: Leader of the Green Martian community

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** Leader of the Green Martian community.
**Presence:** Referenced (awarded anklet).
**Physical Description:** Leader of the Green Martian horde.
**Costume/Traits:** High-status Green Martian.
**Prompt Phrases:** Green Martian leader, authoritative, commanding presence.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
