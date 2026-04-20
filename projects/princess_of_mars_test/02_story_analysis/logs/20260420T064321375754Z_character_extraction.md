# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T06:43:21.376255+00:00
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

In this chapter, John Carter introduces himself as Captain Jack Carter of Virginia. He recounts finding a gold-bearing quartz vein with Captain James K. Powell in Arizona during the winter of 1865. After locating a million dollars worth of ore, Powell leaves to purchase machinery while Carter guards the claim. On March 3, 1866, Apaches attack Powell's party. Carter pursues them, finds Powell dead surrounded by Apache tepees, and charges into the camp scattering the warriors. He retrieves Powell's body and flees into a cave after being led astray by his horse. Inside the cave, Carter lays Powell to rest and falls asleep due to exhaustion.
````

## Raw Response
````text


[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - Chapter CH001

## John Carter / Captain Jack Carter
- **Asset ID:** john_carter
- **Status:** Physically present protagonist
- **Role:** Narrator and main survivor of the Apache attack
- **Description:** Sparse physical detail provided in source material

## Captain James K. Powell
- **Asset ID:** captain_powell
- **Status:** Referenced character, deceased by end of chapter
- **Role:** Mining partner who dies during Apache attack
- **Description:** Limited physical description available

## Apaches
- **Asset ID:** apaches
- **Status:** Referenced group characters
- **Role:** Attackers in the mining claim incident
- **Description:** No individual physical details provided

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: john_carter

canonical_character_id: CH001 John Carter

aliases: Captain Jack Carter, Narrator, Conscious Entity

is_fully_identified: false

manual_description_required: true

manual_description_reason: Sparse physical detail in source material.

clarification_required: true

clarification_reason: Needs identity clarification for image generation.

clarification_question: What is John Carter's physical form and origin?

[[SECTION markdown]]

# John Carter / Captain Jack Carter

**Chapter Role:** Protagonist, Narrator, Main Survivor

**Physical Presence:** Physically present throughout chapter

**Description:** Limited physical description provided in source material. Character introduces himself as Captain Jack Carter of Virginia.

**Continuity Notes:** 
- Survives the Apache attack on mining claim
- Pursues Powell's party after finding him dead
- Retrieves Powell's body and flees into cave
- Falls asleep from exhaustion inside cave

**Uncertainty:** Physical appearance details are sparse in source material. No costume, silhouette, or specific physical traits documented beyond name and rank.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: captain_powell

canonical_character_id: CH001 Captain James K. Powell

aliases: Captain Powell, Mining Partner

is_fully_identified: true

manual_description_required: true

manual_description_reason: Limited physical description available in source material.

clarification_required: false

clarification_reason: Character is clearly identified by name and role.

clarification_question: 

[[SECTION markdown]]

# Captain James K. Powell

**Chapter Role:** Mining Partner, Deceased Character

**Physical Presence:** Referenced character, deceased by end of chapter

**Description:** Limited physical description provided in source material. Identified as mining partner who works with John Carter on gold-bearing quartz vein in Arizona.

**Continuity Notes:** 
- Works with John Carter during winter of 1865
- Leaves to purchase machinery after finding million dollars worth of ore
- Killed during Apache attack on March 3, 1866
- Body found surrounded by Apache tepees
- Retrieved by John Carter before fleeing into cave

**Uncertainty:** Physical appearance details are sparse in source material. No costume or specific physical traits documented beyond name and rank.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: apaches

canonical_character_id: CH001 Apaches

aliases: Apache Warriors, Attackers

is_fully_identified: false

manual_description_required: true

manual_description_reason: Group characters with no individual physical details provided in source material.

clarification_required: true

clarification_reason: Needs identity clarification for image generation of group members.

clarification_question: What are the physical characteristics and attire of Apache warriors in this historical setting?

[[SECTION markdown]]

# Apaches / Apache Warriors

**Chapter Role:** Attackers, Antagonists

**Physical Presence:** Referenced group characters throughout chapter

**Description:** No individual physical description provided in source material. Group identified as attackers during mining claim incident.

**Continuity Notes:** 
- Launch attack on Powell's party
- Surround Powell's body with tepees
- Scattered by John Carter's charge into camp
- Warriors flee after being charged by protagonist

**Uncertainty:** Individual physical appearance details are sparse in source material. No costume, silhouette, or specific physical traits documented for group members. Historical setting is 1865-1866 Arizona.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
