# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:01:03.178771+00:00
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
*   **Visual State:** Alice is giant (over nine feet tall). Her feet are distant and small from her perspective.
*   **Event:** Alice experiences a growth spurt/size shift, observing her feet as being far away. She contemplates the logistics of sending boots to her feet via carrier.
*   **Action:** Alice's head strikes the ceiling of the hall. She picks up a **small golden key**.
*   **Action:** Alice moves to the garden door. She lies on her side to peer through the keyhole into the garden, but she is too large to pass through.

**Location: The Hall (The Pool of Tears)**
*   **Visual State:** Alice begins crying profusely. A pool of salt water forms around her, approximately four inches deep, extending halfway down the hall.
*   **Character Entrance:** The **White Rabbit** enters, trotting hurriedly. He is dressed splendidly and carries **white kid gloves** and a **large fan**. He mutters about "the Duchess."
*   **Interaction:** Alice attempts to speak to the Rabbit. The Rabbit reacts violently, drops the **gloves** and the **fan**, and scurries away into the darkness.
*   **Action/Object Interaction:** Alice picks up the fan and gloves. She uses the fan to cool herself due to the heat in the hall.
*   **Character Internal State:** Alice undergoes an identity crisis, attempting to verify her identity through math (fails), geography (fails), and reciting poetry (the "Crocodile" poem). Her voice sounds hoarse/strange during recitation.
*   **Visual State/Transformation:** Alice notices she is wearing one of the Rabbit's white kid gloves. She measures herself against a table; she has shrunk to approximately two feet tall.
*   **Action/Object Interaction:** Alice realizes the **fan** is causing her to shrink. She drops it to stop the process.
*   **Event:** Alice runs to the garden door, but finds it shut. The **golden key** is back on the glass table.
*   **Visual State/Shift:** Alice slips and falls into the pool of tears. She is now submerged up to her chin in salt water.

**Location: The Pool (Submerged)**
*   **Character Entrance:** A **Mouse** enters the pool, splashing nearby.
*   **Interaction:** Alice attempts to communicate with the Mouse using formal/Latin-inspired address ("O Mouse"). 
*   **Action/Dialogue:** Alice speaks French ("Où est ma chatte?") to the Mouse. The Mouse reacts with fright and indignation.
*   **Conflict:** Alice tries to soothe the Mouse by talking about her cat, **Dinah**. This offends the Mouse, who declares a family hatred for "nasty, low, vulgar" cats.
*   **Conflict:** Alice attempts to pivot the conversation to dogs (a terrier). The Mouse becomes increasingly agitated and swims away.
*   **Resolution/Exit:** Alice calls the Mouse back. The Mouse agrees to tell its history once they reach the shore.
*   **Character Entrance (Mass):** A crowd of animals enters the pool: a **Duck**, a **Dodo**, a **Lory**, an **Eaglet**, and other creatures.
*   **Action:** Alice leads the group of animals swimming toward the shore to exit the pool.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[FILMCREATOR_RECORD type=character]]
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
direct_identity_evidence: "Alice's name is used throughout the text."
direct_visual_evidence: "Described as growing to over nine feet tall, then shrinking to two feet tall; experiences a pool of tears up to her chin."
costume_or_covering_evidence: "Wears one of the Rabbit's white kid gloves at one point."
movement_evidence: "Walks, lies on side, runs, slips and falls into water."
associated_entities: ["white_rabbit", "mouse", "dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present

**Physical Description:**
A human girl who undergoes extreme size fluctuations. At one point, she is over nine feet tall; later, she shrinks to approximately two feet tall. She experiences a period of profuse crying that creates a pool of salt water.

**Costume & Silhouette:**
Her specific clothing is not detailed in this chapter, though she is noted to be wearing a white kid glove belonging to the White Rabbit during her shrinking phase.

**Descriptive Noun Phrases:**
- Giant girl (9ft+)
- Tiny girl (2ft)
- Submerged girl in salt water
- Girl with hoarse voice

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: []
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
confidence: 0.9
direct_identity_evidence: "Identified as the White Rabbit."
direct_visual_evidence: "Described as trotting hurriedly, dressed splendidly, carrying white kid gloves and a large fan."
costume_or_covering_evidence: "Dressed splendidly; carries white kid gloves and a large fan."
movement_evidence: "Trots hurriedly, scurries away into darkness."
associated_entities: ["alice", "the_duchess"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# White Rabbit
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A white rabbit that moves with haste.

**Costume & Silhouette:**
Dressed "splendidly." He carries a large fan and a pair of white kid gloves.

**Descriptive Noun Phrases:**
- Dapper white rabbit
- Rabbit in splendid clothing
- Hurried white rabbit

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: mouse
canonical_character_id: mouse
aliases: []
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
confidence: 0.8
direct_identity_evidence: "Identified as a Mouse."
direct_visual_evidence: "Enters the pool, splashes, swims."
costume_or_covering_evidence: ""
movement_evidence: "Splashing, swimming."
associated_entities: ["alice", "dinah"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Mouse
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A small animal that enters the pool of tears.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Swimming mouse
- Indignant mouse
- Small splashing mouse

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: dinah
canonical_character_id: dinah
aliases: ["Alice's cat"]
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.7
direct_identity_evidence: "Named Dinah and referred to as Alice's cat."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: "Referred to as 'my cat' by Alice."
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dinah
**Role:** Referenced Character

**Status:** Referenced (Not Present)

**Physical Description:**
A cat belonging to Alice. No specific physical traits are provided in this chapter.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Alice's cat
- A cat (described as "nasty, low, vulgar" by the Mouse)

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: animal_crowd
canonical_character_id: animal_crowd
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as a crowd of animals."
direct_visual_evidence: "A Duck, a Dodo, a Lory, an Eaglet, and other creatures swimming in the pool."
costume_or_covering_evidence: ""
movement_evidence: "Swimming toward the shore."
associated_entities: ["alice", "mouse"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Animal Crowd
**Role:** Supporting Group

**Status:** Physically Present

**Physical Description:**
A collection of various animals swimming in the pool. Specific members include a Duck, a Dodo, a Lory, and an Eaglet.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Swimming animal crowd
- Group of pool creatures (Duck, Dodo, Lory, Eaglet)

[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "The character is only mentioned by name in dialogue and has no physical description provided."
clarification_required: true
clarification_reason: "Character is only a verbal reference; no visual data exists."
clarification_question: "What is the Duchess's appearance/species?"
character_type_hint: unknown
morphology_hint: unknown
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Mentioned by the White Rabbit."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: ""
unknowns: ["physical appearance", "species"]
source_refs: []
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# The Duchess
**Role:** Referenced Character

**Status:** Referenced (Not Present)

**Physical Description:**
Unknown. Mentioned by the White Rabbit as he scurries away.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- The Duchess (referenced)

[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
