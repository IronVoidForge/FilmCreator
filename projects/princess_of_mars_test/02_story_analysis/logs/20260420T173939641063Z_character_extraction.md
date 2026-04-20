# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T17:39:39.641562+00:00
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

Chapter id: CH001

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

**Setting:** The Arizona hills and mountains; specifically a remote gold-bearing quartz vein, a high plateau filled with Apache tepees, and a large, mysterious cave near a cliffside trail.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer and soldier of fortune. He is characterized by an instinctive sense of duty and a physical resilience that borders on the supernatural.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.

**Events:**
* **The Discovery:** Carter and Powell locate a massive gold vein in the Arizona mountains in 1865.
* **The Departure:** Powell departs to fetch machinery, leaving Carter to guard the claim.
* **The Pursuit:** Noticing suspicious movement in the valley, Carter tracks what he believes to be an Apache raiding party. He discovers signs of a struggle and follows the trail through the night.
* **The Skirmish:** Carter stumbles upon a large Apache camp on a plateau. He launches a sudden, aggressive charge with his revolvers, causing the warriors to scatter in confusion.
* **The Aftermath:** Amidst the chaos, Carter finds Powell dead, riddled with arrows. He retrieves the body and flees the pursuing warriors.
* **The Cave:** While attempting to evade capture, Carter's horse leads him to a large cave at the end of a cliffside trail. After confirming Powell is deceased, Carter enters the cave to scout it. 
* **The Collapse:** Inside the cave, Carter experiences an overwhelming, unnatural drowsiness and loses consciousness on the floor.
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
- [Captain James K. Powell](#captain-james-k-powell)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Captain Jack Carter

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter

**Role:** Protagonist

**Presence:** Physically Present

**Physical Description:** A former Confederate cavalry officer and soldier of fortune. Characterized by extreme physical resilience and an instinctive sense of duty.

**Costume/Silhouette:** Likely wearing mid-19th century frontier/cavalry attire suitable for prospecting and combat in the Arizona mountains.

**Descriptive Noun Phrases:** Former Confederate officer, resilient frontiersman, armed prospector, cavalry soldier.

**Uncertainty Notes:** Specific facial features or exact clothing colors are not detailed in this chapter.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: james_k_powell

canonical_character_id: CH001 James K. Powell

aliases: Captain Powell

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Captain James K. Powell

**Role:** Supporting Character (Deceased)

**Presence:** Physically Present (deceased)

**Physical Description:** A mining engineer and former Confederate officer; friend and partner to John Carter.

**Costume/Silhouette:** Mid-19th century attire consistent with a mining engineer/officer.

**Descriptive Noun Phrases:** Mining engineer, deceased Confederate officer, prospecting partner.

**Uncertainty Notes:** Specific physical appearance is not described beyond his profession and rank.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
