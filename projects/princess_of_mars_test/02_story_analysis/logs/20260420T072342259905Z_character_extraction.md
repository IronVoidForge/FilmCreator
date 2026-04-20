# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T07:23:42.259905+00:00
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

**Chapter Title:** Champion and Chief
**Chapter ID:** CH010
**Summary:**
Early in the morning, John Carter explores outside the city limits with Woola, testing the hound's loyalty and affection. He experiences a moment of misunderstanding when he laughs at Woola's playful affection; on Mars, laughter signifies torture and death, causing him to realize his mistake immediately. Upon returning to the plaza, Carter observes Dejah Thoris before Lorquas Ptomel and the Thark chieftains. During the interrogation, Dejah Thoris explains her peaceful scientific mission from Helium and pleads for amity between the red and green men. Sarkoja is present and displays cruelty toward the prisoner. When a young warrior strikes Dejah Thoris across the face, John Carter intervenes, killing the brute in his rage. He gains the status of a Tharkian chieftain through this act, receiving the dead warrior's trappings. John Carter explains himself to Dejah Thoris, revealing his name and origin (Virginia, Earth). Tars Tarkas informs him that he is now accorded respect as a conqueror but warns him of the responsibilities attached to his new status, including the potential danger if Tal Hajus deems him unworthy. The chapter concludes with John Carter and Dejah Thoris leaving the audience chamber together, accompanied by Woola, having established a bond of protection and friendship despite their captor status.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH010 (Champion and Chief)

## John Carter

Short, grounded character markdown.

[[/SECTION]]

## Woola

Short, grounded character markdown.

[[/SECTION]]

## Dejah Thoris

Short, grounded character markdown.

[[/SECTION]]

## Lorquas Ptomel

Short, grounded character markdown.

[[/SECTION]]

## Thark Chieftains

Short, grounded character markdown.

[[/SECTION]]

## Sarkoja

Short, grounded character markdown.

[[/SECTION]]

## Tars Tarkas

Short, grounded character markdown.

[[/SECTION]]

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Narrator, Conscious Entity, Virginia Man

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: true

clarification_reason: Needs identity clarification.

clarification_question: What is the protagonist's physical form and origin?

[[SECTION markdown]]

# John Carter

**Chapter Role:** Protagonist, Tharkian Chieftain

**Physical Presence:** Referenced throughout chapter

**Physical Description:** Sparse - no detailed physical description provided in source material

**Costume/Silhouette:** Receives dead warrior's trappings after killing the brute; status as conqueror established

**Continuity-Critical Traits:** 
- Origin: Virginia, Earth
- Status: Tharkian chieftain through act of killing young warrior
- Bond: Protection and friendship with Dejah Thoris established
- Companion: Woola (hound) accompanies him

**Uncertainty Notes:** Physical appearance details are missing from source material; relies on canonical identification only

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: woola

canonical_character_id: CH002 Woola

aliases: Hound, Companion Dog

is_fully_identified: true

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Woola

**Chapter Role:** Hound Companion

**Physical Presence:** Present throughout chapter

**Physical Description:** Sparse - no detailed physical description provided in source material

**Costume/Silhouette:** None specified; hound form implied

**Continuity-Critical Traits:** 
- Loyalty: Tested and affirmed by John Carter
- Affection: Demonstrates playful affection toward Carter
- Bond: Protection and friendship established with Carter

**Uncertainty Notes:** Physical appearance details are missing from source material; relies on canonical identification only

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dejah_thoris

canonical_character_id: CH003 Dejah Thoris

aliases: Princess, Helium Missionary

is_fully_identified: true

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Dejah Thoris

**Chapter Role:** Prisoner, Helium Missionary

**Physical Presence:** Present throughout chapter

**Physical Description:** Sparse - no detailed physical description provided in source material

**Costume/Silhouette:** None specified; prisoner status implied

**Continuity-Critical Traits:** 
- Mission: Peaceful scientific mission from Helium
- Plea: Amity between red and green men
- Status: Prisoner under Tharkian custody
- Bond: Protection and friendship with John Carter established
- Companion: Woola accompanies her when leaving audience chamber

**Uncertainty Notes:** Physical appearance details are missing from source material; relies on canonical identification only

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: lorquas_ptomel

canonical_character_id: CH004 Lorquas Ptomel

aliases: Thark Leader, Audience Member

is_fully_identified: true

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Lorquas Ptomel

**Chapter Role:** Thark Leader, Audience Member

**Physical Presence:** Present during interrogation scene

**Physical Description:** Sparse - no detailed physical description provided in source material

**Costume/Silhouette:** None specified; Thark attire implied

**Continuity-Critical Traits:** 
- Status: Thark chieftain/leader
- Role: Audience member during Dejah Thoris's plea
- Setting: Plaza/Audience chamber

**Uncertainty Notes:** Physical appearance details are missing from source material; relies on canonical identification only

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: thark_chieftains

canonical_character_id: CH005 Thark Chieftains

aliases: Red Men, Audience Members

is_fully_identified: true

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Thark Chieftains

**Chapter Role:** Audience Members, Prisoners' Custodians

**Physical Presence:** Present during interrogation scene

**Physical Description:** Sparse - no detailed physical description provided in source material

**Costume/Silhouette:** None specified; Thark attire implied

**Continuity-Critical Traits:** 
- Status: Red Men (Thark people)
- Role: Audience members during Dejah Thoris's plea
- Setting: Plaza/Audience chamber
- Group: Multiple chieftains present

**Uncertainty Notes:** Physical appearance details are missing from source material; relies on canonical identification only

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: sarkoja

canonical_character_id: CH006 Sarkoja

aliases: Cruel One, Prisoner's Oppressor

is_fully_identified: true

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Sarkoja

**Chapter Role:** Prisoner's Oppressor, Audience Member

**Physical Presence:** Present during interrogation scene

**Physical Description:** Sparse - no detailed physical description provided in source material

**Costume/Silhouette:** None specified; Thark attire implied

**Continuity-Critical Traits:** 
- Status: Present during interrogation
- Behavior: Displays cruelty toward prisoner (Dejah Thoris)
- Setting: Plaza/Audience chamber

**Uncertainty Notes:** Physical appearance details are missing from source material; relies on canonical identification only

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: tars_tarkas

canonical_character_id: CH007 Tars Tarkas

aliases: Tharkian Authority, Conqueror's Advisor

is_fully_identified: true

manual_description_required: true

manual_description_reason: Sparse physical detail in chapter summary.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Tars Tarkas

**Chapter Role:** Tharkian Authority, Advisor to John Carter

**Physical Presence:** Present during audience chamber scene

**Physical Description:** Sparse - no detailed physical description provided in source material

**Costume/Silhouette:** None specified; Thark attire implied

**Continuity-Critical Traits:** 
- Status: Tharkian authority figure
- Role: Informs John Carter of his new status as conqueror
- Warning: Advises on responsibilities attached to chieftain status
- Concern: Potential danger if Tal Hajus deems him unworthy
- Setting: Audience chamber

**Uncertainty Notes:** Physical appearance details are missing from source material; relies on canonical identification only

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_PACKET]]
````
