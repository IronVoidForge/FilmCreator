# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:37:32.490594+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Keep the response deterministic and grounded in the supplied chapter text.
````

## User Prompt
````text
Project slug: alice_in_wonderland

Chapter id: CH004

Task: extract visible and referenced characters into a character index plus one Markdown file per character.

Packet contract:
- task: character_extraction
- version: 1
- first line: [[FILMCREATOR_PACKET]]
- last line: [[/FILMCREATOR_PACKET]]
- required sections: character_index_markdown
- record type character: fields=asset_id, canonical_character_id, aliases, is_fully_identified, manual_description_required, manual_description_reason, clarification_required, clarification_reason, clarification_question, character_type_hint, morphology_hint, scale_hint, renderability_hint, confidence, direct_identity_evidence, direct_visual_evidence, costume_or_covering_evidence, movement_evidence, associated_entities, alias_or_role_evidence, unknowns, source_refs sections=markdown



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

character_type_hint: unknown

morphology_hint: unknown

scale_hint: unknown

renderability_hint: unknown

confidence: 0.3



[[SECTION markdown]]

# Protagonist

Short, grounded character markdown.

[[/SECTION]]

[[/FILMCREATOR_RECORD]]



Important rules:

- keep one record per meaningful character mention

- prefer short facts over long prose

- if uncertain, use clarification_required instead of guessing

- if clarification is not required, still include clarification_reason and clarification_question as empty values

- still emit explicit character records; do not collapse them into index bullets only



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
- The White Rabbit’s House: A tidy house with a brass nameplate ("W. RABBIT"), featuring a window with a table, a looking-glass, and a chimney.
- The Wood: A thick forest area where Alice flees after leaving the house.

**Characters:**
- **Alice:** Currently giant-sized; she is curious, resourceful, and somewhat anxious about her shifting size.
- **The White Rabbit:** Anxious, authoritative, and prone to temperamental outbursts.
s- **Pat (Bill):** A small creature/animal who falls down the chimney.
- **The Puppy:** An enormous dog that interacts with Alice in the wood.
- **The Blue Caterpillar:** A large blue caterpillar smoking a hookah on top of a mushroom.

**Key Events & Visual Continuity:**
- **The Search:** The White Rabbit searches for his lost fan and gloves; Alice finds him and is mistaken for a housemaid named "Mary Ann."
- **The House Entry:** Alice enters the Rabbit's house to find the items. She finds a fan and tiny white kid gloves on a table in the window.
- **Size Change (Growth):** Alice drinks from a small bottle near the looking-glass. She grows so large her head presses against the ceiling, then she fills the room entirely, eventually having to put an arm out the window and a foot up the chimney to fit.
- **The Interaction with Pat/Bill:** The Rabbit and Pat (the one who falls) attempt to enter the house. Alice's elbow blocks the door; the Rabbit tries the window. A "snatch" by Alice causes a crash in the garden/window area. 
- **The Chimney Kick:** As the Rabbit sends "Bill" down the chimney, Alice kicks him. Bill (the lizard) is sent flying out of the house like a "Jack-in-the-box."
- **Size Change (Shrinking):** The Rabbit throws pebbles through the window; they turn into small cakes on the floor. Alice eats one and shrinks to a manageable size.
- **The Escape:** Alice runs from the crowd of animals (including the recovering Bill) into the thick wood.
- **The Puppy Encounter:** In the wood, Alice encounters an enormous puppy. She plays with it using a stick before fleeing its size/energy.
- **The Discovery:** While resting by a large mushroom, Alice peers over the top to discover a large Blue Caterpillar smoking a hookah.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

