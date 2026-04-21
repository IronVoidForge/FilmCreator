# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T07:09:41.539856+00:00
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

Chapter id: CH010

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

**Setting:** The city of the Tharks (green Martians) and its surrounding hills/ravines.

**Characters:**
- **John Carter:** An Earthman, now recognized as a Tharkian chieftain due to his combat prowess.
- **Woola:** A loyal, large Martian creature (white ape-like/hound-like) who serves as Carter's protector.
- **Dejah Thoris:** The Princess of Helium (a red Martian), currently held captive by the Tharks.
- **Sola:** A kind and civilized green Martian woman who has been instructing Carter in the Martian language.
- **Tars Tarkas:** A prominent Tharkian warrior/leader.
- **Lorquas Ptomel:** A Thark chieftain presiding over a council.
- **Sarkoja:** A cruel green Martian woman acting as a guard for the prisoner.

**Events:**
- **Bonding with Woola:** Carter explores the outskirts of the city and successfully uses affection to establish a deeper bond of friendship and authority with Woola, overcoming the creature's instinctual warnings.
- **The Audience Chamber:** Carter observes the trial of Dejah Thoris. The Princess delivers a powerful plea for amity and civilization, appealing to the Tharks' sense of humanity, which briefly touches even the hardened warriors like Tars Tarkas.
- **The Outburst:** A young Thark warrior breaks the tension by striking Dejah Thoris in the face as a form of "humor." 
- **Combat and Ascension:** Enraged, John Carter intervenes and kills the young warrior in single combat. Because he killed a fellow warrior, he is immediately accorded the status and regalia of a Tharkian chieftain.
- **Meeting Dejah Thoris:** Carter tends to the Princess's injuries and reveals his identity as an Earthman from Virginia. 
- **Diplomatic Stand:** Tars Tarkas informs Carter that while he is respected as a chieftain, he is still responsible for being delivered to the supreme ruler, Tal Hajus. Carter delivers a defiant speech asserting his moral code and his intent to protect Dejah Thoris from any further insult or injury.
- **Departure:** Having gained status through combat, Carter leads Dejah Thoris out of the audience chamber, accompanied by Woola.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH010

- [john_carter](#john_carter)
- [woola](#woola)
- [dejah_thoris](#dejah_thoris)
- [sola](#sola)
- [tars_tarkas](#tars_tarkas)
- [lorquas_ptomel](#lorquas_ptomel)
- [sarkoja](#sarkoja)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: john_carter
canonical_character_id: CH001 John Carter
aliases: Earthman, Tharkian Chieftain
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# John Carter
**Role:** Protagonist / Tharkian Chieftain

**Status:** Physically Present

**Description:** An Earthman from Virginia. Recognized as a Tharkian chieftain due to combat prowess and regalia.

**Prompting Phrases:** Human male, Earthling, warrior, Tharkian chieftain regalia, combatant.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: woola
canonical_character_id: CH003 Woola
aliases: Martian creature, protector
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Woola
**Role:** Companion / Protector

**Status:** Physically Present

**Description:** A large, white, ape-like or hound-like Martian creature. Loyal to John Carter.

**Prompting Phrases:** Large white Martian creature, white hound-like beast, white ape-like creature, loyal protector.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dejah_thoris
canonical_character_id: CH004 Dejah Thoris
aliases: Princess of Helium, Red Martian
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Dejah Thoris
**Role:** Princess / Captive

**Status:** Physically Present

**Description:** A Red Martian princess. Currently held captive by the Tharks; suffers a facial injury from a warrior's strike.

**Prompting Phrases:** Red Martian woman, Princess of Helium, noble red Martian.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sola
canonical_character_id: CH005 Sola
aliases: Kind green Martian
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sola
**Role:** Instructor / Ally

**Status:** Referenced/Present (Contextual)

**Description:** A kind and civilized green Martian woman who has been teaching Carter the Martian language.

**Prompting Phrases:** Civilized green Martian woman, kind female Tharkian.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: tars_tarkas
canonical_character_id: CH006 Tars Tarkas
aliases: Prominent warrior
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Tars Tarkas
**Role:** Warrior / Leader

**Status:** Physically Present

**Description:** A prominent Tharkian warrior and leader. Shows brief signs of being moved by Dejah Thoris's plea.

**Prompting Phrases:** Prominent green Martian warrior, Tharkian leader, large green Martian.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lorquas_ptomel
canonical_character_id: CH007 Lorquas Ptomel
aliases: Thark chieftain
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Lorquas Ptomel
**Role:** Chieftain

**Status:** Physically Present

**Description:** A Thark chieftain presiding over the council/trial.

**Prompting Phrases:** Green Martian chieftain, presiding Thark warrior.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: sarkoja
canonical_character_id: CH008 Sarkoja
aliases: Cruel green Martian woman
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
[[SECTION markdown]]
# Sarkoja
**Role:** Guard

**Status:** Physically Present

**Description:** A cruel green Martian woman acting as a guard for the prisoner.

**Prompting Phrases:** Cruel green Martian woman, female Tharkian guard.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
