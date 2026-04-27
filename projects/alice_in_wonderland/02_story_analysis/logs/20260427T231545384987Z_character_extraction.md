# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-27T23:15:45.384987+00:00
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

Chapter id: CH002

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

**Location: The Hall / The Garden Door**
- **Visual State:** Alice is giant (over nine feet tall). Her head strikes the ceiling of the hall.
- **Event:** Alice looks down at her feet, which appear distant and small from her perspective. She contemplates sending boots to her feet via carrier.
- **Object Interaction:** Alice picks up a little golden key.
- **Action:** Alice hurries toward the garden door but finds she is too large to fit through. She sits and cries.
- **Environmental Change:** As Alice cries, a pool of salt water forms around her, roughly four inches deep, covering half the hall.

**Character Entrance: The White Rabbit**
- **Entrance:** The White Rabbit trots into the hall in a hurry. He is dressed splendidly, carrying white kid gloves and a large fan.
- **Action/Dialogue:** The Rabbit mutters about "the Duchess." Alice attempts to speak to him.
- **Reaction:** The Rabbit starts violently, drops the gloves and the fan, and scurries into the darkness.
- **Object Interaction:** Alice picks up the fan and the gloves.

**Character Internal State: Identity Crisis**
- **Action:** Alice fans herself due to the heat. She undergoes a philosophical monologue regarding her identity (questioning if she is "Mabel").
- **Action/Dialogue:** Alice attempts to recite multiplication tables and geography, but fails. She attempts to recite "How doth the little crocodile," but her voice sounds hoarse and strange.
- **Visual Reveal:** Alice realizes she has accidentally put on one of the Rabbit's white kid gloves.

**Physical Transformation: Shrinking**
- **Action/Scale Shift:** Alice stands by a table to measure herself; she is now approximately two feet high and shrinking rapidly.
- **Object Interaction:** She discovers the fan causes the shrinking and drops it to stabilize her size.
- **Action:** Alice runs back to the garden door, but finds it shut and the golden key sitting on the glass table.
- **Environmental Shift:** Alice slips and falls into the pool of tears. She is now swimming in salt water up to her chin.

**Character Interaction: The Mouse**
- **Event:** Alice hears splashing and swims toward a creature she initially thinks is a walrus or hippopotamus, but identifies as a Mouse.
- **Dialogue/Interaction:** Alice addresses the Mouse in formal English ("O Mouse"), then switches to French ("Où est ma chatte?") to test its intelligence.
- **Reaction:** The Mouse becomes agitated and offended by the mention of "cats." 
- **Conflict:** Alice tries to soothe the Mouse by mentioning her cat Dinah and a terrier dog, but these topics only make the Mouse more distressed/offended.
- **Resolution of Interaction:** The Mouse agrees to swim to the shore to tell its history once they are out of the water.

