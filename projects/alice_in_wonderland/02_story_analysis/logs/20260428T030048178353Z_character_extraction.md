# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T03:00:48.178353+00:00
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
*   **Event:** Alice experiences rapid growth, reaching over nine feet in height. Her head strikes the ceiling of the hall.
*   **Character State:** Alice is disoriented and struggling to speak coherent English.
*   **Object Interaction:** Alice picks up a small golden key.
*   **Action/Movement:** Alice moves toward the garden door but finds it impossible to peer through due to her size. She sits down and begins to cry.
*   **Visual Continuity/Environment Shift:** Alice's crying creates a large pool of salt water, approximately four inches deep, spreading halfway down the hall.

**Location: The Hall (Near the Pool)**
*   **Character Entrance:** The White Rabbit enters, trotting hurriedly. He is dressed splendidly and carries white kid gloves and a large fan.
*   **Dialogue/Action:** The White Rabbit mutters about "the Duchess." Alice attempts to speak to him; the Rabbit reacts violently, drops the gloves and the fan, and flees into the darkness.
*   **Object Interaction:** Alice picks up the fan and the white kid gloves.
*   **Character State/Internal Monologue:** Alice experiences an identity crisis, questioning if she has been transformed into another child (Mabel or Ada). She attempts to verify her identity through math (multiplication tables), geography (capitals of Europe), and reciting poetry ("How doth the little crocodile"), but fails all tests.
*   **Visual Continuity/Transformation:** Alice notices she is wearing one of the Rabbit's white kid gloves. She measures herself against a table and finds she has shrunk to approximately two feet tall.
*   **Action/Decision:** Alice realizes the fan causes her to shrink; she drops it to prevent shrinking away entirely.
*   **Movement/Failure:** Alice runs toward the garden door, but finds it shut. The golden key is back on the glass table.

**Location: The Pool of Tears**
*   **Event/Action:** Alice slips and falls into the pool of salt water, which now reaches up to her chin.
*   **Character State:** Alice believes she might be drowning in her own tears.
*   **Character Entrance:** A Mouse enters the pool, swimming nearby.
*   **Interaction (Alice & Mouse):** 
    *   Alice attempts to communicate with the Mouse using formal "O Mouse" address and then French ("Où est ma chatte?").
    *   The Mouse reacts with fright/agitation at the mention of cats.
    *   Alice attempts to soothe the Mouse by describing her cat, Dinah, which causes the Mouse to bristle and become offended.
    *   Alice attempts to change the subject to dogs (a terrier), which causes the Mouse to swim away in a commotion.
    *   Alice calls the Mouse back, promising not to mention cats or dogs.
*   **Dialogue/Reveal:** The Mouse agrees to return and proposes they go to the shore so he can explain his history regarding cats and dogs.
*   **Character Entrances (Crowd):** As the pool becomes crowded, several animals emerge: a Duck, a Dodo, a Lory, and an Eaglet.
*   **Movement/Exit:** Alice leads the group of animals/birds out of the water toward the shore.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index

