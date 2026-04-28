# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:18:59.685009+00:00
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

Chapter id: CH012

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

**Setting:** A courtroom populated by a jury of various creatures and presided over by the King and Queen of Hearts.

**Characters:**
- **Alice:** Currently experiencing rapid growth; she is nearly two miles high.
- **The King of Hearts:** Presiding judge, prone to making arbitrary rules and linguistic errors.
- **The Queen of Hearts:** Volatile authority figure, prone to outbursts and ordering executions.
- **The White Rabbit:** Court official/messenger.
- **The Knave of Hearts:** The prisoner on trial.
- **The Jury:** A collection of various creatures (including a Lizard).

**Key Events:**
- **Jury Disturbance:** Alice jumps up in excitement, accidentally tipping over the jury-box and spilling the jurymen onto the crowd below. She attempts to pick them up, mistakenly treating them like goldfish.
- **The Lizard Incident:** Alice places the Lizard back into the box head-downwards; it is unable to move.
- **Interrogation of Alice:** The King questions Alice regarding her knowledge of the crime; she claims to know nothing.
- **Rule 42 Enforcement:** The King attempts to invoke "Rule Forty-two," stating all persons more than a mile high must leave the court. Alice refuses, challenging the legitimacy of the rule.
- **Introduction of Evidence:** The White Rabbit presents a piece of paper found at the scene. It is revealed not to be a letter, but a set of cryptic verses.
- **The Verses:** The White Rabbit reads a six-stanza poem containing nonsensical references to swimming, tarts, and "fits."
- **The King's Interpretation:** The King attempts to find meaning in the verses, linking them to the tarts on the table and making a pun regarding the Queen's "fits."
- **Conflict Escalation:** Alice argues that the verses have no meaning. The Queen demands a sentence before a verdict. Alice defies the Queen.
- **The Climax/Transition:** The Queen shouts, "Off with her head!" Alice declares the court is nothing but a pack of cards. The deck of cards rises and flies at her.
- **The Awakening:** Alice wakes up on a riverbank, her head in her sister's lap. She recounts her dream to her sister.
- **Epilogue/Sister's Dream:** As Alice runs off to tea, the sister remains, drifting into a daydream where she imagines the sounds and creatures of Alice's Wonderland (the White Rabbit, the Mouse, the March Hare, the Queen, etc.) blending with the sounds of the real world (rustling grass, sheep-bells, farmyard clamor).
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]
[[SECTION character_index_markdown]]
# Character Index: Chapter 12

