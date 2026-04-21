# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T15:25:20.430016+00:00
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

Chapter id: CH024

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
John Carter's craft is shot down during a battle between Tharks and Warhoons. He intervenes to save Tars Tarkas from being killed by three Warhoon warriors, establishing a bond of friendship between them. Following the battle, John Carter reunites with his faithful hound, Woola. 

The narrative shifts to political maneuvering within Thark. To avoid the wrath of the current Jeddak, Tal Hajus, John Carter and Tars Tarkas decide to face him in council. Beforehand, Tars Tarkas uses a clever threat to force the treacherous Sarkoja to flee. In the council, John Carter publicly challenges Tal Hajus's fitness to rule, citing his cowardice in battle. The council decrees a combat between Tal Hajus and Tars Tarkas; Tars Tarkas wins, becoming the new Jeddak and elevating John Carter to the rank of chieftain.

Leveraging this new power, John Carter proposes an alliance to the Thark hordes: a raid on Zodanga to rescue Dejah Thoris and seize their wealth. The Tharks enthusiastically agree, amassing a force of 150,000 warriors. After a ten-day march, the army reaches Zodanga. John Carter leads a small group in a stealthy infiltration of the city by scaling the massive carborundum walls using a human ladder and leather straps. He successfully enters the palace grounds and begins coordinating a silent takeover of the city gates to prepare for the main assault.

**Characters:**
- **John Carter:** The protagonist; uses his Earthly strength and tactical mind to rise to chieftain status.
- **Tars Tarkas:** A mighty Thark warrior who becomes Jeddak after defeating Tal Hajus.
- **Woola:** John Carter's loyal, giant hound.
- **Tal Hajus:** The former Jeddak of Thark; a coward defeated in combat.
- **Sarkoja:** A treacherous Thark woman forced into exile by Tars Tarkas.
- **Lorquas Ptomel:** A Thark chieftain who supports the challenge against Tal Hajus.

**Settings:**
- **The Battlefield:** A plain near an ancient dead city where the Thark/Warhoon conflict occurs.
- **Thark (City):** The seat of power for the Green Martians.
- **Zodanga:** A massive, walled city built of carborundum; the target of the Thark expedition.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [john_carter](#john_carter)
- [tars_tarkas](#tars_tarkas)
- [woola](#woola)
- [tal_hajus](#tal_hajus)
- [sarkoja](#sarkoja)
- [lorquas_ptomel](#lorquas_ptomel)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Protagonist
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist, Thark Chieftain.
**Presence:** Physically present.
**Description:** An Earthman with superhuman strength and tactical intelligence. Capable of scaling massive carborundum walls using human ladders and leather straps.
**Prompt Phrases:** Human male, superhuman strength, tactical leader, infiltrator.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: Jeddak of Thark
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Mighty Thark warrior, new Jeddak.
**Presence:** Physically present.
**Description:** A powerful Green Martian (Thark) warrior who defeated Tal Hajus in combat to claim leadership.
**Prompt Phrases:** Large green martian, Thark warrior, powerful silhouette, Jeddak leader.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: Faithful Hound
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** John Carter's loyal companion.
**Presence:** Physically present.
**Description:** A giant, loyal hound belonging to John Carter.
**Prompt Phrases:** Giant alien hound, loyal beast, massive canine.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal Hajus
aliases: Former Jeddak
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Deposed Jeddak.
**Presence:** Physically present (referenced/defeated).
**Description:** A Thark leader characterized by cowardice in battle, subsequently defeated by Tars Tarkas.
**Prompt Phrases:** Green martian warrior, defeated leader, cowardly demeanor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: Sarkoja
aliases: Treacherous Thark woman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja
**Role:** Treacherous political actor.
**Presence:** Physically present (exiled).
**Description:** A treacherous Thark woman who was forced to flee by Tars Tarkas.
**Prompt Phrases:** Female Thark, green martian, treacherous expression.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: Lorquas Ptomel
aliases: Thark Chieftain
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Supporting Thark Chieftain.
**Presence:** Physically present (referenced in council).
**Description:** A Thark chieftain who supported the challenge against Tal Hajus.
**Prompt Phrases:** Green martian, Thark chieftain, warrior leader.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