**Group Event: The Escape to Shore**
- **Environmental Change:** The pool becomes crowded with various animals (a Duck, a Dodo, a Lory, an Eaglet).
- **Action:** Alice leads the group of animals/birds swimming toward the shore to exit the pool.
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
- [The White Rabbit](#the_white_rabbit)
- [The Mouse](#the_mouse)
- [Dinah](#dinah)
- [The Duck](#the_duck)
- [The Dodo](#the_dodo)
- [The Lory](#the_lory)
- [The Eaglet](#the_eaglet)

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: alice

canonical_character_id: CH002 Alice

aliases: Mabel (suspected identity)

is_fully_identified: true

manual_description_required: true

manual_description_reason: Rapidly changing scale and physical state.

clarification_required: true

clarification_reason: Scale is highly dynamic throughout the chapter.

clarification_question: What is Alice's exact height at the moment of interaction with the Mouse?

character_type_hint: human girl

morphology_hint: human female, child-like

scale_hint: variable (9ft -> 2ft)

renderability_hint: high; requires scale-relative environment assets.

confidence: 0.9

direct_identity_evidence: Named as Alice.

direct_visual_evidence: Described as giant (9ft), then shrinking (2ft).

costume_or_covering_evidence: Accidentally wearing one of the White Rabbit's white kid gloves.

movement_evidence: Walking, sitting/crying, running, swimming.

associated_entities: The White Rabbit, The Mouse, Dinah

alias_or_role_evidence: Questions if she is "Mabel".

unknowns: Exact facial features not specified.

[[SECTION markdown]]

# Alice
**Role:** Protagonist

**Status:** Physically Present (Dynamic Scale)

**Physical Description:** 
A girl who undergoes extreme scale shifts, starting at over nine feet tall and shrinking to approximately two feet. She is seen swimming in a pool of salt water.

**Costume & Traits:** 
Accidentally wears a white kid glove belonging to the White Rabbit.

**Uncertainty Notes:** 
Her identity is internally questioned (is she "Mabel"?); her physical scale is highly unstable during this chapter.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_white_rabbit

canonical_character_id: CH002 White Rabbit

aliases: The Rabbit

is_fully_identified: true

manual_description_required: true

manual_description_reason: Specific costume/accessory details provided.

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: anthropomorphic animal

morphology_hint: rabbit

scale_hint: small (relative to Alice's giant state)

renderability_hint: high; requires specific accessories.

confidence: 0.95

direct_identity_evidence: Named as The White Rabbit.

direct_visual_evidence: Described as wearing splendid clothes, carrying white kid gloves and a large fan.

costume_or_covering_evidence: Splendidly dressed; carries white kid gloves and a large fan.

movement_evidence: Trots in a hurry; starts violently; scurries into darkness.

associated_entities: Alice, The Duchess (referenced)

alias_or_role_evidence: ""

unknowns: Specific color of the "splendid" clothing.

[[SECTION markdown]]

# The White Rabbit
**Role:** Supporting Character

**Status:** Physically Present (Briefly)

**Physical Description:** 
A rabbit dressed in splendid attire.

**Costume & Traits:** 
Carries white kid gloves and a large fan.

**Uncertainty Notes:** 
His exact clothing colors are not specified, only described as "splendid."

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: the_mouse

canonical_character_id: CH002 Mouse

aliases: O Mouse

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: true

clarification_reason: Initial visual confusion with other animals.

clarification_question: What is the specific breed/appearance of the mouse?

character_type_hint: animal

morphology_hint: rodent

scale_hint: small

renderability_hint: medium; part of a crowded pool scene.

confidence: 0.8

direct_identity_evidence: Identified by Alice as a Mouse after initial confusion.

direct_visual_evidence: Seen swimming in the salt water pool.

costume_or_covering_evidence: ""

movement_evidence: Swimming, becoming agitated/offended.

associated_entities: Alice, Dinah (referenced)

alias_or_role_evidence: ""

unknowns: Specific color or fur texture.

[[SECTION markdown]]

# The Mouse
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:** 
A small creature swimming in the pool of tears.

**Costume & Traits:** 
Highly sensitive to mentions of cats and terriers.

**Uncertainty Notes:** 
Initially mistaken by Alice for a walrus or hippopotamus.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: dinah

canonical_character_id: CH002 Dinah

aliases: ""

is_fully_identified: true

manual_description_required: false

manual_description_reason: ""

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: cat

morphology_hint: feline

scale_hint: small/medium

renderability_hint: low (referenced only)

confidence: 0.7

direct_identity_evidence: Named as Dinah; identified as Alice's cat.

direct_visual_evidence: None (referenced).

costume_or_covering_evidence: ""

movement_evidence: ""

associated_entities: Alice, The Mouse

alias_or_role_evidence: ""

unknowns: Physical appearance/color.

[[SECTION markdown]]

# Dinah
**Role:** Referenced Character

**Status:** Referenced (Not physically present)

**Physical Description:** 
A cat belonging to Alice.

**Costume & Traits:** 
Mentioned as a source of distress for the Mouse.

**Uncertainty Notes:** 
No visual description provided in this chapter.

[[/SECTION]]

[[FILMCREATOR_RECORD]]

type: character

asset_id: group_animals

canonical_character_id: CH002 Group Animals

aliases: ""

is_fully_identified: false

manual_description_required: true

manual_description_reason: This is a collection of distinct entities.

clarification_required: false

clarification_reason: ""

clarification_question: ""

character_type_hint: various animals/birds

morphology_hint: avian and aquatic/semi-aquatic

scale_hint: small

renderability_hint: medium; group shot.

confidence: 0.6

direct_identity_evidence: Identified as a group of animals/birds in the pool.

direct_visual_evidence: Seen swimming toward the shore with Alice.

costume_or_covering_evidence: ""

movement_evidence: Swimming toward the shore.

associated_entities: Alice

alias_or_role_evidence: ""

unknowns: Individual descriptions for most members.

[[SECTION markdown]]

# Group Animals
**Role:** Background/Ensemble Characters

**Status:** Physically Present (Group)

**Physical Description:** 
A collection of various animals and birds swimming in the pool.

**Costume & Traits:** 
Includes a Duck, a Dodo, a Lory, and an Eaglet.

**Uncertainty Notes:** 
Individual physical traits for the Duck, Dodo, Lory, and Eaglet are not detailed beyond their species names.

[[/SECTION]]

[[/FILMCREATOR_PACKET]]
````
