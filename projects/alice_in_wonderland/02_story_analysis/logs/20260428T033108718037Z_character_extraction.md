# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:31:08.718037+00:00
- task: character_extraction

## System Prompt
````text
You are FilmCreator's chapter analysis engine.
Return only FilmCreator packets with the requested sections and records.
Do not wrap the packet in code fences unless explicitly requested.
Do not produce JSON-only responses.
If a packet asks for markdown sections, emit the section name on its own line and wrap the body in [[SECTION ...]] ... [[/SECTION]].
Do not put another [[SECTION ...]] tag inside a section body.
Copy every FILMCREATOR structural tag literally.
Do not rename, translate, partially rewrite, or decorate any PACKET, RECORD, or SECTION tag.
The only valid closing tags are [[/FILMCREATOR_PACKET]], [[/FILMCREATOR_RECORD]], and [[/SECTION]].
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



Literal tag rules:

- begin with [[FILMCREATOR_PACKET]] on its own line

- end with [[/FILMCREATOR_PACKET]] on its own line

- wrap each character item in [[FILMCREATOR_RECORD]] ... [[/FILMCREATOR_RECORD]]

- use [[SECTION character_index_markdown]] and [[SECTION markdown]] exactly as written

- do not invent alternate closing tags such as [[/FIL_RECORD]], [[end_section]], or misspelled FILMCREATOR tags

- do not echo this instruction block back as an example packet; return the actual packet only



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

**Location: The Hall / The Garden Door Subzone**
*   **Visual State:** Alice is giant-sized, standing over nine feet tall. Her feet appear extremely distant from her perspective.
*   **Event:** Alice experiences a growth spurt/size shift; she looks down at her feet and contemplates sending them Christmas presents via carrier.
*   **Action:** Alice's head strikes the roof of the hall. She picks up a small golden key.
*   **Action:** Alice moves to the garden door, lying on her side to peer through it. The door is too small for her current size.
*   **Event/Visual:** Alice begins to cry intensely. Her tears create a large pool of salt water, approximately four inches deep, spreading halfway down the hall.

**Location: The Hall (Near the Pool)**
*   **Character Entrance:** The White Rabbit enters, trotting hurriedly. He is dressed splendidly and carries white kid gloves in one hand and a large fan in the other. He mutters about "the Duchess."
*   **Interaction:** Alice attempts to speak to the Rabbit.
*   **Reaction:** The Rabbit starts violently, drops the white kid gloves and the fan, and scurries away into the darkness.
*   **Action/Object Interaction:** Alice picks up the fan and the gloves. She uses the fan to cool herself due to the heat in the hall.
*   **Internal State/Dialogue:** Alice undergoes an identity crisis, attempting to verify her identity through math (fails), geography (fails), and reciting poetry ("How doth the little crocodile"). Her voice sounds hoarse and strange during recitation.
*   **Visual Shift:** Alice notices she is wearing one of the Rabbit's white kid gloves. She realizes she is shrinking.
*   **Action/Measurement:** Alice stands by a table to measure herself; she is now approximately two feet high.
*   **Object Interaction/Risk:** Alice discovers the fan causes her to shrink. She drops the fan hastily to prevent shrinking into non-existence.
*   **Event:** Alice runs to the garden door, but it is shut. The golden key is back on the glass table.

**Location: The Pool of Tears**
*   **Event/Visual:** Alice slips and falls into the pool of salt water she previously created. She is submerged up to her chin.
*   **Character Entrance:** A Mouse enters the pool, swimming nearby.
*   **Interaction:** Alice attempts to communicate with the Mouse using formal "O Mouse" address and then French ("Où est ma chatte?").
*   **Reaction:** The Mouse leaps in fright at the mention of cats.
*   **Dialogue/Conflict:** Alice tries to soothe the Mouse by describing her cat, Dinah. This causes the Mouse to become highly offended and "bristle." Alice attempts to pivot to talking about a dog, which also offends the Mouse (due to its association with killing rats).
*   **Character Exit/Movement:** The Mouse swims away in a commotion but returns after Alice promises not to mention cats or dogs.
*   **Character Entrance/Group Assembly:** A crowd of animals enters the pool: a Duck, a Dodo, a Lory, an Eaglet, and other creatures.
*   **Action:** Alice leads the group (the "party") swimming toward the shore to escape the crowded pool.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
[[markdown]]
# Character Index - Chapter CH002

