# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-20T16:41:07.671086+00:00
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

**Setting:**
A vast, circular basin on Mars covered in a thick, yellowish, moss-like vegetation. The landscape features low hills, quartz-bearing rock outcroppings, and a specific glass-roofed enclosure acting as an incubator for Martian life.

**Characters:**
* **The Protagonist:** An Earthman, currently naked and unarmed, possessing superhuman agility and leaping ability due to the low Martian gravity.
* **Martian Warriors:** A group of twenty massive beings (approx. 15 feet tall) with multiple arms and red eyes, riding large, four-legged, multi-limbed mounts. They are heavily armed with long spears and advanced long-range rifles.
* **The Martian Leader:** The head of the hunting party; he demonstrates a capacity for peaceful diplomacy by approaching the protagonist unarmed to offer a gesture of friendship.
* **Hatchlings:** Newly emerged, grotesque creatures from large white eggs, characterized by yellowish-green skin, six limbs, and protruding eyes.

**Key Events:**
1. **Awakening on Mars:** The protagonist wakes in a Martian basin and discovers the effects of low gravity, finding that even simple walking results in uncontrolled hopping.
2. **Discovery of the Incubator:** While exploring for water, the protagonist finds a glass-roofed structure containing large white eggs and observes the hatching of strange, multi-limbed creatures.
3. **The Ambush:** A party of twenty Martian warriors approaches silently. The protagonist is nearly killed by the tip of a massive spear held by the lead warrior.
4. **The Great Leap:** To escape the immediate threat, the protagonist utilizes the low gravity to perform a massive 30-foot leap, landing safely on the far side of the incubator. This display of agility transforms the Martians' view of him from prey to a "wonderful discovery."
5. **Diplomatic Contact:** The Martian leader dismounts and approaches the protagonist unarmed. He offers a metal armlet as a sign of peace; the protagonist accepts it, signaling his intent for friendship.
6. **Departure:** The leader escorts the protagonist away, placing him on the back of one of the Martian mounts to join the retreating cavalcade heading toward the distant hills.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

* [Protagonist](#protagonist)
* [Martian Warriors](#martian-warriors)
* [Martian Leader](#martian-leader)
* [Hatchlings](#hatchlings)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: protagonist

canonical_character_id: CH003 Protagonist

aliases: Earthman

is_fully_identified: false

manual_description_required: true

manual_description_reason: No facial features, hair color, or specific body build provided.

clarification_required: true

clarification_reason: Needs identity clarification to establish a consistent visual persona.

clarification_question: What is the protagonist's facial structure, hair color, and specific physical build?

[[SECTION markdown]]

# Protagonist

**Role:** Earthman explorer/survivor.

**Presence:** Physically present.

**Physical Description:** An Earthman appearing naked and unarmed. He exhibits superhuman agility and an uncontrolled leaping ability due to the low Martian gravity.

**Uncertainty Notes:** Facial features, hair, and specific body type are currently unknown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_warriors

canonical_character_id: CH003 Martian Warriors

aliases: Martian hunting party

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Warriors

**Role:** A group of twenty hunters.

**Presence:** Physically present.

**Physical Description:** Massive beings, approximately 15 feet tall, featuring multiple arms and red eyes. They ride large, four-legged, multi-limbed mounts.

**Costume/Equipment:** Heavily armed with long spears and advanced long-range rifles.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: martian_leader

canonical_character_id: CH003 Martian Leader

aliases: 

is_fully_identified: false

manual_description_required: true

manual_description_reason: Lacks distinguishing physical traits or facial details separate from the general warrior class.

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Martian Leader

**Role:** Head of the hunting party and diplomat.

**Presence:** Physically present.

**Physical Description:** A member of the Martian warrior group (15ft tall, multiple arms, red eyes). He approaches the protagonist unarmed to offer a gesture of peace.

**Costume/Equipment:** Carries a metal armlet as a diplomatic gift.

**Uncertainty Notes:** It is unclear if he possesses any unique visual identifiers or armor that distinguishes him from the other warriors.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: hatchlings

canonical_character_id: CH003 Hatchlings

aliases: 

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

[[SECTION markdown]]

# Hatchlings

**Role:** Newly emerged Martian organisms.

**Presence:** Physically present (within the incubator).

**Physical Description:** Grotesque creatures emerging from large white eggs. They feature yellowish-green skin, six limbs, and protruding eyes.

**Uncertainty Notes:** None; physical traits are clearly defined.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
