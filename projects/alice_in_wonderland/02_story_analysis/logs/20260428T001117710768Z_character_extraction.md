# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:11:17.710768+00:00
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

Chapter id: CH011

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

**Setting:** A crowded courtroom filled with birds, beasts, and a pack of cards. In the center is a table holding a large dish of tarts. The King sits on his throne wearing a great wig (with his crown over it), acting as judge. Twelve jurors (a mix of animals and birds) sit in a jury-box, writing on sleates.

**Characters:**
*   **The King of Hearts:** The judge; wears a large wig under his crown.
*   **The Queen of Hearts:** Seated with the King; stares intensely at witnesses.
*   **The Knave of Hearts:** In chains, guarded by two soldiers.
*   **The White Rabbit:** Official/Herald; carries a trumpet and a parchment scroll.
*   **Alice:** A young girl observing the trial; she is growing larger in size during the proceedings.
*   **The Gryphon:** Sitting near Alice.
*   **The Jury (including Bill the Lizard):** Twelve creatures writing on slates.
*   **The Hatter:** The first witness; carries a teacup and bread-and-butter.
*   **The March Hare & The Dormouse:** Accompanying the Hatter as witnesses/entourage.
*   **The Duchess’s Cook:** The second witness; carries a pepper-box.

**Key Events:**
1.  **The Arrival:** The King and Queen arrive at court with the Knave in chains. Alice observes the jury, noting they are writing their names on slates to avoid forgetting them.
2.  **The Accusation:** The White Rabbit reads the charge: The Knave of Hearts stole the Queen's tarts.
3.  **Theft of the Pencil:** Alice steals a squeaky pencil from Bill the Lizard (a juror) to stop the noise; Bill is left writing with a finger, which leaves no marks on his slate.
4.  **The Hatter’s Testimony:** The Hatter enters with tea-time items. He gives confusing testimony about when he began his tea (March 14th, 15th, or 16th). The King and jury record the dates as a monetary value on their slates.
5.  **Alice’s Growth:** Alice begins to grow larger physically. She has a brief, sulky argument with the Dormouse about her "unreasonable" growth rate.
6.  **The Hatter's Exit:** The Queen stares at the Hatter; he becomes nervous and accidentally bites his teacup. After a confusing exchange regarding "twinkling," the King tells him to stand down. The Hatter leaves hurriedly, even leaving his shoes behind.
7.  **The Cook’s Testimony:** The Duchess’s Cook enters, causing everyone to sneeze due to her pepper-box. When asked what tarts are made of, she says "pepper." 
8.  **Chaos in Court:** The Dormouse suggests "treacle," prompting the Queen to erupt in a frenzy of commands to collar/behead/suppress the Dormouse. During the chaos, the Cook disappears.
9.  **The Reveal:** As the court settles, the White Rabbit reads the next name on the list: Alice.
````

## Raw Response
````text
[[FILMCREATOR_PACKET]]

task: character_extraction

version: 1

character_index_markdown:

[[SECTION character_index_markdown]]

