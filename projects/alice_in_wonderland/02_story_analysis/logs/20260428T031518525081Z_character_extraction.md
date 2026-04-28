# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:15:18.525081+00:00
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
*   **Visual State:** Alice is giant-sized, standing over nine feet tall. Her feet appear extremely distant from her torso due to perspective/scale.
*   **Event:** Alice experiences a growth spurt/size shift where she feels like a "telescope opening out." She contemplates the logistics of sending Christmas boots to her own feet via carrier.
*   **Action:** Alice's head strikes the ceiling of the hall. She retrieves a small golden key.
*   **Action:** Alice attempts to look into the garden through the tiny door by lying on her side and using one eye, but she is too large to pass.
*   **Event/Transition:** Alice begins to cry uncontrollably. Her tears create a large pool of salt water, approximately four inches deep, spreading halfway down the hall.

**Location: The Hall (Flooded)**
*   **Character Entrance:** The White Rabbit enters, trotting hurriedly. He is dressed splendidly and carries white kid gloves in one hand and a large fan in the other. He mutters about "the Duchess."
*   **Interaction:** Alice attempts to speak to the Rabbit. The Rabbit reacts violently, drops the gloves and the fan, and scurries away into the darkness.
*   **Object Interaction:** Alice picks up the fan and the white kid gloves. 
*   **Character State/Internal Monologue:** Alice experiences an identity crisis, questioning if she has been changed into another child (Ada or Mabel). She attempts to verify her identity through math (4x5=12) and geography (London is the capital of Paris), failing both. She recites "How doth the little crocodile" but finds her voice sounds hoarse and strange.
*   **Visual/Scale Shift:** Alice notices she is wearing one of the Rabbit's white kid gloves. She measures herself against a table and realizes she has shrunk to approximately two feet tall. 
*   **Action/Risk:** Alice discovers that holding the fan causes her to shrink rapidly. She drops the fan to prevent shrinking into non-existence.
*   **Event:** Alice runs toward the garden door, but finds it shut. The golden key is back on the glass table.
*   **Physical Event:** Alice slips and falls into the pool of tears she previously created. She is now swimming in salt water up to her chin.

**Location: The Pool (In the Hall)**
*   **Character Encounter:** Alice hears splashing and discovers a Mouse swimming nearby.
*   **Interaction/Dialogue:** Alice attempts to communicate with the Mouse using formal "O Mouse" address and then switches to French ("Où est ma chatte?"). 
*   **Conflict:** The Mouse reacts with fright/anger to the mention of cats. Alice tries to soothe the Mouse by describing her cat, Dinah, which causes the Mouse to bristle and tremble with indignation.
*   **Conflict Escalation:** Alice attempts to change the subject to dogs (a terrier), but mentions the dog kills rats. The Mouse becomes highly offended and swims away in a commotion.
*   **Resolution of Interaction:** Alice calls the Mouse back, promising not to mention cats or dogs. The Mouse agrees to return and tells her they should reach the shore so he can explain his history.
*   **Character/Creature Entrance:** As they swim toward the shore, other animals emerge in the pool: a Duck, a Dodo, a Lory, and an Eaglet.
*   **Action/Exit:** Alice leads the group of animals/birds swimming toward the edge of the pool (the shore).
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[FILMCREATOR_RECORD type=character]]
asset_id: alice
canonical_character_id: alice
aliases: Ada, Mabel
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: renderable
confidence: 1.0
direct_identity_evidence: Alice identifies herself and questions if she is Ada or Mabel.
direct_visual_evidence: Described as growing to nine feet tall, then shrinking to two feet tall; head strikes ceiling; swims in a pool of tears.
costume_or_covering_evidence: Wears one of the Rabbit's white kid gloves at one point.
movement_evidence: Walking, lying on side to look through doors, crying, running, slipping/falling into water, swimming.
associated_entities: White Rabbit, Mouse, Dinah (referenced), Duck, Dodo, Lory, Eaglet
alias_or_role_evidence: 
unknowns: Specific hair color or eye color not mentioned in this chapter.
source_refs: 
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present (Variable Scale)

