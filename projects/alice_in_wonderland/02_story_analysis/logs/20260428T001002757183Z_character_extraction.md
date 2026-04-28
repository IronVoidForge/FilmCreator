# LM Studio Authoring Exchange
- timestamp_utc: 2026-04-28T00:10:02.757183+00:00
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

# Character Index
- [Alice](#alice)
- [The King of Hearts](#the-king-of-hearts)
- [The Queen of Hearts](#the-queen-of-hearts)
- [The Knave of Hearts](#the-knave-of-hearts)
- [The White Rabbit](#the-white-rabbit)
- [The Gryphon](#the-gryphon)
- [Bill the Lizard](#bill-the-lizard)
- [The Jury](#the-jury)
- [The Hatter](#the-hatter)
- [The March Hare](#the-march-hare)
- [The Dormouse](#the-dormouse)
- [The Duchess’s Cook](#the-duchesss-cook)

[[/SECTION]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: alice
canonical_character_id: CH002 Alice
aliases: 
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clariction_reason: 
clarification_question: 
character_type_hint: human
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_gryphon, the_jury]
alias_or_role_evidence: false
unknowns: []
source_refs: []

[[SECTION markdown]]
# Alice
**Role:** Observer/Witness.
**Physical Description:** A young girl who is physically growing larger in size during the proceedings. 
**Notes:** She is present in the courtroom and interacts with the jury (stealing a pencil) and the Dormouse.
[[/SECTION]]
[[/FILcit_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: king_of_hearts
canonical_character_id: CH001 King of Hearts
aliases: The King
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: true
movement_evidence: false
associated_entities: [the_queen_of_hearts, the_knave_of_hearts]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The King of Hearts
**Role:** Judge.
**Physical Description:** Wears a great wig with his crown placed over it. 
**Notes:** He presides over the trial and records dates as monetary values on a slate.
[[/end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: queen_of_hearts
canonical_character_id: CH001 Queen of Hearts
aliases: The Queen
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_king_of_hearts, the_knave_of_hearts]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Queen of Hearts
**Role:** Judge/Authority.
**Physical Description:** Seated with the King; known for staring intensely at witnesses and erupting in fury.
**Notes:** She is a source of tension in the courtroom, often commanding the collar or beheading of others.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: knave_of_hearts
canonical_character_id: CH003 Knave of Hearts
aliases: The Knave
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_king_of_hearts, the_queen_of_hearts]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Knave of Hearts
**Role:** Accused.
**Physical Description:** Held in chains and guarded by soldiers.
**Notes:** He is accused of stealing the Queen's tarts.
[[/SECTION]]
[[cut_end_section]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: white_rabbit
canonical_character_id: CH004 White Rabbit
aliases: The White Rabbit, Herald
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: biped
scale_hint: small
renderability_hint: renderable
confidence: 0.9
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The White Rabbit
**Role:** Official/Herald.
**Physical Description:** An animal-type entity acting as a herald.
**Notes:** Carries a trumpet and a parchment scroll; reads the charges to the court.
[[/SECTION]]
[[/FILcut_record]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: gryphon
canonical_character_id: CH005 Gryphon
aliases: The Gryphon
is_fully_identified: true
manual_description_required: true
manual_description_reason: Physical traits beyond being a "Gryphon" are not detailed in this chapter.
clarification_required: false
clarification_reason: 
clarification_question: 
character_type_hint: creature
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.5
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [alice]
alias_or_role_evidence: true
unknowns: [physical morphology]
source_refs: []

[[SECTION markdown]]
# The Gryphon
**Role:** Court attendee.
**Physical Description:** A creature sitting near Alice.
**Notes:** Specific visual details of its form are not provided in this text segment.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: bill_the_lizard
canonical_character_id: CH006 Bill the Lizard
aliases: Bill
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: quadruped
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_jury]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# Bill the Lizard
**Role:** Juror.
**Physical Description:** A lizard-like creature writing on a slate.
**Notes:** He loses his pencil to Alice, forcing him to write with his finger.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: jury
canonical_character_id: CH007 The Jury
aliases: The Twelve Jurors
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: group
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.6
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: true
unknowns: [individual composition]
source_refs: []

[[SECTION markdown]]
# The Jury
**Role:** Legal body.
**Physical Description:** A group of twelve creatures, including birds and beasts, sitting in a jury-box writing on slates.
**Notes:** They use their names on slates to avoid forgetting them.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: hatter
canonical_character_id: CH008 The Hatter
aliases: The Hatter
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: humanoid_nonhuman
morphology_hint: biped
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_march_hare, the_dormouse]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Hatter
**Role:** Witness.
**Physical Description:** Carries a teacup and bread-and-butter. 
**Notes:** He gives confusing testimony regarding dates; he is nervous under the Queen's gaze and accidentally bites his teacup.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMcut_record]]
type: character
asset_id: march_hare
canonical_character_id: CH009 March Hare
aliases: The March Hare
is_fully_identified: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: unknown
scale_hint: small
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_hatter, the_dormouse]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The March Hare
**Role:** Witness/Entourage.
**Physical Description:** An animal-type entity accompanying the Hatter.
**Notes:** Part of the tea-time witness group.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: dormouse
canonical_character_id: CH009 Dormouse
aliases: The Dormouse
is_fully_identified: true
manual_description_required: false
manualdescription_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: animal
morphology_hint: unknown
scale_hint: tiny
renderability_hint: renderable
confidence: 0.8
direct_identity_evidence: true
direct_visual_evidence: false
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: [the_hatter, the_march_hare]
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Dormouse
**Role:** Witness/Entourage.
**Physical Description:** A small animal-type entity.
**Notes:** Suggests "treacle" as a tart ingredient, prompting the Queen's fury.
[[/SECTION]]
[[/FILMCREATOR_RECORD]]

[[FILMCREATOR_RECORD]]
type: character
asset_id: duchess_cook
canonical_character_id: CH010 Duchess’s Cook
aliases: The Cook
is_fully_identifed: true
manual_description_required: false
manual_description_reason: 
clarification_required: false
clarification_reason: 
character_type_hint: humanoid_nonhuman
morphology_hint: unknown
scale_hint: human_scale
renderability_hint: renderable
confidence: 0.7
direct_identity_evidence: true
direct_visual_evidence: true
costume_or_covering_evidence: false
movement_evidence: false
associated_entities: []
alias_or_role_evidence: true
unknowns: []
source_refs: []

[[SECTION markdown]]
# The Duchess’s Cook
**Role:** Witness.
**Physical Description:** Carries a pepper-box.
**Notes:** Her entrance causes sneezing; she claims tarts are made of "pepper."
[[/SECTION]]
[[/FILcut_record]]

[[/FILMCREATOR_PACKET]]
````
