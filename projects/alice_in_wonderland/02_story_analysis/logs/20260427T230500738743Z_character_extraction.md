# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:05:00.738743+00:00
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
- [The White Rabbit](#the-white-rabbit)
- [Alice's Sister](#alices-sister)
- [Dinah](#dinah)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: alice

canonical_character_id: Alice

aliases: Girl, Young girl

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Alice is explicitly named and acts as the protagonist throughout the fall and transformations.

direct_visual_evidence: Described as a young girl; undergoes size changes from human scale to ten inches tall.

costume_or_covering_evidence: Not explicitly detailed in this chapter, though she interacts with various objects.

movement_evidence: Chases the rabbit, falls down a well, climbs a table leg, eats cake/drinks liquid.

associated_entities: The White Rabbit, Alice's Sister, Dinah, Golden Key

alias_or_role_evidence: Referred to as "Alice" and "the girl".

unknowns: Specific hair color or clothing color not provided in this chapter.

[[SECTION markdown]]

# Alice
**Role:** Protagonist

**Status:** Physically Present

**Description:** A young girl characterized by intense curiosity and a tendency toward internal monologue. She experiences significant scale shifts, shrinking to ten inches tall after drinking from the "DRINK ME" bottle, but remaining at her original size after eating the "EAT ME" cake.

**Visual Traits:** 
- Scale: Human scale (initially), then tiny (10 inches).
- Key interactions: Grabs an orange marmalade jar; uses a golden key; eats cake and drinks from a bottle.

**Uncertainty Notes:** Specific clothing colors and hair details are not explicitly defined in this chapter, requiring stylistic choice for rendering.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: white_rabbit

canonical_character_id: The White Rabbit

aliases: Rabbit

is_fully_identified: true

manual_description_required: false

manual_description_reason: 

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: renderable

confidence: 0.9

direct_identity_evidence: Explicitly named as The White Rabbit.

direct_visual_evidence: An anthropomorphic rabbit wearing a waistcoat and carrying a watch.

costume_or_covering_evidence: Wears a waistcoat; carries a watch in its pocket.

movement_evidence: Runs past Alice, enters the rabbit-hole, leads Alice into the hall.

associated_entities: Alice

alias_or_role_evidence: Referred to as "the Rabbit".

unknowns: Specific breed or exact color of fur beyond "white".

[[SECTION markdown]]

# The White Rabbit
**Role:** Catalyst / Supporting Character

**Status:** Physically Present

**Description:** An anthropomorphic rabbit that initiates the adventure by running past Alice and leading her into the rabbit-hole.

**Visual Traits:** 
- Type: Anthropomorphic rabbit.
- Costume: Wears a waistcoat.
- Accessory: Carries a watch.
- Scale: Small/Animal scale.

**Uncertainty Notes:** While "white" is in the name, specific fur texture or exact waistcoat color is not specified.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: alices_sister

canonical_character_id: Alice's Sister

aliases: Sister

is_fully_identified: true

manual_description_required: true

manual_description_reason: Only present at the very beginning; no physical description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: human

morphology_hint: biped

scale_hint: human_scale

renderability_hint: context_only

confidence: 0.7

direct_identity_evidence: Identified as Alice's sister sitting on the bank.

direct_visual_evidence: None.

costume_or_covering_evidence: None.

movement_evidence: Sitting on the riverbank reading.

associated_entities: Alice

alias_or_role_evidence: 

unknowns: Physical appearance, age (beyond being older than Alice), and clothing.

[[SECTION markdown]]

# Alice's Sister
**Role:** Supporting Character (Introductory)

**Status:** Physically Present (briefly)

**Description:** Alice's sister who is sitting on the riverbank at the start of the story.

**Visual Traits:** 
- Scale: Human scale.
- Appearance: Unknown.

**Uncertainty Notes:** Very little visual information is provided; she serves primarily to establish the initial setting before Alice follows the rabbit.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dinah

canonical_character_id: Dinah

aliases: Cat

is_fully_identified: true

manual_description_required: true

manual_description_reason: Only mentioned in thought; no visual description provided.

clarification_required: false

clarification_reason: 

clarification_question: 

character_type_hint: animal

morphology_hint: quadruped

scale_hint: small

renderability_hint: context_only

confidence: 0.6

direct_identity_evidence: Named as Alice's cat in her internal monologue.

direct_visual_evidence: None (referenced only).

costume_or_covering_evidence: None.

movement_evidence: None.

associated_entities: Alice

alias_or_role_evidence: 

unknowns: Breed, color, or physical appearance of the cat.

[[SECTION markdown]]

# Dinah
**Role:** Referenced Character

**Status:** Referenced (not physically present)

**Description:** Alice's cat, mentioned during her descent down the well as part of her internal monologue.

**Visual Traits:** 
- Type: Cat.
- Scale: Small/Animal scale.

**Uncertainty Notes:** No physical description is provided in this chapter; she is a mental reference for Alice.
[[/SECTION]]

[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