**Physical Description:**
A young girl who undergoes extreme scale shifts. At the start of the chapter, she is giant-sized (over nine feet tall), causing her head to strike the ceiling and making her feet appear distant from her torso. Later, she shrinks to approximately two feet tall. She is capable of swimming in a pool of salt water.

**Costume & Silhouette:**
Her silhouette changes drastically due to scale. At one point, she is noted to be wearing a white kid glove belonging to the White Rabbit.

**Descriptive Noun Phrases:**
- Giant-sized girl
- Two-foot-tall child
- Swimming girl in salt water pool
- Child with identity crisis

**Uncertainty Notes:**
Specific facial features, hair color, and eye color are not provided in this text segment. Her scale is highly unstable.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: 
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
direct_identity_evidence: Identified as the White Rabbit.
direct_visual_evidence: White fur, trotting hurriedly, carries white kid gloves and a large fan.
costume_or_covering_evidence: Dressed "splendidly"; carries white kid gloves and a large fan.
movement_evidence: Trotting hurriedly, scurrying away into darkness.
associated_entities: Alice, The Duchess (referenced)
alias_or_role_evidence: 
unknowns: Specific clothing items beyond being "splendidly dressed" are not detailed.
source_refs: 
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# White Rabbit
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A small, white-furred rabbit that moves with urgency.

**Costume & Silhouette:**
Dressed in splendid attire. He carries a large fan and a pair of white kid gloves.

**Descriptive Noun Phrases:**
- Splendidly dressed white rabbit
- Hurried white rabbit with fan and gloves
- Small scurrying rabbit

**Uncertainty Notes:**
The exact style of his "splendid" clothing is not specified.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: mouse
canonical_character_id: mouse
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: tiny
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: Identified as a Mouse.
direct_visual_evidence: Swimming in the pool of tears; bristles and trembles with indignation.
costume_or_covering_evidence: 
movement_evidence: Swimming, bristling, trembling.
associated_entities: Alice, Dinah (referenced)
alias_or_role_evidence: 
unknowns: Color or specific breed/type of mouse.
source_refs: 
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Mouse
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:**
A small animal capable of swimming in a pool of salt water. Reacts with visible emotion (fright, anger, indignation).

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Swimming mouse
- Indignant mouse
- Small wet mouse

**Uncertainty Notes:**
No specific color or fur texture is mentioned.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: dinah
canonical_character_id: dinah
aliases: 
is_fully_identified: false
manual_description_required: true
manual_description_reason: Character is only mentioned in dialogue; no visual description provided.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: Alice refers to "my cat, Dinah."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: Alice
alias_or_role_evidence: 
unknowns: Appearance, color, size.
source_refs: 
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Dinah
**Role:** Referenced Character

**Status:** Referenced (Not Present)

**Physical Description:**
A cat belonging to Alice. No physical details are provided in this chapter.

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Alice's cat

**Uncertainty Notes:**
This character is purely a conversational reference and lacks any visual description for rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD type=character]]
asset_id: pool_animals
canonical_character_id: pool_animals
aliases: 
is_fully_identified: true
manual_description_required: true
manual_description_reason: These characters are listed as a group without individual physical descriptions.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: Identified as a Duck, Dodo, Lory, and Eaglet.
direct_visual_evidence: Emerging from the pool of tears.
costume_or_covering_evidence: 
movement_evidence: Swimming toward the shore.
associated_entities: Alice
alias_or_role_evidence: 
unknowns: Individual appearance/color for each bird/animal.
source_refs: 
[[SECTION character_index_markdown]]
[[SECTION markdown]]
# Pool Animals (Group)
**Role:** Supporting Characters

**Status:** Physically Present

**Physical Description:**
A collection of various animals and birds that emerge from the pool of tears to swim toward the shore. The group includes:
- A Duck
- A Dodo
- A Lory
- An Eaglet

**Costume & Silhouette:**
N/A

**Descriptive Noun Phrases:**
- Group of swimming birds and animals
- A duck, dodo, lory, and eaglet in a pool

**Uncertainty Notes:**
Individual colors, sizes (relative to each other), and specific species details beyond their names are not provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