- [Alice](#alice)
- [The King of Hearts](#the_king_of_hearts)
- [The Queen of Hearts](#the_queen_of_hearts)
- [The White Rabbit](#the_white_rabbit)
- [The Knave of Hearts](#the_knave_of_hearts)
- [The Jury](#the_jury)
- [Alice's Sister](#alices_sister)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=alice
canonical_character_id=alice
aliases=[]
is_fully_identified=true
manual_description_required=true
manual_description_reason="While her scale is defined (nearly two miles high), specific facial features, hair color/style, and clothing details are not provided in this chapter text to ensure consistent rendering."
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=human
morphology_hint=biped
scale_hint=giant
renderability_hint=renderable
confidence=1.0
direct_identity_evidence="Alice"
direct_visual_evidence="Nearly two miles high; jumps up in excitement."
costume_or_covering_evidence=""
movement_evidence="Jumps up, attempts to pick up jurymen."
associated_entities=["the_king_of_hearts", "the_queen_of_hearts", "the_white_rabbit"]
alias_or_role_evidence=""
unknowns=[]
source_refs=["CH012"]
[[SECTION markdown]]
# Alice
**Role:** Protagonist / Defendant (challenged)

**Status:** Physically Present (as a giant)

**Physical Description:**
- **Scale:** Massive; nearly two miles high.
- **Features:** Not explicitly described in this chapter.

**Costume & Silhouette:**
- No specific clothing details provided in this text.

**Descriptive Noun Phrases:**
- Giant girl
- Two-mile-high human
- Colossal Alice

**Uncertainty Notes:**
- Specific visual traits (hair, eyes, dress) are missing from the source text; requires external character sheet for continuity.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_king_of_hearts
canonical_character_id=the_king_of_hearts
aliases=[]
is_fully_identified=true
manual_description_required=true
manual_description_reason="The text identifies him as the presiding judge but provides no visual description of his appearance, clothing, or physical form."
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=humanoid_nonhuman
morphology_hint=biped
scale_hint=human_scale
renderability_hint=renderable
confidence=0.8
direct_identity_evidence="The King of Hearts"
direct_visual_evidence="Presiding judge in court."
costume_or_covering_evidence=""
movement_evidence="Attempts to invoke Rule 42; interprets verses."
associated_entities=["the_queen_of_hearts", "alice"]
alias_or_role_evidence="Presiding judge"
unknowns=[]
source_refs=["CH012"]
[[SECTION markdown]]
# The King of Hearts
**Role:** Presiding Judge

**Status:** Physically Present

**Physical Description:**
- **Scale:** Human scale (relative to the court).
- **Features:** Not described.

**Costume & Silhouette:**
- No specific clothing details provided in this text.

**Descriptive Noun Phrases:**
- Arbiter of the court
- Rule-making King
- Linguisticly error-prone monarch

**Uncertainty Notes:**
- Visual appearance is entirely unstated; requires design direction for royal attire and physical features.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_queen_of_hearts
canonical_character_id=the_queen_of_hearts
aliases=[]
is_fully_identified=true
manual_description_required=true
manual_description_reason="The text identifies her as a volatile authority figure but provides no visual description of her appearance or attire."
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=humanoid_nonhuman
morphology_hint=biped
scale_hint=human_scale
renderability_hint=renderable
confidence=0.8
direct_identity_evidence="The Queen of Hearts"
direct_visual_evidence="Demands a sentence; shouts 'Off with her head!'"
costume_or_covering_evidence=""
movement_evidence="Outbursts and shouting."
associated_entities=["the_king_of_hearts", "alice"]
alias_or_role_evidence="Volatile authority figure"
unknowns=[]
source_refs=["CH012"]
[[SECTION markdown]]
# The Queen of Hearts
**Role:** Volatile Authority Figure

**Status:** Physically Present

**Physical Description:**
- **Scale:** Human scale.
- **Features:** Not described.

**Costume & Silhouette:**
- No specific clothing details provided in this text.

**Descriptive Noun Phrases:**
- Temperamental Queen
- Execution-ordering monarch
- Volatile ruler

**Uncertainty Notes:**
- Visual appearance is entirely unstated; requires design direction for royal attire and facial expression/features.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_white_rabbit
canonical_character_id=the_white_rabbit
aliases=[]
is_fully_identified=true
manual_description_required=true
manual_description_reason="While known as a rabbit, specific visual details (clothing, size relative to humans) are not provided in this chapter."
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=animal
morphology_hint=quadruped
scale_hint=small
renderability_hint=renderable
confidence=0.9
direct_identity_evidence="The White Rabbit"
direct_visual_evidence="Presents a piece of paper; reads verses."
costume_or_covering_evidence=""
movement_evidence="Presenting evidence/reading."
associated_entities=["alice"]
alias_or_role_evidence="Court official/messenger"
unknowns=[]
source_refs=["CH012"]
[[SECTION markdown]]
# The White Rabbit
**Role:** Court Official / Messenger

**Status:** Physically Present

**Physical Description:**
- **Scale:** Small (rabbit scale).
- **Features:** White rabbit.

**Costume & Silhouette:**
- No specific clothing details provided in this text.

**Descriptive Noun Phrases:**
- Rabbit messenger
- Court official rabbit

**Uncertainty Notes:**
- Specifics on whether the rabbit is anthropomorphic (wearing clothes) or a natural animal are not explicitly detailed here, though his role suggests anthropomorphism.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_knave_of_hearts
canonical_character_id=the_knave_of_hearts
aliases=[]
is_fully_identified=true
manual_description_required=true
manual_description_reason="The character is mentioned as the prisoner on trial, but no physical description or visual presence is provided."
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=humanoid_nonhuman
morphology_hint=biped
scale_hint=human_scale
renderability_hint=context_only
confidence=0.7
direct_identity_evidence="The Knave of Hearts"
direct_visual_evidence=""
costume_or_covering_evidence=""
movement_evidence=""
associated_entities=[]
alias_or_role_evidence="The prisoner on trial"
unknowns=[]
source_refs=["CH012"]
[[SECTION markdown]]
# The Knave of Hearts
**Role:** Prisoner on Trial

**Status:** Referenced (Present in court but no visual description)

**Physical Description:**
- **Scale:** Human scale.
- **Features:** Not described.

**Costume & Silhouette:**
- No specific clothing details provided in this text.

**Descriptive Noun Phrases:**
- The accused knave
- Prisoner of the court

**Uncertainty Notes:**
- Character is a functional part of the scene but lacks any visual descriptors for rendering.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=the_jury
canonical_character_id=the_jury
aliases=[]
is_fully_identified=true
manual_description_required=true
manual_description_reason="The jury is described as a 'collection of various creatures,' but specific visual details for individual members are sparse."
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=group
morphology_hint=unknown
scale_hint=small
renderability_hint=renderable
confidence=0.6
direct_identity_evidence="The Jury"
direct_visual_evidence="Spilled from the jury-box; includes a Lizard."
costume_or_covering_evidence=""
movement_evidence="Spilling onto the crowd; Lizard unable to move when placed head-down."
associated_entities=[]
alias_or_role_evidence="Jurymen"
unknowns=["Specific species of most members"]
source_refs=["CH012"]
[[SECTION markdown]]
# The Jury
**Role:** Jurors

**Status:** Physically Present

**Physical Description:**
- **Scale:** Small (fit into a jury-box).
- **Features:** A collection of various creatures. One specific member is a Lizard.

**Costume & Silhouette:**
- No specific clothing details provided in this text.

**Descriptive Noun Phrases:**
- Assorted creature jurors
- The spilled jury

**Uncertainty Notes:**
- The composition of the group is vague beyond the mention of a lizard; requires creative direction for the variety of creatures.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type=character
asset_id=alices_sister
canonical_character_id=alices_sister
aliases=[]
is_fully_identified=true
manual_description_required=true
manual_description_reason="The sister is mentioned as being on a riverbank, but no physical description (age, hair, clothing) is provided."
clarification_required=false
clarification_reason=""
clarification_question=""
character_type_hint=human
morphology_hint=biped
scale_hint=human_scale
renderability_hint=renderable
confidence=0.9
direct_identity_evidence="Alice's sister"
direct_visual_evidence="Sitting on a riverbank with Alice's head in her lap."
costume_or_covering_evidence=""
movement_evidence="Drifting into a daydream."
associated_entities=["alice"]
alias_or_role_evidence=""
unknowns=[]
source_refs=["CH012"]
[[SECTION markdown]]
# Alice's Sister
**Role:** Observer / Dreamer

**Status:** Physically Present (Real world)

**Physical Description:**
- **Scale:** Human scale.
- **Features:** Not described.

**Costume & Silhouette:**
- No specific clothing details provided in this text.

**Descriptive Noun Phrases:**
- The dreaming sister
- Alice's companion on the riverbank

**Uncertainty Notes:**
- Lacks any physical descriptors; requires character design to establish her appearance and age relative to Alice.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
