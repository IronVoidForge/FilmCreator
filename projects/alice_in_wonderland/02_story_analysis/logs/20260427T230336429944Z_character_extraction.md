# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:03:36.429944+00:00
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

Chapter id: CH001

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



Entity taxonomy rules:

- identify what the entity itself appears to be, not what it wears or rides

- do not confuse nearby/associated things with the entity

- if source says a person rides a mount, classify the person separately from the mount

- if source says a character wears foreign/alien/exotic clothing, do not change their species/type

- character_type_hint: human, humanoid_nonhuman, animal, creature, group, object, machine, abstract, unknown

- morphology_hint: biped, quadruped, multi_legged, serpentine, winged, constructed, amorphous, unknown

- scale_hint: tiny, small, human_scale, large, giant, unknown

- renderability_hint: renderable, context_only, alias_or_role, unknown

- confidence: 0.0 to 1.0 for each type/morphology/renderability hint

- if uncertain, use unknown and explain the missing evidence in the markdown section



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
- A riverbank (sunny, hot day).
- A large rabbit-hole under a hedge.
- A deep vertical well/tunnel lined with cupboards, bookshelves, maps, and pictures.
- A long, low hall lit by a row of hanging lamps, featuring many locked doors.
- A small passage (rat-hole sized) leading to a lush garden with bright flowers and fountains.

**Characters:**
- Alice: A young girl, curious and prone to internal monologue/self-instruction.
- The White Rabbit: An anthropomorphic rabbit wearing a waistcoat and carrying a watch.
- Alice's Sister: Present on the bank at the start.
- Dinah: Alice's cat (mentioned in thought).

**Key Events & Transitions:**
- **The Bank:** Alice sits by her sister, feeling bored/sleepy. The White Rabbit runs past, checking a watch from its waistcoat pocket.
- **The Chase:** Alice chases the Rabbit to the hedge and follows it down the rabbit-hole.
- **The Fall:** Alice falls down a deep well/tunnel. 
    - *Visual Detail:* The walls are lined with cupboards and bookshelves. 
    - *Object Interaction:* Alice grabs an empty "ORANGE MARMALADE" jar from a shelf and places it in a cupboard to avoid dropping it.
    - *Internal State:* Alice talks to herself about the center of the earth, latitude/longitude, and her cat Dinah.
- **The Landing:** Alice hits a heap of sticks and dry leaves at the bottom.
- **The Hallway:** Alice follows the White Rabbit into a long, lamp-lit hall. She discovers all the doors are locked.
- **The Discovery (Key):** Alice finds a three-legged glass table with a tiny golden key. The key is too small for the large doors.
- **The Discovery (Door):** Alice finds a low curtain hiding a small door (15 inches high). She uses the golden key; it fits.
- **The Garden Reveal:** Through the small door, Alice sees a beautiful garden but realizes she is too large to fit through.
- **The Transformation (Shrinking):** Alice finds a bottle labeled "DRINK ME" on the glass table. She tastes it (flavor: cherry-tart, custard, pineapple, roast turkey, toffee, and hot buttered toast) and shrinks to ten inches tall.
- **The Conflict:** Now small enough for the door, she realizes she left the golden key on top of the high glass table. She tries to climb the slippery table leg but fails and cries.
- **The Transformation (Cake):** Alice finds a glass box under the table containing a cake labeled "EAT ME." 
- **The Decision:** Alice eats the cake, hoping it will either make her large enough to reach the key or small enough to fit under the door. After eating it, she remains the same size.
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
- [White Rabbit](#white_rabbit)
- [Alice's Sister](#alices_sister)
- [Dinah](#dinah)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: alice

canonical_character_id: CH001 Alice

aliases: Girl

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: "Alice is the primary actor throughout the chapter."

direct_visual_evidence: "She interacts with objects, eats cake/drinks liquid, and undergoes size changes."

costume_or_covering_evidence: ""

movement_evidence: "Chases rabbit, falls down a hole, climbs table legs, cries."

associated_entities: White Rabbit, Dinah, Alice's Sister

alias_or_role_evidence: "Identified as 'Alice'."

unknowns: ""

[[SECTION markdown]]

# Alice
**Role:** Protagonist

**Status:** Physically Present (undergoes size changes)

**Physical Description:** A young girl. While specific hair/eye color is not explicitly detailed in this chapter, she is a human child capable of significant scale shifts.

**Size/Scale:** Starts at human scale; shrinks to ten inches tall after drinking from the "DRINK ME" bottle; returns to original size after eating the "EAT ME" cake.

**Key Traits:** Curious, prone to internal monologue, highly observant of her surroundings (noting flavors like cherry-tart and custard).

[[/SECTION]]

[[FILMCREA_RECORD]]

type: character

asset_id: white_rabbit

canonical_character_id: CH001 White Rabbit

aliases: The Rabbit

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: renderable

confidence: 0.8

direct_identity_evidence: "Identified as the White Rabbit."

direct_visual_evidence: "Seen running past with a watch in a waistcoat pocket."

costume_or_covering_evidence: "Wearing a waistcoat and carrying a watch."

movement_evidence: "Runs past Alice, leads her into the hall."

associated_entities: Alice

alias_or_role_evidence: "The White Rabbit."

unknowns: ""

[[SECTION markdown]]

# The White Rabbit
**Role:** Catalyst / Recurring Figure

**Status:** Physically Present

**Physical Description:** An anthropomorphic rabbit.

**Costume/Silhouette:** Wears a waistcoat and carries a watch.

**Key Traits:** Hurried, preoccupied with time.

[[/SECTION]]

[[FILMCREA_RECORD]]

type: character

asset_id: alices_sister

canonical_character_id: CH001 Alice's Sister

aliases: Sister

is_fully_identified: true

manual_description_required: true

manual_description_reason: Only mentioned as sitting on the bank; no physical description provided.

clarification_required: true

clarification_reason: Physical appearance is entirely absent from the text.

clarification_question: What does Alice's sister look like?

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.5

direct_identity_evidence: "Identified as Alice's sister."

direct_visual_evidence: ""

costume_or_covering_evidence: ""

movement_evidence: "Sitting on the bank."

associated_entities: Alice

alias_or_role_evidence: "Alice's Sister."

unknowns: "Physical appearance, clothing, and age relative to Alice."

[[SECTION markdown]]

# Alice's Sister
**Role:** Supporting Character (Reference)

**Status:** Physically Present (at the start)

**Physical Description:** No physical description provided in this chapter.

**Uncertainty Note:** She is a static presence at the beginning of the story, serving as a foil to Alice's boredom/curiosity.

[[/SECTION]]

[[FILMCREA_RECORD]]

type: character

asset_id: dinah

canonical_character_id: CH001 Dinah

aliases: Cat

is_fully_identified: true

manual_description_required: true

manual_description_reason: Only mentioned in thought; no visual description provided.

clarification_required: true

clarification_reason: No physical traits (color, breed) are given.

clarification_question: What color/breed is Dinah the cat?

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: context_only

confidence: 0.4

direct_identity_evidence: "Identified as Alice's cat."

direct_visual_evidence: ""

costume_or_covering_evidence: ""

movement_evidence: ""

associated_entities: Alice

alias_or_role_evidence: "Alice's cat Dinah."

unknowns: "Visual appearance and physical presence in the scene."

[[SECTION markdown]]

# Dinah
**Role:** Referenced Character

**Status:** Referenced (in thought)

**Physical Description:** A cat, but no specific visual details are provided.

**Uncertainty Note:** Dinah is not physically present in the scene; she is a mental reference for Alice.

[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
