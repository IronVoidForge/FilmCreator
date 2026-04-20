# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:56:52.994991+00:00
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

**Setting:** The city of the green Martians (Tharks) and its surrounding plazas/avenues; night time under the two moons of Barsoom.

**Characters:**
- **John Carter:** An Earthman, now a trained Thark warrior.
- **Tars Tarkas:** A Thark leader who instructs Carter in Martian warfare.
- **Dejah Thoris:** A Red Martian Princess and the love interest of John Carter.
- **Sola:** Dejah Thoris's companion.
- **Lorquas Ptomel:** A Thark leader/chieftain.

**Events:**
- **Thoat Training:** Following a battle with airships, the community remains in the city for several days. During this time, John Carter uses his Earthly experience with animals to train the vicious Martian "thoats" through kindness and authority rather than just brute force. His success makes him a wonder among the Tharks and leads Lorquas Ptomel to reward him with a gold anklet.
- **Martian Warfare Intel:** Dejah Thoris explains the mechanics of Martian radium-based projectiles, noting they are dangerous because sunlight causes them to explode.
- **Social Friction:** Dejah Thoris reveals that the older women of the Thark retinue have been intentionally separating her from Carter and forcing her into arduous labor (mixing radium powder) out of jealousy of her noble lineage.
- **Romantic Development:** Carter and Dejah Thoris share a private moment in the evening. Dejah Thoris uses the term "my chieftain" to address him, a significant cultural gesture Carter does not yet fully grasp. The chapter concludes with an intimate moment where Carter realizes the depth of his love for her as they walk together under the Martian moons.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH013

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
**Role:** Protagonist / Earthman turned Thark warrior.
**Presence:** Physically present.
**Description:** An Earthman trained in Martian warfare. He demonstrates unique psychological methods for training animals (thoats) using kindness and authority rather than brute force.
**Traits:** Skilled warrior, empathetic trainer, romantic interest of Dejah Thoris.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH003 Tars Tarkas

aliases: Thark leader

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas
**Role:** Thark Leader / Instructor.
**Presence:** Physically present (referenced as instructor).
**Description:** A leader of the Tharks who has been instructing John Carter in Martian warfare.
**Traits:** Martial authority, Thark chieftain.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH004 Dejah Thoris

aliases: Red Martian Princess

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Love Interest / Red Martian Princess.
**Presence:** Physically present.
**Description:** A noble Red Martian princess. She is knowledgeable about Martian technology (radium projectiles) and is currently facing social friction from older Thark women due to her lineage.
**Traits:** Noble, intelligent, target of jealousy by Thark retinue.
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
**Presence:** Physically present (referenced).
**Description:** A companion to the Princess, though no specific visual details are provided in this chapter.
**Uncertainty Note:** Physical appearance is currently undefined.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH006 Lorquas Ptomel

aliases: Thark chieftain

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel
**Role:** Thark Leader/Chieftain.
**Presence:** Physically present (referenced).
**Description:** A Thark leader who rewards John Carter with a gold anklet for his success in training the thoats.
**Traits:** Authoritative, rewarding.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