- [Alice](#alice)
- [White Rabbit](#white_rabbit)
- [The Duchess](#the_duchess)
- [Mabel](#mabel)
- [Ada](#ada)
- [Mouse](#mouse)
- [Dinah](#dinah)
- [Duck](#duck)
- [Dodo](#dodo)
- [Lory](#lory)
- [Eaglet](#eaglet)

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
direct_identity_evidence: "Explicitly named as Alice throughout the text."
direct_visual_evidence: "Described as growing to nine feet tall and shrinking to two feet tall; experiences an identity crisis regarding her appearance/self."
costume_or_covering_evidence: "Wears one of the White Rabbit's white kid gloves at one point."
movement_evidence: "Moves toward garden door, sits down, cries, runs, slips into a pool of tears."
associated_entities: ["white_rabbit", "mouse", "dinah", "duck", "dodo", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Alice
**Role:** Protagonist

**Status:** Physically Present (Variable Scale)

**Physical Description:** 
A young girl whose size fluctuates dramatically. She grows to over nine feet tall (head striking the ceiling) and later shrinks to approximately two feet tall. 

**Costume & Traits:** 
- Wears a white kid glove (belonging to the White Rabbit) during her shrinking phase.
- Subject to extreme scale shifts.

**Descriptive Noun Phrases:** 
- Giant young girl
- Tiny child
- Girl in a pool of tears

**Uncertainty Notes:** 
Specific clothing details (color/style) are not explicitly detailed in this chapter, though she is clearly a child.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: white_rabbit
aliases: ["White Rabbit"]
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
direct_identity_evidence: "Explicitly named as the White Rabbit."
direct_visual_evidence: "Described as trotting hurriedly, dressed splendidly, carrying white kid gloves and a large fan."
costume_or_covering_evidence: "Dressed splendidly; carries white kid gloves and a large fan."
movement_evidence: "Trots hurriedly, reacts violently, drops items, flees into darkness."
associated_entities: ["alice", "the_duchess"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# White Rabbit
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:** 
A rabbit that moves with human-like urgency.

**Costume & Traits:** 
- Dressed splendidly (specific attire not detailed).
- Carries white kid gloves and a large fan.

**Descriptive Noun Phrases:** 
- Splendidly dressed rabbit
- Hurried rabbit with accessories

**Uncertainty Notes:** 
The specific style of his "splendid" clothing is unknown.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_duchess
canonical_character_id: the_duchess
aliases: ["Duchess"]
is_fully_identified: false
manual_description_required: true
manual_description_reason: "The character is only mentioned in dialogue and has no physical description provided in this chapter."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: unknown
morphology_hint: unknown
scale_hint: unknown
renderability_hint: alias_or_role
confidence: 0.5
direct_identity_evidence: "Mentioned by the White Rabbit."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["white_rabbit"]
alias_or_role_evidence: "Referenced as a subject of the Rabbit's mutterings."
unknowns: ["physical appearance", "species", "scale"]
source_refs: []
[[SECTION markdown]]
# The Duchess
**Role:** Referenced Character

**Status:** Referenced Only

**Physical Description:** 
No physical description available.

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Mentioned Duchess

**Uncertainty Notes:** 
Character is currently a non-visual entity in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: mabel
canonical_character_id: mabel
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Mentioned only as a name Alice uses to question her own identity; no physical description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.3
direct_identity_evidence: "Alice questions if she has been transformed into Mabel."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: ["physical appearance", "age", "relation to Alice"]
source_refs: []
[[SECTION markdown]]
# Mabel
**Role:** Referenced Identity

**Status:** Referenced Only

**Physical Description:** 
Unknown.

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Potential identity (Mabel)

**Uncertainty Notes:** 
Likely a peer or friend of Alice, but no visual data exists.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: ada
canonical_character_id: ada
aliases: []
is_fully_identified: false
manual_description_required: true
manual_description_reason: "Mentioned only as a name Alice uses to question her own identity; no physical description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: human
morphology_hint: biped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.3
direct_identity_evidence: "Alice questions if she has been transformed into Ada."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: ["physical appearance", "age", "relation to Alice"]
source_refs: []
[[SECTION markdown]]
# Ada
**Role:** Referenced Identity

**Status:** Referenced Only

**Physical Description:** 
Unknown.

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Potential identity (Ada)

**Uncertainty Notes:** 
Likely a peer or friend of Alice, but no visual data exists.
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
confidence: 0.8
direct_identity_evidence: "Explicitly identified as a Mouse."
direct_visual_evidence: "Enters the pool, swimming nearby; reacts with fright/agitation at the mention of cats."
costume_or_covering_evidence: ""
movement_evidence: "Swimming in the pool, bristling, swimming away in a commotion."
associated_entities: ["alice"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Mouse
**Role:** Supporting Character

**Status:** Physically Present

**Physical Description:** 
A small mouse capable of swimming.

**Costume & Traits:** 
- Becomes agitated/bristles when cats are mentioned.

**Descriptive Noun Phrases:** 
- Swimming mouse
- Agitated mouse

**Uncertainty Notes:** 
Specific breed or color is not specified.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dinah
canonical_character_id: dinah
aliases: ["Dinah"]
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only mentioned by name; no physical description provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: quadruped
scale_hint: unknown
renderability_hint: context_only
confidence: 0.5
direct_identity_evidence: "Alice refers to her as 'my cat, Dinah'."
direct_visual_evidence: ""
costume_or_covering_evidence: ""
movement_evidence: ""
associated_entities: ["alice"]
alias_or_role_evidence: "Alice's pet."
unknowns: ["physical appearance", "color", "breed"]
source_refs: []
[[SECTION markdown]]
# Dinah
**Role:** Referenced Pet

**Status:** Referenced Only

**Physical Description:** 
A cat. No specific colors or markings are mentioned.

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Alice's cat

**Uncertainty Notes:** 
Visual details are entirely absent from the text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duck
canonical_character_id: duck
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only identified by species; no specific visual details provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as a Duck."
direct_visual_evidence: "Emerges from the water to join the group on the shore."
costume_or_covering_evidence: ""
movement_evidence: "Emerges from the pool/water."
associated_entities: ["alice", "dodo", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Duck
**Role:** Background Character

**Status:** Physically Present

**Physical Description:** 
A duck.

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Swimming duck
- Group of animals

**Uncertainty Notes:** 
No specific color or breed details are provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dodo
canonical_character_id: dodo
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only identified by species; no specific visual details provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as a Dodo."
direct_visual_evidence: "Emerges from the water to join the group on the shore."
costume_or_covering_evidence: ""
movement_evidence: "Emerges from the pool/water."
associated_entities: ["alice", "duck", "lory", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Dodo
**Role:** Background Character

**Status:** Physically Present

**Physical Description:** 
A dodo bird.

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Extinct bird (Dodo)
- Group of animals

**Uncertainty Notes:** 
No specific visual details provided beyond species.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: lory
canonical_character_id: lory
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only identified by species; no specific visual details provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as a Lory."
direct_visual_evidence: "Emerges from the water to join the group on the shore."
costume_or_covering_evidence: ""
movement_evidence: "Emerges from the pool/water."
associated_entities: ["alice", "duck", "dodo", "eaglet"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Lory
**Role:** Background Character

**Status:** Physically Present

**Physical Description:** 
A lory (parrot).

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Small parrot
- Group of animals

**Uncertainty Notes:** 
No specific color or plumage details are provided.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: eaglet
canonical_character_id: eaglet
aliases: []
is_fully_identified: true
manual_description_required: true
manual_description_reason: "Only identified by species; no specific visual details provided."
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: animal
morphology_hint: winged
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: "Identified as an Eaglet."
direct_visual_evidence: "Emerges from the water to join the group on the shore."
costume_or_covering_evidence: ""
movement_evidence: "Emerges from the pool/water."
associated_entities: ["alice", "duck", "dodo", "lory"]
alias_or_role_evidence: ""
unknowns: []
source_refs: []
[[SECTION markdown]]
# Eaglet
**Role:** Background Character

**Status:** Physically Present

**Physical Description:** 
An eaglet (young eagle).

**Costume & Traits:** 
Unknown.

**Descriptive Noun Phrases:** 
- Young eagle
- Group of animals

**Uncertainty Notes:** 
No specific visual details provided beyond species.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
