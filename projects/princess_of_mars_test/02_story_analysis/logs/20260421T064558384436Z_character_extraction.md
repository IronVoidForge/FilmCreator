# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:45:58.384436+00:00
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

**Setting:** The Arizona hills and mountains; specifically a remote mining site, a high plateau with Apache tepees, and a large, ancient cave.

**Characters:**
* **John Carter (Captain Jack Carter):** A former Confederate cavalry officer, driven by a sense of duty and a search for gold. He is an experienced fighter who possesses a unique, near-immortal quality.
* **Captain James K. Powell:** A mining engineer and fellow Confederate officer; Carter's friend and partner in prospecting.

**Events:**
* **Introduction:** An elderly John Carter introduces himself, explaining his unusual longevity and his intent to record the strange events of his life, specifically the ten years he spent in an Arizona cave.
* **The Gold Discovery:** Following the Civil War, Carter and Powell discover a massive gold-bearing quartz vein in the Arizona mountains. 
* **The Separation:** To secure machinery for the mine, Powell departs for civilization while Carter stays to guard the claim.
* **The Pursuit:** Noticing suspicious movement in the valley, Carter suspects Powell is being pursued by Apaches. He arms himself and tracks the trail into the night.
* **The Skirmish:** Carter discovers a large Apache camp on a plateau. He launches a sudden, loud charge with his revolvers, causing the warriors to scatter in confusion.
* **Finding Powell:** Amidst the chaos, Carter finds Powell dead, riddled with arrows. Carter retrieves the body to prevent mutilation.
* **The Escape and the Cave:** Pursued by the Apaches, Carter flees through a mountain pass. He eventually reaches a large cave at the end of a cliffside trail. After confirming Powell is deceased, Carter enters the cave to explore.
* **The Drowsiness:** Inside the cave, Carter experiences an overwhelming, unnatural drowsiness that overcomes his physical will, leading him to collapse on the floor.
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

aliases: Captain Jack Carter, Former Confederate cavalry officer

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance (age, facial features, build) is not described beyond his status as "elderly" during the narration.

clarification_required: true

clarification_reason: Needs specific physical traits for consistent character design across different time periods (elderly vs. younger soldier).

clarification_question: What are John Carter's specific facial features, hair color, and build during his younger years in Arizona?

[[SECTION markdown]]

# John Carter

**Role:** Protagonist / Narrator

**Presence:** Physically present (as an elderly man and via flashback/narrative)

**Physical Description:** 
- Described as "elderly" in the framing narrative.
- A former Confederate cavalry officer.
- Possesses a unique, near-immortal quality.

**Costume & Silhouette:** 
- Implied frontier/cavalry attire during the Arizona events (revolvers mentioned).

**Prompt Phrases:** elderly man, former Confederate officer, experienced fighter, survivor.

**Uncertainty Notes:** Specific physical appearance and clothing details for his younger self are not provided in this chapter.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: james_k_powell

canonical_character_id: CH001 Captain James K. Powell

aliases: Powell, Mining engineer

is_fully_identified: false

manual_description_required: true

manual_description_reason: No physical description provided in the text.

clarification_required: true

clarification_reason: Needs visual identification to distinguish him from Carter.

clarification_question: What does Captain James K. Powell look like?

[[SECTION markdown]]

# Captain James K. Powell

**Role:** Supporting Character (Deceased)

**Presence:** Physically present (deceased in flashback/narrative)

**Physical Description:** 
- No specific physical description provided.
- Identified as a mining engineer and fellow Confederate officer.

**Costume & Silhouette:** 
- Implied frontier/prospector attire.

**Prompt Phrases:** mining engineer, Confederate officer, deceased character.

**Uncertainty Notes:** Character is identified by role and rank only; no visual descriptors are available.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
