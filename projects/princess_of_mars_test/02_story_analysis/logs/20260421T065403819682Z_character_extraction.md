# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-21T06:54:03.819682+00:00
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

Chapter id: CH003

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

**Setting:** A circular basin on Mars covered in yellowish, moss-like vegetation, featuring a low walled enclosure with a glass roof (an incubator).

**Events:**
- The protagonist wakes up on Mars and discovers the effects of low gravity, finding that simple movements cause him to leap great distances.
- He explores a nearby enclosure and discovers it is an incubator containing large white eggs; several grotesque, multi-limbed young Martians have already hatched.
- A party of twenty mounted Martian warriors approaches. The protagonist narrowly avoids being killed by the leader's spear after hearing the rattle of equipment.
- To escape, the protagonist performs a massive leap (thirty feet into the air), landing on the far side of the enclosure. This display of agility shifts the Martians' perception of him from prey to a "wonderful discovery."
- The protagonist observes the Martians' advanced weaponry, specifically long-range rifles made of white metal and wood.
- The leader of the party dismounts, approaches unarmed, and offers the protagonist a metal armlet as a gesture of peace.
- The protagonist accepts the armlet, signaling his peaceful intent. He is then lifted onto a Martian mount and taken away with the cavalcade toward distant hills.

**Characters:**
- **The Protagonist:** An Earthman, currently naked and unarmed, possessing superior agility due to the low gravity.
- **Martian Warriors:** Large (15ft), four-armed humanoids with olive-green skin, red eyes, and tusks. They ride eight-legged, slate-colored animals.
- **The Leader:** A Martian warrior who initiates peaceful contact through gesture and a gift of an armlet.

**Key Details for Scene Extraction:**
- The physical sensation of low gravity (the "ludicrous" attempts at walking).
- The visual description of the hatching Martians inside the glass incubator.
- The tension of the near-death encounter with the spear.
- The non-verbal communication exchange between the protagonist and the Martian leader.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index - CH003

- [Protagonist](#protagonist)
- [Martian Warriors](#martian-warriors)
- [The Leader](#the-leader)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH003 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: Physical appearance (face, hair, build) is not described; only state of dress (naked).

clarification_required: true

clarification_reason: Identity and physical features are unknown.

clarification_question: What is the protagonist's age, hair color, eye color, and general body type?

[[SECTION markdown]]

# Protagonist
**Role:** Central Character / Survivor

**Status:** Physically Present

**Physical Description:** 
An Earthman currently naked and unarmed. Exhibits extreme agility and high-leaping capabilities due to the low Martian gravity.

**Costume/Silhouette:** 
Naked; no clothing or equipment present in this chapter.

**Prompt Phrases:** 
Naked human male, agile movement, leaping through low gravity, vulnerable Earthman.

**Uncertainty Notes:** 
No facial features, hair, or specific body build are provided in the text.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH003 Martian Warriors

aliases: Martians

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Warriors
**Role:** Antagonists / Encounter Group

**Status:** Physically Present

**Physical Description:** 
Large humanoids standing approximately 15 feet tall. They possess olive-green skin, red eyes, and tusks. They have four arms.

**Costume/Silhouette:** 
Mounted on eight-legged, slate-colored animals. Equipped with long-range rifles made of white metal and wood.

**Prompt Phrases:** 
15ft tall humanoid, olive-green skin, four arms, red eyes, tusks, riding eight-legged slate animal, white metal rifle.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_leader

canonical_character_id: CH003 Martian Leader

aliases: Leader of the party

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# The Leader
**Role:** Diplomatic Contact

**Status:** Physically Present

**Physical Description:** 
A member of the Martian warrior race (15ft, olive-green skin, four arms, red eyes, tusks).

**Costume/Silhouette:** 
Dismounts from his eight-legged mount to approach unarmed. Carries a metal armlet as a peace offering.

**Prompt Phrases:** 
Martian leader, four-armed humanoid, offering metal armlet, peaceful gesture, dismounted.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
