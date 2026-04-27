# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:36:58.700876+00:00
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
- [alice](#alice)
- [white_rabbit](#white_rabbit)
- [bill](#bill)
- [the_puppy](#the_puppy)
- [blue_caterpillar](#blue_caterpillar)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH002 Alice
aliases: Mary Ann
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biquped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: white_rabbit, bill, the_puppy, blue_caterpillar
alias_or_role_evidence: true
unknowns: false
source_refs: CH004

[[SECTION markdown]]
# Alice
**Role:** Protagonist / Explorer

**Status:** Physically Present (Variable Size)

**Physical Description:** 
A young girl of human proportions. In this chapter, her size fluctuates wildly from giant-sized (filling a house/pressing against the ceiling) to human-scale after eating a cake.

**Costume & Silhouette:** 
Specific clothing details are not provided in this chapter, though she is mistaken for a housemaid named "Mary Ann."

**Notes for Rendering:** 
Focus on her shifting scale relative to her environment (the house, the wood, and the puppy). She is resourceful but prone to anxiety due to her size changes.
[[/SECTION]]
[[/FILcut_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH001 White Rabbit
aliases: W. Rabbit
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
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: alice, bill
alias_or_role_evidence: true
unknowns: false
source_refs: CH004

[[SECTION markdown]]
# The White Rabbit
**Role:** Anxious Antagonist / Catalyst

**Status:** Physically Present

**Physical Description:** 
A rabbit-sized creature with an authoritative yet temperamental demeanor.

**Costume & Silhouette:** 
The text mentions a nameplate "W. RABBIT" on his house, implying he is the master of the residence.

**Notes for Rendering:** 
He should appear frantic and prone to outbursts as he searches for his lost fan and gloves.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill
canonical_character_id: CH003 Bill
aliases: Pat
is_fully_identified: false
manual_description_required: true
manual_description_reason: The text uses "Pat" and "Bill" interchangeably for a creature falling down the chimney, but its exact species is ambiguous (lizard vs. animal).
clarification_required: true
clarification_reason: Is Bill/Pat a lizard or another type of small animal?
clarification_question: What is the specific morphology of the creature known as Bill/Pat?
character_type_hint: unknown
morphology_hint: unknown
scale_hint: tiny
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: white_rabbit, alice
alias_or_role_evidence: true
unknowns: true
source_refs: CH004

[[SECTION markdown]]
# Bill (Pat)
**Role:** Chaotic Element / Victim of Circumstance

**Status:** Physically Present

**Physical Description:** 
A small creature that falls down a chimney and is kicked out of a house. The text suggests he might be a lizard or a similar small animal.

**Costume & Silhouette:** 
Small, agile enough to be sent flying like a "Jack-t-the-box."

**Notes for Rendering:** 
The identity is somewhat fluid in the text; should be rendered as a small, much-handled creature.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_puppy
canonical_character_id: CH005 The Puppy
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: large
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: true
associated_entities: alice
alias_or_role_evidence: false
unknowns: false
source_refs: CH004

[[SECTION markdown]]
# The Puppy
**Role:** Playful Obstacle

**Status:** Physically Present

**Physical Description:** 
An enormous dog-like creature encountered in the wood.

**Costume & Silhouette:** 
Large scale relative to Alice.

**Notes for Rendering:** 
The puppy is massive, requiring a stick for interaction. It represents a sudden burst of energy/scale in the forest setting.
[[
/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: blue_caterpillar
canonical_character_id: CH006 Blue Caterpillar
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: multi_legged
scale_hint: large
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: alice
alias_or_role_evidence: false
unknowns: false
source_refs: CH004

[[SECTION markdown]]
# The Blue Caterpillar
**Role:** Mysterious Observer

**Status:** Physically Present (Discovered)

**Physical Description:** 
A large blue caterpillar.

**Costume & Silhouette:** 
Large enough to sit atop a mushroom and smoke a hookah.

**Notes for Rendering:** 
The character is seen peering over the top of a mushroom, suggesting a massive or elevated presence. The smoking of a hookah adds a surreal, calm element to its appearance.
[[/SECTION]]
[[cut_record]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
