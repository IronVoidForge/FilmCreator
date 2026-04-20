# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T18:01:36.628100+00:00
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

Chapter id: CH016

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

After a twenty-day journey across Martian sea bottoms and cultivated lands, John Carter and Dejah Thoris arrive at the ancient city of Thark, the stronghold of the green Tharks ruled by Tal Hajus. Upon settling into their quarters, John Carter confesses his absolute devotion to Dejah Thoris and enlists her help in planning an escape. They attempt to persuade Sola to join them, promising her sanctuary among the red men of Helium, but she expresses deep skepticism regarding the safety of their route. Using a diamond to map out waterways on a marble floor, the group decides on a northern route to bypass Thark territory.

The escape is set for that night, but as John Carter prepares his thoats and moves toward the rendezvous point, he realizes the plan has been compromised after overhearing mounted warriors discussing their intentions. While maneuvering through the city to find the women, Carter climbs into Dejah Thoris's quarters and overhears a Thark chieftain instructing warriors to ambush him and imprison him in the vaults for Tal Hajus. He also learns that Sola has already been taken into custody.
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
**Role:** Protagonist / Escape Planner

**Status:** Physically Present

**Physical Description:** (Specific visual details not provided in this chapter text, though established as a human/red man).

**Costume/Silhouette:** Preparing thoats for travel.

**Prompt Phrases:** Human male, red man, warrior, strategist.

**Uncertainty Notes:** Chapter focuses on his actions and dialogue rather than physical appearance.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Dejah Thoris

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris
**Role:** Deuteragonist / Escape Planner

**Status:** Physically Present

**Physical Description:** (Specific visual details not provided in this chapter text).

**Costume/Silhouette:** Resident of Thark quarters.

**Prompt Phrases:** Female, red woman, noble, companion to John Carter.

**Uncertainty Notes:** Visual specifics are absent from the narrative text in this segment.
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
**Role:** Potential Escapee / Prisoner

**Status:** Physically Present (later captured)

**Physical Description:** (Specific visual details not provided in this chapter text).

**Costume/Silhouette:** Resident of Thark.

**Prompt Phrases:** Female, red woman, skeptic.

**Uncertainty Notes:** Visual description is missing from the text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tal_hajus

canonical_character_id: CH005 Tal Hajus

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Only mentioned as the ruler of the Tharks; no physical description provided.

clarification_required: true

clarification_reason: Needs physical identification to distinguish from other Thark warriors.

clarification_question: What is the physical appearance and stature of Tal Hajus?

[[SECTION markdown]]

# Tal Hajus
**Role:** Antagonist / Ruler of the Tharks

**Status:** Referenced

**Physical Description:** Unknown.

**Costume/Silhouette:** Not described.

**Prompt Phrases:** Green Thark, ruler, chieftain, antagonist.

**Uncertainty Notes:** Character is only mentioned by name as the authority figure in Thark.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_chieftain

canonical_character_id: UNKNOWN Thark Chieftain

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Character is a generic functional role (chieftain) without specific identifying features.

clarification_required: true

clarification_reason: Is this a specific named character or a generic Thark leader?

clarification_question: Does the chieftain have a name or unique visual identifiers?

[[SECTION markdown]]

# Thark Chieftain
**Role:** Antagonist / Plot Driver

**Status:** Physically Present (heard/seen in shadows)

**Physical Description:** Green Thark.

**Costume/Silhouette:** Warrior attire.

**Prompt Phrases:** Green Thark, warrior, chieftain, commanding voice.

**Uncertainty Notes:** Identity is generic; no specific facial or body details provided.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
