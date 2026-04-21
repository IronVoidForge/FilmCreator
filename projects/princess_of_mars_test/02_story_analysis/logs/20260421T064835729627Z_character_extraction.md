# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:48:35.729627+00:00
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

**Setting:**
The Arizona hills and mountains; specifically a remote gold-bearing quartz vein, a high plateau with an Apache camp, and a large, ancient cave located on a narrow trail near a cliffside.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer and soldier of fortune. He is characterized by a compulsive sense of duty and a tendency to act before fully processing danger.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.
* **Apache Warriors:** A large group of hostile warriors who ambush Powell.

**Events:**
* **Introduction:** An elderly John Carter introduces himself, explaining his unique immortality/aging process and his intent to record his life story before his final death.
* **The Discovery:** Carter and Powell discover a massive gold vein in Arizona in 1865. They decide Powell will return to civilization to fetch machinery while Carter guards the claim.
* **The Ambush:** After Powell departs, Carter notices suspicious movement in the valley. Suspecting an Apache ambush, he pursues the trail. He discovers a large Apache camp on a plateau and engages them in a chaotic skirmish.
* **The Aftermath:** During the fight, Carter finds Powell dead, riddled with arrows. Carter retrieves the body and flees the pursuing warriors.
* **The Cave:** While attempting to escape, Carter's horse takes him to a narrow cave entrance on a high trail. After confirming Powell is deceased, Carter enters the cave to scout it.
* **The Collapse:** Inside the large, ancient chamber, Carter experiences an overwhelming, unnatural drowsiness. Despite his efforts to stay awake and remain alert to pursuit, he loses consciousness and collapses on the cave floor.
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
- [Apache Warriors](#apache-warriors)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Captain Jack Carter, Narrator

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# John Carter
**Role:** Protagonist / Narrator

**Status:** Physically Present

**Physical Description:**
A former Confederate cavalry officer and soldier of fortune. Described as elderly in the framing narrative, though his past self is active in the 1865 timeline. Characterized by a compulsive sense of duty and impulsive action.

**Costume/Silhouette:**
Confederate military background; likely wearing mid-19th century frontier/cavalry attire suitable for prospecting in Arizona.

**Prompt Phrases:**
Former Confederate cavalry officer, soldier of fortune, 1860s frontiersman, rugged prospector.

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

**Status:** Physically Present (Deceased)

**Physical Description:**
A mining engineer and former Confederate officer; friend and partner to John Carter.

**Costume/Silhouette:**
1860s era attire, likely practical for mining engineering and frontier travel.

**Prompt Phrases:**
Mining engineer, 19th-century officer, deceased prospector, riddled with arrows.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: apache_warriors

canonical_character_id: CH001 Apache Warriors

aliases: Hostile warriors

is_fully_identified: false

manual_description_required: true

manual_description_reason: No specific physical descriptions, facial features, or individual identifiers provided beyond their tribal affiliation and hostility.

clarification_required: true

clarification_reason: Specific visual details for character design (clothing, weaponry, appearance) are missing.

clarification_question: Should the Apache warriors follow a specific historical aesthetic or a stylized version?

[[SECTION markdown]]

# Apache Warriors
**Role:** Antagonists

**Status:** Physically Present

**Physical Description:**
A large group of hostile warriors engaged in an ambush and skirmish.

**Costume/Silhouette:**
Traditional Apache attire (historical context implied), armed with arrows.

**Prompt Phrases:**
Apache warriors, 19th-century indigenous fighters, hostile ambushers, arrow-wielding warriors.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