# Character Index
- [Alice](#alice)
- [White Rabbit](#white-rabbit)
- [Bill](#bill)
- [The Puppy](#the-puppy)
- [Blue Caterpillar](#blue-caterpillar)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: alice

canonical_character_id: CH001 Alice

aliases: Mary Ann

is_fully_identified: true

manual_description_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: human/girl

morphology_hint: variable size (giant to small)

scale_hint: fluctuates from room-filling to manageable

renderability_hint: high contrast between scale shifts

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: true

costume_or_covering_evidence: true

movement_evidence: true

associated_entities: White Rabbit, Bill, The Puppy, Blue Caterpillar

alias_or_role_evidence: Mistaken for Mary Ann; protagonist.

unknowns: ""

source_refs: ""

[[SECTION markdown]]

# Alice
**Role:** Protagonist

**Status:** Physically present.

**Physical Description:** A girl whose size fluctuates wildly due to eating/drinking items. At one point, she is large enough to fill a house, pressing her head against the ceiling and sticking limbs out of windows and chimneys. Later, she shrinks to a manageable size.

**Costume & Traits:** Often mistaken for a housemaid (Mary Ann). s-size shifting is a core trait.

**Prompt Phrases:** Giant girl filling a room, shrinking girl, curious explorer.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: white_rabbit

canonical_character_id: CH002 White Rabbit

aliases: W. Rabbit

is_fully_identified: true

manual_description_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: anthropomorphic rabbit

morphology_hint: animal-humanoid hybrid

scale_hint: small/standard

renderability_hint: high

confidence: 0.9

direct_identity_evidence: true

direct_visual_evidence: true

costume_or_covering_evidence: true

movement_evidence: true

associated_entities: Alice, Bill

alias_or_role_evidence: Owner of the house with the nameplate "W. RABBIT".

unknowns: ""

source_refs: ""

[[SECTION markdown]]

# White Rabbit
**Role:** Supporting Character / Antagonist (briefly)

**Status:** Physically present.

**Physical Description:** Anxious and authoritative rabbit. 

**Costume & Traits:** Associated with a brass nameplate "W. RABsbit" on his house. Carries/searches for fan and tiny white kid gloves.

**Prompt Phrases:** Anxious rabbit, authoritative rabbit, frantic animal.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: bill

canonical_character_id: CH003 Bill

aliases: Pat (Bill)

is_fully_identified: true

manual_description_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: small creature/lizard

morphology_hint: small animal-like

scale_hint: very small

renderability_hint: high

confidence: 0.8

direct_identity_evidence: true

direct_visual_evidence: true

costume_or_covering_evidence: false

movement_evidence: true

associated_entities: White Rabbit, Alice

alias_or_role_evidence: Identified as "Bill" or "Pat".

unknowns: ""

source_refs: ""

[[SECTION markdown]]

# Bill
**Role:** Minor Character

**Status:** Physically present.

**Physical Description:** A small creature (possibly a lizard) that falls down the chimney.

**Costume & Traits:** Sent flying out of the house like a "Jack-in-the-box" after being kicked by Alice.

**Prompt Phrases:** Small lizard, falling from chimney, Jack-in-the-box motion.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: puppy

canonical_character_id: CH004 The Puppy

aliases: ""

is_fully_identified: true

manual_description_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: dog

morphology_hint: enormous/giant

scale_hint: massive

renderability_hint: high

confidence: 0.8

direct_identity_evidence: true

direct_visual_evidence: true

costume_s_covering_evidence: false

movement_evidence: true

associated_entities: Alice

alias_or_role_evidence: ""

unknowns: ""

source_refs: ""

[[SECTION markdown]]

# The Puppy
**Role:** Encountered Entity

**Status:** Physically present.

**Physical Description:** An enormous dog encountered in the woods.

**Costume & Traits:** Massive scale compared to Alice.

**Prompt Phrases:** Enormous puppy, giant dog, playful massive beast.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: blue_caterpillar

canonical_character_id: CH005 Blue Caterpillar

aliases: ""

is_fully_identified: true

manual_description_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: caterpillar

morphology_hint: large insectoid

scale_hint: large/significant

renderability_hint: high

confidence: 0.8

direct_identity_evidence: true

direct_visual_evidence: true

costume_or_covering_evidence: false

movement_evidence: false

associated_entities: Alice

alias_or_role_evidence: ""

unknowns: ""

source_refs: ""

[[SECTION markdown]]

# Blue Caterpillar
**Role:** Mysterious Entity

**Status:** Physically present.

**Physical Description:** A large blue caterpillar sitting on top of a mushroom.

**Costume & Traits:** Smoking a hookah.

**Prompt Phrases:** Large blue caterpillar, smoking hookah, mushroom dweller.

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