- [Alice](#alice)
- [White Rabbit](#white_rabbit)
- [The Duchess](#the_duchess) (referenced)
- [Mouse](#mouse)
- [Dinah](#dinah) (referenced)
- [Duck](#duck)
- [Dodo](#dodo)
- [Lory](#lory)
- [Eaglet](#eaglet)

[[/markdown]]
[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: "Alice is the protagonist throughout the chapter."
direct_visual_evidence: "Described as giant-sized (9ft+), then shrinking to two feet, then submerged in a pool of tears."
costume_or_covering_evidence: "Wears one of the Rabbit's white kid gloves at one point."
movement_evidence: "Walking, lying on her side, crying, running, slipping/falling into water, swimming."
associated_entities: ["white_rabbit", "mouse", "duck", "dodo", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
[[markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present (Dynamic Scale)

**Physical Description:**
Alice undergoes extreme size fluctuations in this chapter. Initially, she is a giant standing over nine feet tall. Later, she shrinks to approximately two feet in height. She has a voice that becomes hoarse and strange during her identity crisis.

**Costume & Silhouette:**
Her specific clothing details are sparse, but she is noted to be wearing one of the White Rabbit's white kid gloves during her shrinking phase.

**Descriptive Noun Phrases:**
- Giant girl (9ft+)
- Tiny girl (2ft)
- Swimming girl in a pool of salt water
- Girl with hoarse voice

**Uncertainty Notes:**
Specific colors and textures of her primary outfit are not detailed in this chapter text.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: ["Rabbit"]
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
confidence: 1.0
direct_identity_evidence: "Identified as the White Rabbit."
direct_visual_evidence: "Dressed splendidly, carries white kid gloves and a large fan."
costume_or_covering_evidence: "Splendidly dressed; carries white kid gloves and a large fan."
movement_evidence: "Trotting hurriedly, starting violently, scurrying away into darkness."
associated_entities: ["alice", "the_duchess"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
[[markdown]]
# White Rabbit
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A rabbit that moves with human-like urgency.

**Costume & Silhouette:**
Dressed "splendidly." He carries two distinct props: white kid gloves in one hand and a large fan in the other.

**Descriptive Noun Phrases:**
- Splendidly dressed rabbit
- Hurried rabbit with gloves and fan
- Scuttling rabbit

**Uncertainty Notes:**
The specific style of his "splendid" clothing (e.g., waistcoat, coat) is not explicitly defined.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only mentioned by name as a subject of the Rabbit's muttering; no physical description provided."
clarification_required: true
clarification_reason: "Only a verbal reference exists."
clarification_question: "What is the Duchess's physical appearance and species?"
character_type_hint: unknown
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.1
direct_identity_evidence: ""
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "Mentioned by the White Rabbit."
unknowns: ["physical appearance", "species", "scale"]
source_refs: []
[[SECTION markdown]]
[[markdown]]
# The Duchess
**Role:** Referenced Character

**Status:** Referenced Only

**Physical Description:**
No physical description is provided in this chapter.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Mentioned Duchess

**Uncertainty Notes:**
Extremely low information. The character exists only as a name mentioned by the White Rabbit.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mouse
canonical_character_id: mouse
aliases: ["O Mouse"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: "Identified as a Mouse."
direct_visual_evidence: "Swimming in the pool of tears."
costume_or_covering_evidence: ""
movement_evidence: "Swimming, leaping in fright, bristling, swimming away, returning."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
[[markdown]]
# Mouse
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A small creature capable of swimming in a pool of salt water.

**Costume & Silhouette:**
None mentioned.

**Descriptive Noun Phrases:**
- Swimming mouse
- Offended, bristling mouse

**Uncertainty Notes:**
Specific breed or color is not specified.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: ["Alice's cat"]
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Character is only mentioned by Alice; no visual description provided."
clarification_required: true
clarification_reason: "Only a verbal reference exists."
clarification_question: "What does Dinah look like (color, breed, size)?"
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: ""
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: "Alice refers to her as 'my cat, Dinah'."
unknowns: ["physical appearance"]
source_refs: []
[[SECTION markdown]]
[[markdown]]
# Dinah
**Role:** Referenced Character

**Status:** Referenced Only

**Physical Description:**
None provided. Known to be a cat.

**Costume & Silhouette:**
Unknown.

**Descriptive Noun Phrases:**
- Alice's cat

**Uncertainty Notes:**
The character is mentioned in dialogue but does not appear on screen.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duck
canonical_character_id: duck
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Identified as a Duck."
direct_visual_evidence: "Part of the crowd of animals entering the pool."
costume_or_covering_evidence: ""
movement_evidence: "Swimming toward the shore."
associated_entities: ["alice", "dodo", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
[[markdown]]
# Duck
**Role:** Background Character / Party Member

**Status:** Physically Present

**Physical Description:**
A duck that is part of a group of animals swimming in the pool.

**Costume & Silhouette:**
None mentioned.

**Descriptive Noun Phrases:**
- Swimming duck
- Part of the animal party

**Uncertainty Notes:**
Specific color or breed not specified.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dodo
canonical_character_id: dodo
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Identified as a Dodo."
direct_visual_evidence: "Part of the crowd of animals entering the pool."
costume_or_covering_evidence: ""
movement_evidence: "Swimming toward the shore."
associated_entities: ["alice", "duck", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
[[markdown]]
# Dodo
**Role:** Background Character / Party Member

**Status:** Physically Present

**Physical Description:**
A dodo bird that is part of a group of animals swimming in the pool.

**Costume & Silhouette:**
None mentioned.

**Descriptive Noun Phrases:**
- Swimming dodo
- Part of the animal party

**Uncertainty Notes:**
Specific visual details are not provided beyond species identification.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lory
canonical_character_id: lory
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Identified as a Lory."
direct_visual_evidence: "Part of the crowd of animals entering the pool."
costume_or_covering_evidence: ""
movement_evidence: "Swimming toward the shore."
associated_entities: ["alice", "duck", "dodo", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
[[markdown]]
# Lory
**Role:** Background Character / Party Member

**Status:** Physically Present

**Physical Description:**
A lory (parrot) that is part of a group of animals swimming in the pool.

**Costume & Silhouette:**
None mentioned.

**Descriptive Noun Phrases:**
- Swimming lory
- Part of the animal party

**Uncertainty Notes:**
Specific color/plumage details are not provided.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: eaglet
canonical_character_id: eaglet
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: "Identified as an Eaglet."
direct_visual_evidence: "Part of the crowd of animals entering the pool."
costume_or_covering_evidence: ""
movement_evidence: "Swimming toward the shore."
associated_entities: ["alice", "duck", "dodo", "lory"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
[[markdown]]
# Eaglet
**Role:** Background Character / Party Member

**Status:** Physically Present

**Physical Description:**
An eaglet that is part of a group of animals swimming in the pool.

**Costume & Silhouette:**
None mentioned.

**Descriptive Noun Phrases:**
- Swimming eaglet
- Part of the animal party

**Uncertainty Notes:**
Specific visual details are not provided beyond species identification.
[[/markdown]]
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
