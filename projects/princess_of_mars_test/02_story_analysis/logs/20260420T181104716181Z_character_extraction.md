# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:11:04.716181+00:00
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

Chapter id: CH021

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

As John Carter travels toward Zodanga, he observes Barsoom's advanced irrigation systems that pump water from polar ice caps through underground conduits. During his journey, he meets members of the Zodangan nobility who express their discontent with the unjust war between Zodanga and Helium and discuss the disappearance of Princess Dejah Thoris. Upon reaching the walled city of Zodanga, Carter separates from Woola to avoid detection and enters the metropolis, noting its unique architecture designed for protection against assassination.

In the central plaza, Carter reunites with Kantos Kan, a Red Martian, who reveals his plan to infiltrate the Zodangan navy as an air scout to gain access to Prince Sab Than, who is rumored to be holding Dejah Thoris captive. Using a ruse, Kantos Kan successfully enrolls Carter into the air-scout squadron. During his training, Carter learns to pilot aircraft using the "eighth Barsoomian ray," a repulsive force of gravity derived from light.

While on a solo flight, Carter intervenes in a skirmish, saving a Red Martian scout from three Green warriors by ramming one of them and subsequently killing the remaining two on foot. The scout is revealed to be a cousin of Than Kosis, the Jeddak of Zodanga. Following their return to the city, Carter is called forward during a massive military ceremony. In recognition of his bravery in defeating the Green warriors, Than Kosis confers an honor upon him and appoints him a padwar of The Guards, granting him quarters within the palace.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index

- [John Carter](#john-carter)
- [Woola](#woola)
- [Dejah Thoris](#dejah-thoris)
- [Kantos Kan](#kantos-kan)
- [Prince Sab Than](#prince-sab-than)
- [Red Martian Scout](#red-martian-scout)
- [Than Kosis](#than-kosis)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: Carter
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Padwar of The Guards

**Presence:** Physically Present

**Description:** A human traveler on Barsoom. He demonstrates exceptional combat skills, piloting air-scout aircraft using the eighth Barsoomian ray, and engaging in hand-to-hand combat with Green warriors.

**Prompting Phrases:** Human male, warrior, pilot, combatant, agile.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Companion

**Presence:** Physically Present (referenced as separating from Carter)

**Description:** A companion to John Carter who stays behind to avoid detection during the infiltration of Zodanga.

**Prompting Phrases:** Loyal creature, Barsoomian animal.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Princess Dejah Thoris
is_fully_identified: false
manual_description_required: true
manual_description_reason: No physical description provided in this chapter; she is only mentioned as missing/captive.
clarification_required: true
clarification_reason: Physical appearance unknown from text.
clarification_question: What is the physical appearance and attire of Princess Dejah Thoris?
[[SECTION markdown]]
# Dejah Thoris
**Role:** Missing Princess

**Presence:** Referenced (Captive)

**Description:** The Princess of Helium, currently rumored to be held captive by Prince Sab Than.

**Prompting Phrases:** Martian royalty, missing princess.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: kantos_kan
canonical_character_id: Kantos Kan
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Kantos Kan
**Role:** Ally / Infiltrator

**Presence:** Physically Present

**Description:** A Red Martian who assists John Carter by facilitating his enrollment into the Zodangan air-scout squadron.

**Prompting Phrases:** Red Martian, strategist, infiltrator.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sab_than
canonical_character_id: Prince Sab Than
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Only mentioned as a rumored captor; no physical details provided.
clarification_required: true
clarification_reason: Physical appearance unknown from text.
clarification_question: What is the physical description of Prince Sab Than?
[[SECTION markdown]]
# Prince Sab Than
**Role:** Potential Antagonist

**Presence:** Referenced

**Description:** A prince rumored to be holding Princess Dejah Thoris captive.

**Prompting Phrases:** Zodangan prince, captor.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: red_martian_scout
canonical_character_id: Red Martian Scout
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Identified only by role/relation; no specific physical traits provided.
clarification_required: true
clarification_reason: Character is a generic type with specific relation.
clarification_question: Does this scout have specific distinguishing features?
[[SECTION markdown]]
# Red Martian Scout
**Role:** Victim / Relative of Royalty

**Presence:** Physically Present

**Description:** A Red Martian scout saved by John Carter during an aerial skirmish. He is a cousin to Than Kosis.

**Prompting Phrases:** Red Martian, air-scout, warrior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: than_kosis
canonical_character_id: Than Kosis
aliases: Jeddak of Zodanga
is_fully_identified: false
manual_description_required: true
manual_description_reason: Mentioned as a ruler, but no physical description is given.
clarification_required: true
clarification_reason: Physical appearance unknown from text.
clarification_question: What does the Jeddak of Zodanga look like?
[[SECTION markdown]]
# Than Kosis
**Role:** Ruler of Zodanga

**Presence:** Physically Present (at ceremony)

**Description:** The Jeddak of Zodanga who honors John Carter for his bravery against Green warriors.

**Prompting Phrases:** Martian ruler, Jeddak, authoritative.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