* [king_of_hearts](#king_of_hearts)
* [queen_of_hearts](#queen_of_hearts)
* [knave_of_hearts](#knave_of_hearts)
* [white_rabbit](#white_rabbit)
* [alice](#alice)
* [gryphon](#gryction)
* [bill_the_lizard](#bill_the_lizard)
* [the_jury](#the_jury)
* [the_hatter](#the_hatter)
* [march_hare](#march_hare)
* [dormouse](#dormouse)
* [duchesss_cook](#duchesss_cook)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH011 King of Hearts
aliases: The King
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: royal/judge
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: queen_of_hearts, knave_of_hearts
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# King of Hearts
**Role:** Judge of the court.
**Presence:** Physically present in the courtroom.
**Description:** Wears a great wig with his crown placed over it. 
**Notes:** Acts as the presiding judge during the trial proceedings.
[[/SECTION]]
[[/FILctions_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH011 Queen of Hearts
aliases: The Queen
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: royal/judge
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: king_of_hearts, knave_of_hearts
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Queen of Hearts
**Role:** Judge/Royal authority.
**Presence:** Physically present in the courtroom.
**Description:** Seated with the King; known for staring intensely at witnesses and erupting into commands to collar or behead subjects.
**Notes:** A source of tension and sudden command in the court.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH011 Knave of Hearts
aliases: The Knave
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
clarification_question: ""
character_type_hint: prisoner
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: king_of_hearts, queen_of_hearts
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Knave of Hearts
**Role:** The accused.
**Presence:** Physically present in the courtroom.
**Description:** Held in chains and guarded by two soldiers.
**Notes:** Accused of stealing the Queen's tarts.
[[/SECTION]]
[[/FILMCREcially_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH011 White Rabbit
aliases: The White Rabbit, Herald
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal/official
morphology_hint: rabbit-like
scale_hint: small to human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: alice, knave_of_hearts
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# White Rabbit
**Role:** Official/Herald.
**Presence:** Physically present in the courtroom.
**Description:** Carries a trumpet and a parchment scroll.
**Notes:** Reads the charges and manages the list of names for the trial.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH011 Alice
aliases: Alice
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: human/girl
morphology_hint: young girl
scale_hint: growing larger
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: white_rabbit, gryphon, dormouse
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Alice
**Role:** Observer/Witness.
**Presence:** Physically present in the courtroom.
**Description:** A young girl who is growing larger in size during the proceedings.
**Notes:** Observes the jury and has a brief argument with the Dormouse regarding her growth rate.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gryphon
canonical_character_id: CH011 Gryphon
aliases: The Gryphon
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: mythical beast
morphology_hint: gryphon-like
scale_hint: large
renderability_hint: high
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: alice
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Gryphon
**Role:** Court attendee.
**Presence:** Physically present in the courtroom.
**Description:** Sitting near Alice.
**Notes:** Part of the crowd of beasts and birds.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill_the_lizard
canonical_character_id: CH011 Bill the Lizard
aliases: Bill
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal/juror
morphology_hint: lizard-like
scale_hint: small to human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: the_jury, alice
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# Bill the Lizard
**Role:** Juror.
**Presence:** Physically present in the courtroom.
**Description:** A lizard-like creature writing on a slate.
**Notes:** Loses his pencil to Alice, forcing him to write with his finger.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_jury
canonical_character_id: CH011 The Jury
aliases: The Twelve Jurors
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: group/animals
morphology_hint: mix of animals and birds
scale_hint: various
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: king_of_hearts, queen_of_hearts
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Jury
**Role:** Legal body.
**Presence:** Physically present in the courtroom.
**Description:** A group of twelve creatures (animals and birds) writing on slates.
**Notes:** They record names and monetary values/dates on their slates.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: the_hatter
canonical_character_id: CH011 The Hatter
aliases: The Hatter
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: human/witness
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: march_hare, dormouse
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Hatter
**Role:** First witness.
**Presence:** Physically present in the courtroom.
**Description:** Carries a teacup and bread-and-butter. 
**Notes:** Provides confusing testimony about tea-time dates; becomes nervous under the Queen's gaze, accidentally biting his teacup. He leaves his shoes behind when exiting.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: march_hare
canonical_character_id: CH011 March Hare
aliases: The March Hare
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal/witness
morphology_hint: hare-like
scale_hint: small to human-sized
renderability_hint: high
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: the_hatter, dormouse
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The March Hare
**Role:** Witness/Entourage.
**Presence:** Physically present in the courtroom.
**Description:** Accompanying the Hatter.
**Notes:** Part of the tea-time themed group of witnesses.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dormouse
canonical_character_id: CH011 Dormouse
aliases: The Dormouse
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: animal/witness
morphology_hint: mouse-like
scale_hint: small
renderability_hint: high
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: the_hatter, march_hare
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Dormouse
**Role:** Witness/Entourage.
**Presence:** Physically present in the courtroom.
**Description:** Small creature accompanying the Hatter.
**Notes:** Suggests "treacle" as a tart ingredient, prompting the Queen's fury.
[[/cut_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchesss_cook
canonical_character_id: CH011 The Duchess’s Cook
aliases: The Cook
is_fully_identified: true
manual_description_required: false
manual_description_reason: ""
clarification_required: false
clarification_reason: ""
character_type_hint: human/witness
morphology_hint: unknown
scale_hint: human-sized
renderability_hint: high
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: ""
alias_or_role_evidence: true
unknowns: ""
source_refs: ""

[[SECTION markdown]]
# The Duchess’s Cook
**Role:** Second witness.
**Presence:** Physically present in the courtroom.
**Description:** Carries a pepper-box.
**Notes:** Her entrance causes sneezing due to her pepper-box; she claims tarts are made of pepper. She disappears during the chaos.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[/FILMCREATOR_PACKET]]
````
