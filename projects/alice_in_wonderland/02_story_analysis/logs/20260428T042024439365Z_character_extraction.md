# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T04:20:24.439365+00:00
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
[[markdown]]
# Character Index

## Alice
- [Alice](#alice)

## The King of Hearts
- [The King of Hearts](#the-king-of-hearts)

## The Queen of Hearts
- [The Queen of Hearts](#the-queen-of-hearts)

## The White Rabbit
- [The White Rabbit](#the-white-rabbit)

## The Knave of Hearts
- [The Knave of Hearts](#the-knave-of-hearts)

## The Jury
- [The Jury](#the-jury)

## Alice's Sister
- [Alice's Sister](#alices-sister)

---

<a name="alice"></a>
# Alice
**Role:** Protagonist / Defendant (accused of being too tall)
**Status:** Physically Present (in dream); Referenced (in sister's daydream)
**Description:** Currently experiencing rapid growth; nearly two miles high.
**Traits:** Defiant, argumentative, confused by nonsensical rules.

<a name="the-king-of-hearts"></a>
# The King of Hearts
**Role:** Presiding Judge
**Status:** Physically Present (in dream)
**Description:** Prone to making arbitrary rules and linguistic errors.

<a name="the-queen-of-hearts"></a>
# The Queen of Hearts
**Role:** Volatile Authority Figure
**Status:** Physically Present (in dream)
**Description:** Known for outbursts and ordering executions ("Off with her head!").

<a name="the-white-rabbit"></a>
# The White Rabbit
**Role:** Court Official / Messenger
**Status:** Physically Present (in dream); Referenced (in sister's daydream)
**Description:** Presents evidence (cryptic verses).

<a name="the-knave-of-hearts"></a>
# The Knave of Hearts
**Role:** Prisoner on trial
**Status:** Physically Present (in dream)
**Description:** Subject of the court proceedings.

<a name="the-jury"></a>
# The Jury
**Role:** Jurors
**Status:** Physically Present (in dream)
**Description:** A collection of various creatures, including a Lizard.

<a name="alices-sister"></a>
# Alice's Sister
**Role:** Observer / Dreamer
**Status:** Physically Present (real world); Referenced (as dreamer)
**Description:** Sitting on a riverbank; imagines the sounds of Wonderland.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: alice
canonical_character_id: alice
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: giantess (two miles high)
scale_hint: massive
renderability_hint: extreme scale contrast required
confidence: 1.0
direct_identity_evidence: "Alice jumps up in excitement..."
direct_visual_evidence: "she is nearly two miles high"
costume_or_covering_evidence: 
movement_evidence: "jumps up", "attempts to pick them [jury] up"
associated_entities: ["the_king_of_hearts", "the_queen_of_hearts", "the_white_rabbit"]
alias_or_role_evidence: 
unknowns: []
source_refs: [[SECTION markdown]]
# Alice
**Role:** Protagonist / Defendant (accused of being too tall)
**Status:** Physically Present (in dream); Referenced (in sister's daydream)
**Physical Description:** Experiencing rapid growth; nearly two miles high.
**Costume/Silhouette:** Not explicitly described in this chapter.
**Prompt Phrases:** giant girl, massive scale, towering over courtroom, defiant expression.
**Uncertainty Notes:** Specific clothing details are not provided in this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_king_of_hearts
canonical_character_id: king_of_hearts
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid/playing_card
morphology_hint: 
scale_hint: standard
renderability_hint: 
confidence: 0.9
direct_identity_evidence: "The King of Hearts: Presiding judge..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "attempts to invoke 'Rule Forty-two'"
associated_entities: ["the_queen_of_hearts", "alice"]
alias_or_role_evidence: "Presiding judge"
unknowns: []
source_refs: [[SECTION markdown]]
# The King of Hearts
**Role:** Presiding Judge
**Status:** Physically Present (in dream)
**Physical Description:** Prone to linguistic errors and arbitrary rule-making.
**Costume/Silhouette:** Likely follows playing card motif.
**Prompt Phrases:** king of hearts, royal judge, nonsensical ruler, authoritative but error-prone.
**Uncertainty Notes:** Visual appearance beyond role is implied by title.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_queen_of_hearts
canonical_character_id: queen_of_hearts
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid/playing_card
morphology_hint: 
scale_hint: standard
renderability_hint: 
confidence: 0.9
direct_identity_evidence: "The Queen of Hearts: Volatile authority figure..."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "shouts, 'Off with her head!'"
associated_entities: ["the_king_of_hearts", "alice"]
alias_or_role_evidence: "Volatile authority figure"
unknowns: []
source_refs: [[SECTION markdown]]
# The Queen of Hearts
**Role:** Volatile Authority Figure
**Status:** Physically Present (in dream)
**Physical Description:** Prone to outbursts.
**Costume/Silhouette:** Likely follows playing card motif.
**Prompt Phrases:** queen of hearts, volatile queen, shouting monarch, demanding execution.
**Uncertainty Notes:** Specific visual traits not detailed in text.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_white_rabbit
canonical_character_id: white_rabbit
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: anthropomorphic_animal
morphology_hint: rabbit
scale_hint: small/standard
renderability_hint: 
confidence: 1.0
direct_identity_evidence: "The White Rabbit: Court official/messenger."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: "reads a six-stanza poem"
associated_entities: ["alice", "the_jury"]
alias_or_role_evidence: "Court official/messenger"
unknowns: []
source_refs: [[SECTION markdown]]
# The White Rabbit
**Role:** Court Official / Messenger
**Status:** Physically Present (in dream); Referenced (in sister's daydream)
**Physical Description:** A white rabbit.
**Costume/Silhouette:** 
**Prompt Phrases:** white rabbit, court messenger, anthropomorphic rabbit, holding paper.
**Uncertainty Notes:** Clothing not specified in this chapter.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_knave_of_hearts
canonical_character_id: knave_of_hearts
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid/playing_card
morphology_hint: 
scale_hint: standard
renderability_hint: 
confidence: 0.9
direct_identity_evidence: "The Knave of Hearts: The prisoner on trial."
direct_visual_evidence: 
costume_or_covering_evidence: 
movement_evidence: 
associated_entities: ["the_king_of_hearts", "the_queen_of_hearts"]
alias_or_role_evidence: "The prisoner on trial"
unknowns: []
source_refs: [[SECTION markdown]]
# The Knave of Hearts
**Role:** Prisoner on trial
**Status:** Physically Present (in dream)
**Physical Description:** 
**Costume/Silhouette:** Likely follows playing card motif.
**Prompt Phrases:** knave of hearts, prisoner, defendant, playing card character.
**Uncertainty Notes:** Visual details are minimal.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: the_jury
canonical_character_id: jury
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: group_of_creatures
morphology_hint: various
scale_hint: small
renderability_hint: 
confidence: 0.9
direct_identity_evidence: "The Jury: A collection of various creatures (including a Lizard)."
direct_visual_evidence: "spilling the jurymen onto the crowd below"
costume_or_covering_evidence: 
movement_evidence: "spilling... onto the crowd", "unable to move [the lizard]"
associated_entities: ["alice"]
alias_or_role_evidence: "A collection of various creatures"
unknowns: []
source_refs: [[SECTION markdown]]
# The Jury
**Role:** Jurors
**Status:** Physically Present (in dream)
**Physical Description:** A diverse collection of various creatures. Includes a Lizard.
**Costume/Silhouette:** 
**Prompt Phrases:** jury of creatures, mixed animal jury, small creatures, courtroom jurors.
**Uncertainty Notes:** Specific species beyond the lizard are not listed.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
asset_id: alices_sister
canonical_character_id: alice_sister
aliases: []
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: 
scale_hint: standard
renderability_hint: 
confidence: 1.0
direct_identity_evidence: "Alice... recounts her dream to her sister."
direct_visual_evidence: "her head in her sister's lap"
costume_or_covering_evidence: 
movement_evidence: "remains, drifting into a daydream"
associated_entities: ["alice"]
alias_or_role_evidence: 
unknowns: []
source_refs: [[SECTION markdown]]
# Alice's Sister
**Role:** Observer / Dreamer
**Status:** Physically Present (real world); Referenced (as dreamer)
**Physical Description:** Sitting on a riverbank.
**Costume/Silhouette:** 
**Prompt Phrases:** sister, daydreaming woman, sitting by riverbank, listening to stories.
**Uncertainty Notes:** Physical appearance and clothing are not described.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]
[[/FILMCREATOR_PACKET]]
````
