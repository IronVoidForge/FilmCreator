# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:25:45.217766+00:00
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

Chapter id: CH017

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
John Carter infiltrates the city of Thark to rescue Dejah Thoris from the clutches of the Thark Jeddak, Tal Hajus. After observing the terrifying presence of Tal Hajus and witnessing Tars Tarkas's silent loathing for the beast, Carter intervenes just as Tal Hajus attempts to seize the Princess. Instead of using his sword, Carter knocks the Jeddak unconscious with a single blow. 

Carter, Dejah Thoris, and Sola escape the city on thoats, heading northeast across a mossy waste toward Helium. The journey becomes a desperate struggle for survival as they run out of food and water. Their progress is slowed by the exhaustion of their mounts; one thoat collapses, forcing Carter and Sola to walk while Dejah Thoris rides. 

The group is eventually spotted by a Thark scouting party. A chieftain discovers them with a fieldglass and leads a charge. To ensure the escape of the women, Carter uses his Martian rifle to kill the charging chieftain and then stays behind to provide cover fire. After exhausting his ammunition, he uses his superior physical abilities to distract the approaching thousand-man Thark army. While successfully leading the warriors away from Dejah Thoris, Carter is eventually overtaken and beaten into unconsciousness by the pursuing force.

**Characters:**
* **John Carter:** The protagonist; a resourceful and brave warrior who sacrifices his own safety to ensure Dejah Thoris's escape.
* **Dejah Thoris:** Princess of Helium; maintains her dignity even in captivity and expresses profound love for Carter during their escape.
* **Sola:** Dejah Thoris's companion; assists in the escape and helps manage the Princess during the flight.
* **Tal Hajus:** The cruel and bestial Jeddak of the Tharks; defeated by Carter.
* **Tars Tarkas:** A Thark warrior who harbors deep hatred for Tal Hajus but fails to intervene in time.
* **Woola:** Carter's faithful Martian hound, who tracks the group through the waste.

**Settings:**
* **The City of Thark:** A fortified settlement inhabited by the green-skinned Tharks, featuring large circular halls and high platforms.
* **The Mossy Waste:** A vast, trackless, and dangerous expanse between Thark and Helium, characterized by a lack of waterways and low mountains.
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
- [Dejah Thoris](#dejah_thoris)
- [Sola](#sola)
- [Tal Hajus](#tal_hajus)
- [Tars Tarkas](#tars_tarkas)
- [Woola](#woola)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: John Carter
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist; Warrior.
**Presence:** Physically present.
**Description:** A resourceful and brave warrior with superior physical abilities compared to Martians. Uses a Martian rifle and sword.
**Traits:** Highly athletic, sacrificial, capable of single-blow knockouts.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: Dejah Thoris
aliases: Princess of Helium
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess of Helium.
**Presence:** Physically present.
**Description:** A noble figure who maintains her dignity even under captivity.
**Traits:** Dignified, expressive of profound love for Carter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: Sola
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Companion to Dejah Thoris.
**Presence:** Physically present.
**Description:** Assists in the escape and helps manage the Princess during their flight across the mossy waste.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tal_hajus
canonical_character_id: Tal Hajus
aliases: Jeddak of the Tharks
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tal Hajus
**Role:** Antagonist; Jeddak of the Tharks.
**Presence:** Physically present.
**Description:** Described as a cruel and bestial leader of the green-skinned Tharks.
**Traits:** Terrifying presence, defeated by Carter via blunt force.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: Tars Tarkas
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Thark Warrior.
**Presence:** Physically present (observed).
**Description:** A Thark warrior who harbors a silent, deep loathing for Tal Hajus.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: Woola
aliases: Martian hound
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Companion.
**Presence:** Referenced/Present in context of tracking.
**Description:** A faithful Martian hound capable of tracking the group through the mossy waste.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
