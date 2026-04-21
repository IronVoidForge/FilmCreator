# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:15:21.511218+00:00
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

Chapter id: CH012

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

**Events:**
John Carter is summoned to an audience with Lorquas Ptomel, a Thark leader. Ptomel confronts Carter regarding his status as a prisoner who nonetheless commands respect, and accuses him of plotting an escape with Dejah Thoris. Ptomel warns that while they are a just people, Carter will be executed if he attempts to flee or attacks a Thark in self-defense. Carter realizes that Sarkoja, a powerful female Thark, has been spying on him and reporting his intentions to undermine him.

Driven by the fear that Dejah Thoris will face cruelty at the hands of the brutal Tal Hajus, Carter becomes more determined to escape. Tars Tarkas approaches Carter and offers him quarters in a building near Sola and her charges. Following Thark custom, Carter is granted the spoils of the two chieftains he previously defeated, including weapons, silks, furs, and food. Carter selects a room on the third floor of a large building, positioned strategically to be near Dejah Thoris's quarters, hoping to establish a way to communicate with her. He also assumes responsibility for a retinue of women and youths who were part of the defeated chieftains' retinues, directing them to occupy the upper floors while he settles into his new quarters.

**Characters:**
* **John Carter:** The protagonist; a human prisoner navigating Thark politics and planning an escape to save Dejah Thoris.
* **Lorquas Ptomel:** A Thark leader who confronts Carter with warnings and accusations of plotting escape.
* **Tars Tarkas:** A respected Thark warrior who treats Carter with professional courtesy and assists him in finding quarters.
* **Sarkoja (Mentioned):** A powerful female Thark and trusted lieutenant of Tars Tarkas, identified by Carter as the one sabotaging him.
* **Tal Hajus (Mentioned):** A brutal and feared Thark leader described as a personification of cruelty.
* **Dejah Thoris (Mentioned):** The Red Martian princess held captive by the Tharks; the primary motivation for Carter's escape plans.

**Settings:**
* **The Audience Chamber:** Where Lorquas Ptomel delivers his warning to Carter.
* **The Plaza/Thark Settlement:** A large area containing various buildings, courtyards, and streets where the Thark warriors and their retinues reside.
* **Carter's New Quarters:** A room on the third floor of a multi-story building overlooking an overgrown central court filled with fountains and statuary.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john_carter)
- [Lorquas Ptomel](#lorquas_ptomel)
- [Tars Tarkas](#tars_tarkas)
- [Sarkoja](#sarkoja)
- [Tal Hajus](#tal_hajus)
- [Dejah Thoris](#dejah_thoris)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Carter
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist; human prisoner.
**Presence:** Physically present.
**Description:** A human male navigating Thark politics and planning an escape to save Dejah Thoris.
**Notes:** Currently a prisoner but commands respect among the Tharks.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH012 Lorquas Ptomel
aliases: Ptomel
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in text.
clarification_required: true
clarification_reason: Physical appearance and Thark features unknown.
clarification_question: What is Lorquas Ptomel's physical appearance and specific Thark morphology?
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Thark leader.
**Presence:** Physically present.
**Description:** A Thark leader who confronts John Carter with accusations of plotting escape.
**Notes:** Represents the authority and legalistic warnings of the Thark people.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH012 Tars Tarkas
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No specific physical description provided in this chapter.
clarification_required: true
clarification_reason: Physical appearance and Thark morphology unknown.
clarification_question: What is the visual appearance of Tars Tarkas?
[[SECTION markdown]]
# Tars Tarkas
**Role:** Respected Thark warrior.
**Presence:** Physically present.
**Description:** A Thark warrior who treats Carter with professional courtesy and assists him in finding quarters.
**Notes:** Acts as a facilitator for Carter's living arrangements.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH012 Sarkoja
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided.
clarification_required: true
clarification_reason: Visual identity and Thark features unknown.
clarification_question: What does Sarkoja look like?
[[SECTION markdown]]
# Sarkoja
**Role:** Powerful female Thark; lieutenant of Tars Tarkas.
**Presence:** Referenced (Spying/Sabotaging).
**Description:** A powerful female Thark identified by Carter as a spy working against him.
**Notes:** Characterized by her political maneuvering and subversion.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: CH012 Tal Hajus
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided.
clarification_required: true
clarification_reason: Visual identity and Thark morphology unknown.
clarification_question: What is the physical appearance of Tal Hajus?
[[SECTION markdown]]
# Tal Hajus
**Role:** Brutal Thark leader.
**Presence:** Referenced.
**Description:** A feared Thark described as a personification of cruelty.
**Notes:** Used as a source of dread regarding Dejah Thoris's safety.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH012 Dejah Thoris
aliases: Princess
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter.
clarification_required: true
clarification_reason: Visual appearance and specific attire unknown.
clarification_question: What is the physical appearance of Dejah Thoris?
[[SECTION markdown]]
# Dejah Thoris
**Role:** Red Martian Princess.
**Presence:** Referenced.
**Description:** A captive princess; the primary motivation for Carter's escape.
**Notes:** Held by the Tharks.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
